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
        pass

    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        logging.info("Beginning SAL method get customer by ID")
        pass

    def service_login(self, username: str, password: str) -> Customer:
        logging.info("Beginning SAL method login")
        pass

    def service_update_customer(self, customer: Customer) -> Customer:
        logging.info("Beginning SAL method update customer")
        pass

    def service_delete_customer(self, customer_id: int) -> bool:
        logging.info("Beginning SAL method delete customer")
        if type(customer_id) != int:
            logging.warning("SAL method delete customer, customer ID not an integer")
            raise FailedTransaction("The customer ID field must be an integer, please try again!")
        else:
            result = self.customer_dao.delete_customer(customer_id)
            if result is False:
                logging.warning("SAL method delete customer, no customer found to delete")
                raise FailedTransaction("This customer cannot be found so nothing was deleted, please try again!")
            else:
                logging.info("Finishing SAL method delete customer")
                return result

