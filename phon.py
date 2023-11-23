from random import *
import json

phone_book = {}

def new():
    name = input('Введите имя абонента ')
    phone = input('Введите телефоны абонента через запятую ').split(',')
    email = input('Введите электронный адрес ')
    print('Незабудьте сохранить введенный контакт')
    if "@" in email:
        phone_book[name] = {'phones': phone, 'email': email}
    else:
        phone_book[name] = {'phones': phone}
    

def save():
    with open('phone_book.json', 'a') as file:
        json.dump(phone_book, file,indent=4, ensure_ascii=False)
    print('Абонент успешно добавлен в телефонную книгу')




while True:
    command = input('Введите команду ')
    if command == '/start':                                      # Начало работы 
        print('Добро пожаловать в вашу телефонную книгу')
    if command == '/stop':                                       # Конец работы
        break
    elif command == '/all':                                      # Показать список контактов
        print(phone_book.keys())
    elif command == '/new':                                      # Добавить новый контакт
        new()
    elif command == '/save':                                     # Сохранить контакт
        save()
    elif command == '/show':                                     # Показать данные контакта
        name_1 = input('Введите имя абонента ')
        print(phone_book[name_1])
    elif command == '/del':                                      # Удаление контакта
        name_2 = input('Введите имя абонента ')
        del(phone_book[name_2])
        print('Абонент успешно удален из телефонной книги')
    elif command == '/load':                                     #Загрузить файл контактов
        with open('phone_book.json') as file:
            phone_book=json.load(file)