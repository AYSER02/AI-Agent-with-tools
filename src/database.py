import sqlite3

def create_database():
    conn = sqlite3.connect("skills.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT
    )
    """)

    skills = [
        ("Python", "Programming"),
        ("Machine Learning", "AI"),
        ("Deep Learning", "AI"),
        ("LangChain", "LLM"),
        ("FastAPI", "Backend")
    ]

    cursor.executemany(
        "INSERT INTO skills (name, category) VALUES (?, ?)", skills
    )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
