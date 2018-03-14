#coding=UTF-8

import sys

sys.path.append("../")
sys.path.append("../imps")

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
