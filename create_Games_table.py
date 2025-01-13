import sqlite3

def create_game_table():
    """Create the Games table and insert an initial game record."""
    conn = sqlite3.connect("Main.db")
    cursor = conn.cursor()

    # Drop the table if it already exists
    cursor.execute("DROP TABLE IF EXISTS Games")

    # Create the Games table
    cursor.execute("""
        CREATE TABLE Games (
            game_id INTEGER PRIMARY KEY,
            wager REAL,
            win REAL,
            loss REAL,
            score INTEGER,
            game_point INTEGER
        )
    """)

    # Insert an initial game record
    cursor.execute("INSERT INTO Games (game_id, wager, win, loss, score, game_point) VALUES (1, 100, 0, 0, 0, 0)")

    conn.commit()  # Commit the creation and insertion
#create_game_table()

def create_game_counter():
    conn = sqlite3.connect("Main.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS GameCounter (counter INTEGER)")
    cursor.execute("INSERT INTO GameCounter (counter) VALUES (1)")
    conn.commit()
    conn.close()
create_game_counter()