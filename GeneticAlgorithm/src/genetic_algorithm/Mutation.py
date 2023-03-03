import random


def swap(tour, mutation_rate):
    for start_city in range(0, tour.get_size()):
        if random.random() < mutation_rate:
            end_city = int(tour.get_size() * random.random())  # randomly select an index of a swap city
            # swap:
            city1 = tour.get_city(start_city)
            city2 = tour.get_city(end_city)
            tour.set_city(end_city, city1)
            tour.set_city(start_city, city2)


def invert(tour, mutation_rate):
    for start_city in range(0, tour.get_size()):
        if random.random() < mutation_rate:
            end_city = int(tour.get_size() * random.random())
            tour[start_city:end_city] = tour[start_city:end_city][::-1]


def scramble(tour, mutation_rate):
    for start_city in range(0, tour.get_size()):
        if random.random() < mutation_rate:
            end_city = int(tour.get_size() * random.random())
            copy = tour[start_city:end_city]
            random.shuffle(copy)
            tour[start_city:end_city] = copy
