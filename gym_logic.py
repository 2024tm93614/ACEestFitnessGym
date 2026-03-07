import sqlite3

DB_NAME = "aceest_fitness.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        program TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_member(name, age, program):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO members (name, age, program) VALUES (?, ?, ?)",
        (name, age, program)
    )

    conn.commit()
    conn.close()


def get_members():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT * FROM members")
    members = cur.fetchall()

    conn.close()
    return members