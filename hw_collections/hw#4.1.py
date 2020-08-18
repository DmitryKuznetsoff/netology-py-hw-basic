geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

result = [items for items in geo_logs for location in items.values() if location[1] == 'Россия']
for i in result:
    print(i)

print()

# вариант попроще:
result = []
for items in geo_logs:
    for location in items.values():
        if location[1] == 'Россия':
            result.append(items)

for i in result:
    print(i)

print()

# вопрос: стоит ли испопльзовать вложенные list comprehension
# или это делает код менее читаемым? можно ли отсортировать
# данный список по ключу через lambda функцию? если да, то
# каким образом? и какой из способов будет оптимальным?

# -------------> доработано: <-------------
result = []

for visit in geo_logs:
    x = next(iter(visit.values()))  # <- либо этот вариант
    # x = list(visit.values())[0]   # <- либо этот
    if x[1] == 'Россия':
        result.append(visit)

for i in result:
    print(i)
# -------------> доработано: <-------------
