import requests
from recipe import StoreRecipe

# Making the api call
def call_diet_api_with_requirement(requirement):
    url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(requirement)
    response = requests.get(url, headers={'X-Api-Key': '4aMjDI71/zFUTVQgSk5Oow==59V4Rb7LfOul3ls3'})

    if response.status_code == requests.codes.ok:
        avail_choice = response.json()[:5]
        return avail_choice
    else:
        print("Error:", response.status_code, response.text)

def get_data_from_requiement_input(input):
    # call raw data from api
    raw = call_diet_api_with_requirement(input)

    # map all the elements in 'raw' to an instance of StoreRecipe (StoreRecipe([rawElement])) - then turning that map into a list so we can loop thruogh it and a bunch of other good stuff
    the_recipes = list(map(StoreRecipe, raw))

    # return 
    return the_recipes


# raw = [{}]
# the_recipes = [StoreRecipe()]

