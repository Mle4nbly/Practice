import psycopg2

class DB:
    def __init__(self, cursor, connect):
        self.conn = connect
        self.cur = cursor

    def create_db(self):
        self.cur.execute("""
        DROP TABLE clientphone;
        DROP TABLE clients;
        """)

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS clients(
            id SERIAL PRIMARY KEY,
            name VARCHAR(60) NOT NULL,
            surname VARCHAR(60) NOT NULL,
            email VARCHAR(60) UNIQUE NOT NULL
        );
        """)

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS clientphone(
            id SERIAL PRIMARY KEY,
            number VARCHAR(19) UNIQUE NOT NULL,
            client_id INTEGER REFERENCES clients(id)
        );
        """)
        self.conn.commit()

    def add_client(self, name, surname, email):
        self.cur.execute("""
        DELETE FROM clientphone;
        DELETE FROM clients;
        """)

        self.cur.execute("""
        INSERT INTO clients(id, name, surname, email)
        VALUES (%s,%s,%s,%s)
        """, (1, name, surname, email))
        self.conn.commit()

    def add_phone(self, number, client_id):
        self.cur.execute("""
        INSERT INTO clientphone(id, number, client_id)
        VALUES (%s,%s,%s)
        """, (1, number, client_id))
        self.conn.commit()

    def change_client(self, client_id, data_for_change, select):
        if select == 1:
            self.cur.execute("""
            UPDATE clients SET %s WHERE id=%s;
            """, (data_for_change, client_id))
            self.conn.commit()
        elif select == 2:
            self.cur.execute("""
            UPDATE clientphone SET number=%s WHERE client_id=%s;
            """, (data_for_change, client_id))
            self.conn.commit()

    def delete_phone(self, client_id):
        self.cur.execute("""
        DELETE FROM clientphone WHERE client_id=%s;
        """, (client_id))
        self.conn.commit()

    def delete_client(self, client_id):
        self.cur.execute("""
        DELETE FROM clientphone WHERE client_id=%s;
        DELETE FROM clients WHERE id=%s;
        """, (client_id, client_id))
        self.conn.commit()

    def find_client(self, select, data_for_find):
        if select == 1:
            self.cur.execute("""
            SELECT id, name, surname, email FROM clients
            WHERE %s;
            """, (data_for_find))
            print(self.cur.fetchall())
        elif select == 2:
            self.cur.execute("""
            SELECT c.id, c.name, c.surname, c.email FROM clients c
            JOIN clientphone cp ON cp.client_id = c.id
            WHERE cp.number=%s;
            """, (data_for_find))
            print(self.cur.fetchall())

if __name__ == '__main__':
    client_id = '1'
    name = 'Никита'
    surname = 'Кирсанов'
    email = '123@gmail.com'
    number = '123123'

    conn = psycopg2.connect(database="client_manager",user='postgres',password='q1w2e3r4tyu')
    with conn.cursor() as cur:
        start = DB(cursor=cur, connect=conn)

        start.create_db()
        start.add_client(name=name, surname=surname ,email=email)
        start.add_phone(number=number, client_id=1)

        change_select = int(input("""
        Выберите данные, с которыми хотите работать:
        1.Имя, фамилия, email;
        2.Номер телефона;
        Введите нужную цифру: """))

        if change_select == 1:
            choice = 1
            counter = 0
            while choice != 0:
                choice = int(input("""
                Выберите или добавьте параметры, которые хотите изменить:
                1.Имя;
                2.Фамилия;
                3.Email;
                0.Выход;
                Выберите нужную цифру: """))
                if choice == 1:
                    name_data = input("\nВведите новое имя: ")
                    counter += 1
                    if counter == 1:
                        data_for_change = "name=" + name_data
                    else: 
                        data_for_change = data_for_change + ", name=" + name_data
                elif choice == 2:
                    surname_data = input("\nВведите новую фамилию: ")
                    counter += 1
                    if counter == 1:
                        data_for_change = "surname=" + surname_data
                    else:
                        data_for_change = data_for_change + ", surname=" + surname_data
                elif choice == 3:
                    email_data = input("\nВведите новый email: ")
                    counter += 1
                    if counter == 1:
                        data_for_change = "email=" + email_data
                    else:
                        data_for_change = data_for_change + ", email=" + email_data
            start.change_client(client_id=client_id, data_for_change=data_for_change, select=change_select)

        elif change_select == 2:
            data_for_change = input("Напишите новый номер телефона: ")
            start.change_client(client_id=client_id, data_for_change=data_for_change, select=change_select)

        find_select = int(input("""
        Выберите по каким данным осуществлять поиск:\n
        # 1. По имени, фамилии и email;\n
        # 2. По номеру телефона;\n
        # Введите нужную цифру: 
        # """))

        if find_select == 1:
            choice = 1
            counter = 0
            while choice != 0:
                choice = int(input("""
                Выберите или добавьте параметры, по которым хотите осуществить поиск:\n
                1.Имя;\n
                2.Фамилия;\n
                3.Email;\n
                0.Выход;\n
                Выберите нужную цифру: 
                """))
                if choice == 1:
                    name_data = input("Введите имя: ")
                    counter += 1
                    if counter == 1:
                        data_for_find = 'name=' + name_data
                    else:
                        data_for_find = data_for_find + ' AND name=' + name_data
                elif choice == 2:
                    surname_data = input("Введите фамилию: ")
                    counter += 1
                    if counter == 1:
                        data_for_find = 'surname=' + surname_data
                    else:
                        data_for_find = data_for_find + ' AND surname=' + surname_data
                elif choice == 3:
                    email_data = input("Введите email: ")
                    counter += 1
                    if counter == 1:
                        data_for_find = 'email=' + email_data
                    else:
                        data_for_find = data_for_find + 'email=' + email_data
            start.find_client(select=find_select, data_for_find=data_for_find)
            
        elif find_select == 2:
            data_for_find = input("Введите номер телефона, по которому хотите осуществить поиск: ")
            start.find_client(select=find_select, data_for_find=data_for_find)

        start.delete_phone(client_id=client_id)
        start.delete_client(client_id=client_id)
    conn.close()