import flask
from flask import request, jsonify
import sqlite3

app=flask.Flask(__name__)
app.config["DEBUG"]=True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/',methods=['GET'])
def home():
    return "DATASET"


@app.route('/api', methods=['GET'])
def api_all():
    conn = sqlite3.connect('twimAI_dataset.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_data = cur.execute('SELECT * FROM twimm;').fetchall()

    return jsonify(all_data)




app.run()
