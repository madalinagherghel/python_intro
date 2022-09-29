class BankingAccount:
    # constructor
    def __init__(self, name, iban):
        # attributes, fields
        self.name=name
        self.iban=iban
        self.sold=0
        self.active= False
        self.pin = 6666
        self.activation_try = 0

    def sold_query(self):
        print(f'Account owner is: {self.name}')
        print(f'IBAN is: {self.iban}')
        print(f'Sold is: {self.sold}')
        print(f'Status is: {self.active}')
        print(f'Activation try number is: {self.activation_try}')
        print('-------------')

    def account_activation(self, user_pin):
        self.hi()
        if user_pin ==self.pin:
            print(f'Activated card')
            self.active=True
        else:
            print(f'Wrong pin')
            self.activation_try=self.activation_try+1

    def card_funding(self, amount_deposited):
        self.hi()
        self.sold= self.sold + amount_deposited
        print(f'You deposited {amount_deposited}')
        print(f'You currently have in your account {self.sold}')

    def card_payments(self, spent_sum):
        self.hi()
        if spent_sum<=self.sold:
            self.sold=self.sold-spent_sum
            print(f'You have spent the sum of: {spent_sum}')
            print(f'You have left into your account: {self.sold}')
        else:
            print('Insufficient money')

    def hi(self):
        print(f'Hello {self.name}')
# we cannot put a method into another method
# we call a method inside another method
