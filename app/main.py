from flask import Flask, request, abort
import json
import sqlite3
import datetime

app = Flask(__name__)

with open('alert.json', mode='r', encoding='utf-8') as f:
    alertData = json.load(f)

@app.route('/webhook', methods=['GET'])
def webhook():
    if request.method == 'GET':

        json_str = json.dumps(alertData)
        print(json_str)

        now = datetime.datetime.now()
        print(now)
        now_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
        print(now_datetime)

        try:
            print(sqlite3.version)
            # con = sqlite3.connect('/Users/cocopop1106/PycharmProjects/zcp-webhook/app/static/database.db')
            con = sqlite3.connect('C:/Users/Administrator/PycharmProjects/zcp-webhook/app/static/database.db')

            with con:
                cs = con.cursor()

                sql = "create table if not exists alert (json json, date varchar(30)) "
                cs.execute(sql)

                sql2 = "insert into alert(json, date) values(?, ?) "
                cs.execute(sql2, (json_str, now_datetime))

                cs.execute('select * from alert')
                print(cs.fetchall())

                con.commit()
                cs.close()

            con.close()

        except Exception as err:
            print('ERROR:', err)

        return json_str
    else:
        abort(400)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')

