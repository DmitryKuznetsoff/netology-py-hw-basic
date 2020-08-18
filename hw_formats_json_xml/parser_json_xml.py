import json
import xml.etree.ElementTree as ET
from collections import Counter


def parser_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        file = json.load(file)

    # находим значения ключа items:
    items = file.get('rss').get('channel').get('items')

    # находим значения ключей description в items
    descriptions_list = [items.get('description') for items in items]
    return descriptions_list


def parser_xml(xml_file):
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(xml_file, parser)
    root = tree.getroot()

    # собираем в список текст тэга description внутри тэга item:
    descriptions_list = [description.text for description in root.iterfind('./channel/item/description')]
    return descriptions_list


def get_top_10_words(descriptions_list):
    # переводим строки в списке в нижний регистр и делим по пробелу:
    descriptions_list = list(map(lambda x: x.lower().split(), descriptions_list))
    description_words = []
    # отбираем слова более 6 символов:
    for description in descriptions_list:
        more_than_six = list(filter(lambda x: len(x) > 6, description))
        description_words.extend(more_than_six)

    # используя Counter, получаем словарь слов с их количеством в списке:
    description_words = Counter(description_words)

    # сортируем словарь по возрастанию значений и выводим топ 10 слов:
    description_words = sorted(description_words.items(), key=lambda x: x[1], reverse=True)
    result = [description_words[i] for i in range(0, 10)]
    return result


if __name__ == "__main__":
    print(*get_top_10_words(parser_json('newsafr.json')), sep='\n')
    print()
    print(*get_top_10_words(parser_xml('newsafr.xml')), sep='\n')
