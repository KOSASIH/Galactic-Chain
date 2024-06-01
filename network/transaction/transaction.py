class Transaction:
    def __init__(self, transaction_id, sender, recipient, amount):
        self.transaction_id = transaction_id
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def __repr__(self):
        return f"Transaction({self.transaction_id}, {self.sender}, {self.recipient}, {self.amount})"
