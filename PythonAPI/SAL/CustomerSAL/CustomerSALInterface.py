from abc import ABC, abstractmethod
from Entities import Customer


class CustomerSALInterface(ABC):

    @abstractmethod
    def service_create_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def service_login(self, username: str, password: str) -> Customer:
        pass

    @abstractmethod
    def service_update_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_delete_customer(self, customer_id: int) -> bool:
        pass
