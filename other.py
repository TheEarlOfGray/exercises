class Budget():
    def __init__(self, category, balance):
        self.category = category
        self.balance = balance
        
    def __repr__(self):
        return f"{self.category}: {self.balance}"
    
    def deposit(self, amount):
        self.balance += amount
        return amount
    
    def withdraw(self, amount):
        self.balance -= amount
        return amount

def store_var(budget_item):
    with open(f"{budget_item.category}.txt", "w") as file:
        file.write(f"{budget_item.category},{budget_item.balance}")

def main():
    control = 1
    while control:
        control = input("Choose: 1 - Create Budget, 2 - View Budget, 3 - Deposit, 4 - Withdraw, 0 - Close.\nResponse: ")
        if not control.isdigit():
            print("Invalid response, not number.")
            continue
        if int(control) == 1:
            pass
        elif int(control) == 2:
            pass
        elif int(control) == 3:
            pass
        elif int(control) == 4:
            pass
        elif int(control) == 0:
            control = int(control)
            continue
        else:
            print("Invalid response.")