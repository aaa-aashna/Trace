from pynput import keyboard
import sqlite3
from datetime import datetime

keystrokes = 0

def on_press(key):
    global keystrokes

    keystrokes += 1

    conn = sqlite3.connect("trace.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO activity(timestamp, keystrokes, active_app)
        VALUES (?, ?, ?)
        """,
        (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            keystrokes,
            "Unknown"
        )
    )

    conn.commit()
    conn.close()

    print(f"Keystrokes: {keystrokes}")

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()