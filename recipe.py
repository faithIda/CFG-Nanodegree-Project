# Created a class to store and format recipe data
class StoreRecipe:
    def __init__(self, item):
        self.title = item["title"]
        self.ingredients = item["ingredients"]
        self.instructions = item["instructions"]
        self.servings = item["servings"]
    def __str__(self):
        return f'\nTitle: {self.title}\n'\
               f'Ingredients: {self.ingredients}\n' \
               f'Instructions: {self.instructions}\n' \
               f'Serving: {self.servings} \n'
