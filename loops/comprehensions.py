import pprint
from datetime import datetime

def convert2ampm(time24:str):
    return datetime.strptime(time24,'%H:%M').strftime('%I:%M%p')

with open('buzzers.csv', mode='r') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k,v = line.strip().split(',') # strip takes away /n and other leading or trailing whitespaces
        flights[k]=v    
    pprint.pprint(flights)

    flights2={}
    for key, value in flights.items():
        flights2[convert2ampm(key)] = value.title() 

    pprint.pprint(flights)
    pprint.pprint(flights2)

    destinations = [x.title() for x in flights.values()]
    print(destinations)

    more_flights = {convert2ampm(k):v.title() for k,v in flights.items()}

    print(more_flights)

#comprehensions are faster than for loops!

#535