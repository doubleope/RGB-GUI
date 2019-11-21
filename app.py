import time

from flask_influxdb import InfluxDB
from flask import Flask, render_template, jsonify, request
import webbrowser

app = Flask(__name__)

influx_db = InfluxDB(app=app)


@app.route('/')
def index():
    return render_template('dashboard.html', )

@app.route('/getInfo', methods = ['GET'])
def getInfo():
    return jsonify(result=time.time())

@app.route('/level1')
def level1():
    return render_template('level1.html')

@app.route('/level2')
def level2():
    return render_template('level2.html')

@app.route('/level3')
def level3():
    return render_template('level3.html')

app.run()
