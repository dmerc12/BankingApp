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

