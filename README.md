Задание
Вопросы по заданию
Это задание для самостоятельной работы — оно не будет проверяться экспертом.

Почему его важно и полезно выполнить:

· Загрузив своё решение в личный кабинет, вы получите эталонное решение.
· Сколько бы теории вы ни изучали, мастерство приходит только с практикой. Не научившись решать простые задачи, вы будете испытывать всё больше затруднений при переходе к более сложным.

Инструкция к выполнению

· Пройдите по шагам, описанным в задании.
· Приложите ссылку на решения в поле «Ссылка на решение» и нажмите «Отправить решение»
· Вам откроется эталонный ответ.

Сравните ваше решение с эталоном.

Задание

Создайте программу для управления клиентами на Python.Требуется хранить персональную информацию о клиентах:

имя
фамилия
email
телефон
Сложность в том, что телефон у клиента может быть не один, а два, три и даже больше. А может и вообще не быть телефона, например, он не захотел его оставлять.

Вам необходимо разработать структуру БД для хранения информации и несколько функций на Python для управления данными.

Функция, создающая структуру БД (таблицы).
Функция, позволяющая добавить нового клиента.
Функция, позволяющая добавить телефон для существующего клиента.
Функция, позволяющая изменить данные о клиенте.
Функция, позволяющая удалить телефон для существующего клиента.
Функция, позволяющая удалить существующего клиента.
Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.
Функции выше являются обязательными, но это не значит, что должны быть только они. При необходимости можете создавать дополнительные функции и классы.

Также предоставьте код, демонстрирующий работу всех написанных функций.

Результатом работы будет .py файл.

Подсказка

Не читайте этот раздел сразу, попытайтесь сначала решить задачу самостоятельно :)

Каркас кода

import psycopg2

def create_db(conn):
    pass

def add_client(conn, first_name, last_name, email, phones=None):
    pass

def add_phone(conn, client_id, phone):
    pass

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    pass

def delete_phone(conn, client_id, phone):
    pass

def delete_client(conn, client_id):
    pass

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    pass


with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
    pass  # вызывайте функции здесь

conn.close()