from pprint import pprint

def open_cook_book(file_path):
    with open('recipes.txt') as file:
        cook_book = {}
        for line in file:
          dishes = []
          dish = line.strip()
        quantity = int(file.readline().strip())
        for igridients in range(quantity):
            list_ingridients = file.readline().strip().split(' | ')
            recipe =  {}
            for i in range(len(list_ingridients)):
                recipe['ingridient_name'] = list_ingridients[0]
                recipe['quantity'] = list_ingridients[1]
                recipe['measure'] = list_ingridients[2]
                dishes.append(recipe)
            
            file.readline()
        cook_book[dish] = dishes
    pprint(cook_book, sort_dicts= False)    

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = open_cook_book()
    orders = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingridient in cook_book[dish]:
                   name = ingridient['ingridient_name']
                   quantity = int(ingridient['quantity'])* person_count
                   measure = ingridient['measure']
                   if name not in orders.keys():
                       orders[name] = {'quantity': quantity, 'measure': measure}
                   else:
                       orders[name]['quantity'] += quantity
        else:
            pprint(f'Нет блюда в меню')
    return orders


get_shop_list_by_dishes(['Омлет'], 2)

