from flask import Flask, request, abort, jsonify, render_template
import json
import redis
import datetime

app = Flask(__name__)

conn = redis.Redis('redis-master', port=6379, db=0)  # connect to server
ttl = 31104000


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d(%H:%M:%S)')
        req_data = request.get_json()

        print(json.dumps(req_data))

        alertname = req_data['commonLabels']['alertname']
        receiver = req_data['receiver']
        key_name = nowDatetime + "_" + alertname + "_" + receiver
        print(key_name)
        conn.hmset(key_name, {key: req_data[key] for key in req_data})

    # if not conn.exists(key_name):
    #     print
    #     "Error: thing doesn't exist"

    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)