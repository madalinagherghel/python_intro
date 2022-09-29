from oop.banking_account import BankingAccount
account1=BankingAccount('Mada G', 'RO0001')
account2=BankingAccount('Anna A', 'RO002')

account1.account_activation(7777)
account1.account_activation(6666)
account2.account_activation(6666)

account1.sold_query()

account2.card_funding(2000)
account2.card_funding(500)

account1.card_payments(2000)