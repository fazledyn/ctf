from PIL import Image

def get_main_color(file):
    img = Image.open(file)
    colors = img.getcolors(256) #put a higher value if there are many colors in your image
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        return most_present
    except TypeError:
        raise Exception("Too many colors in the image")

for i in range(568):
    color_code = get_main_color(f"{i}.png")
    if color_code[0] == 255:
        print(1,end="")
    elif color_code[1] == 128:
        print(0,end="")
