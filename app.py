from flask_influxdb import InfluxDB
from flask import Flask, render_template

app = Flask(__name__)

influx_db = InfluxDB(app=app)


@app.route('/')
def index():
    return render_template('index.html', )


@app.route('/newdb/<dbname>')
def newdb(dbname):
    dbcon = influx_db.connection
    dbcon.create_database(dbname)
    return 'created'





app.run()
