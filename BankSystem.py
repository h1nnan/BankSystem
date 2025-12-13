import Person
import Girocard

class BankSystem (Person, Girocard):


    def createAccount(self, firstName, lastName, dateOfBirth, occupation, password,username):
        account = Person.Person(firstName, lastName, dateOfBirth, occupation, password,username)

    def aquireGirocard(self):
        pass

    def transferMoney(self):
        pass

    def takeMoney(self):
        pass

    def viewBalance(self):
        pass

    def viewBalanceHistory(self):
        pass

