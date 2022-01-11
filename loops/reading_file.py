import csv
import pprint
from datetime import datetime

with open('buzzers.csv', mode='r') as raw_data:
    #whole:
    print(raw_data.read())

    print('_'*50)


with open('buzzers.csv', mode='r') as raw_data:
    # as list:
    for line in csv.reader(raw_data):
        print(line)

    print('_'*50)

with open('buzzers.csv', mode='r') as raw_data:
    # as dictionary:
    for line in csv.DictReader(raw_data):
        print(line)

    print('_'*50)

with open('buzzers.csv', mode='r') as raw_data:
    ignore = raw_data.readline()
    flights = {}
    for line in raw_data:
        k,v = line.strip().split(',') # strip takes away /n and other leading or trailing whitespaces
        flights[k]=v
    pprint.pprint(flights)
    print('_'*50)

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

#534