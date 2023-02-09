import logging

from PythonAPI.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from PythonAPI.Entities.Customer import Customer
from PythonAPI.Entities.FailedTransaction import FailedTransaction
from PythonAPI.SAL.CustomerSAL.CustomerSALInterface import CustomerSALInterface


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
        elif type(customer.email) != str:
            logging.warning("SAL method crete customer, email not a string")
            raise FailedTransaction("The email field must be a string, please try again!")
        elif len(customer.email) > 36:
            logging.warning("SAL method create customer, email longer than 36 characters")
            raise FailedTransaction("The email field cannot exceed 36 characters, please try again!")
        elif len(customer.email) == 0:
            logging.warning("SAL method create customer, email left empty")
            raise FailedTransaction("The email field cannot be left empty, please try again!")
        elif type(customer.phone_number) != str:
            logging.warning("SAL method create customer, phone number not a string")
            raise FailedTransaction("The phone number field must be a string, please try again!")
        elif len(customer.phone_number) > 13:
            logging.warning("SAL method create customer, phone number longer than 13 characters")
            raise FailedTransaction("The phone number field cannot exceed 13 characters, please try again!")
        elif len(customer.phone_number) == 0:
            logging.warning("SAL method create customer, phone number left empty")
            raise FailedTransaction("The phone number field cannot be left empty, please try again!")
        elif (customer.phone_number[3] and customer.phone_number[7]) != "-":
            logging.warning("SAL method create customer, phone number in incorrect format")
            raise FailedTransaction("The phone number must follow the format xxx-xxx-xxxx, please try again!")
        elif type(customer.address) != str:
            logging.warning("SAL method create customer, address not a string")
            raise FailedTransaction("The address field must be a string, please try again!")
        elif len(customer.address) > 50:
            logging.warning("SAL method create customer, address longer than 50 characters")
            raise FailedTransaction("The address field cannot exceed 50 characters, please try again!")
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
                logging.info("Finishing SAL method create customer")
                new_customer = self.customer_dao.create_customer(customer)
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
            logging.info("Finishing SAL method login")
            customer = self.customer_dao.login(email, password)
            return customer

    def service_update_customer(self, customer: Customer) -> Customer:
        logging.info("Beginning SAL method update customer")
        if type(customer.first_name) != str:
            logging.warning("SAL method update customer, first name not a string")
            raise FailedTransaction("The first name field must be a string, please try again!")
        elif len(customer.first_name) > 36:
            logging.warning("SAL method update customer, first name longer than 36 characters")
            raise FailedTransaction("The first name field cannot exceed 36 characters, please try again!")
        elif type(customer.last_name) != str:
            logging.warning("SAL method update customer, last name not a string")
            raise FailedTransaction("The last name field must be a string, please try again!")
        elif len(customer.last_name) > 36:
            logging.warning("SAL method update customer, last name longer than 36 characters")
            raise FailedTransaction("The last name field cannot exceed 36 characters, please try again!")
        elif type(customer.password) != str:
            logging.warning("SAL method update customer, password not a string")
            raise FailedTransaction("The password field must be a string, please try again!")
        elif len(customer.password) > 36:
            logging.warning("SAL method update customer, password longer than 36 characters")
            raise FailedTransaction("The password field cannot exceed 36 characters, please try again!")
        elif type(customer.email) != str:
            logging.warning("SAL method update customer, email not a string")
            raise FailedTransaction("The email field must be a string, please try again!")
        elif len(customer.email) > 36:
            logging.warning("SAL method update customer, email longer than 36 characters")
            raise FailedTransaction("The email field cannot exceed 36 characters, please try again!")
        elif type(customer.phone_number) != str:
            logging.warning("SAL method update customer, phone number not a string")
            raise FailedTransaction("The phone number field must be a string, please try again!")
        elif len(customer.phone_number) > 13:
            logging.warning("SAL method update customer, phone number longer than 13 characters")
            raise FailedTransaction("The phone number field cannot exceed 13 characters, please try again!")
        elif type(customer.address) != str:
            logging.warning("SAL method update customer, address not a string")
            raise FailedTransaction("The address field must be a string, please try again!")
        elif len(customer.address) > 50:
            logging.warning("SAL method update customer, address longer than 50 characters")
            raise FailedTransaction("The address field cannot exceed 50 characters, please try again!")
        else:
            current_customer_information = self.service_get_customer_by_id(customer.customer_id)
            if customer.first_name == "":
                customer.first_name = current_customer_information.first_name
            if customer.last_name == "":
                customer.last_name = current_customer_information.last_name
            if customer.password == "":
                customer.password = current_customer_information.password
            if customer.email == "":
                customer.email = current_customer_information.email
            if customer.phone_number == "":
                customer.phone_number = current_customer_information.phone_number
            if customer.address == "":
                customer.address = current_customer_information.address
            logging.info("Finishing SAL method update customer")
            updated_customer = self.customer_dao.update_customer(customer)
            return updated_customer

    def service_delete_customer(self, customer_id: int) -> bool:
        logging.info("Beginning SAL method delete customer")
        self.customer_dao.get_customer_by_id(customer_id)
        result = self.customer_dao.delete_customer(customer_id)
        logging.info("Finishing SAL method delete customer")
        return result

