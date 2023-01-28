from flask import current_app
from itsdangerous import Serializer

from PythonAPI.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from PythonAPI.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)

class Customer:

    def __init__(self, customer_id: int, first_name: str, last_name: str, username: str, password: str, email: str,
                 phone_number: str, address: str):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def convert_to_dictionary(self):
        return {
            "customerId": self.customer_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "phoneNumber": self.phone_number,
            "address": self.address
        }

    def get_reset_token(self, expires_sec=1800):
        serializer = Serializer(current_app.config["SECRET_KEY"], f"{expires_sec}")
        return serializer.dumps({'user_id': self.customer_id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        serializer = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = serializer.loads(token)["user_id"]
        except:
            return None
        return customer_sao.service_get_customer_by_id(user_id)
