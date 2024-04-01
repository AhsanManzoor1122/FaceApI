from Model.Users import Users
import DBHandler
from DBHandler import return_session
from DBHandler import DBHandler
from sqlalchemy.exc import SQLAlchemyError
session = return_session()
from deepface import DeepFace





def sign_up_user(username,email,gender,verification,faceimage):
    try:
        entity=Users(username=username,email=email,gender=gender,verification=verification,faceimage=faceimage)
        session.add(entity)
        session.commit()
        return {"response":"SignUp Successfull"},200
    except Exception as ex:
        return{"Error":str(ex)},500
    finally:session.close()

#varify Face

def verify_face(ref_image_path, input_image_path):
    # Perform face verification using DeepFace
    result = DeepFace.verify(img1_path=ref_image_path, img2_path=input_image_path)

    # Check if the 'verified' key exists in the result dictionary
    if "verified" in result:
        # Check if the images match
        if result["verified"]:
            # Return 1 if match is successful
            return 1
        else:
            # Return 0 if no match
            return 0
    else:
        # Return 0 if verification result is not available
        return 0



# Login User

def login_user(username,faceimage):
    try:
        user = session.query(Users).filter_by(username=username).first()
        if user:
            refimg=user.faceimage
            result_code=verify_face(refimg,faceimage)
            if result_code==1:
                user.verification=1
            elif result_code==0:
                user.verification=0
            session.commit()
            return {"username":user.username,"verification":user.verification},200
        else:
            return {"Invalid"}, 400
    except Exception as ex:
        session.rollback()
        return {"error": str(ex)}, 500
    finally:
        session.close()