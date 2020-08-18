import requests


class VkUser:
    # user_id принимаем в str чтобы можно было вводить не только цифровые id, но и никнеймы:
    def __init__(self, user_id: str, token):
        self.token = token
        self.id = user_id
        self.base_url = 'https://api.vk.com/method'

    def get_params(self, add_params: dict):
        """
        Формирование параметров для последующих
        запросов на основе базовых params
        """
        params = {'access_token': self.token,
                  'v': '5.120',
                  'user_ids': self.id
                  }
        if add_params:
            params.update(add_params)
            return params

    def get_request(self, method_name, params: dict):
        """
        Формирование запроса на основе базового url
        и параметров из метода get_params
        """
        response = requests.get(f'{self.base_url}/{method_name}', params=params)
        if not response.ok:
            return response.text
        else:
            return response.json()

    def get_user_info(self):
        """
        Делает get запрос по методу users.get
        Возвращает словарь с данными пользователя
        """
        params = self.get_params({'user_ids': self.id, 'fields': 'domain'})
        response = self.get_request('/users.get', params)
        vk_id = response.get('response')[0].get('id')
        first_name = response.get('response')[0].get('first_name')
        last_name = response.get('response')[0].get('last_name')
        is_closed = response.get('response')[0].get('is_closed')
        user_info = {'vk_id': vk_id,
                     'first_name': first_name,
                     'last_name': last_name,
                     'is_closed': is_closed,
                     }
        return user_info

    def get_friends_list(self):
        """
        Делает get запрос по методу friends.get
        Возвращает список id всех друзей пользователя
        """
        user_info = self.get_user_info()
        # возвращаем пустой список если у пользователя закрытый аккаунт:
        if user_info.get('is_closed'):
            print('Пользователь ограничил доступ к своему аккаунту. Невозможно получить список друзей')
            return []
        params = self.get_params({'user_id': user_info.get('vk_id'), 'name_case': 'nom', 'order': 'name'})
        response = self.get_request('/friends.get', params)
        friends_list = response.get('response').get('items')
        return friends_list

    def __and__(self, other_user):
        """
        Обращается к списку id из метода get_friends_list
        и находит общих друзей у 2х пользователей с помощью оператора &.
        Возвращает список объектов класса VkUser
        """
        user1_friends_list = set(self.get_friends_list())
        user2_friends_list = set(other_user.get_friends_list())
        mutual_friends = user1_friends_list & user2_friends_list
        # создаём объекты класса по найденным общим id и возвращаем их список:
        mutual_friends = [VkUser(user, self.token) for user in mutual_friends]
        return mutual_friends

    def __str__(self):
        """Возвращает ссылку на пользователя vk"""
        return 'https://vk.com/id' + str(self.id)


if __name__ == '__main__':
    VK_ACCESS_TOKEN = ''
    user1 = VkUser('', VK_ACCESS_TOKEN)
    user2 = VkUser('', VK_ACCESS_TOKEN)
    result = user1 & user2
    if result:
        user1_info = user1.get_user_info()
        user2_info = user2.get_user_info()
        print(f'У пользователей {user1_info.get("first_name")} {user1_info.get("last_name")} '
              f'и {user2_info.get("first_name")} {user2_info.get("last_name")} найдено общих друзей: {len(result)}')
        print(*result, sep='\n')
