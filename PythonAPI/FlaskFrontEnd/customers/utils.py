from flask import url_for, current_app
from flask_mail import Message
from itsdangerous import Serializer
from PythonAPI.API import mail
from PythonAPI.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from PythonAPI.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)

def send_reset_email(user):
    token = user.get_reset_token()
    message = Message('Password Reset Request', sender='noreply@flaskbanking.com', recipients=[user.email])
    message.body = f"""To reset your password, visit the following link \
                   {url_for('customers.reset_token', token=token, _external=True)}
                   If you did not make this request then simply ignore this email and no changes will be made."""
    mail.send()

def get_reset_token(self, expires_sec=1800):
    serializer = Serializer(current_app.config["SECRET_KEY"], f"{expires_sec}")
    return serializer.dumps({'user_id': self.customer_id}).decode('utf-8')

def verify_reset_token(token):
    serializer = Serializer(current_app.config['SECRET_KEY'])
    try:
        user_id = serializer.loads(token)["user_id"]
    except:
        return None
    return customer_sao.service_get_customer_by_id(user_id)
