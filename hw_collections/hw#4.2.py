from itertools import chain
from collections import Counter

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

# создаём список из значений словаря:
result = []
for i in ids:
    result = result + ids[i]
# конвертируем в множество чтобы удалить неуникальные элементы:
result = set(result)
print(result)
# в дз сказано, что нужно вывести списком, так что:
print(list(result))

# -------------> доработано: <-------------
# собираем все values словаря в общий список:
chained = list(chain.from_iterable(ids.values()))
result = []
# чтобы сохранить порядок элементов, проходимся по списку
# и пишем неповторяющиеся элементы в result
for i in chained:
    if i not in result:
        result.append(i)
print(result)

# или просто используем Counter:
result = list(Counter(chained).keys())
print(result)
# -------------> доработано: <-------------
