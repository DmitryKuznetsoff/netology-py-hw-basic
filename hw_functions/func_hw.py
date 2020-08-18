# Я работаю секретарем и мне постоянно приходят различные документы.
# Я должен быть очень внимателен чтобы не потерять ни один документ.
# Каталог документов хранится в следующем виде:
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def docs_management():
    # проверяет, существует ли введённый пользователем номер документа:
    def validate_doc():
        doc_number = input('введите номер документа: ')
        if doc_number in [doc.get('number') for doc in documents]:
            return doc_number  # возвращает номер документа для последующей обработки в других функциях
        else:
            print(f'документ № {doc_number} не существует')
            return False  # если введён неверный номер, возвращает False

    # проверяет, существует ли введённый пользователем номер полки:
    def validate_shelf():
        shelf_number = input('введите номер полки, на которую требуется поместить документ: ')
        if shelf_number in directories.keys():
            return shelf_number  # возвращает номер полки для последующей обработки в других функциях
        else:
            print(f'полки с номером {shelf_number} не существует')
        return False  # если введён неверный номер, возвращает False

    # поиск владельца по номеру документа:
    def get_owner_name():
        doc_number = validate_doc()
        if not doc_number:
            return  # если номер документа == False, прекращает работу функции
        else:
            for doc in documents:
                if doc_number == doc.get('number'):  # если находим входящий номер документа по ключу number
                    return print('владелец запрашиваемого документа: ', doc.get('name'))  # возвращаем имя владельца

    # поиск документа на полке по его номеру:
    def get_shelf_num():
        doc_number = validate_doc()
        if not doc_number:
            return  # если номер документа == False, прекращает работу функции
        else:
            for shelf in directories:
                if doc_number in directories.get(shelf):
                    return print(f'документ № {doc_number} находится на полке № {shelf}')

    # выводит список всех документов:
    def docs_list():
        for doc in documents:
            print(*doc.values())
        # выводим и папки просто потому что так удобно отслеживать операции с ними:
        print()
        # можно ли вывести ключи и значения словаря directories
        # с помощью **kwargs аналогично выводоу *args в 59 строке?
        for dir_keys, dir_values in directories.items():
            print(dir_keys, dir_values)
        return

    # добавление нового документа:
    def add_doc():
        shelf_number = validate_shelf()
        if not shelf_number:
            return  # если номер документа и номер полки == False, прекращает работу функции
        else:
            # если валидация прошла успешно, запрашиваем данные и пишем в список
            doc_type, doc_number, doc_owner = input(
                'введите через запятую тип документа, номер документа и имя владельца: ').split(
                ',')
        # вот из-за этих пробелов у меня ничего и не работало =)
        doc_type = doc_type.strip()
        doc_number = doc_number.strip()
        doc_owner = doc_owner.strip()
        documents.append({'type': doc_type, 'number': doc_number, 'name': doc_owner})
        directories[shelf_number].append(doc_number)
        return print(f'документ № {doc_number} был добавлен')

    # удаление документа по номеру:
    def del_doc():
        doc_number = validate_doc()
        if not doc_number:
            return  # если номер документа == False, прекращает работу функции
        else:
            for doc in documents:
                if doc_number == doc.get('number'):
                    documents.remove(doc)  # удаляем из documents:
            for shelf in directories.values():
                if doc_number in shelf:
                    shelf.remove(doc_number)  # удаляем из directories:
        return print(f'документ № {doc_number} был удалён')

    # перемещает документ из одной папки в другую:
    def move_doc():
        doc_number = validate_doc()
        if not doc_number: return
        shelf_number = validate_shelf()
        # тут более уместно было бы использовать elif вместо второго if, но как
        # в таком случае выполнить shelf_number = validate_shelf() внутри блока elif?
        if not shelf_number:
            return
        elif doc_number in directories[shelf_number]:
            return print(f'документ № {doc_number} уже находится на полке {shelf_number}')
        else:
            # находим номер документа и удаляем его со старой полки:
            for shelf in directories.values():
                if doc_number in shelf:
                    shelf.remove(doc_number)
            # находим новую полку для документа и добавляем его:
            for shelf in directories:
                if shelf_number == shelf:
                    directories[shelf].append(doc_number)
            return print(f'документ № {doc_number} был перемещён на полку {shelf_number}')

    # добавляет новую полку:
    def add_shelf():
        shelf_number = input('введите номер новой полки: ')
        # не стал писать эту проверку в отдельную функцию
        # по аналогии с validate_doc и validate_shelf
        # потому что она нужна только в этом случае
        if shelf_number in directories:
            return print(f'полка с номером {shelf_number} уже существует')
        else:
            directories.update({shelf_number: []})
            return print(f'папка № {shelf_number} была создана')

    # обработка команд пользователя:
    while True:
        command = input('введите команду(q - выход): ')
        if command == 'q':
            print('завершение работы')
            break  # или вместо break было бы более уместно return?
        else:
            if command == 'p': get_owner_name()
            elif command == 's': get_shelf_num()
            elif command == 'l': docs_list()
            elif command == 'a': add_doc()
            elif command == 'd': del_doc()
            elif command == 'm': move_doc()
            elif command == 'as': add_shelf()
            else: print('введена неверная команда')


docs_management()
# можно было бы не заморачиваться и прописать валидацию напрямую в каждой
# из функций, но мне показалось, что так будет правильнее. ну и интереснее =)
