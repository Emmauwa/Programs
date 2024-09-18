import json

class Recipe:
    # Structure of a recipe with title, ingredients, and instructions.
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions

    def to_dict(self):
        return {
            'title': self.title,
            'ingredients': self.ingredients,
            'instructions': self.instructions
        }
    
    @staticmethod
    def from_dict(data):
        return Recipe(data['title'], data['ingredients'], data['instructions'])
    
    def __str__(self):
        ingredients_list = '\n'.join(f"- {ingredient}" for ingredient in self.ingredients)
        instructions_list = '\n'.join(f"{i + 1}. {instruction}" for i, instruction in enumerate(self.instructions))
        return (f"Title: {self.title}\n"
                f"Ingredients:\n{ingredients_list}\n"
                f"Instructions:\n{instructions_list}")


class Recipes:
    def __init__(self):
        # Initialize an empty list to store the recipes.
        self.recipes = []

    def add_recipe(self):
        title = input("Enter title: ")

        # Collect ingredients.
        ingredients = []
        print("Enter ingredients (leave blank to finish):")
        while True:
            ingredient = input("> ")
            if not ingredient:
                break
            ingredients.append(ingredient)

        # Collect instructions.
        instructions = []
        print("Enter instructions (leave blank to finish):")
        while True:
            instruction = input("> ")
            if not instruction:
                break
            instructions.append(instruction)

        # Create a new Recipe object and add it to the list.
        recipe = Recipe(title, ingredients, instructions)
        self.recipes.append(recipe)
        print(f"Recipe '{title}' added successfully!")

    def list_recipes(self):
        if not self.recipes:
            print("No recipes found.")
        else:
            for i, recipe in enumerate(self.recipes):
                print(f"{i}. {recipe.title}")

    def search_by_title(self):
        if not self.recipes:
            print("No recipes found.")
            return
        
        title = input("Enter title of Recipe you are looking for: ")
        # Search for a recipe by title, ignoring case
        for recipe in self.recipes:
            if recipe.title.lower() == title.lower():
                print(recipe)
                return
        print("No recipes found.")

    def search_by_ingredients(self, ingredient):
        # Search for recipe by ingredient, ignoring case
        for recipe in self.recipes:
            if any(ing.lower() == ingredient.lower() for ing in recipe.ingredients):
                print(recipe)
                return
        print("Recipe not found.")

    def edit_recipe(self):
        if not self.recipes:
            print("No recipes found.")
            return
        
        title = input("Enter title of recipe you want to edit: ")

        for recipe in self.recipes:
            if recipe.title.lower() == title.lower():
                # Collect ingredients.
                ingredients = []
                print("Enter ingredients (leave blank to finish):")
                while True:
                    ingredient = input("> ")
                    if not ingredient:
                        break
                    ingredients.append(ingredient)

                # Collect instructions.
                instructions = []
                print("Enter instructions (leave blank to finish):")
                while True:
                    instruction = input("> ")
                    if not instruction:
                        break
                    instructions.append(instruction)

                recipe.ingredients = ingredients
                recipe.instructions = instructions
                print(f"Recipe '{title}' edited successfully!")
                return
       
        print(f"Recipe '{title}' not found.")

    def delete_recipe(self):
        if not self.recipes:
            print("No recipes to be deleted.")
            return
        
        # Lists recipes to be chosen to be deleted
        self.list_recipes()
        
        title = input("Enter title of recipe you want to delete: ")

        # Finds recipe by title and deletes it
        for recipe in self.recipes:
            if recipe.title.lower() == title.lower():
                self.recipes.remove(recipe)
                print(f"Recipe '{title}' deleted successfully!")
                return
        
        print(f"Recipe '{title}' not found.")
    
    def save_recipes(self):
        recipe_data = [recipe.to_dict() for recipe in self.recipes]

        with open("recipes.json", "w") as file:
            json.dump(recipe_data, file, indent=4)
        print("Recipes successfully saved!")

    def load_recipes(self):
        try:
            with open("recipes.json", "r") as file:
                recipe_data = json.load(file)
            
            self.recipes = [Recipe.from_dict(data) for data in recipe_data]
            print("Recipes successfully loaded!")

        except (FileNotFoundError, json.JSONDecodeError):
            print("File not found or contains invalid data.")


def main() -> None:
    manager = Recipes()
    manager.load_recipes()  # Load existing recipes from file
    while True:
        print("\nRecipe Manager")
        print("1. Add recipe")
        print("2. View recipes")
        print("3. Search recipes by title")
        print("4. Search recipes by ingredients")
        print("5. Edit recipe")
        print("6. Delete recipe")
        print("7. Save and exit")
        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            manager.add_recipe()
        elif choice == "2":
            manager.list_recipes()
        elif choice == "3":
            manager.search_by_title()
        elif choice == "4":
            ingredient = input("Enter ingredient to search for: ")
            manager.search_by_ingredients(ingredient)
        elif choice == "5":
            manager.edit_recipe()
        elif choice == "6":
            manager.delete_recipe()
        elif choice == "7":
            manager.save_recipes()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
