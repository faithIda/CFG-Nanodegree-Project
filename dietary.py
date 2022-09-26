class DietaryRequirements:
    # The requirements that we allow
    requirements = [
        "veggie", 
        "vegan"
    ]

    # A string representation of an instance of this class. eg. print([className]) -> returns this
    def __str__(self):
        return f"Requirements are " + ", ".join(self.requirements)

    def get_valid_dietary_requirement(self):
        while True:
            req = input("\nWhat is your requirement? [" + self.__str__() + "]: ").lower()
            if req not in self.requirements:
                print("\nSorry, that is an incorrect input. Please try again.")
                continue
            else: 
                return req
