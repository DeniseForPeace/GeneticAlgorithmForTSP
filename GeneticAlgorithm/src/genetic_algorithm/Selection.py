import math
import random
import numpy
from genetic_algorithm.Population import Population


def deterministic_truncation(population, p):
    very_small_percentage = False
    # sort genomes by fitness
    sorted_genomes = sorted(population.genomes, key=lambda tour: tour.get_fitness(), reverse=True)
    # calculate index for genomes to keep from p (p is a float/percentage)
    number_of_selected_fittest = population.get_size() * p
    if number_of_selected_fittest < 1: #  to make sure at least 1 genome is chosen
        very_small_percentage = True
        number_of_selected_fittest *= 2
    # slice array; get only p fittest genomes
    fittest = sorted_genomes[:int(number_of_selected_fittest)]
    to_be_evolved = []
    for i in range(0, int(number_of_selected_fittest)):
        for _ in range(0, int(math.ceil(1 / p))):
            to_be_evolved.append(fittest[i])
    if very_small_percentage:
        return to_be_evolved[:int(len(to_be_evolved)/2)]
    return to_be_evolved


def tournament(population, genes, tournament_size):
    random_candidates = Population(genes, tournament_size, False)
    for i in range(0, tournament_size):  # get given number of competitors
        # choose and save random genome from population array
        random_id = int(random.random() * population.get_size())
        random_candidates.save_genome(i, population.get_genome(random_id))
    fittest_candidate = random_candidates.get_fittest_genome()  # the fitter genome wins
    return fittest_candidate


def roulette_wheel(population):
    total_fitness = sum([genome.get_fitness() for genome in population])
    all_fitnesses = [genome.get_fitness() for genome in population]
    genome_probabilities = [genome.get_fitness() / total_fitness for genome in population]
    # select based on probability
    randomly_selected_fitness = numpy.random.choice(a=all_fitnesses, size=1, p=genome_probabilities)
    return get_genome_with_fitness(population, randomly_selected_fitness)


def rank_based_roulette_wheel(population):
    ranked_genomes = sorted(population.genomes, key=lambda genome: genome.get_fitness(), reverse=True)
    ranked_fitnesses = [genome.get_fitness() for genome in ranked_genomes]
    n = population.get_size()
    genome_probabilities = []
    for i in range(1, n + 1):
        p = (2 * (n + 1 - i)) / (n ** 2 + n)
        genome_probabilities.append(p)
    # select random genome based on probability
    randomly_selected_fitness = numpy.random.choice(a=ranked_fitnesses, size=1, p=genome_probabilities)
    return get_genome_with_fitness(population, randomly_selected_fitness)


def get_genome_with_fitness(population, f):
    for i in range(0, population.get_size()):
        if population[i].get_fitness() == f:
            return population[i]
