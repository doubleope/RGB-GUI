from flask_influxdb import InfluxDB
from flask import Flask, render_template

app = Flask(__name__)

influx_db = InfluxDB(app=app)


@app.route('/')
def index():
    return render_template('index.html', )


app.run()
