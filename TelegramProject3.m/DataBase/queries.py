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