from os import system

class Customer:
    def __init__(self, ID, PASSWORD, NAME):
        self.id=ID
        self.password=PASSWORD
        self.name=NAME
        self.balance=0

class Bank:
    def __init__(self):
        self.costumers=list()

    def be_costumer(self, ID, PASSWORD, NAME):
        self.costumers.append(Customer(ID, PASSWORD, NAME))
        print("Wellcome to our bank :)")

def main():
    bank = Bank()
    while True:
        system("cls")
        print("""
        ========================================
        ||                                    ||
        ||   { 1 } I'm costumer               ||
        ||                                    ||
        ||   { 2 } I want to be a costumer    ||
        ||                                    ||
        ========================================
        """)
        ch1 = input("Your choice: ")
        if ch1=="1":
            IDs = [i.id for i in bank.costumers]
            ID = input("Enter your ID: ")
            if ID in IDs:
                for costumer in bank.costumers:
                    if ID == costumer.id:
                        print("Wellcome, {}:".format(costumer.name))
                        password = input("Your password: ")
                        if password == costumer.password:
                            print("Succesfully entered.")
                            input("Press to enter to get to menu..")

                            while True:
                                system("cls")
                                print("""
        ========================================
        ||   { 1 } Show the balance           ||
        ||   { 2 } Add to your balance        ||
        ||   { 3 } Add to another balance     ||
        ||   { 4 } Take the money             ||
        ||   { 5 } Quit                       ||
        ========================================
                                """)

                                ch2=input("Your choice: ")
                                if ch2 == "1":
                                    print("Ypur nalance: ",costumer.balance)
                                    input("Press to enter to back menu..")

                                elif ch2 == "2":
                                    sum = int(input("Enter a sum of money: "))
                                    confirm = input("Are you sure to add {} $ money to your balance? Y/N \n" .format(sum))
                                    if confirm =="y"or confirm=="Y":
                                        costumer.balance += sum
                                        print("Balance added.")
                                    elif confirm=="n"or confirm=="N":
                                        print("Process canceled")
                                    else: print(" Wrong input !!")
                                    input("Press to enter to back menu..")

                                elif ch2 == "3":
                                    otherID = input("Enter ID whose you send money`")
                                    if otherID in IDs:
                                        for j in bank.costumers:
                                            if otherID == j.id:
                                                sum = int(input("Enter a sum of money: "))
                                                if sum <= costumer.balance:
                                                    confirm = input("Are you sure to add {} $ money to your balance? Y/N \n".format(sum))
                                                    if confirm =="y"or confirm=="Y":
                                                        j.balance += sum
                                                        costumer.balance -= sum
                                                        print("Balance added.")
                                                    elif confirm == "n" or confirm == "N":
                                                        print("Process canceled")
                                                    else:
                                                        print("Wrong input !!")
                                                else: print("Insufficient balance")
                                    else: print("Wrong ID!!")
                                    input("Press to enter to back menu..")

                                elif ch2 == "4":
                                    sum = int(input("Enter a sum of money: "))
                                    if sum <= costumer.balance:
                                        costumer.balance -= sum
                                        print("Process completed. Take the money. ")
                                    else:
                                        print("Insufficient balance")
                                    input("Press to enter to back menu..")

                                elif ch2 == "5":
                                    break
                                else:
                                    print("Wrong choice. Try again")
                                    input("Press to enter to back menu..")

                        else:
                            print("Wrong password. Try again")
                            input("Press to enter to back menu..")

            else:
                print("Wrong ID. Try again.")
                input("Press to enter to back menu..")


        elif ch1 == "2":
            ID = input("Your ID: ")
            NAME = input("Your name: ")
            PASSWORD = input("Your password: ")
            bank.be_costumer(ID,PASSWORD, NAME)
            input("Press to enter to back menu..")

        else:
            print("Wrong choice. Try again")
            input("Press to enter to back menu..")


if __name__ == "__main__":
    main()
else:
    print("This is a module.")













