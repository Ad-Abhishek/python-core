from bank_accounts import *

abhishek = BankAccount("Abhishek", 1000)
abhishek.get_balance()
abhishek.deposit(100)
abhishek.withdraw(500)

manisha = BankAccount("Manisha", 5000)
abhishek.transfer(600, manisha)

manisha.transfer(1500, abhishek)

amrit = InterestRewarsAccount("Amrit", 3000)
amrit.deposit(100)

sita = SavingAccount("Sita", 4000)
sita.withdraw(200)
