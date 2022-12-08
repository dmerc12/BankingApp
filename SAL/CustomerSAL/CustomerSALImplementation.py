from DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from Entities.Customer import Customer
from SAL.CustomerSAL.CustomerSALInterface import CustomerSALInterface

class CustomerSALImplementation(CustomerSALInterface):

    def __init__(self, customer_dao: CustomerDALImplementation):
        self.customer_dao = customer_dao

    def service_create_customer(self, customer: Customer) -> Customer:
        pass

    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    def service_login(self, username: str, password: str) -> Customer:
        pass

    def service_update_customer(self, customer: Customer) -> Customer:
        pass

    def service_delete_customer(self, customer_id: int) -> bool:
        pass
