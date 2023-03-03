import random
from tsp.Tour import Tour
from genetic_algorithm import Selection, Mutation, Crossover
from genetic_algorithm.Population import Population
from util.Visualiser import Visualiser
from matplotlib import pyplot as plt

early_stopping = 100


class GeneticAlgorithm:

    def __init__(self, genes, population, number_of_generations,
                 elite, selection, p, tournament_size,
                 crossover, mutation, mutation_rate):
        # Population data for evolution
        self.genes = genes
        self.population = population
        self.number_of_generations = number_of_generations

        # Chosen evolution strategies
        self.elite = elite
        self.selection = selection
        self.p = p
        self.tournament_size = tournament_size
        self.crossover = crossover
        self.mutation = mutation
        self.mutation_rate = mutation_rate

        # Data for evaluation
        self.stopped_at_gen = number_of_generations
        self.distance_before = population.get_fittest_genome().get_length()
        self.distance_after = 0.0
        self.improvement_score = 0.0
        self.best_route = None

    def run_with_visualisation(self):
        # Visualise the algorithm
        vis = Visualiser()
        filenames = []
        fig = plt.figure()

        # variables to check early stopping
        current_fitness = self.population.get_fittest_genome().get_length()
        unchanged_fitness_for = 0

        for i in range(0, self.number_of_generations):
            self.population = self.evolve_population(self.population)

            # show process for every 20th generation
            if i % 20 == 0:
                print("Gen " + str(i) + " - Best Tour Length: " + str(current_fitness))

            # save graph for visualisation
            Visualiser.save_graph(vis, self.population.get_fittest_genome(), i, filenames)
            fig.clear()

            # early stopping?
            new_fitness = self.population.get_fittest_genome().get_length()
            if current_fitness == new_fitness:
                unchanged_fitness_for += 1
            if unchanged_fitness_for >= early_stopping:
                print("Stopping early: Fitness did not change for " + str(early_stopping) + " evolutions.")
                self.stopped_at_gen = i
                break
            current_fitness = new_fitness

        self.distance_after = current_fitness
        self.best_route = self.population.get_fittest_genome()
        self.improvement_score = round((self.distance_before - self.distance_after) / self.distance_before * 100, 2)
        vis.save_gif(filenames)
        return self.improvement_score

    def run(self):
        # variables to check early stopping
        current_fitness = self.population.get_fittest_genome().get_length()
        unchanged_fitness_for = 0

        for i in range(0, self.number_of_generations):
            self.population = self.evolve_population(self.population)
            # early stopping?
            new_fitness = self.population.get_fittest_genome().get_length()
            if current_fitness == new_fitness:
                unchanged_fitness_for += 1
            if unchanged_fitness_for >= early_stopping:
                self.stopped_at_gen = i
                break
            current_fitness = new_fitness
        self.distance_after = current_fitness
        self.best_route = self.population.get_fittest_genome()
        self.improvement_score = round((self.distance_before - self.distance_after) / self.distance_before * 100, 2)
        return self.improvement_score

    def evolve_population(self, population):
        next_generation = Population(self.genes, population.get_size(), False)
        self.handle_elitism(population, next_generation)
        self.select_and_crossover(population, next_generation)
        self.mutate(next_generation)
        return next_generation

    def handle_elitism(self, population, next_generation):
        if self.elite > 0:
            genome_list = population.genomes  # should be a list of Tours
            genome_list = sorted(genome_list, key=lambda g: g.get_fitness(), reverse=True)
            for i in range(0, self.elite):
                next_generation.save_genome(i, genome_list[0])
                genome_list = genome_list[1:]

    def select_and_crossover(self, population, next_generation):
        parent1 = Tour(cities=self.genes)
        parent2 = Tour(cities=self.genes)

        if self.selection == 1:  # deterministic truncation selection
            genomes_to_be_evolved = Selection.deterministic_truncation(population, self.p)
            for i in range(self.elite, next_generation.get_size()):
                parent1 = genomes_to_be_evolved[int(random.random() * len(genomes_to_be_evolved))]
                parent2 = genomes_to_be_evolved[int(random.random() * len(genomes_to_be_evolved))]
                self.create_and_add_new_child(i, next_generation, parent1, parent2)

        # go through all population members:
        for i in range(self.elite, next_generation.get_size()):
            if self.selection == 2:
                parent1 = Selection.tournament(population, self.genes, self.tournament_size)  # choose parents
                parent2 = Selection.tournament(population, self.genes, self.tournament_size)
            elif self.selection == 3:
                parent1 = Selection.roulette_wheel(population)
                parent2 = Selection.roulette_wheel(population)
            elif self.selection == 4:
                parent1 = Selection.rank_based_roulette_wheel(population)
                parent2 = Selection.rank_based_roulette_wheel(population)
            self.create_and_add_new_child(i, next_generation, parent1, parent2)

    def create_and_add_new_child(self, i, next_gen, p1, p2):
        child = self.cross(p1, p2)  # create 1 new child by crossing the parents
        next_gen.save_genome(i, child)

    def cross(self, parent1, parent2):
        if self.crossover == 1:
            return Crossover.one_point_cut(self.genes, parent1, parent2)
        elif self.crossover == 2:
            return Crossover.two_point_cut(self.genes, parent1, parent2)

    def mutate(self, next_generation):
        mutation_function = Mutation.scramble
        if self.mutation == 2:
            mutation_function = Mutation.invert
        elif self.mutation == 3:
            mutation_function = Mutation.swap
        # go through all new tours and mutate a little:
        for i in range(self.elite, next_generation.get_size()):
            mutation_function(next_generation.get_genome(i), self.mutation_rate)
