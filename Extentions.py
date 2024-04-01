import os

from werkzeug.utils import secure_filename
from DBHandler import return_session
from main import app
from Model.Users import Users

session = return_session()

UPLOAD_FOLDER = r'C:\Users\Asi Shaiq\Desktop\FaceLogin\Images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def username_exist(username):
    existing_doctor = session.query(Users).filter_by(username=username).first()
    session.close()
    return existing_doctor is not None


def allowed_file(filename):
    # Check if the file extension is allowed
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


async def save_image(file):
    # Save the uploaded file to the specified folder
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return filepath
    else:
        raise ValueError("Invalid file or file extension not allowed")
