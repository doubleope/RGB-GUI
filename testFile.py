from influxdb import InfluxDBClient
client = InfluxDBClient(host='localhost', port=8086)

client.switch_database('rgb')


client.write_points([
    {
        "fields": {
            'cluster_name': 78,
            'type': 98,
            'ip': 56,
            'port': 4543,
            'mac_address': 338
        },
        "measurement": "clusters"
    }
])

dbData = client.query('SELECT * FROM testseries')

data_points = []
for measurement, tags in dbData.keys():
    for p in dbData.get_points(measurement=measurement, tags=tags):
        data_points.append(p)



dbData_points = list(dbData.get_points(measurement = 'clusters'))
final_points = []

for i in dbData_points:
    final_points.append(i)




temp = ResultSet({'('clusters', None)': [{'time': '2020-01-03T05:39:42.88922125Z', 'cluster_name': 'Node1'}]})
