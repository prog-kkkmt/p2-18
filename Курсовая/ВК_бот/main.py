import re # Библиотека регулярных выражений
import random # Библиотека генерации случайных чисел
import requests # Библиотека для отправки HTTP запросов
import vk_api # Библиотека для бота
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType # Модуль для работы с Bots Long Poll API для работы с событиями
from vk_api.utils import get_random_id
# База ответов
commands = {"Привет": "Привет", "привет": "Привет ))",
            "こんにちわ": "Конитива конитива", "Hi": "Hi", "hi": "Hi ))",
            "Help": "Доступные команды: Погода (город с большой буквы), число(знак)число",
            ";0": ":0", ":0": ":000",
            "как дела": "Вполне не плохо", "как дела?": "Ну вот какие у бота могут быть дела :D",
            "как дела ?": "Ну вот какие у бота могут быть дела :D",
            "Как дела": "Пока функционирую - значит все хорошо", "Как дела?": "Ну вот какие у бота могут быть дела :D",
            "Как дела ?": "Ну вот какие у бота могут быть дела :D", "я человек": "А я бот .-.", "Погода Москва": '',
            "Погода Астрахань": '', "Погода СПб": '', "Погода Котельнич": '', "Погода Самара": '', "Погода Тюмень": '', "Погода Мытищи": ''}
# Главная функция работы бота
def main():
    print("Hello")
    # Токен, ключ для идентификации бота
    vk_session = vk_api.VkApi(
        token='Токен бота/сообщества')
    # longpoll для работы с пользователем, id бота, wait - время ожидания
    longpoll = VkBotLongPoll(vk_session, 'id бота/сообщества', wait=1)
    vk = vk_session.get_api()
    # Слушает сообщения от пользователя
    for event in longpoll.listen():
        # Если событие это новое сообщение от пользователя
        if event.type == VkBotEventType.MESSAGE_NEW:
            print('Новое сообщение:')
            print('Для меня от: ', end='')
            print(event.obj.from_id)
            print('Текст:', event.obj.text)
            print()
            # Поиск комманд в базе
            if event.obj.text in commands:
                # Показать погоду в городе по запросу к сайту
                if event.obj.text == "Погода Москва":
                    r = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?q=Moscow&APPID=e718fecef4a70834c41d4a1a688b0dba")
                    vk.messages.send(
                        # peer_id - общий id объекта, пользователя
                        peer_id=event.obj.from_id,
                        # random_id - уникальный идентификатор для предотвращения повторной отправки одинакового сообщения
                        random_id=get_random_id(),
                        # Отправка ответа ботом пользователю
                        message="Москва\nТемпература {0} ℃\nСкорость ветра {1} м/с\nВлажность {2}%".format(str(round(
                            int(r.json()['main']['temp'])-273.15, 2)), str(round(int(r.json()['wind']['speed']))),
                            str(round(int(r.json()['main']['humidity']))))
                    )
                elif event.obj.text == "Погода Мытищи":
                    r = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?q=Mytishchi&APPID=e718fecef4a70834c41d4a1a688b0dba")
                    vk.messages.send(
                        peer_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message="Мытищи\nТемпература {0} ℃\nСкорость ветра {1} м/с\nВлажность {2}%".format(str(
                            round(int(r.json()['main']['temp'])-273.15, 2)), str(round(int(r.json()['wind']['speed']))),
                            str(round(int(r.json()['main']['humidity']))))
                    )
                elif event.obj.text == "Погода Котельнич":
                    r = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?q=Kotelnich&APPID=e718fecef4a70834c41d4a1a688b0dba")
                    vk.messages.send(
                        peer_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message="Котельнич\nТемпература {0} ℃\nСкорость ветра {1} м/с\nВлажность {2}%".format(str(
                            round(int(r.json()['main']['temp'])-273.15, 2)), str(round(int(r.json()['wind']['speed']))),
                            str(round(int(r.json()['main']['humidity']))))
                    )
                elif event.obj.text == "Погода СПб":
                    r = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?q=Petersburg&APPID=e718fecef4a70834c41d4a1a688b0dba")
                    vk.messages.send(
                        peer_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message="Санкт-Петербург\nТемпература {0} ℃\nСкорость ветра {1} м/с\nВлажность {2}%".format(
                            str(round(int(r.json()['main']['temp'])-273.15, 2)),
                            str(round(int(r.json()['wind']['speed']))), str(round(int(r.json()['main']['humidity']))))
                    )
                elif event.obj.text == "Погода Астрахань":
                    r = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?q=Astrakhan&APPID=e718fecef4a70834c41d4a1a688b0dba")
                    vk.messages.send(
                        peer_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message="Астрахань\nТемпература {0} ℃\nСкорость ветра {1} м/с\nВлажность {2}%".format(str(
                            round(int(r.json()['main']['temp'])-273.15, 2)), str(round(int(r.json()['wind']['speed']))),
                            str(round(int(r.json()['main']['humidity']))))
                    )
                elif event.obj.text == "Погода Тюмень":
                    r = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?q=Tyumen&APPID=e718fecef4a70834c41d4a1a688b0dba")
                    vk.messages.send(
                        peer_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message="Тюмень\nТемпература {0} ℃\nСкорость ветра {1} м/с\nВлажность {2}%".format(str(round(
                            int(r.json()['main']['temp'])-273.15, 2)), str(round(int(r.json()['wind']['speed']))),
                            str(round(int(r.json()['main']['humidity']))))
                    )
                elif event.obj.text == "Погода Самара":
                    r = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?q=Samara&APPID=e718fecef4a70834c41d4a1a688b0dba")
                    vk.messages.send(
                        peer_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message="Самара\nТемпература {0} ℃\nСкорость ветра {1} м/с\nВлажность {2}%".format(str(round(
                            int(r.json()['main']['temp'])-273.15, 2)), str(round(int(r.json()['wind']['speed']))),
                            str(round(int(r.json()['main']['humidity']))))
                    )
                else:
                    vk.messages.send(
                        peer_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message=commands[event.obj.text]
                    )
            # Использование регулярных выражений чтобы найти и посчитать числа если ввести пример
            elif re.match(r"(\d+)([\+\-\*\/])(\d+)([\+\-\*\/])(\d+)([\+\-\*\/])(\d+)", event.obj.text):
                try:
                	vk.messages.send(
                 	   peer_id=event.obj.from_id,
               	     random_id=get_random_id(),
              	      message=eval(str(re.match(r"(\d+)([\+\-\*\/])(\d+)([\+\-\*\/])(\d+)([\+\-\*\/])(\d+)",event.obj.text).group(0)))
              	  )
                # В случае если будет деление на 0
                except:
                	vk.messages.send(
                 	   peer_id=event.obj.from_id,
               	     random_id=get_random_id(),
              	      message='Ошибка'
                	)
            elif re.match(r"(\d+)([\+\-\*\/])(\d+)([\+\-\*\/])(\d+)", event.obj.text):
                try:
                	vk.messages.send(
                 	   peer_id=event.obj.from_id,
               	     random_id=get_random_id(),
              	      message=eval(str(re.match(r"(\d+)([\+\-\*\/])(\d+)([\+\-\*\/])(\d+)", event.obj.text).group(0)))
              	  )
                except:
                	vk.messages.send(
                 	   peer_id=event.obj.from_id,
               	     random_id=get_random_id(),
              	      message='Ошибка'
                	)
            elif re.match(r"(\d+)([\+\-\*\/])(\d+)", event.obj.text):
                try:
                	vk.messages.send(
                 	   peer_id=event.obj.from_id,
               	     random_id=get_random_id(),
              	      message=eval(str(re.match(r"(\d+)([\+\-\*\/])(\d+)", event.obj.text).group(0)))
              	  )
                except:
                	vk.messages.send(
                 	   peer_id=event.obj.from_id,
               	     random_id=get_random_id(),
              	      message='Ошибка'
                	)
            # Если ни одно условие не сработало
            else:
                vk.messages.send(
                    peer_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message="Команда не найдена"
                )
        # Отображает в консоли информацию о действиях пользователя
        elif event.type == VkBotEventType.MESSAGE_REPLY:
            print('Новое сообщение:')

            print('От меня для: ', end='')

            print(event.obj.peer_id)

            print('Текст:', event.obj.text)
            print()

        elif event.type == VkBotEventType.MESSAGE_TYPING_STATE:
            print('Печатает ', end='')
            print(event.obj.from_id, end=' ')
            print('для ', end='')
            print(event.obj.to_id)
            print()

        elif event.type == VkBotEventType.GROUP_JOIN:
            print(event.obj.user_id, end=' ')
            print('Вступил в группу!')
            print()

        elif event.type == VkBotEventType.GROUP_LEAVE:
            print(event.obj.user_id, end=' ')
            print('Покинул группу!')
            print()

        else:
            print(event.type)
            print()
# Модуль для функций
if __name__ == '__main__':
    main()
