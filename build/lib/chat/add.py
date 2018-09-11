import sqlite3, argparse
import generate

conn = sqlite3.connect("server.db")
cursor = conn.cursor()

parser = argparse.ArgumentParser()
parser.add_argument("--login", help = "Login", required = True)
parser.add_argument("--level", help = "Level", required = True)
parser.add_argument("--password", help = "Password", required = True)
args = parser.parse_args()

h = generate.get_hash(args.login, args.level, args.password)

cursor.execute("insert into pass (h) values ('%s')" % h)
conn.commit()

pid = cursor.lastrowid

try:
    cursor.execute("insert into user (login, level, pass) values ('%s', %d, %d)" % (args.login, int(args.level), pid))
except sqlite3.IntegrityError:
    print("User with this login and level already registered.")

conn.commit()


