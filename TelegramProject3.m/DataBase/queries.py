class Queries:
    CREATE_FEEDBACK_TABLE = """
        CREATE TABLE IF NOT EXISTS feedback_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name  TEXT, 
        phone_number TEXT, 
        instagram TEXT, 
        estimation INTEGER,
        commentary TEXT    
        )
    """
    DROP_FEEDBACK_TABLE = "DROP TABLE feedback"
    DROP_CATEGORIES_TABLE = "DROP TABLE categories"
    DROP_ORDERS_TABLE = "DROP TABLE orders"

    CREATE_CATEGORIES_TABLE= """
        CREATE TABLE IF NOT EXISTS categories ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT 
    )
    """

    CREATE_DISHES_TABLE = """
        CREATE TABLE IF NOT EXISTS dishes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category_id INTEGER,
            image TEXT,
            price INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    """

    CREATE_ORDERS_TABLE = """
        CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        user_id INTEGER, 
        dish_id INTEGER, 
        review TEXT,
        FOREIGN KEY (dish_id) REFERENCES dishes(id)
        )
    """


    # Вставка данных в таблицу категорий блюд
    INSERT_INTO_CATEGORIES = '''
        INSERT INTO categories(name) VALUES 
        ('Завтраки'),
        ('Обеды'),
        ('Ужины');
    '''

    # Вставка данных в таблицу блюд
    INSERT_INTO_DISHES = '''
        INSERT INTO dishes(name, category_id,image,price) VALUES
        ('Омлет', 1,'images/Пицца.jpg',100),
        ('Плов', 2,'images/Плов.jpg', 200),
        ('Манты', 2,'images/Манты.jpg', 200),
        ('Бозо', 1,'images/Бозо.jpg', 50),
        ('Шашлыки', 3,'images/Шашлыки.jpg', 220),
        ('Пицца', 3, 'images/Пицца.jpg', 300);
    '''