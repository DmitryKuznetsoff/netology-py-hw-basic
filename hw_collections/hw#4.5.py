# def dict_gen(source_list):
#     i = -2  # индекс предпоследнего элемента списка, с которого начнётся итерация
#     in_dict = {}
#
#     while i >= -len(source_list):  # итерация с предпоследнего элемента до первого
#         tmp_dict = {}
#         if len(in_dict) == 0:  # на 1 итерации создаём первичный словарь {list[-2]:list[-1]}
#             in_dict.update({source_list[i]: source_list[-1]})
#             i -= 1
#         else:
#             tmp_dict.update({source_list[i]: in_dict})  # на 2 и последующих итерациях наращиваем уровни вложенности
#             in_dict = tmp_dict
#             i -= 1
#     return in_dict


# -------------> доработано: <-------------
# новый вариант функции. не такой извратный, как первый =)
# пофиксил косяк, из-за которого возникала ошибка в преобразовании
# вложенного списка data в список словарей в 54 строке;
# сформировал 1ый словарь до цикла и убрал из цикла ненужное
# условие и временную переменную. стало немного почище =)
def dict_gen(source_list):
    reversed_list = reversed(source_list)  # создаём копию исходного списка в обратном порядке
    last_item = next(reversed_list)  # исключаем последний элемент из последующей итерации

    in_dict = {next(reversed_list), last_item}  # создаём 1ый словарь из последнего и предпоследнего элементов списка

    for item in reversed_list:
        in_dict = ({item: in_dict})  # итерируясь по остальным элементам списка, наращиваем уровни вложенности
    return in_dict


# -------------> доработано: <-------------


source_list = ['2018-01-01', 'yandex', 'cpc', 100]
print('исходный список source_list: ')
print(source_list)

print('после преобразования в словарь target_dict: ')
target_dict = dict_gen(source_list)
print(target_dict)
print()

print('дополним данные и создадим вложенный список data: ')
data = [
    ['2018-01-01', 'yandex', 'cpc', 100],
    ['2018-01-01', 'google', 'cpc', 130],
    ['2018-01-01', 'vk', 'cpc', 90],
    ['2018-01-01', 'amazon', 'cpc', 110],
]
for record in data:
    print(record)
print()

print('преобразуем его в список словарей по аналогии с предыдущим: ')
data_dict = [dict_gen(item) for item in data]
for i in data_dict: print(i)
print()

print('отсортируем список по названию компании: ')
sort_by_name = sorted(data, key=lambda x: x[1])
for item in sort_by_name:
    print(item)
print()

print('отсортируем список по показателю cpc и выведем соответствующую компанию:')
sort_by_cpc = sorted(data, key=lambda x: x[3], reverse=True)
for item in sort_by_cpc:
    print(item)

max_cpc = sort_by_cpc[0][3]
max_cpc_company = sort_by_cpc[0][1]
print(f'максимальный показатель cpc {max_cpc} у компании {max_cpc_company}')

# всю сортировку гораздо проще производить именно со вложенным списком, а не со вложенным словарём.
# если есть аналогичные способы отсортировать словарь такой вложенности то какие?
