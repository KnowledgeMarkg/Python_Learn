class ATM:
    def __init__(self):
        self.pin=""
        self.balance =0
        self.menu()
        self.bool = True
    while self.bool:    
        def menu(self):
             user_input = input("""
                        Hello How would like you to Proceed?
                        1. Enter 1 to Create Pin
                        2. Enter 2 to Deposit
                        3. Enter 3 to Withdraw
                        4. Enter 4 to check Balanace
                        5. Enter 5 to Exit           
""")
