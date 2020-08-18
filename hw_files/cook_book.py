def get_dict_from_file(file):
    with open(file, 'r', encoding='utf-8') as recipes:
        # делим файл на блюда по пустой строке:
        recipes = recipes.read().split('\n\n')
        # делим каждый из элементов списка по '\n' и получаем вложенный список:
        recipes = list(map(lambda x: x.split('\n'), recipes))

    result = {}

    for dish in recipes:
        # 0 элемент списка всегда будет key для словаря result
        key = dish[0]
        values_list = []
        # элементы с индексом 2 и далее всегда будут ингридиентами:
        for ingredients in dish[2:]:
            # разбиваем строку по ' | ' и формируем словарь из получившихся элементов:
            ingredient_name, quantity, measure = ingredients.split(' | ')
            ingredients_dict = {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure}
            # словари объединяем в список и получаем value для словаря result
            values_list.append(ingredients_dict)
        # пишем key и value в словарь result:
        result.update({key: values_list})
    return result


def get_shop_list_by_dishes(dishes_list, persons):
    # формируем список необходимых ингридиентов:
    cook_book = get_dict_from_file('recipes.txt')
    result = {}
    for dish in dishes_list:
        for ingredient in cook_book.get(dish):
            name = ingredient.get('ingredient_name')
            measure = ingredient.get('measure')
            quantity = int(ingredient.get('quantity')) * persons
            # проверка на повторяющиеся ингридиенты:
            if name in result.keys():
                quantity = result.get(name).get('quantity') + quantity
            result.update({name: {'measure': measure, 'quantity': quantity}})

    return result


def get_input_from_user():
    cook_book = get_dict_from_file('recipes.txt')
    dishes_list = input('Введите наименования блюд через запятую: ').split(',')
    dishes_list = list(map(lambda x: x.strip().capitalize(), dishes_list))
    not_in_cook_book = set(dishes_list) - set(cook_book)
    # проверка, есть ли введённое блюдо в списке рецептов:
    if not_in_cook_book:
        print('Блюда отсутствуют в списке рецептов: ', *not_in_cook_book, sep='\n')
        # удаляем отсутствующие блюда, если они есть:
        dishes_list = list(filter(lambda x: x not in not_in_cook_book, dishes_list))
        # если были удалены все блюда - return
        if not dishes_list:
            return print('Ни одно из введённых блюд не найдено в списке рецептов')
        else:
            print('Из списка введённых блюд удалены отсутствующие, список изменён:', *dishes_list, sep='\n')
    persons = int(input('Введите количество персон: '))
    if persons <= 0:
        return print('Введено неверное значение')

    return dishes_list, persons


if __name__ == '__main__':

    shop_list = get_shop_list_by_dishes(*get_input_from_user())

    print('\nshop_list: ')
    for k, v in shop_list.items():
        print(k, v)
