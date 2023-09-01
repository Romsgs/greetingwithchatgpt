# database.py
import sqlite3

DATABASE_NAME = "users.db"

def create_tables():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    # Create the Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            greeting_phrase TEXT,
            password TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def connect_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn
  
def get_all_user():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    
    users = []
    for user_data in cursor.fetchall():
        user_dict = {
            "id": user_data[0],
            "name": user_data[1],
            "email": user_data[2],
            "greeting_phrase": user_data[3],
            "password": user_data[4]
        }
        users.append(user_dict)
    
    conn.close()
    return users

def get_user_by_id(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_email(email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user

def create_user(user_data):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO users (name, email, greeting_phrase, password)
        VALUES (?, ?, ?, ?)
    ''', (user_data['name'], user_data['email'], user_data['greeting_phrase'], user_data['password']))
    
    user_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return user_id

def update_user(user_id, user_data):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE users
        SET name = ?, email = ?, greeting_phrase = ?
        WHERE id = ?
    ''', (user_data['name'], user_data['email'], user_data['greeting_phrase'], user_id))
    
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    
    conn.commit()
    conn.close()
