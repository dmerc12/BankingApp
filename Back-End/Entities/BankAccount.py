class BankAccount:

    def __init__(self, account_id: int, customer_id: int, balance: float):
        self.account_id = account_id
        self.customer_id = customer_id
        self.balance = balance

    def convert_to_dictionary(self):
        return {
            "accountId": self.account_id,
            "balance": self.balance
        }
