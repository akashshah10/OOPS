class Atm:
    
    #Constructor
     
    def __init__(self):
        self.pin = ""
        self.balance = 0
    
        self.menu()
    
    def menu(self):
        user_input = input("""
                        Hello, how would you like to proceed?
                           1. Enter 1 to create pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
 """)
        if user_input == "1":
            self.create_pin()

        elif user_input == "2":
            print("Deposit")

        elif user_input == "3":
            print("Deposit")

        elif user_input == "4":
            print("Check balance")

        else:
            print("Bye")


    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Pin set succesfully")

atm = Atm()