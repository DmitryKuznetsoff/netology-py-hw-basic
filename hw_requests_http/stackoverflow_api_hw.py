import requests
import datetime
import time
from pprint import pprint


def get_questions_from_stackoverflow(tag, n):
    """функция возвращает вопросы на stackoverflow с тэгом tag за прошедшие n дней:"""
    today = datetime.date.today()
    today_unix_date = int(time.mktime(today.timetuple()))
    # дата unix n дней назад:
    fromdate = today_unix_date - 86400 * n

    url = 'https://api.stackexchange.com/2.2/questions'

    params = {'page': 1,
              'pagesize': 100,
              'fromdate': fromdate,
              'todate': today_unix_date,
              'order': 'desc',
              'sort': 'creation',
              'tagged': tag,
              'site': 'stackoverflow'
              }

    result = []

    while True:
        r = requests.get(url, params=params)
        r_dict = r.json()
        # если на странице нет вопросов, останавливаем цикл:
        if not r_dict.get('items'):
            break
        else:
            for questions in r_dict.get('items'):
                # получаем дату создания вопроса в читабельном формате:
                date = questions.get('creation_date')
                date = datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
                # формируем словарь с датой вопроса, заголовком и ссылкой на вопрос:
                questions_on_page = {'date': date, 'title': questions.get('title'), 'link': questions.get('link')}
                result.append(questions_on_page)
        params['page'] += 1
    return result


if __name__ == "__main__":
    questions_dict = get_questions_from_stackoverflow('python', 2)
    pprint(questions_dict)
    print('\nобщее количество вопросов: ', len(questions_dict))
