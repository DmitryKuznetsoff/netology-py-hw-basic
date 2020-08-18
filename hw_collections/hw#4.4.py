stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

# сортируем словарь по значению от большего к меньшему
# конвертируем в список и берём первый элемент:
result = list(sorted(stats.items(), key=lambda x: x[1], reverse=True))
print(result[0][0])

print()

# вариант попроще:
# создаём список со значениями и находим из них максимальное:
max_value = max([values for values in stats.values()])
# в цикле for ищем значние, совпадающее с максимальным и выводим ключ:
for key, value in stats.items():
    if value == max_value:
        print(key)

print()

# -------------> доработано: <-------------
# интересное решение с помощью zip, спасибо
result = max(zip(stats.values(), stats.keys()))
print(result[1])
# -------------> доработано: <-------------

print()

result = max(stats, key=stats.get)
print(result)