import sqlite3

def get_table_names():
    conn = sqlite3.connect("SkyModels")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [table[0] for table in cursor.fetchall()]
    conn.close()
    return tables

def get_table_columns(table_name):
    conn = sqlite3.connect("SkyModels")
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info({});".format(table_name))
    columns = [column[1] for column in cursor.fetchall()]
    conn.close()
    return columns

def insert_into_table(table_name, columns, values):
    try:
        conn = sqlite3.connect("SkyModels")
        cursor = conn.cursor()

        # Construiește comanda SQL pentru inserare
        sql_command = "INSERT INTO {} ({}) VALUES ({})".format(
            table_name,
            ', '.join(columns),
            ', '.join(['?'] * len(columns))
        )

        # Execută comanda SQL
        cursor.execute(sql_command, values)

        # Commit la schimbările din baza de date
        conn.commit()
        conn.close()

        return True
    except Exception as e:
        print("Eroare de inserare:", str(e))
        return False

def get_user_credentials(username, password):
    conn = sqlite3.connect("SkyModels")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Utilizator WHERE Username = ? AND Parola = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

def get_table_content(table_name):
    conn = sqlite3.connect("SkyModels")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM {}".format(table_name))
    content = cursor.fetchall()
    conn.close()
    return content
