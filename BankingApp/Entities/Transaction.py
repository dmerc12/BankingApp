class Transaction:

    def __init__(self, transaction_id: int, date_time: str, transaction_type: str, account_id: int, amount: float):
        self.transaction_id = transaction_id
        self.date_time = date_time
        self.transaction_type = transaction_type
        self.account_id = account_id
        self.amount = amount

    def convert_to_dictionary(self):
        return {
            "transaction_id": self.transaction_id,
            "date_time": self.date_time,
            "transaction_type": self.transaction_type,
            "account_id": self.account_id,
            "amount": self.amount
        }
