class Customer:

    def __init__(self, customer_id: int, first_name: str, last_name: str, password: str, email: str,
                 phone_number: str, address: str):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.phone_number = phone_number
        self.address = address
