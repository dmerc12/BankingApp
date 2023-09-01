import logging

import bcrypt

from DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from Entities.Customer import Customer
from Entities.FailedTransaction import FailedTransaction
from SAL.CustomerSAL.CustomerSALInterface import CustomerSALInterface

class CustomerSALImplementation(CustomerSALInterface):

    def __init__(self, customer_dao: CustomerDALImplementation):
        self.customer_dao = customer_dao

    def service_create_customer(self, customer: Customer, password_confirmation: str) -> Customer:
        logging.info("Beginning SAL method create customer")
        if type(customer.first_name) != str:
            logging.warning("SAL method create customer, first name not a string")
            raise FailedTransaction("The first name field must be a string, please try again!")
        elif len(customer.first_name) > 36:
            logging.warning("SAL method create customer, first name longer than 36 characters")
            raise FailedTransaction("The first name field cannot exceed 36 characters, please try again!")
        elif len(customer.first_name) == 0:
            logging.info("SAL method create customer, first name empty")
            raise FailedTransaction("The first name field cannot be left empty, please try again!")
        elif type(customer.last_name) != str:
            logging.warning("SAL method create customer, last name not a string")
            raise FailedTransaction("The last name field must be a string, please try again!")
        elif len(customer.last_name) > 36:
            logging.warning("SAL method create customer, last name longer than 36 characters")
            raise FailedTransaction("The last name field cannot exceed 36 characters, please try again!")
        elif len(customer.last_name) == 0:
            logging.warning("SAL method create customer, last name empty")
            raise FailedTransaction("The last name field cannot be left empty, please try again!")
        elif type(customer.password) != str:
            logging.warning("SAL method create customer, password not a string")
            raise FailedTransaction("The password field must be a string, please try again!")
        elif len(customer.password) == 0:
            logging.warning("SAL method create customer, password left empty")
            raise FailedTransaction("The password field cannot be left  empty, please try again!")
        elif type(password_confirmation) != str:
            logging.warning("SAL method create customer, confirmation password not a string")
            raise FailedTransaction("The confirmation password field must be a string, please try again!")
        elif len(password_confirmation) == 0:
            logging.warning("SAL method create customer, confirmation password empty")
            raise FailedTransaction("The confirmation password field cannot be left empty, please try again!")
        elif type(customer.email) != str:
            logging.warning("SAL method crete customer, email not a string")
            raise FailedTransaction("The email field must be a string, please try again!")
        elif len(customer.email) > 60:
            logging.warning("SAL method create customer, email longer than 60 characters")
            raise FailedTransaction("The email field cannot exceed 60 characters, please try again!")
        elif len(customer.email) == 0:
            logging.warning("SAL method create customer, email left empty")
            raise FailedTransaction("The email field cannot be left empty, please try again!")
        elif type(customer.phone_number) != str:
            logging.warning("SAL method create customer, phone number not a string")
            raise FailedTransaction("The phone number field must be a string, please try again!")
        elif len(customer.phone_number) > 12:
            logging.warning("SAL method create customer, phone number longer than 12 characters")
            raise FailedTransaction("The phone number field cannot exceed 12 characters, please try again!")
        elif len(customer.phone_number) == 0:
            logging.warning("SAL method create customer, phone number left empty")
            raise FailedTransaction("The phone number field cannot be left empty, please try again!")
        elif type(customer.address) != str:
            logging.warning("SAL method create customer, address not a string")
            raise FailedTransaction("The address field must be a string, please try again!")
        elif len(customer.address) > 60:
            logging.warning("SAL method create customer, address longer than 60 characters")
            raise FailedTransaction("The address field cannot exceed 60 characters, please try again!")
        elif len(customer.address) == 0:
            logging.warning("SAL method create customer, address left empty")
            raise FailedTransaction("The address field cannot be left empty, please try again!")
        elif password_confirmation != customer.password:
            logging.warning("SAL method create customer, password and confirmation don't match")
            raise FailedTransaction("The passwords do not match, please try again!")
        else:
            existing_customer_check = self.service_get_customer_by_email(customer.email).email
            if customer.email == existing_customer_check:
                logging.warning("SAL method create customer, customer already exists")
                raise FailedTransaction("A customer already exists with this username, please log in!")
            else:
                hashed_password = bcrypt.hashpw(customer.password.encode('utf-8'), bcrypt.gensalt())
                customer.password = hashed_password.decode('utf-8')
                new_customer = self.customer_dao.create_customer(customer)
                logging.info("Finishing SAL method create customer")
                return new_customer

    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        logging.info("Beginning SAL method get customer by ID")
        if type(customer_id) != int:
            logging.warning("SAL method get customer by ID, customer ID not an integer")
            raise FailedTransaction("CustomerRoutes ID field must be an integer, please try again!")
        else:
            logging.info("Finishing SAL method get customer by ID")
            customer = self.customer_dao.get_customer_by_id(customer_id)
            return customer

    def service_get_customer_by_email(self, email: str) -> Customer:
        logging.info("Beginning SAL method get customer by email")
        if type(email) != str:
            logging.warning("SAL method get customer by email, email not a string")
            raise FailedTransaction("Email field must be a string, please try again!")
        else:
            logging.info("Finishing SAL method get customer by email")
            customer = self.customer_dao.get_customer_by_email(email)
            return customer

    def service_login(self, email: str, password: str) -> Customer:
        logging.info("Beginning SAL method login")
        if type(email) != str:
            logging.warning("SAL method login, username not a string")
            raise FailedTransaction("The email field must be a string, please try again!")
        elif len(email) == 0:
            logging.warning("SAL method login, username left empty")
            raise FailedTransaction("The email field cannot be left empty, please try again!")
        elif type(password) != str:
            logging.warning("SAL method login, password not a string")
            raise FailedTransaction("The password field must be a string, please try again!")
        elif len(password) == 0:
            logging.warning("SAL method login, password left empty")
            raise FailedTransaction("The password field cannot be left empty, please try again!")
        else:
            customer = self.service_get_customer_by_email(email)
            if customer.customer_id == 0 or not bcrypt.checkpw(password.encode(), customer.password.encode()):
                logging.warning("DAL method login, cannot validate credentials")
                raise FailedTransaction("Either the email or password are incorrect, please try again!")
            else:
                self.customer_dao.login(email, password)
                logging.info("Finishing SAL method login")
                return customer

    def service_update_customer(self, updated_customer_info: Customer, customer_id: int) -> Customer:
        logging.info("Beginning SAL method update customer")
        if type(updated_customer_info.first_name) != str:
            logging.warning("SAL method update customer, first name not a string")
            raise FailedTransaction("The first name field must be a string, please try again!")
        elif len(updated_customer_info.first_name) == 0:
            logging.warning("SAL method update customer, first name empty")
            raise FailedTransaction("The first name field cannot be empty, please try again!")
        elif len(updated_customer_info.first_name) > 36:
            logging.warning("SAL method update customer, first name longer than 36 characters")
            raise FailedTransaction("The first name field cannot exceed 36 characters, please try again!")
        elif type(updated_customer_info.last_name) != str:
            logging.warning("SAL method update customer, last name not a string")
            raise FailedTransaction("The last name field must be a string, please try again!")
        elif len(updated_customer_info.last_name) == 0:
            logging.warning("SAL method update customer, last name empty")
            raise FailedTransaction("The last name field cannot be empty, please try again!")
        elif len(updated_customer_info.last_name) > 36:
            logging.warning("SAL method update customer, last name longer than 36 characters")
            raise FailedTransaction("The last name field cannot exceed 36 characters, please try again!")
        elif type(updated_customer_info.email) != str:
            logging.warning("SAL method update customer, email not a string")
            raise FailedTransaction("The email field must be a string, please try again!")
        elif len(updated_customer_info.email) == 0:
            logging.warning("SAL method update customer, email empty")
            raise FailedTransaction("The email field cannot be empty, please try again!")
        elif len(updated_customer_info.email) > 60:
            logging.warning("SAL method update customer, email longer than 60 characters")
            raise FailedTransaction("The email field cannot exceed 60 characters, please try again!")
        elif type(updated_customer_info.phone_number) != str:
            logging.warning("SAL method update customer, phone number not a string")
            raise FailedTransaction("The phone number field must be a string, please try again!")
        elif len(updated_customer_info.phone_number) == 0:
            logging.warning("SAL method update customer, phone number empty")
            raise FailedTransaction("The phone number field cannot be empty, please try again!")
        elif len(updated_customer_info.phone_number) > 12:
            logging.warning("SAL method update customer, phone number longer than 12 characters")
            raise FailedTransaction("The phone number field cannot exceed 12 characters, please try again!")
        elif type(updated_customer_info.address) != str:
            logging.warning("SAL method update customer, address not a string")
            raise FailedTransaction("The address field must be a string, please try again!")
        elif len(updated_customer_info.address) == 0:
            logging.warning("SAL method update customer, address empty")
            raise FailedTransaction("The address field cannot be empty, please try again!")
        elif len(updated_customer_info.address) > 60:
            logging.warning("SAL method update customer, address longer than 60 characters")
            raise FailedTransaction("The address field cannot exceed 60 characters, please try again!")
        else:
            current_customer_information = self.service_get_customer_by_id(customer_id)
            if updated_customer_info.first_name == current_customer_information.first_name and \
                    updated_customer_info.last_name == current_customer_information.last_name and \
                    updated_customer_info.email == current_customer_information.email and \
                    updated_customer_info.phone_number == current_customer_information.phone_number and \
                    updated_customer_info.address == current_customer_information.address:
                logging.warning("SAL method update customer, no information changed")
                raise FailedTransaction("No information has changed!")
            logging.info("Finishing SAL method update customer")
            updated_customer = self.customer_dao.update_customer(updated_customer_info, customer_id)
            return updated_customer

    def service_change_password(self, customer_id: int, new_password: str, confirmation_password: str) -> bool:
        logging.info("Beginning SAL method change password")
        if type(customer_id) != int:
            logging.warning("SAL method change password, customer ID not an integer")
            raise FailedTransaction("The customer ID field must be an integer, please try again!")
        else:
            current_information = self.service_get_customer_by_id(customer_id)
            if type(new_password) != str:
                logging.warning("SAL method change password, new password not a string")
                raise FailedTransaction("The new password field must be a string, please try again!")
            elif type(confirmation_password) != str:
                logging.warning("SAL method change password, confirmation password not a string")
                raise FailedTransaction("The confirmation password field must be a string, please try again!")
            elif len(new_password) == 0:
                logging.warning("SAL method change password, password left empty")
                raise FailedTransaction("The password field cannot be left empty, please try again!")
            elif len(confirmation_password) == 0:
                logging.warning("SAL method change password, confirmation password empty")
                raise FailedTransaction("The confirmation password cannot be left empty, please try again!")
            elif len(new_password) > 36:
                logging.warning("SAL method change password, password too long")
                raise FailedTransaction("The password field cannot exceed 36 characters, please try again!")
            elif len(confirmation_password) > 36:
                logging.warning("SAL method change password, confirmation password too long")
                raise FailedTransaction("The confirmation password field cannot exceed 36 characters, please try "
                                        "again!")
            elif confirmation_password == new_password:
                logging.info("SAL method change password, hashing password")
                hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                new_password_bytes = new_password.encode('utf-8')
                current_password_bytes = current_information.password.encode('utf-8')
                if bcrypt.checkpw(new_password_bytes, current_password_bytes):
                    logging.warning("SAL method change password, nothing changed")
                    raise FailedTransaction("Nothing has changed, please try again!")
                else:
                    logging.info("Finishing SAL method change password")
                    result = self.customer_dao.change_password(customer_id, hashed_password)
                    return result
            else:
                logging.warning("SAL method change password, passwords don't match")
                raise FailedTransaction("The passwords don't match, please try again!")

    def service_delete_customer(self, customer_id: int) -> bool:
        logging.info("Beginning SAL method delete customer")
        self.customer_dao.get_customer_by_id(customer_id)
        result = self.customer_dao.delete_customer(customer_id)
        logging.info("Finishing SAL method delete customer")
        return result
