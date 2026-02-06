def sensor_data():
    i = 1
    while True:
        yield i
        i += 1

def alert_filter(data):
    for value in data:
        if value > 5:
            yield value


pipeline = alert_filter(sensor_data())

for val in pipeline:
    print(val)
    if val > 10:
        break
