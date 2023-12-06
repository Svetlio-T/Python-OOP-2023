from inheritance_lab.multiply_inheritence.person import Person
from inheritance_lab.multiply_inheritence.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
