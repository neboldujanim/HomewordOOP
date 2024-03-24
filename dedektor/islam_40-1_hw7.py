import sqlite3


def connection(hw_db):
    connect = None
    try:
        connect = sqlite3.connect(hw_db)
        return connect
    except sqlite3.Error as oops:
        print(oops)
    return connect


def table_creation(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as oops:
        print(oops)


def add_product(connection, product_title, price, quantity):
    sql = '''INSERT INTO PRODUCTS
    (product_title,price, quantity)
    VALUES (?,?,?)

    '''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (product_title, price, quantity))
        connection.commit()
    except sqlite3.Error as oops:
        print(oops)


sql_to_create_a_shop = '''
CREATE TABLE IF NOT EXISTS PRODUCTS(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL, 
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''


def update_quantity(connection, product):
    sql = '''UPDATE PRODUCTS SET quantity = ? WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as oops:
        print(oops)


def update_price(connection, product):
    sql = '''UPDATE PRODUCTS SET price = ?  WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as oops:
        print(oops)


def delete_product(connection, id):
    sql = '''DELETE FROM PRODUCTS WHERE id = ? '''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as oops:
        print(oops)


def show_products(connection):
    sql = '''SELECT * FROM PRODUCTS '''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        all_products = cursor.fetchall()
        for products in all_products:
            print(products)
    except sqlite3.Error as oops:
        print(oops)


def select_products(connection):
    sql = '''SELECT * FROM products WHERE price < ? and quantity > ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        all_products = cursor.fetchall()
        print('\n')
        for products in all_products:
            print(products)
    except sqlite3.Error as oops:
        print(oops)


def search_products(products, title):
    sql = '''SELECT * FROM products WHERE product_title LIKE ? '''
    try:
        cursor = products.cursor()
        cursor.execute(sql, ('%' + title + '%',))
        search_products = cursor.fetchall()
        for product in search_products:
            print(product)
    except sqlite3.Error as e:
        print(e)


products = connection('product1.db')
if connection is not None:
    print('You are successfully connetcted to DATABASE')
    table_creation(products, sql_to_create_a_shop)
    list_products = [
        ("Губная помада", 50.49, 40),
        ("Крем для лица с SPF 30", 29.99, 8),
        ("Мыло для чувствительной кожи", 120.99, 16),
        ("Шампунь для окрашенных волос", 13.99, 10),
        ("Мыло для бритья", 78.99, 14),
        ("Дезодорант в стике", 7.49, 28),
        ("Кондиционер для волос", 250.49, 17),
        ("Крем для рук", 99.99, 22),
        ("Очищающий лосьон для лица", 210.99, 18),
        ("Хозяйственное Мыло", 100.49, 12),
        ("Гель для душа с алоэ вера", 140.99, 4),
        ("Зубная паста с мятой", 80.99, 30),
        ("Шампунь для волос", 285.49, 15),
        ("Мыло для детей", 90.50, 20),
        ("Жидкое Мыло с ароматом ванили", 123.99, 10)
    ]

    for p in list_products:
        add_product(products, *p)

    update_quantity(products, (25, 4))
    update_price(products, (75, 15))
    delete_product(products, 12)
    show_products(products)
    select_products(products)
    search_products(products, 'Мыло')

    products.close()