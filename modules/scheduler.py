import sqlite3
import datetime

DB_PATH = "database/tasks.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT,
            run_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def handle_scheduler(task):
    init_db()

    task_type = task.get("type")

    if task_type == "add_task":
        task_text = task.get("task")
        run_time = task.get("run_at")

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tasks (task, run_at) VALUES (?, ?)",
            (task_text, run_time)
        )

        conn.commit()
        conn.close()

        return f"Task scheduled for {run_time}"

    return "Scheduler task not supported."