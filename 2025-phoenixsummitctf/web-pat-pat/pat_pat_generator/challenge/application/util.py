import tempfile, glob, os
from application import main
from PIL import Image

generate = lambda x: os.urandom(x).hex()

def patmotion(user_image, frames):
    outputFrames = []
    for frame in frames:
        newFrame, i = Image.new('RGBA', frame.size), frames.index(frame)
        width   = int(75*(0.8 + i * 0.02))
        height  = int(75*(0.8 + i * 0.05))
        resized_user_image = user_image.resize((width, height))
        frame   = frame.convert('RGBA')
        newFrame.paste(resized_user_image, mask=resized_user_image, box=(30, 37))
        newFrame.paste(frame, mask=frame)
        outputFrames.append(newFrame)
    return outputFrames

def save_tmp(file):
    tmp  = tempfile.gettempdir()
    path = os.path.join(tmp, file.filename)
    file.save(path)
    return path

def patpat(file):
    try:
        tmp_path = save_tmp(file)
        user_image = Image.open(tmp_path).convert('RGBA')
        frames = [Image.open(f) for f in sorted(glob.glob('application/static/img/*'))]
        finalpat = patmotion(user_image, frames)

        filename = f'{generate(14)}.gif'
        finalpat[0].save(
            f'{main.app.config["UPLOAD_FOLDER"]}/{filename}', 
            save_all=True, 
            duration=30, 
            loop=0, 
            append_images=finalpat[1:],
        )
        return {'status': 'success', 'image': f'static/patpats/{filename}'}, 200
    except:
        return {'status': 'failed', 'message': 'Something went wrong'}, 500
