import sqlite3
import generate
import client

def main():

    conn = sqlite3.connect("server.db")
    cursor = conn.cursor()

    h = generate.get_hash(client.name, '1', client.password)

    cursor.execute("""
        select login
            from user inner join pass on user.pass = pass.pid
            where
                user.login = '%s' and user.level = %d and pass.h = '%s'"""
        %
        (client.name, 1, h))

    res = cursor.fetchall()

    if len(res):

        print("Login success")
        return 1

    else:

        print("We have a problem!")

        return 0

if __name__ == "__main__":
    main()
