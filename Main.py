class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_user_id(self):
        return self.user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.__user_list = []

    def add_user(self, user):
        self.__user_list.append(user)
        print(f"Пользователь '{user.get_name()}' добавлен.")

    def remove_user(self, user_id):
        for user in self.__user_list:
            if user.get_user_id() == user_id:
                self.__user_list.remove(user)
                print(f"Пользователь '{user.get_name()}' удалён.")
                return
        print("Пользователь не найден.")

    def get_user_list(self):
        return self.__user_list


def print_user_info():
    user_list = user3.get_user_list()
    for user in user_list:
        print(f"ID пользователя: {user.get_user_id()}, Логин: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

# Создание пользователей
user1 = User(1, "Лариса")
user2 = User(2, "Вова")
user3 = Admin(1, "Админ")

# Добавление обычных пользователей в список пользователей администратора
user3.add_user(user1)
user3.add_user(user2)

# Отображение пользователей
print_user_info()

# Удалить пользователя
user3.remove_user(user1.get_user_id())
user3.remove_user(3)

# Отображение пользователей
print_user_info()
