from flask import url_for
from flask_mail import Message

from PythonAPI.API import mail


def send_reset_email(user):
    token = user.get_reset_token()
    message = Message('Password Reset Request', sender='noreply@flaskbanking.com', recipients=[user.email])
    message.body = f"""To reset your password, visit the following link \
                   {url_for('customers.reset_token', token=token, _external=True)}
                   If you did not make this request then simply ignore this email and no changes will be made."""
    mail.send()
