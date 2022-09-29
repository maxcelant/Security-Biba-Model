class Object:
    def __init__(self, name='', balance=0.00):
        self.name = name
        self.balance = balance
    
    def __repr__(self):
        return f'(Name:{self.name}, Balance:{self.balance})'