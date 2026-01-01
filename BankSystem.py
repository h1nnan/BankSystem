import Person
import Girocard



class BankSystem (Person, Girocard):

    def __init__(self):
        self.accList = []

    def createAccount(self, firstName, lastName, dateOfBirth, occupation, password,username,balance):
        account = Person.Person(firstName, lastName, dateOfBirth, occupation, password,username)
        account.setGirocard(username,balance)
        self.accList.append(account)
        return account

    def findAcc(self, username):
        n = 0
        try:
            while self.accList[n].getUsername() != username:
                n += 1
        except IndexError:
            return ""
        return self.accList[n]

    def transferMoney(self, fUsername, tUsername, amount):
        h1 = self.findAcc(fUsername)
        h2 = self.findAcc(tUsername)
        if h1 == 0 or h2 == 0:print("Account doesnt exist")
        elif h1==h2:print("Cannot send money to self")
        elif h2 == tUsername and h1==fUsername:
            h1NewCurrentBalance = h1.getGirocard(fUsername).getBalance(h1)
            h2NewCurrentBalance = h2.getGirocard(fUsername).getBalance(h2)
            h2.setGirocard(fUsername, amount+h2NewCurrentBalance)
            h1.setGirocard(fUsername,  h1NewCurrentBalance - amount)

            h1.getGirocard(h1).setBalanceHistory(f"From: {h1} to {h2}: -{amount}")
            h2.getGirocard(h1).setBalanceHistory(f"From: {h1} to {h2}: +{amount}")

    def takeMoney(self, amount, acc):
        acc = self.findAcc(acc)
        currentBalance = acc.getGirocard(acc).getBalance()
        acc.getGirocard(acc).setBalance(currentBalance - amount)

    def viewBalance(self, acc):
        print(self.findAcc(acc).getGirocard(acc).getBalance())

    def viewBalanceHistory(self, acc):
        h1 = self.findAcc(acc).getGirocard(acc).getBalanceHistory()
        for h in h1: print(h)
