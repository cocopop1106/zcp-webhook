from flask import Flask
import json
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

if __name__ == "__main__":
    app.run()
ß