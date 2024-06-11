import random
import string

# Функция для создания рандомного пароля из 8 символов
def random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))
password = random_password()

# Функция для записи пользователя в файл
def write_user_to_file(user_data, password, filename):
    with open(filename, 'a') as file:
        file.write(user_data + ' - ' + password + '\n')

# Главная часть программы
if __name__ == "__main__":
    # Запускаем цикл для ввода пользователей
    while True:
        # Получаем данные от пользователя
        user_name = input("Введите имя пользователя (или 'exit' для выхода): ")
        
        # Проверяем условие выхода из цикла
        if user_name.lower() == 'exit':
            break
        
        # Записываем пользователя и рандомный пароль в файл
        write_user_to_file(user_name, password, 'userspasses.txt')

    print("Данные пользователей записаны в файл 'userspasses.txt'.")
