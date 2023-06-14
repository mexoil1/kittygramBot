import requests  # Импортируем библиотеку для работы с запросами

from telegram import Bot

bot = Bot(token='5609186344:AAH3Kd8qQMhGZ3eoViLmsNSwWinhrLgC5cU')
# Адрес API сохраним в константе
URL = 'https://api.thecatapi.com/v1/images/search'  
# Сделаем GET-запрос к API
# метод json() преобразует полученный ответ JSON в тип данных, понятный Python
response = requests.get(URL).json()

# Рассмотрим структуру и содержимое переменной response
print(response)

# Посмотрим, какого типа переменная response
print(type(response))

# response - это список. А какой длины?
print(len(response))

# Посмотрим, какого типа первый элемент
print(type(response[0])) 