import json
from pprint import pprint
with open ('recipes.txt', 'r', encoding="utf-8") as file:
    cook_book = {}
    for recipe in file:
        ingredients = int(file.readline())
        ingredients_list = []
        for i in range(ingredients):
            ingredient_name, quantity, measure = file.readline().split(' | ')
            ingredients_list.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure.strip()
            })
        file.readline()

        cook_book[recipe.strip()] = (ingredients_list)
        
for key, value in cook_book.items():
    print(f'\n{key}\n')
    for key in value:
        print(f'{key}')

print()

def get_shop_list_by_dishes(dishes, persons):
    shop_list = {}
    for dish in dishes:
        for component in cook_book[dish]:
            if component['ingredient_name'] not in shop_list:
                shop_list[component['ingredient_name']] = {}
            for key, value in component.items():
                if value != component['ingredient_name']:
                    shop_list[component['ingredient_name']].setdefault(key, value)
                else:
                    continue
            shop_list[component['ingredient_name']]['quantity'] *= persons

    for key, value in shop_list.items():
        print("{0}: {1}".format(key,value))
get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)

