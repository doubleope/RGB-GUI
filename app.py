import sys

from flask_influxdb import InfluxDB
from flask import Flask, render_template, jsonify, request
import webbrowser
import time


app = Flask(__name__)

influx_db = InfluxDB(app=app)


@app.route('/postClusterInfo')
def postClusterInfo():
    client = influx_db.connection
    client.switch_database('cluster_info_db')
    cluster_name = request.args.get('cluster_name')
    cluster_type = request.args.get('cluster_type')
    ip = request.args.get('ip')
    port = request.args.get('port')
    mac_address = request.args.get('mac_address')
    client.write_points([
        {
            "fields": {
                'cluster_name': cluster_name,
                'cluster_type': cluster_type,
                'ip': ip,
                'port': port,
                'mac_address': mac_address
            },
            "measurement": "clusters2"
        }
    ])



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
    return render_template('home.html', )



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
