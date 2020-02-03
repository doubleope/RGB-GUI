import json
import sys
import os
import re
from IPy import IP
from flask_influxdb import InfluxDB
from flask import Flask, render_template, jsonify, request, flash
from werkzeug.utils import secure_filename, redirect

import RGB_L1
import RGB_L2
import RGB_L3
import RGB_Telemetry
import RGB_Checker

UPLOAD_FOLDER = '/home/ope/PyEMD/Documents/Projects/RGB-GUI/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
influx_db = InfluxDB(app=app)


def get_info(client):
    db_data = client.query('SELECT * FROM clusters')
    data_points = list(db_data.get_points())
    return data_points


@app.route('/upload_file')
def upload_file():
    client = influx_db.connection
    client.switch_database('cluster_info_db')

    with open('uploads/JSON_test_file') as json_file:
        file = json.load(json_file)
    client.write_points([
        {
            "fields": {
                'cluster_name': file["cluster_name"],
                'cluster_type': file["cluster_type"],
                'ip': file["ip"],
                'port': file["port"],
                'mac_address': file["mac_address"]
            },
            "measurement": "clusters"
        }
    ])
    return jsonify(get_info(client))


@app.route('/post_cluster_info')
def post_cluster_info():
    client = influx_db.connection
    client.switch_database('cluster_info_db')

    ip_verification = re.match("^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", request.args.get('ip'))
    mac_verification = re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$",
                                    request.args.get('mac_address').lower())
    port_verification = re.match("^([1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$", request.args.get('port'))
    

    if ip_verification and mac_verification and port_verification:
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
    if not ip_verification:
        return jsonify("ip error")

    if not mac_verification:
        return jsonify("mac error")

    if not port_verification:
        return jsonify("port error")
        
    return jsonify(get_info(client))


@app.route('/show_data_center_info', methods=['GET'])
def show_data_center_info():
    client = influx_db.connection
    client.switch_database('cluster_info_db')
    return jsonify(get_info(client))


@app.route('/result1')
def result1():
    client = influx_db.connection
    client.switch_database('cluster_info_db')
    res1 = RGB_L1.runGreenTest(get_info(client))
    return jsonify(res1)


@app.route('/result2')
def result2():
    client = influx_db.connection
    client.switch_database('cluster_info_db')
    res2 = RGB_L2.runGreenTest(get_info(client))
    return jsonify(res2)


@app.route('/result3')
def result3():
    client = influx_db.connection
    client.switch_database('cluster_info_db')
    res3 = RGB_L3.runGreenTest(get_info(client))
    return jsonify(res3)


@app.route('/')
def index():
    flash("you are in the home page")
    return render_template('home.html')     


@app.route('/level1', methods=['GET', 'POST'])
def level1():
    if request.method == 'POST':
        if request.files['file'] or request.args.get('ip'):
            file = request.files['file']
            if file:
                client = influx_db.connection
                client.switch_database('cluster_info_db')

                file = json.load(file)
                for i in file:
                    client.write_points([
                        {
                            "fields": {
                                'cluster_name': i['cluster_name'],
                                'cluster_type': i['cluster_type'],
                                'ip': i['ip'],
                                'port': i['port'],
                                'mac_address': i['mac_address']
                            },
                            "measurement": "clusters"
                        }
                    ])
    level_type = "Level One"
    return render_template('measurement-results-page.html', level_type=level_type)


@app.route('/level2')
def level2():
    if request.method == 'POST':
        if request.files['file'] or request.args.get('ip'):
            file = request.files['file']
            if file:
                client = influx_db.connection
                client.switch_database('cluster_info_db')

                file = json.load(file)
                for i in file:
                    client.write_points([
                        {
                            "fields": {
                                'cluster_name': i['cluster_name'],
                                'cluster_type': i['cluster_type'],
                                'ip': i['ip'],
                                'port': i['port'],
                                'mac_address': i['mac_address']
                            },
                            "measurement": "clusters"
                        }
                    ])
    level_type = "Level One"
    return render_template('measurement-results-page.html', level_type=level_type)


@app.route('/level3')
def level3():
    if request.method == 'POST':
        if request.files['file'] or request.args.get('ip'):
            file = request.files['file']
            if file:
                client = influx_db.connection
                client.switch_database('cluster_info_db')

                file = json.load(file)
                for i in file:
                    client.write_points([
                        {
                            "fields": {
                                'cluster_name': i['cluster_name'],
                                'cluster_type': i['cluster_type'],
                                'ip': i['ip'],
                                'port': i['port'],
                                'mac_address': i['mac_address']
                            },
                            "measurement": "clusters"
                        }
                    ])
    level_type = "Level One"
    return render_template('measurement-results-page.html', level_type=level_type)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()
