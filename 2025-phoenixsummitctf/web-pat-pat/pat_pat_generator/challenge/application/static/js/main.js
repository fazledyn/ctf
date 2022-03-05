const form   = document.getElementById('form');
const alerts = document.getElementById('alerts');
const image = document.getElementById('image');
const fileLabel = document.querySelector('.custom-file-label');

const flash = (message, level) => {
    alerts.innerHTML += `
        <div class="alert alert-${level}" role="alert">
            <p id="closeAlert" class="close" data-dismiss="alert" aria-label="Close"></p>
            <strong>${message}</strong>
        </div>
    `;
};



form.addEventListener('submit', e => {
    e.preventDefault();

    const imageFile = document.getElementById('imageFile').files[0];
    if (!imageFile) {
        flash('Please select an image file', 'danger');
        return;
    }

    const formData = new FormData();
    formData.append('file', imageFile);

    axios
        .post('/api/upload', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
        .then(({ data }) => {
            if (!data.image) {
                flash(data.message, 'danger');
            } else {
                $('#image').attr('src', data.image);
            }
        })
        .catch(error => {
            flash('Error processing image file', 'danger');
        });
});