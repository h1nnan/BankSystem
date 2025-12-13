import random
import datetime
import dateutil.relativedelta

class Girocard:


    def createExpirationDate(self):
        expDate = datetime.date.today() + dateutil.relativedelta.relativedelta(months=6, years=6)
        return expDate

    def createIBAN(cls):
        space = 0
        IBAN = "DE"
        while len(IBAN) < 22:
            space += 1
            ranNum = str(random.randint(0, 9))
            if space == 3:
                IBAN += " "
                space = -2
            else:
                IBAN += ranNum

        return IBAN

    def createPIN(self):
        space = 0
        PIN = ""
        while len(PIN) < 4:
            space += 1
            ranNum = str(random.randint(0, 9))

            PIN += ranNum

        return PIN

    def __init__(self, username):
        self.username = username
        self.company = "Mastercard"
        self.balance = 00.00
        self.IBAN = self.createIBAN()
        self.PIN = self.createPIN()
        self.expirationDate = self.createExpirationDate()
        self.balanceHistory = []

    def setBalance(self, balance):
        self.balance = balance

    def setUsername(self, username):
        self.username = username

    def setBalanceHistory(self, balanceHistory):
        self.balanceHistory.append(balanceHistory)

    def setExpirationDate(self, change):
        if change == True:
            self.expirationDate = self.createExpirationDate()
        else:
            pass

    def getUsername(self):
        return self.username

    def getBalance(self):
        return self.balance

    def getExpirationDate(self):
        return self.expirationDate

    def getIBAN(self):
        return self.IBAN

    def getPIN(self):
        return self.PIN

    def getBalanceHistory(self):
        return self.balanceHistory