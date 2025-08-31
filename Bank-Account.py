import  json
import os 

data_file = "ACCOUNT.json"

def view_accounts():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return {}

def save_accounts(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

class account:
    def __init__(self, acc_num, name):
        self.acc_num = str(acc_num)
        self.name = name
        self.accounts = view_accounts()

        if self.acc_num not in self.accounts:
            self.accounts[self.acc_num] = {"name": self.name, "balance": 0}
            save_accounts(self.accounts)
    
    def debit(self):
        x = int(input("Enter amount to debit : $ "))
        if self.accounts[self.acc_num]["balance"] < x:
            print("❌ Insufficient Balance!")
            return
        else:
            self.accounts[self.acc_num]["balance"] -= x
            print("$",x,"Debited Success")
            save_accounts(self.accounts)
            print("Your account Balance = ", "$",self.accounts[self.acc_num]["balance"])

    def credit(self):
        x = int(input("Enter amount to credit: $ "))
        self.accounts[self.acc_num]["balance"] += x
        save_accounts(self.accounts)
        print("$",x,"Credited Success")
        print("Your account Balance = ", "$",self.accounts[self.acc_num]["balance"])

    def info(self):
        print("Hi.." , self.name, "Your Account Is Active... ")
        print("ACCOUNT NUMBER",self.acc_num,"\nACCOUNT BALANCE $", self.accounts[self.acc_num]["balance"])
        if self.accounts[self.acc_num]["balance"]>=100:
            deb = input(" Now DO YOU WANT TO DEBIT/CREDIT YOUR MONEY ENTER Debit/Credit\nOTHERWISE ENTER Cancel = ").strip().lower()
            if deb == "debit":
                account.debit(self)
            elif deb == "credit":
                account.credit(self)
            elif deb == "cancel":
                print("THANKU \U0001F607")
            else:
                print("Invalid Input...")
        else:
            print("YOUR ACCOUNT BALANCE IS LOW YOU CAN'T MAKE WITHDRAWAL")
            print("MAIN BALANCE $", self.accounts[self.acc_num]["balance"])


def menu(account):
    while True:
        print("\n🧾 MENU:")
        print("1. Show Account Info")
        print("2. Credit Money")
        print("3. Debit Money")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            account.info()
        elif choice == '2':
            account.credit()
        elif choice == '3':
            account.debit()
        elif choice == '4':
            print("Thank you...")
            break
        else:
            print("Invalid choice! Try again.")

def main():
    while True:
        data = view_accounts()
        user_input = input("If you want to create an account ENTER:'open' OR Make tansactions in an existing account ENTER:'Menu' = ").strip().lower()
        if user_input == "open":
            acc_num = input("Enter your account number: ")
            if acc_num in data:
                print("You Already Have An Account")
                continue
            else:
                name = input("Enter your name: ")
                print("---YOUR ACCOUNT HAS BEEN SUCCESSFULLY OPENED---")
                acc = account(acc_num, name)
                menu(acc)
        elif user_input == "menu":
            acc_num = input("Enter your account number: ")
            if acc_num in data:
                name = data[acc_num]['name']
                acc = account(acc_num, name)
                menu(acc)
        else:
            print("Please Enter Valid Input: open/Menu")
            continue
                
        return
        
        
main()
