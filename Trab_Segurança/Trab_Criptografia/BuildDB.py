import sqlite3
connection_obj = sqlite3.connect('unifor.db')
cursor_obj = connection_obj.cursor()
table = """ CREATE TABLE users (
            username CHAR(25) NOT NULL,
            password CHAR(25) NOT NULL
        ); """
cursor_obj.execute(table)
cursor_obj.execute("INSERT INTO users(username, password) VALUES ('test', 'test')")
cursor_obj.execute(f"SELECT * FROM users")
print(cursor_obj.fetchall())
connection_obj.commit()
connection_obj.close()