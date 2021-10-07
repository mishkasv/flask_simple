import os

from flask_security import uia_email_mapper,uia_username_mapper


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI","mysql+pymysql://flask:flask@mysql:3306/flask")
    SECRET_KEY = os.environ.get('SECRET_KEY','pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw')
    CATALOG_TITLE = "Catalog"
    FLASK_ADMIN_SWATCH = 'cerulean'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Security config
    SECURITY_URL_PREFIX = "/admin"
    SECURITY_PASSWORD_HASH = os.environ.get('SECURITY_PASSWORD_HASH', 'pbkdf2_sha512')
    SECURITY_PASSWORD_SALT =os.environ.get('SECURITY_PASSWORD_SALT',939054732152594777450394806232108144334)

    # Flask-Security URLs, overridden because they don't put a / at the end
    SECURITY_LOGIN_URL = "/login/"
    SECURITY_LOGOUT_URL = "/logout/"
    SECURITY_REGISTER_URL = "/register/"

    SECURITY_POST_LOGIN_VIEW = "/admin/"
    SECURITY_POST_LOGOUT_VIEW = "/admin/"
    SECURITY_POST_REGISTER_VIEW = "/admin/"

    # Flask-Security features
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_USER_IDENTITY_ATTRIBUTES = [
        {'email':{"mapper": uia_email_mapper, "case_insensitive": True}},
        {'username':{"mapper": uia_username_mapper, "case_insensitive": True}}]