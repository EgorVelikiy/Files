import json
def cook_book():
    with open ('recipes.txt', 'r', encoding='utf-8') as file:
        recipes = {}
        for recipe in file:
            ingredients = int(file.readline())
            ingredients_list = []
            for i in range(ingredients):
                ingredient_name, quantity, measure = file.readline().split(' | ')
                ingredients_list.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            file.readline()
            recipes[recipe.strip()] = (ingredients_list)
        res = json.dumps(recipes, indent = 2)
        return res

print(cook_book())