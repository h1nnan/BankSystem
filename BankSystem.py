from contextlib import nullcontext

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
            return 0
        return self.accList[n]

    def transferMoney(self, fUsername, tUsername, amount):
        h1 = self.findAcc(fUsername)
        h2 = self.findAcc(tUsername)
        if h1 == 0 or h2 == 0:print("Account doesnt exist")
        elif h1==h2:print("Cannot send money to self")
        elif h2 == tUsername and h1==fUsername:
            h1.getGirocard(fUsername).


    def takeMoney(self):
        pass

    def viewBalance(self):
        pass

    def viewBalanceHistory(self):
        pass