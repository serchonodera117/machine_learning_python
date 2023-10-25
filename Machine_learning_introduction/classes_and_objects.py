class Person:
    is_authorized = False

    def __init__(self,name, last_name, age):
        self.name = name
        self.age = age
        self.last_name = last_name

    def check_is_authorized(self):
        self.is_authorized = True if self.age >= 18 else False

    def  introduce_yourself(self):
        myString = "you're authorized" if self.is_authorized else "you're not authorized"
        print (f"Hello {self.name} {self.last_name}, your age is: {self.age} {myString.upper()}")


singlePerson = Person("Serch", "Onodera", 18)
singlePerson.check_is_authorized()
singlePerson.introduce_yourself()