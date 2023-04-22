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

    def change_client(self, query, select):
        if select == 1:
            self.cur.execute(query)
            self.conn.commit()
        elif select == 2:
            self.cur.execute(query)
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

    def find_client(self, select, query):
        if select == 1:
            self.cur.execute(query)
            print(self.cur.fetchall())
        elif select == 2:
            self.cur.execute(query)
            print(self.cur.fetchall())

if __name__ == '__main__':
    
    conn = psycopg2.connect(database="client_manager",user='postgres',password='q1w2e3r4tyu')
    with conn.cursor() as cur:
        start = DB(cursor=cur, connect=conn)
        start.create_db()
        start.add_client(name='Никита', surname='Кирсанов' ,email='123@gmail.com')
        start.add_phone(number='+123', client_id='1')
        # start.delete_phone(client_id='1')
        # start.delete_client(client_id='1')

        change_select = int(input("""\nВыберите данные, с которыми хотите работать:
        1.Имя, фамилия, email;
        2.Номер телефона;
        Введите нужную цифру: """))

        if change_select == 1:
            choice = 1
            counter = 0
            while choice != 0:
                choice = int(input("""\nВыберите или добавьте параметры, которые хотите изменить:
                1.Имя;
                2.Фамилия;
                3.Email;
                0.Выход;
                Выберите нужную цифру: """))
                if choice == 1:
                    name_data = input("\nВведите новое имя: ")
                    counter += 1
                    if counter == 1:
                        data_for_change = "name='%s'" % name_data
                    else: 
                        data_for_change = data_for_change + ", name='%s'" % name_data
                elif choice == 2:
                    surname_data = input("\nВведите новую фамилию: ")
                    counter += 1
                    if counter == 1:
                        data_for_change = "surname='%s'" % surname_data
                    else:
                        data_for_change = data_for_change + ", surname='%s'" % surname_data
                elif choice == 3:
                    email_data = input("\nВведите новый email: ")
                    counter += 1
                    if counter == 1:
                        data_for_change = "email='%s'" % email_data
                    else:
                        data_for_change = data_for_change + ", email='%s'" % email_data
            query = "UPDATE clients SET " + data_for_change + "WHERE id=%s" % '1'
            start.change_client(query=query, select=change_select)

        elif change_select == 2:
            data_for_change = input("\nНапишите новый номер телефона: ")
            query = "UPDATE clientphone SET number='%s'" % data_for_change + " WHERE id=%s" % '1'
            start.change_client(query=query, select=change_select)

        find_select = int(input("""\nВыберите по каким данным осуществлять поиск:
        1. По имени, фамилии и email;
        2. По номеру телефона;
        Введите нужную цифру: """))

        if find_select == 1:
            choice = 1
            counter = 0
            while choice != 0:
                choice = int(input("""\nВыберите или добавьте параметры, по которым хотите осуществить поиск:\n
                1.Имя;
                2.Фамилия;
                3.Email;
                0.Выход;
                Выберите нужную цифру: """))
                if choice == 1:
                    name_data = input("\nВведите имя: ")
                    counter += 1
                    if counter == 1:
                        data_for_find = "name='%s'" % name_data
                    else:
                        data_for_find = data_for_find + " AND name='%s'" % name_data
                elif choice == 2:
                    surname_data = input("\nВведите фамилию: ")
                    counter += 1
                    if counter == 1:
                        data_for_find = "surname='%s'" % surname_data
                    else:
                        data_for_find = data_for_find + " AND surname='%s'" % surname_data
                elif choice == 3:
                    email_data = input("\nВведите email: ")
                    counter += 1
                    if counter == 1:
                        data_for_find = "email='%s'" % email_data
                    else:
                        data_for_find = data_for_find + "email='%s'" % email_data
            query = "SELECT id, name, surname, email FROM clients WHERE " + data_for_find + ";"            
            start.find_client(select=find_select, query=query)
            
        elif find_select == 2:
            data_for_find = input("\nВведите номер телефона, по которому хотите осуществить поиск: ")
            query = "SELECT c.id, c.name, c.surname, c.email FROM clients c JOIN clientphone cp ON cp.client_id = c.id WHERE cp.number='%s'" % data_for_find + ";"
            start.find_client(select=find_select, query=query)
    conn.close()