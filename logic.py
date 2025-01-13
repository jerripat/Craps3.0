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

import sqlite3

import sqlite3

def create_game_table():
    """Create the Games table and insert an initial game record."""
    conn = sqlite3.connect("Main.db")
    cursor = conn.cursor()

    # Drop the table if it already exists
    #cursor.execute("DROP TABLE IF EXISTS Games")

    # Create the Games table with the correct schema
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            game_id INTEGER,
            wager REAL,
            win REAL, 
            loss REAL,
            score INTEGER
        )
    """)

    # Insert a new game entry with default values
    cursor.execute("""
        INSERT INTO Games (game_id, wager, win, loss, score)
        VALUES (?, ?, ?, ?, ?)
    """, (300, 100, 0, 0, 0))  # Adjusted to match the column count

    conn.commit()  # Commit the changes
    conn.close()

# Call the function to create the table and add the initial record
#create_game_table()

def insert_into_games(game_id, wager, win, loss, score, game_point):
    """Insert a new game record into the Games table."""
    conn = sqlite3.connect("Main.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Games (game_id, wager, win, loss, score,game_point)
        VALUES (?,?,?,?,?,?)
    """, (game_id, wager, win, loss, score, game_point))

    conn.commit()  # Commit the changes
    conn.close()

def get_game_counter():
    """Retrieve the current game counter from the GameCounter table."""
    conn = sqlite3.connect("Main.db")
    cursor = conn.cursor()

    cursor.execute("SELECT counter FROM GameCounter LIMIT 1")
    result = cursor.fetchone()

    if result is None:
        # If the table is empty, set the counter to 1
        cursor.execute("INSERT INTO GameCounter (counter) VALUES (1)")
        conn.commit()  # Commit the insertion
        counter = 1
    else:
        # Retrieve the current counter value
        counter = result[0]

    # Increment the counter
    cursor.execute("UPDATE GameCounter SET counter = counter + 1")
    conn.commit()  # Commit the update

    # Close the connection
    conn.close()

    return counter