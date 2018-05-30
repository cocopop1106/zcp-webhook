from flask import Flask, jsonify, request, abort
import sqlite3

app = Flask(__name__)

@app.route('/alert', methods=['GET'])
def get():
    if request.method == 'GET':
        try:
            # SQLite DB 연결
            con = sqlite3.connect('C:/Users/Administrator/PycharmProjects/zcp-webhook/app/static/database.db')

            with con:
                # Connection 으로부터 Cursor 생성
                cs = con.cursor()

                # SQL 쿼리 실행
                cs.execute('select json from alert')

                # 데이타 Fetch
                rows = cs.fetchall()
                print(rows)
                for row in rows:
                    print(row)

                cs.close()

            con.close()

        except Exception as err:
            print('ERROR:', err)

        # return {'hello': 'world'}
        return jsonify(row)

    else:
        abort(400)


if __name__ == '__main__':
    app.run(debug=True)