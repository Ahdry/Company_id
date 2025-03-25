class User:
    def __init__(self, user_id: int, name: str):
        """Инициализация базового пользователя"""
        self._user_id = user_id  # Защищенный атрибут
        self._name = name        # Защищенный атрибут
        self._access_level = 'user'  # Защищенный атрибут с уровнем доступа по умолчанию

    # Геттеры для доступа к защищенным атрибутам
    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def access_level(self) -> str:
        return self._access_level

    def __str__(self) -> str:
        return f"ID: {self._user_id}, Имя: {self._name}, Уровень доступа: {self._access_level}"


class Admin(User):
    def __init__(self, user_id: int, name: str):
        """Инициализация администратора"""
        super().__init__(user_id, name)
        self._access_level = 'admin'  # Переопределяем уровень доступа
        self._users_list = []         # Список пользователей системы

    def add_user(self, user: User) -> None:
        """Добавление пользователя в систему"""
        if not any(u.user_id == user.user_id for u in self._users_list):
            self._users_list.append(user)
            print(f"Пользователь {user.name} добавлен в систему.")
        else:
            print(f"Пользователь с ID {user.user_id} уже существует!")

    def remove_user(self, user_id: int) -> None:
        """Удаление пользователя из системы"""
        for i, user in enumerate(self._users_list):
            if user.user_id == user_id:
                removed_user = self._users_list.pop(i)
                print(f"Пользователь {removed_user.name} удален из системы.")
                return
        print(f"Пользователь с ID {user_id} не найден!")

    def list_users(self) -> None:
        """Вывод списка всех пользователей"""
        print("\nСписок пользователей в системе:")
        for user in self._users_list:
            print(user)


# Демонстрация работы системы
if __name__ == "__main__":
    # Создаем администратора
    admin = Admin(1, "Иван Андреевич Админов")
    print(f"Создан администратор: {admin}")

    # Создаем обычных пользователей
    user1 = User(2, "Алексей Петров")
    user2 = User(3, "Мария Сидорова")
    user3 = User(4, "Сергей Иванов")

    # Администратор добавляет пользователей
    admin.add_user(user1)
    admin.add_user(user2)
    admin.add_user(user3)

    # Пытаемся добавить пользователя с существующим ID
    admin.add_user(User(2, "Дубликат Петрова"))

    # Выводим список пользователей
    admin.list_users()

    # Администратор удаляет пользователя
    admin.remove_user(3)
    admin.remove_user(99)  # Пытаемся удалить несуществующего пользователя

    # Проверяем обновленный список
    admin.list_users()