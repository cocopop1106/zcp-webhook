from flask import Flask, request, abort
import json
import sqlite3

app = Flask(__name__)

with open('alert.json', mode='r', encoding='utf-8') as f:
    alertData = json.load(f)

@app.route('/webhook', methods=['GET'])
def webhook():
    if request.method == 'GET':

        json_str = json.dumps(alertData)
        print(json_str)

        try:
            print(sqlite3.version)
            conn = sqlite3.connect('database.db')
            print(type(conn))
            print(dir(conn))

            with conn:
                cur = conn.cursor()
                print(type(cur))
                for i in dir(cur):
                    if not i.startswith("__"):
                        print(i)

                cur.execute('create table if not exists alert(content text)')
                # cur.execute('select * from alert')
                # print(cur.fetchone())
                # sql = "insert into alert(content) values(?)"
                # cur.execute(sql, '오서우')
                # cur.execute('select * from alert')

                cur.close()

            conn.commit()
            conn.close()
        except Exception as err:
            print(err)

        return json_str
    else:
        abort(400)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')

