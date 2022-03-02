#Write a function to connect posgresql database using psycopg2
# Input: host, user, password, database
# Output: connection object
from dataclasses import dataclass
import psycopg2
import datetime 
import date_tz_formater as dtf

def connect():
    host = "localhost"
    user = "al-amin"
    password = "postgres"
    database = "postgres"
    try:
        conn = psycopg2.connect(host=host, user=user, password=password, database=database)
        return conn
    except:
        print("Unable to connect to the database")
        return None

# get the connection object and create employee table with name, bitrhday, and salary  and insert some data
def create_employee_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(id SERIAL PRIMARY KEY, name VARCHAR(100), birthday DATE, salary NUMERIC(10,2))")
    conn.commit()
    conn.close()

#def create cutomer table with name, purchase_date, and price
def create_customer_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS customer(id SERIAL PRIMARY KEY, name VARCHAR(100), purchase_date text, price NUMERIC(10,2))")
    conn.commit()
    conn.close()

# insert data into employee table
def insert_employee(name, birthday, salary):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO employee(name, birthday, salary) VALUES(%s, %s, %s)", (name, birthday, salary))
    conn.commit()
    conn.close()

# insert data into customer table
def insert_customer(name, purchase_date, price):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO customer(name, purchase_date, price) VALUES(%s, %s, %s)", (name, purchase_date, price))
    conn.commit()
    conn.close()

# get all data from employee table and print it
def get_employee():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()
    return rows

# get purchase_date from customer table and print it
def get_customer():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT purchase_date FROM customer")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()
    return rows
#drop employee table
def drop_employee_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("DROP TABLE employee")
    conn.commit()
    conn.close()

#drop customer table
def drop_customer_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("DROP TABLE customer")
    conn.commit()
    conn.close()

data = [(1, "Ano Taro", datetime.datetime(2011, 1, 1), 100000),
        (2, "Kono Taro", datetime.datetime(2012, 1, 1), 300000),
        (3, "Sono Taro", datetime.datetime(2013, 1, 1), 400000),
        (4, "Henna Taro", datetime.datetime(2014, 1, 1), 500000)]



customers = [(1, "Ebi Taro", "1990-03-02", 100000),
                (2, "Kuma Taro", "2022-03-02", 300000),
                (3, "J Trump", "1999-03-02", 400000),
                (4, "A Trump", "1990-03-02", 500000)]

# create_employee_table()
# for data_tuple in data:
#     insert_employee(data_tuple[1], data_tuple[2], data_tuple[3])
# get_employee()
# drop_employee_table()

#sting to datetime
def string_to_datetime(string):
    return datetime.datetime.strptime(string, "%Y-%m-%d")


@dataclass
class Employee:
    id: int
    name: str
    birthday: datetime.datetime
    salary: float

    def __str__(self):
        return f"{self.id} {self.name} {self.birthday} {self.salary}"

@dataclass
class Customer:
    id: int
    name: str
    purchase_date: str
    price: float

    def __init__(self, id, name, purchase_date, price):
        self.id = id
        self.name = name
        self.purchase_date = self.hex_to_int(purchase_date)
        self.price = price

    # covert hex string to int
    def hex_to_int(self, hex_string):
        return int(hex_string, 16)

    def __str__(self):
        return f"{self.id} {self.name} {self.purchase_date} {self.price}"       


def get_employee_from_db():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()
    employees = []
    for row in rows:
        employees.append(Employee(row[0], row[1], string_to_datetime(row[2]), row[3]))
    conn.close()
    return employees

#get customer from db
def get_customer_from_db():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM customer")
    rows = cur.fetchall()
    customers = []
    for row in rows:
        customers.append(Customer(row[0], row[1], row[2], row[3]))
    conn.close()
    return customers


#get employee from db and print it
def get_employee_from_db_and_print():
    employees = get_employee_from_db()
    for employee in employees:
        print(employee)

#get customer from db and print it
def get_customer_from_db_and_print():
    customers = get_customer_from_db()
    for customer in customers:
        print(customer)

get_customer_from_db_and_print()
# drop_customer_table()
# create_customer_table()
# for customer_tuple in customers:
#     # datet = string_to_datetime(customer_tuple[2])
#     date = dtf.get_current_datetime_jst()
#     date_int = dtf.date_to_int(date)
#     date_hex = hex(date_int)
#     print(f"tyep of date_to_int: {type(date_int)}")

#     insert_customer(customer_tuple[1], date_hex, customer_tuple[3])
# get_customer()
# drop_customer_table()
