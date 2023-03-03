from genetic_algorithm.GeneticAlgorithm import GeneticAlgorithm
from util import FileReader, Statistics
from genetic_algorithm.Population import Population
from util.Options import Options

population_size = 50
number_of_generations = 200

if __name__ == '__main__':
    # get user input
    options = Options()
    options.summarize()

    # gen 1st population from read cities
    cities = FileReader.read_csv('../data/cities_europe.csv')
    population = Population(cities, population_size, True)

    # setup algorithm and run
    print("Best trip length before: " + str(population.get_fittest_genome().get_length()) + "\n")
    print("--------------------Start--------------------")
    algo = GeneticAlgorithm(cities, population, number_of_generations,
                            options.elite, options.selection,
                            options.p, options.tournament_size,
                            options.crossover, options.mutation, options.mutation_rate)
    score = algo.run_with_visualisation()
    print("---------------------Fin---------------------\n")
    print("Best trip length after: " + str(algo.distance_after) + "\n")
    print("Improvmenet score: " + score)

    # write statistics
    Statistics.write(algo, population_size,
          options.selection_to_string(),
          options.crossover_to_string(),
          options.mutation_to_string())
