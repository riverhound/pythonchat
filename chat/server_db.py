import sqlite3
import client
import time
import server

conn = sqlite3.connect('server.db')
cursor = conn.cursor()
cursor.execute("insert into server (login, login_time, address, message) values ('%s','%s','%s','%s')" % (client.name.text(), time.asctime(), server.connection.getpeername(), client.message.text()))
conn.commit()

    