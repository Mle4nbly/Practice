import os

# 1 и 2 задания:

cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }

# Принимает название блюд, количество персон, выдаёт список нужных продуктов.
def get_shop_list_by_dishes(dishes, count):
  shop_list = {}
  for dish in dishes:
    if dish in cook_book.keys():
        for ingredients in cook_book[dish]:
            shop_list[ingredients['ingredient_name']] = {'measure': ingredients['measure'],'quantity': ingredients['quantity'] * count}
    else:
      print(f'Блюда "{dish}" нет в кулинарной книге. Проверьте наличие блюда в книге.')
  print(shop_list)
        
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# Переносит словарь cookbook в текстовый документ.
def rewrite_the_cookbook():
  with open('recipe_book.txt', 'w') as recipe_book:
    for dish in cook_book.keys():
      recipe_book.write(f'\n{dish}\n')
      recipe_book.write(f'{len(cook_book[dish])}\n')
      for ingredients in cook_book[dish]:
        recipe_book.write(f"{ingredients['ingredient_name']} | {ingredients['quantity']} | {ingredients['measure']}\n")

rewrite_the_cookbook()

# 3 задание

location = 'C:\Milkbusiness\Codes\WF\Files'
base_path = os.getcwd()
result = os.path.abspath('C:\Milkbusiness\Codes\WF\Result.txt')
files_dict = {}
sorted_files_dict = {}

for filename in list(os.listdir(os.path.join(base_path, location))):
    with open(os.path.join(location, filename), 'r', encoding='utf-8') as file:
        line = file.readlines()
        count_lines = len(line)
        files_dict[filename] = count_lines

for value in sorted(files_dict.values()):
    for key in files_dict.keys():
        if files_dict[key] == value:
            sorted_files_dict[key] = files_dict[key]
            break

print(sorted_files_dict)
with open(result, 'w') as final_file:
    for filename in sorted_files_dict.keys():
      with open(os.path.join(location, filename), 'r', encoding='utf-8') as reading_file:
        final_file.write(f'{filename}\n')
        final_file.write(f'     {reading_file.read()}\n')





  


