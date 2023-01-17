class Session:

    def __init__(self, session_number: int, session_id: str, customer_id: int, issue_date_time: str,
                 expire_date_time: str):
        self.session_number = session_number
        self.session_id = session_id
        self.customer_id = customer_id
        self.issue_date_time = issue_date_time
        self.expire_date_time = expire_date_time
        