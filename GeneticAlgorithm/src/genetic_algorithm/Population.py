from tsp.Tour import Tour


# genome is tour
# gene is city in tour

class Population:
    def __init__(self, genes, size, initialise):
        self.genomes = []

        # generate empty population
        for i in range(0, size):
            self.genomes.append(None)

        # initialize unique genomes and save them in genomes array
        if initialise:
            for i in range(0, size):
                new_tour = Tour(genes)
                new_tour.get_unique_sequence()
                self.save_genome(i, new_tour)

    def __setitem__(self, key, value):
        self.genomes[key] = value

    def __getitem__(self, index):
        return self.genomes[index]

    def save_genome(self, index, tour):
        self.genomes[index] = tour

    def get_genome(self, index):
        return self.genomes[index]

    def get_size(self):
        return len(self.genomes)

    def __repr__(self):
        return str(self.genomes)

    def get_fittest_genome(self):
        fittest = self.genomes[0]  # 1st genome
        for g in self.genomes:
            if fittest.get_fitness() <= g.get_fitness():  # safe if fitness is higher
                fittest = g
        return fittest
