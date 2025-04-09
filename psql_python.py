import psycopg2
from pprint import pprint

def create_db (conn):          # Функция, создающая структуру БД (таблицы)
    with conn.cursor() as cur:
        cur.execute("""
        DROP TABLE IF EXISTS Telephone;
        DROP TABLE IF EXISTS Person;
        """)
        conn.commit()  # фиксируем в БД

        cur.execute("""                     
                CREATE TABLE IF NOT EXISTS Person(      /* Создаем структуру БД  */
                    id SERIAL PRIMARY KEY,
                    f_name VARCHAR(50) NOT NULL,
                    s_name VARCHAR(50) NOT NULL,
                    email VARCHAR(100) NOT NULL
                );
    
                CREATE TABLE IF NOT EXISTS Telephone (
                    id SERIAL PRIMARY KEY, 
                    tel_number VARCHAR(12),
                    id_person INT NOT NULL,
                    FOREIGN KEY(id_person)	REFERENCES Person(id)	ON DELETE CASCADE
                );
                """)
        conn.commit()  # фиксируем в БД

def insert_person(conn, insert_f_name,insert_s_name, insert_email):# Функция, позволяющая добавить нового клиента.
    with conn.cursor() as cur:
        cur.execute("""            
            INSERT INTO Person (f_name,s_name, email)           
            VALUES  (%s,%s,%s) RETURNING id, f_name,s_name, email; 
        """,(insert_f_name,insert_s_name, insert_email,))
        print(cur.fetchone())

def insert_telephone(conn, insert_tel_number,insert_id_person): # Функция, позволяющая добавить телефон для существующего клиента.
    with conn.cursor() as cur:
        cur.execute("""            
                INSERT INTO Telephone (tel_number,id_person)           
                VALUES  (%s,%s) RETURNING id, tel_number, id_person; 
                """,(insert_tel_number,insert_id_person,))
        print(cur.fetchone())

def update_person(conn, insert_f_name,insert_s_name, id):   # Функция, позволяющая изменить данные о клиенте
    with conn.cursor() as cur:
        cur.execute("""            
                UPDATE Person SET f_name = %s, s_name = %s WHERE id = %s RETURNING id, f_name, s_name;          
                """,(insert_f_name,insert_s_name, id,))
        print(cur.fetchone())

def delete_telephone(conn,insert_id):   # Функция, позволяющая удалить телефон для существующего клиента
    with conn.cursor() as cur:
        cur.execute("""            
                DELETE FROM Telephone WHERE id=%s RETURNING id,tel_number,id_person;           
                    """,(insert_id,))
        print(cur.fetchone())

def delete_person(conn,insert_id):  # Функция, позволяющая удалить существующего клиента.
    with conn.cursor() as cur:
        cur.execute("""            
                DELETE FROM Person WHERE id=%s RETURNING id,f_name,s_name, email;           
                    """,(insert_id,))
        print(cur.fetchone())

def find_person(conn, insert_person_f_name = None,
                insert_person_s_name = None,
                insert_person_email = None,
                insert_telephone_number = None): # Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.
    with conn.cursor() as cur:
        cur.execute("""            
                SELECT p.id AS "ID",                        
                        p.f_name AS "Имя", 
                        p.s_name AS "Фамиилия", 
                        p.email AS "email", 
                        t.tel_number AS "Телефон"  
                FROM person p
                FULL JOIN telephone t ON p.id = t.id_person
                WHERE p.f_name = %s
                    OR p.s_name = %s
                    OR p.email = %s
                    OR t.tel_number = %s;                  
                    """,(insert_person_f_name,
                        insert_person_s_name,
                        insert_person_email,
                        insert_telephone_number,))
        pprint(cur.fetchall())




 #_________________________________

with psycopg2.connect(database="netology_d", user="postgres", password="646312") as conn:
    print('1. Функция, создающая структуру БД (таблицы): \n')
    create_db(conn);

    print('\n2. Функция, позволяющая добавить нового клиента.')
    insert_person(conn,'Алексей', 'Булгаков', 'bul@yandex.ru')
    insert_person(conn,'Александр', 'Пушкин', 'pushkin@gmail.com')
    insert_person(conn,'Maga', 'Li', 'maga_li@mail.ru')
    insert_person(conn, 'Юрий', 'Булгаков', 'bul@yandex.ru')

    print('\n3. Функция, позволяющая добавить телефон для существующего клиента.')
    insert_telephone(conn,'9115264389', 1),
    insert_telephone(conn,'9213465922', 2),
    insert_telephone(conn,'xxxxxxxxxx', 2);

    print('\n4. Функция, позволяющая изменить данные о клиенте.')
    update_person(conn,'Dart','Weider',3)

    print('\n5. Функция, позволяющая удалить телефон для существующего клиента.')
    delete_telephone(conn,1)

    print('\n6. Функция, позволяющая удалить существующего клиента.')
    delete_person(conn,3)

    print('\n7. Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.')
    find_person(conn,
                insert_person_f_name='NULL',
                insert_person_s_name='Булгаков',
                insert_person_email='NULL',
                insert_telephone_number = 'xxxxxxxxxx')
conn.close()