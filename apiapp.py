import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
db = client.dbTweets


@app.route('/')
def todo():

    _items = db.twitterMessagesDocker.find()
    print(_items)
    items = [item for item in _items]

    return render_template('todo.html', items=items)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
