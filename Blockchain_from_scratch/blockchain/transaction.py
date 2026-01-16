class Transaction:
    def __init__(self, sender, receiver, amount, fee=1):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.fee = fee

    def to_dict(self):
        return self.__dict__