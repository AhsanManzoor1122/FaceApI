
from flask import Flask,jsonify,request
from sqlalchemy.exc import SQLAlchemyError
import DBHandler
from DBHandler import return_session
from Controller import UserController
import Extentions

app = Flask(__name__)
session=return_session()

@app.route('/app/signup', methods=['POST'])
async def signup_user():
    try:
        username = request.form.get('username')
        email = request.form.get('email')
        gender=request.form.get('gender')

        faceimage=''
        if request.files.get('img'):
            faceimage = await Extentions.save_image(request.files['img'])

        if Extentions.username_exist(username=username):
            return {"message": "Username already exists"}, 400

        response, status = UserController.sign_up_user(username=username,email=email,gender=gender,verification=0,faceimage=faceimage)
        print(username,email,faceimage)
        return response, status
    except Exception as ex:
        return {"error": str(ex)}, 500


    #login

@app.route('/app/login', methods=['POST'])
async def login_user():
    try:
        username = request.form.get('username')
        faceimage = ''
        if request.files.get('img'):
            faceimage = await Extentions.save_image(request.files['img'])
        response, status = UserController.login_user(username, faceimage)
        return response, status
    except Exception as ex:
        return {"error": str(ex)}, 500

if __name__=="__main__":
    app.run()

