from flask_influxdb import InfluxDB
from flask import Flask, render_template

app = Flask(__name__)

influx_db = InfluxDB(app=app)


@app.route('/')
def index():
    return render_template('index.html', )


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
