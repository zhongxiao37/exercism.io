import time
import threading

lock = threading.Lock()

class BankAccount(object):

    def __init__(self):
        self.status = None
        pass

    def get_balance(self):
        if self.status != 'open':
            raise ValueError('account is not open')
        return self.balance

    def open(self):
        if self.status == 'open':
            raise ValueError('account is already open')
        self.status = 'open'
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('amount should be larger than 0')
        if self.status != 'open':
            raise ValueError('account is not open')
        
        with lock:
            self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError('amount should be larger than 0')
        if self.status != 'open':
            raise ValueError('account is not open')
        if amount > self.balance:
            raise ValueError('balance is not enough')

        with lock:            
            self.balance -= amount

    def close(self):
        if self.status != 'open':
            raise ValueError('account is not open')
        self.status = 'closed'
