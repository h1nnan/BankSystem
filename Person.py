from Girocard import Girocard
import datetime

class Person (Girocard):

    def age(self,DateOfBirth):
        today = datetime.date.today()
        day, month, year = DateOfBirth.split('-')
        age = today - datetime.date(int(year), int(month), int(day))
        return age

    def __init__(self, firstName, lastName, dateOfBirth, occupation, username,password):

        super().__init__(username)
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.age = self.age(self.dateOfBirth)
        self.occupation = occupation
        self.girocard = Girocard(username)
        self.transfer = False
        self.password = password

    def setUsername(self, username):
        self.username = username

    def setTransfer(self, transfer):
        self.transfer = transfer

    def setUsername(self, username):
        self.username = username

    def setBalance(self, balance):
        self.balance = balance

    def setDateOfBirth(self, dateOfBirth):
        self.dateOfBirth = dateOfBirth

    def setOccupation(self, occupation):
        self.occupation = occupation

    def setGiroCard(self, username, balance):
        self.girocard = Girocard(username, balance)

    def getBalance(self):
        return self.girocard.balance

    def getDateOfBirth(self):
        return self.dateOfBirth

    def getOccupation(self):
        return self.occupation

    def getGiroCard(self):
        return self.girocard

    def getUsername(self):
        return self.username

    def getAge(self):
        return self.age

    def getTransfer(self):
        return self.transfer

    def getPassword(self):
        return self.password