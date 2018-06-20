import redis
from flask import Flask, request, abort

REDIS_SERVER = 'redis-master'
REDIS_PORT = '6379'
REDIS_PWD = ''
TTL = 31104000

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_history():
    if request.method == 'GET':

        r = redis.StrictRedis(host='169.56.100.62', port=32000, db=0)

        # for k in r.keys('*'):
        #     print(k)

        init = 0  # cursor 값 0으로 스캔 시작
        while (True):
            ret = r.scan(init)
            print
            init
            init = ret[0]  # 이어지는 scan 명령에 사용할 cursor 값
            print
            ret[1]
            if (init == '0'):  # 반환된 cursor 값이 0이면 스캔 종료
                break

        # conn = Client(host=169.56.100.62, port=32000, db=0, password=REDIS_PWD)
        # conn.jsonget('')
        # params = timestamp + '_' + alert_type + '_' + reciever
        # data = json.dumps(conn.jsonget(params))
        # return render_template('info.html', data=data)
        # json_str = json.dumps(alertData)
        # print(json_str)
        #
        # now = datetime.datetime.now()
        # print(now)
        # now_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
        # print(now_datetime)
        #
        # try:
        #     print(sqlite3.version)
        #     # con = sqlite3.connect('/Users/cocopop1106/PycharmProjects/zcp-webhook/app/static/database.db')
        #     con = sqlite3.connect('C:/Users/Administrator/PycharmProjects/zcp-webhook/app/static/database.db')
        #
        #     with con:
        #         cs = con.cursor()
        #
        #         sql = "create table if not exists alert (json json, date varchar(30)) "
        #         cs.execute(sql)
        #
        #         sql2 = "insert into alert(json, date) values(?, ?) "
        #         cs.execute(sql2, (json_str, now_datetime))
        #
        #         cs.execute('select * from alert')
        #         print(cs.fetchall())
        #
        #         con.commit()
        #         cs.close()
        #
        #     con.close()
        #
        # except Exception as err:
        #     print('ERROR:', err)
        #
        # return json_str
    else:
        abort(400)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')

