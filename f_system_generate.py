from string import ascii_lowercase, digits
from file_system import BASE_DIR, os, random

letters = ' '.join([ascii_lowercase, digits])
folder = os.path.join(BASE_DIR, 'some_data')  # только создает ПУТЬ, а не директорию!!!
os.makedirs(folder, exist_ok=True)  # создает директорию по указанному пути. Только на 1 уровень. exist_ok = True, чтобы не выдавал ошибку, если директория есть
for _ in range(10 ** 3):
    f_name = ''.join(random.sample(letters, random.randint(5, 10)))  # создаем рандомные имена файлов из letters длиной от 5 до 10 символов
    f_content = bytes(random.randint(0, 255) for _ in range(10 ** 5))  # создаем содержимое файла от 0 до 255 байт в количестве 1 млн штук
    with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:  # делаем путь к файлу
        f.write(f_content)  # записываем f_content в каждый файл







