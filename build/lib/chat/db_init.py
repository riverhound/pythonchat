import sqlite3

conn = sqlite3.connect('server.db')

cursor = conn.cursor()

cursor.execute("drop table if exists server")
cursor.execute("drop table if exists user")
cursor.execute("drop table if exists pass")

cursor.execute("""
        create table pass
        (
            pid integer primary key autoincrement,
            h char(64) not null
        )""")

cursor.execute("""
        create table user
        (
            uid integer primary key autoincrement,
            login text not null,
            level integer not null,
            pass integer references pass (pid) not null,
            unique (login, level)
        )""")

conn.execute("""
        CREATE TABLE SERVER
         (id INTEGER PRIMARY KEY AUTOINCREMENT,
         login       CHAR(50) NOT NULL,
         login_time  CHAR(40) NOT NULL,
         address     CHAR(40) NOT NULL,
         message     TEXT
         )""")

conn.commit()