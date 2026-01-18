import sqlite3
from langchain.tools import tool

@tool
def get_skills_by_category(category: str) -> str:
    """
    Fetch skills from the database by category.
    """
    conn = sqlite3.connect("skills.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name FROM skills WHERE category LIKE ?",
        (f"%{category}%",)
    )

    results = cursor.fetchall()
    conn.close()

    if not results:
        return "No skills found."

    return ", ".join([row[0] for row in results])
