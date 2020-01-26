class User:
    def __init__(self, name, surname, birthday, email):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.email = email

    # methods
    def getFullName(self):
        return self.name + " " + self.surname

    def printInfo(self):
        print("Full name: " + self.getFullName(
            self) + '/n' + 'Birthday: ' + self.birthday + '/n' + 'E-mail: ' + self.email)
