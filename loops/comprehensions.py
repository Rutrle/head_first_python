import pprint
from datetime import datetime


def convert2ampm(time24: str):
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv', mode='r') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        # strip takes away /n and other leading or trailing whitespaces
        k, v = line.strip().split(',')
        flights[k] = v
    pprint.pprint(flights)

    flights2 = {}
    for key, value in flights.items():
        flights2[convert2ampm(key)] = value.title()

    pprint.pprint(flights)
    pprint.pprint(flights2)

    destinations = [x.title() for x in flights.values()]
    print(destinations)

    more_flights = {convert2ampm(k): v.title() for k, v in flights.items()}

    print(more_flights)

    # comprehensions are faster than for loops!
    just_freeport2 = {convert2ampm(k): v.title()
                      for k, v in flights.items() if v == 'FREEPORT'}
    pprint.pprint(just_freeport2)

    fts = {convert2ampm(k): v.title() for k, v in flights.items()}


wests = []
for k, v in fts.items():
    if v == 'West End':
        wests.append(k)
print(wests)

wests_comp = [k for k, v in fts.items() if v == 'West End']
print(wests_comp)


when = {}
for dest in set(fts.values()):
    when[dest] = [k for k, v in fts.items() if v == dest]
print(when)

when_comp = {dest: [k for k, v in fts.items() if v == dest]
             for dest in set(fts.values())}
print(when_comp)
