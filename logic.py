import sqlite3

def get_game_id():
    conn = sqlite3.connect("Main.db")
    cursor = conn.cursor()

    # Ensure the GameId table exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS GameId (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            game_id INTEGER
        )
    """)

    # Check if the table is empty
    cursor.execute("SELECT game_id FROM GameId LIMIT 1")
    result = cursor.fetchone()

    if result is None:
        # If empty, insert a default game_id
        cursor.execute("INSERT INTO GameId (game_id) VALUES (1)")
        conn.commit()  # Commit the insertion
        game_id = 1
    else:
        # Retrieve the current game_id
        game_id = result[0]

    # Increment the game_id
    cursor.execute("UPDATE GameId SET game_id = game_id + 1")
    conn.commit()  # Commit the update

    # Close the connection
    conn.close()

    return game_id
