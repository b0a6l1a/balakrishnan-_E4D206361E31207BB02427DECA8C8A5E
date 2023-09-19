class BankAccount:
  def_init_(self,account_number,
            account_holder_name,
initial_balance=0.0)
self._account_number =account_number
self._account_holder_name=account_holder_name
self._account_balance=initial_balance
def deposit(self, amount): 
  if amount > 0: 
self._account_balance += amount  print(f"Deposited $ {amount:.2f} into account{self._account_number}")
 else: 
print("Invalid deposit amount. Please deposit a positive amount.") def withdraw(self, amount): if amount > 0: 
if self._account_balance >= amount: self._account_balance
-= amount
print(f"Withdrew $ {amount:.2f} from account {self._account_number}")
else: 
print("Insufficient balance. Cannot withdraw.") 
else: 
print("Invalid withdrawal amount. Please withdraw a positive amount.")
def display_balance(self): print(f"Account{self._account_number} balance: $ {self._account_balance:.2f}")
  account1.deposit(500.0)
account1.withdraw(200.0)
account1.display_balance()
