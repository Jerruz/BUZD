import os
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # путь к корню проекта
if __name__ == '__main__':
    print()
    print(BASE_DIR)
    print(os.path.dirname(__file__))  # выводит имя директории, где находится файл
    print(os.path.abspath('21.10.py'))  # выводит абсолютный путь к файлу
    parent_dir = os.path.dirname(BASE_DIR)  # выводит директорию на уровень выше, чем BASE_DIR
    print(parent_dir)

    print([file_name for file_name in os.listdir(os.path.dirname(__file__)) if file_name.endswith('.py')])
    print(os.path.basename(__file__))  # посмотреть имя файла

    print(os.listdir(BASE_DIR))  # список файлов и папок в директории

#
#
#
#
#
#
#
#
