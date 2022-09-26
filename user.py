# Created a class to store the users name and dieatary requirment
class User:
    def __init__(self, name, requirement):
        self.name = name
        self.requirement = requirement

    # custom string representation of A particular instance
    def __str__(self):
        return f'\n{self.name}'
