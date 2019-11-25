from influxdb import InfluxDBClient
client = InfluxDBClient(host='localhost', port=8086)

client.switch_database('rgb')


client.write_points([
    {
        "fields": {
            'value_1': 78,
            'value_2': 98,
            'value_3': 56
        },
        "tags": {
            'cluster_id': '1',
            'node_id': '12'
        },
        "measurement": "testseries"
    }
])

dbData = client.query('SELECT * FROM testseries')

data_points = []
for measurement, tags in dbData.keys():
    for p in dbData.get_points(measurement=measurement, tags=tags):
        data_points.append(p)