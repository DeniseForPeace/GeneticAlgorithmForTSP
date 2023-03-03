import random


class Tour:
    def __init__(self, cities, tour=None):
        self.cities = cities
        self.tour = []
        self.tour_size = len(cities)
        self.fitness = 0.0
        self.tour_length = 0
        if tour is not None:
            self.tour = tour
        else:
            for i in range(0, len(cities)):
                self.tour.append(None)

    def __len__(self):
        return len(self.tour)

    def __getitem__(self, index):
        return self.tour[index]

    def __setitem__(self, key, value):
        self.tour[key] = value

    def __repr__(self):
        gene_string = ""
        for i in range(0, self.get_size()):
            gene_string += str(self.get_city(i)) + " > "
        return gene_string

    def get_unique_sequence(self):
        for city_index in range(0, len(self.cities)):
            self.set_city(city_index, self.cities[city_index])
        random.shuffle(self.tour)

    def get_city(self, tour_position):
        return self.tour[tour_position]

    def set_city(self, tour_position, city):
        self.tour[tour_position] = city
        self.fitness = 0.0
        self.tour_length = 0

    def get_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.get_length())
        return self.fitness

    def get_length(self):
        if self.tour_length == 0:
            current_tour_length = 0
            for city_index in range(0, self.tour_size):
                current_city = self.get_city(city_index)
                # destination_city = None
                if city_index + 1 < self.get_size():  # are we at the end of the tour already?
                    destination_city = self.get_city(city_index + 1)
                else:
                    destination_city = self.get_city(0)
                current_tour_length += current_city.calculate_distance_to(destination_city)
            self.tour_length = current_tour_length
        return self.tour_length

    def get_size(self):
        return self.tour_size

    def has_city(self, city):
        return city in self.tour
