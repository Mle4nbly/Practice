import psycopg2

class DB:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def create_db(self):
        conn = psycopg2.connect(database="client_manager",user=f"{self.user}",password=f"{self.password}")
        with conn.cursor() as cur:
            cur.execute("""
            DROP TABLE clientphone;
            DROP TABLE clients;
            """)

            cur.execute("""
            CREATE TABLE IF NOT EXISTS clients(
                id SERIAL PRIMARY KEY,
                name VARCHAR(60) NOT NULL,
                surname VARCHAR(60) NOT NULL,
                email VARCHAR(60) UNIQUE NOT NULL
            );
            """)

            cur.execute("""
            CREATE TABLE IF NOT EXISTS clientphone(
                id SERIAL PRIMARY KEY,
                number VARCHAR(19) UNIQUE NOT NULL,
                client_id INTEGER REFERENCES clients(id)
            );
            """)
            conn.commit()
        conn.close()

    def add_client(self, name, surname, email):
        conn = psycopg2.connect(database="client_manager",user=f"{self.user}",password=f"{self.password}")
        with conn.cursor() as cur:
            cur.execute("""
            DELETE FROM clientphone;
            DELETE FROM clients;
            """)

            cur.execute("""
            INSERT INTO clients(id, name, surname, email)
            VALUES (%s,%s,%s,%s)
            """, (1, name, surname, email))
            conn.commit()
        conn.close()

    def add_phone(self, number, client_id):
        conn = psycopg2.connect(database="client_manager",user=f"{self.user}",password=f"{self.password}")
        with conn.cursor() as cur:
            cur.execute("""
            INSERT INTO clientphone(id, number, client_id)
            VALUES (%s,%s,%s)
            """, (1, number, client_id))
            conn.commit()
        conn.close()

    def change_client(self, client_id, name, surname, email, number):
        conn = psycopg2.connect(database="client_manager",user=f"{self.user}",password=f"{self.password}")
        with conn.cursor() as cur:
            cur.execute("""
            UPDATE clients SET name=%s, surname=%s, email=%s WHERE id=%s;
            UPDATE clientphone SET number=%s WHERE client_id=%s;
            """, (name, surname, email, client_id, number, client_id))
            conn.commit()
        conn.close()

    def delete_phone(self, client_id):
        conn = psycopg2.connect(database="client_manager",user=f"{self.user}",password=f"{self.password}")
        with conn.cursor() as cur:
            cur.execute("""
            DELETE FROM clientphone WHERE client_id=%s;
            """, (client_id))
            conn.commit()
        conn.close()

    def delete_client(self, client_id):
        conn = psycopg2.connect(database="client_manager",user=f"{self.user}",password=f"{self.password}")
        with conn.cursor() as cur:
            cur.execute("""
            DELETE FROM clients WHERE id=%s;
            """, (client_id))
            conn.commit()
        conn.close()

    def find_client(self, select, name, surname, email, number):
        conn = psycopg2.connect(database="client_manager",user=f"{self.user}",password=f"{self.password}")
        with conn.cursor() as cur:
            if select == 1:
                cur.execute("""
                SELECT id, name, surname, email FROM clients
                WHERE name=%s AND surname=%s AND email=%s;
                """, (name, surname, email))
                print(cur.fetchone())
            if select == 2:
                cur.execute("""
                SELECT c.id, c.name, c.surname, c.email FROM clients c
                JOIN clientphone cp ON cp.client_id = c.id
                WHERE cp.number=%s;
                """, (number))
                print(cur.fetchone())
        conn.close()

if __name__ == '__main__':
    login = ''
    password = ''
    start = DB(user=login, password=password)
    select = 1
    # int(input("""Выберите по каким данным осуществлять поиск:\n
    # # 1. По имени, фамилии и email;\n
    # # 2. По номеру телефона;\n
    # # Введите нужную цифру: 
    # # """))
    client_id = '1'
    name = 'Никита'
    surname = 'Кирсанов'
    email = '123@gmail.com'
    number = '123123'
    new_name = 'Николай'
    new_surname = 'Кирсанов'
    new_email = '234@gmail.com'
    new_number = '234234'
    start.create_db()
    start.add_client(name=name, surname=surname ,email=email)
    start.add_phone(number=number, client_id=1)
    # start.change_client(client_id=client_id, name=new_name, surname=new_surname, email=new_email, number=new_number)
    # start.delete_phone(client_id=client_id)
    # start.delete_client(client_id=client_id)
    start.find_client(select=select, name=name, surname=surname, email=email, number=number)
    
    
