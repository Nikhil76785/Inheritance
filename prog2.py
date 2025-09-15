class Person:

    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num

    def display(self):
        print(self.name)
        print(self.id_num)

class Employee(Person):

    def __init__(self, name, id_num, salary, post):
        self.salary = salary
        self.post = post

        Person.__init__(self, name, id_num)

obj = Employee("Nikhil", 123, 1000000, "Data Scientist")

obj.display()