from tsp.City import City
import csv


def read_csv(file):
    with open(file) as csv_file:
        cities = []
        for line in csv.reader(csv_file, delimiter=';'):
            city = City(line[0], int(line[1]), int(line[2]))
            cities.append(city)
        return cities


def read_txt(file):
    cities_raw = []
    with open(file, 'r', encoding='utf8', errors='ignore') as f:
        line = f.readline()
        i = 1
        while line:
            cities_raw = cities_raw + line.split()
            line = f.readline()
            i += 1
    cities = []
    for i in range(0, len(cities_raw)):
        city_parts = cities_raw[i].split(",")
        city = City(city_parts[0], int(city_parts[1]), int(city_parts[2]))
        cities.append(city)
    return cities
