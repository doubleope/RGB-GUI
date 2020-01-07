import sys

from flask_influxdb import InfluxDB
from flask import Flask, render_template, jsonify, request
import webbrowser
import time

import RGB_L1
import RGB_L2
import RGB_L3
import RGB_Telemetry
import RGB_Checker


app = Flask(__name__)

influx_db = InfluxDB(app=app)


@app.route('/postClusterInfo')
def postClusterInfo():
    client = influx_db.connection
    client.switch_database('cluster_info_db')

    client.write_points([
        {
            "fields": {
                'cluster_name': request.args.get('cluster_name'),
                'cluster_type': request.args.get('cluster_type'),
                'ip': request.args.get('ip'),
                'port': request.args.get('port'),
                'mac_address': request.args.get('mac_address')
            },
            "measurement": "clusters"
        }
    ])

    db_data = client.query('SELECT * FROM clusters')
    data_points = list(db_data.get_points())
    return jsonify(data_points)



@app.route('/getInfo', methods = ['GET'])
def getInfo():
    client = influx_db.connection
    client.switch_database('cluster_info_db')
    db_data = client.query('SELECT * FROM clusters')
    data_points = list(db_data.get_points())
    return jsonify(data_points)




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
