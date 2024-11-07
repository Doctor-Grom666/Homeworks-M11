import requests
import numpy as np

# --- Библиотека requests ---

# Получаем ответ от сайта
r = requests.get('http://learn.python.ru')
print('Ответ от сайта')
print(r)

# Скачиваем изображение с сайта
image = requests.get('https://learn.python.ru/media/projects/sl1_Cj4bKxp.png')
with open('new_image.png', 'wb') as f:
    f.write(image.content)

# Загружаем файл на сервер
url = 'https://webhook.site/4c8d20e1-40ba-4a09-98c3-e979db1078d6'
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('текст для проверки загрузки файла')
with open('test.txt', 'rb') as f:
    r = requests.post(url, {'files': f})
    print('Загрузка файла')
    print(r)
    print()

# --- Библиотека numpy ---

# Создаём массивы
a = np.array([[1, 2, 3, 4.0],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [3, 4, 5, 6]])
b = np.array([[2, 3, 5, 6],
              [3, 2, 7, 9],
              [2.3, 6, 6, 7.0101],
              [2.5, 5, 4, 5.0]])

# Математические операции с массивами
print('Операции с массивами')
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** 2)
print()

# Получаем уникальные элементы из массива
print('Уникальные значения массивов')
print(np.unique(a))
print(np.unique(b))
