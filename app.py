

from flask_influxdb import InfluxDB
from flask import Flask, render_template, jsonify, request
import webbrowser
import time


app = Flask(__name__)

influx_db = InfluxDB(app=app)

@app.route('/getInfo', methods = ['GET'])
def getInfo():
    client = influx_db.connection
    client.switch_database('rgb')
    db_data = client.query('SELECT * FROM testseries')
    data_points = []
    for measurement, tags in db_data.keys():
        for p in db_data.get_points(measurement=measurement, tags=tags):
            data_points.append(p)
    return jsonify(data_points[0])

@app.route('/')
def index():
    return render_template('dashboard.html', )



@app.route('/level1')
def level1():
    return render_template('level1.html')

@app.route('/level2')
def level2():
    return render_template('level2.html')

@app.route('/level3')
def level3():
    return render_template('level3.html')


if __name__ == '__main__':
    app.run()
