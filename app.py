import argparse

from flask import Flask, render_template, request, make_response, Response
import peewee
from peewee import *

import models

app = Flask(__name__, template_folder='templates')
app.debug=True
models.db.connect()

@app.route('/', methods=['GET'])
def player_list():
    players = models.Players.select().where(
        ~(models.Players.yahoo_id >> None),
        ~(models.Players.mlb_depth >> None),
    )[0:5]
    return render_template('player_list.html', players=players)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port')
    args = parser.parse_args()
    server_port = 8000

    if args.port:
        server_port = int(args.port)

    app.run(host='0.0.0.0', port=server_port, debug=True)
