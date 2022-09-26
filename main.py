from user import User
from dietary import DietaryRequirements
from api import get_data_from_requiement_input


def run():
    # A little introduction
    print('Hello, to welcome Extra Help!')

    # Setting up the person using the application atm. 
    name = input("\nWhat is your name?: ").capitalize()
    req = DietaryRequirements().get_valid_dietary_requirement()

    # not storing - creating a new instance of a user with name and req
    person = User(name, req)


    # get the recipe data and print it out 
    data = get_data_from_requiement_input(person.requirement)
    print(f'\n Hi {person.name} here are our top 5 {person.requirement} options!')
    for x in data:
        print(x)

    # Looping through and re-running application based on users inputs
    while True:
        a = input("Do you want some more? [Y/yes or N/no]: ").lower()
        if a not in ["no", "yes", "y", "n"]:
            print("Please try again: ")
            continue
        elif a == "yes" or a == "y":
            run()
        else:
            print("Thanks for using Extra Help, see you next time!")
            quit()


if __name__ == "__main__":
    run()