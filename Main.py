from BankSystem import BankSystem



class Main:
    banksystem = BankSystem()
    transfer = banksystem.createAccount("Transfer from self", "Transfer","1-1-1111","Transfer","peronal2322","hfdh7483ytr87fiewuhf",99999999999999999999999)
    emma = banksystem.createAccount("Emma", "Johnson", "14-03-2003", "Designer", "emma_j", "Ej482",93458)
    liam = banksystem.createAccount("Liam", "O'Connor", "22-07-2001", "Engineer", "liamoc", "Lo915",3948394)
    sofia = banksystem.createAccount("Sofia", "Martinez", "09-11-2004", "Student", "sofiam", "Sm274",2000)
    noah = banksystem.createAccount("Noah", "Williams", "18-01-2002", "Researcher", "noahw", "Nw638",47.44)
    aisha = banksystem.createAccount("Aisha", "Al-Farsi", "30-05-2005", "Medical Intern", "aishaf", "Af509",9834)
    kenji = banksystem.createAccount("Kenji", "Tanaka", "12-12-2000", "Software Developer", "kenjit", "Kt821",98394.02)
    amara = banksystem.createAccount("Amara", "Okafor", "06-04-2003", "Entrepreneur", "amarao", "Ao147",3238.3)
    lucas = banksystem.createAccount("Lucas", "Moreau", "25-09-2001", "Marketing Analyst", "lucasm", "Lm396",2000.02)
    fatima = banksystem.createAccount("Fatima", "Zahra", "08-02-2004", "Law Student", "fatimaz", "Fz684",20393)
    mateo = banksystem.createAccount("Mateo", "Rossi", "19-06-2002", "Business Consultant", "mateor", "Mr752",1300)
    priya = banksystem.createAccount("Priya", "Sharma", "27-10-2003", "Data Analyst", "priyas", "Ps918",9000)
    youssef = banksystem.createAccount("Youssef", "Haddad", "04-08-2001", "Civil Engineer", "youssefh", "Yh305",3948)
    elena = banksystem.createAccount("Elena", "Petrova", "15-01-2000", "UX Researcher", "elenap", "Ep864",9873)
    diego = banksystem.createAccount("Diego", "Fernandez", "11-11-2004", "Journalism Student", "diegof", "Df591",2653)
    mina = banksystem.createAccount("Mina", "Park", "03-03-2002", "Product Manager", "minap", "Mp246",8374893)
    def __init__(self):
        self.current = None
        self.banksystem = BankSystem()
        self.signIn = False
        current = None

    def system(self):

        print("Welcome to Bank System")
        while True:
            taken = True
            n = int(input("""Welcome to the interface!
                     You have the following Options, please Press the corresponding number to continue.:
                     [1]Create a new account
                     [2]Sign into your account
                     [3]Transfer from your account
                     [4]View Balance history
                     [5]View Account Information
                     [6]Exit"""))
            if n == 1:
                print("Please create your account")
                firstName = input("Please enter your first name: ")
                lastName = input("Please enter your last name: ")
                dob = input("Please enter your Date of Birth in dd/mm/yyyy: ")
                occ = input("Please enter your occupation: ")
                un = ""
                while taken:
                    un = input("Please enter your unsername: ")
                    taken = False if un == self.banksystem.findAcc(un).username else True
                pwd = input("Please enter your password: ")
                balance = int(input("Please enter the amount of money you'd like to pre-deposit: "))
                person = self.banksystem.createAccount(firstName, lastName, dob,occ, un, pwd,balance)
                self.signIn = True
            elif n == 2:
                exit = False
                attempts = 3
                print("Please Sign in to your account")
                while not exit:
                    username = input("Please enter your username: ")
                    pwd = input("Please enter your password: ")
                    if self.banksystem.findAcc(username).username == username and self.banksystem.findAcc(username).password == pwd:
                        self.signIn = True
                        print(f"Welcome {username}")
                        exit = True
                    else:
                        print("Please enter correct username and password")
                        con = input("Do you wish to continue? (y/n): ")
                        attempts -= 1
                        if con == "n" or attempts == 0: break

            elif n == 3:
               if self.signIn:
                   too = input("Username of the receiver")
                   iban = input ("IBAN of the receiver")
                   amount = int(input("Please enter the amount of money you would like to send: "))
                   self.banksystem.transferMoney(self.current,too,amount)
               else:
                   print("You are not signed in")

            elif n == 4:
                if self.signIn:
                    self.banksystem.viewBalanceHistory(self.current)
                else:
                    print("You are not signed in")
            elif n == 5:
                print(f""" 
                            Account information:
                            
                            first name: {self.current.firstName}
                            last name: {self.current.lastName}
                            D.of.B.: {self.current.dateOfBirth}
                            Occupation: {self.current.occupation}
                            Username: {self.current.username}
                            Password: {self.current.password}
                           
                           Tatal Account Balance: {self.current.balance}""")
            elif n == 6:
                print("Thank you for using our Bank System")
                break





