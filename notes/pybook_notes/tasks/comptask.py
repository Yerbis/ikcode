from datetime import datetime


def convert2ampm(time24: str):
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M:%p')


departures = {"FROG MOUNTAIN": '12:00', 
            "COAST COLLAGE": "13:15",
            "MONEY'S STREET": "14:10",
            "SIESE ISLAND": "15:13"}

print(departures)

line_deps = []

for dep in departures.keys():
    line_deps.append(dep.title())

print(line_deps)

more_deps = [deps.title() for deps in departures.keys()]

print(more_deps)


dep_times = []

for dt in departures.values():
    dep_times.append(convert2ampm(dt))

print(dep_times)

idte = [convert2ampm(idt) for idt in departures.values()]

