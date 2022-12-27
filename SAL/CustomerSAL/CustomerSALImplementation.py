import logging
from DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from Entities.Customer import Customer
from Entities.FailedTransaction import FailedTransaction
from SAL.CustomerSAL.CustomerSALInterface import CustomerSALInterface

class CustomerSALImplementation(CustomerSALInterface):

    def __init__(self, customer_dao: CustomerDALImplementation):
        self.customer_dao = customer_dao

    def service_create_customer(self, customer: Customer) -> Customer:
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
        elif type(customer.username) != str:
            logging.warning("SAL method create customer, username not a string")
            raise FailedTransaction("The username field must be a string, please try again!")
        elif len(customer.username) > 36:
            logging.warning("SAL method create customer, username longer than 36 characters")
            raise FailedTransaction("The username field cannot exceed 36 characters, please try again!")
        elif len(customer.username) == 0:
            logging.warning("SAL method create customer, username left empty")
            raise FailedTransaction("The username field cannot be left empty, please try again!")
        elif type(customer.password) != str:
            logging.warning("SAL method create customer, password not a string")
            raise FailedTransaction("The password field must be a string, please try again!")
        elif len(customer.password) > 36:
            logging.warning("SAL method create customer, password longer than 36 characters")
            raise FailedTransaction("The password field cannot exceed 36 characters, please try again!")
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
        elif customer.email[-15:-1].__contains__("@") and (customer.email[-3:-1] == ".com" or
                                                           customer.email[-3:-1] == ".net" or
                                                           customer.email[-3:-1] == ".org" or
                                                           customer.email[-3:-1] == ".gov" or
                                                           customer.email[-3:-1] == ".edu"):
            logging.warning("SAL method create customer, email in incorrect format")
            raise FailedTransaction("The email field must follow the format of something@somthing.com, please try "
                                    "again!")
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
        elif customer.address.__contains__(3 * ","):
            logging.warning("SAL method create customer, address in incorrect format")
            raise FailedTransaction("The address must follow the format: house number,street name containing St / Ave "
                                    "/ etc, City, State, ZIP, please try again!")
        else:
            logging.info("Finishing SAL method create customer")
            new_customer = self.customer_dao.create_customer(customer)
            return new_customer

    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        logging.info("Beginning SAL method get customer by ID")
        if type(customer_id) != int:
            logging.warning("SAL method get customer by ID, customer ID not an integer")
            raise FailedTransaction("Customer ID field must be an integer, please try again!")
        else:
            logging.info("Finishing SAL method get customer by ID")
            customer = self.customer_dao.get_customer_by_id(customer_id)
            return customer

    def service_login(self, username: str, password: str) -> Customer:
        logging.info("Beginning SAL method login")
        if type(username) != str:
            logging.warning("SAL method login, username not a string")
            raise FailedTransaction("The username field must be a string, please try again!")
        elif len(username) == 0:
            logging.warning("SAL method login, username left empty")
            raise FailedTransaction("The username field cannot be left empty, please try again!")
        elif len(username) > 36:
            logging.warning("SAL method login, username cannot exceed 36 characters")
            raise FailedTransaction("The username field cannot exceed 36 characters, please try again!")
        elif type(password) != str:
            logging.warning("SAL method login, password not a string")
            raise FailedTransaction("The password field must be a string, please try again!")
        elif len(password) == 0:
            logging.warning("SAL method login, password left empty")
            raise FailedTransaction("The password field cannot be left empty, please try again!")
        elif len(password) > 36:
            logging.warning("SAL method login, password longer than 36 characters")
            raise FailedTransaction("The password field cannot exceed 36 characters, please try again!")
        else:
            logging.info("Finishing SAL method login")
            customer = self.customer_dao.login(username, password)
            return customer

    def service_update_customer(self, customer: Customer) -> Customer:
        logging.info("Beginning SAL method update customer")
        if type(customer.first_name) != str:
            logging.warning("SAL method update customer, first name not a string")
            raise FailedTransaction("The first name field must be a string, please try again!")
        elif len(customer.first_name) > 36:
            logging.warning("SAL method update customer, first name longer than 36 characters")
            raise FailedTransaction("The first name field cannot exceed 36 characters, please try again!")
        elif len(customer.first_name) == 0:
            logging.info("SAL method update customer, first name empty")
            raise FailedTransaction("The first name field cannot be left empty, please try again!")
        elif type(customer.last_name) != str:
            logging.warning("SAL method update customer, last name not a string")
            raise FailedTransaction("The last name field must be a string, please try again!")
        elif len(customer.last_name) > 36:
            logging.warning("SAL method update customer, last name longer than 36 characters")
            raise FailedTransaction("The last name field cannot exceed 36 characters, please try again!")
        elif len(customer.last_name) == 0:
            logging.warning("SAL method update customer, last name empty")
            raise FailedTransaction("The last name field cannot be left empty, please try again!")
        elif type(customer.username) != str:
            logging.warning("SAL method update customer, username not a string")
            raise FailedTransaction("The username field must be a string, please try again!")
        elif len(customer.username) > 36:
            logging.warning("SAL method update customer, username longer than 36 characters")
            raise FailedTransaction("The username field cannot exceed 36 characters, please try again!")
        elif len(customer.username) == 0:
            logging.warning("SAL method update customer, username left empty")
            raise FailedTransaction("The username field cannot be left empty, please try again!")
        elif type(customer.password) != str:
            logging.warning("SAL method update customer, password not a string")
            raise FailedTransaction("The password field must be a string, please try again!")
        elif len(customer.password) > 36:
            logging.warning("SAL method update customer, password longer than 36 characters")
            raise FailedTransaction("The password field cannot exceed 36 characters, please try again!")
        elif len(customer.password) == 0:
            logging.warning("SAL method update customer, password left empty")
            raise FailedTransaction("The password field cannot be left empty, please try again!")
        elif type(customer.email) != str:
            logging.warning("SAL method update customer, email not a string")
            raise FailedTransaction("The email field must be a string, please try again!")
        elif len(customer.email) > 36:
            logging.warning("SAL method update customer, email longer than 36 characters")
            raise FailedTransaction("The email field cannot exceed 36 characters, please try again!")
        elif len(customer.email) == 0:
            logging.warning("SAL method update customer, email left empty")
            raise FailedTransaction("The email field cannot be left empty, please try again!")
        elif customer.email[-15:-1].__contains__("@") and (customer.email[-3:-1] == ".com" or
                                                           customer.email[-3:-1] == ".net" or
                                                           customer.email[-3:-1] == ".org" or
                                                           customer.email[-3:-1] == ".gov" or
                                                           customer.email[-3:-1] == ".edu"):
            logging.warning("SAL method update customer, email in incorrect format")
            raise FailedTransaction("The email field must follow the format of something@somthing.com, please try "
                                    "again!")
        elif type(customer.phone_number) != str:
            logging.warning("SAL method update customer, phone number not a string")
            raise FailedTransaction("The phone number field must be a string, please try again!")
        elif len(customer.phone_number) > 13:
            logging.warning("SAL method update customer, phone number longer than 13 characters")
            raise FailedTransaction("The phone number field cannot exceed 13 characters, please try again!")
        elif len(customer.phone_number) == 0:
            logging.warning("SAL method update customer, phone number left empty")
            raise FailedTransaction("The phone number field cannot be left empty, please try again!")
        elif (customer.phone_number[3] and customer.phone_number[7]) != "-":
            logging.warning("SAL method update customer, phone number in incorrect format")
            raise FailedTransaction("The phone number must follow the format xxx-xxx-xxxx, please try again!")
        elif type(customer.address) != str:
            logging.warning("SAL method update customer, address not a string")
            raise FailedTransaction("The address field must be a string, please try again!")
        elif len(customer.address) > 50:
            logging.warning("SAL method update customer, address longer than 50 characters")
            raise FailedTransaction("The address field cannot exceed 50 characters, please try again!")
        elif len(customer.address) == 0:
            logging.warning("SAL method update customer, address left empty")
            raise FailedTransaction("The address field cannot be left empty, please try again!")
        elif customer.address.__contains__(3 * ","):
            logging.warning("SAL method update customer, address in incorrect format")
            raise FailedTransaction("The address must follow the format: house number,street name containing St / Ave "
                                    "/ etc, City, State, ZIP, please try again!")
        else:
            logging.info("Finishing SAL method update customer")
            updated_customer = self.customer_dao.create_customer(customer)
            return updated_customer

    def service_delete_customer(self, customer_id: int) -> bool:
        logging.info("Beginning SAL method delete customer")
        result = self.customer_dao.delete_customer(customer_id)
        if result is False:
            logging.warning("SAL method delete customer, no customer found to delete")
            raise FailedTransaction("This customer cannot be found so nothing was deleted, please try again!")
        else:
            logging.info("Finishing SAL method delete customer")
            return result

