from collections import Counter

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]
# общее количество запросов:
queries_amount = len(queries)
# количества слов, из которрых состоят запросы:
words_amount = []
# колилчество слов в каждом запросе:
words_in_queries = []

for i in queries:
    words_in_queries.append((len(i.split())))
    if len(i.split()) not in words_amount:
        words_amount.append((len(i.split())))

for words in words_amount:
    n = words_in_queries.count(words)
    result = (n * 100) / queries_amount
    print(f'в {queries_amount} запросах {n} строк из {words} слов = {round(result, 2)}%')

print()
# -------------> доработано: <-------------
# так действительно гораздо проще, спасибо
magic_counter = Counter(words_in_queries)
for i in magic_counter.items():
    result = (i[1] * 100) / queries_amount
    print(f'в {queries_amount} запросах {i[1]} строк из {i[0]} слов = {round(result, 2)}%')
# -------------> доработано: <-------------
