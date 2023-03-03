import os

import numpy as np


def write(algo, population_size, selection, crossover, mutation):
    save_path = '../data/statistics/'
    file_name = "population-size-" + str(population_size) + "_" + \
                "num-generations-" + str(algo.num_gens) + "_" + \
                str(algo.elite) + "-elite-genomes_" + \
                selection + "-selection_" + mutation + "-mutation" + ".txt"

    complete_name = os.path.join(save_path, file_name)
    f = open(complete_name, "w")

    f.write("\nAll targeted cities: " + str(algo.genes))
    f.write("\nPopulation size: " + str(population_size))
    f.write("\nNumber of generations: " + str(algo.num_gens))
    f.write("\nEvolution stopped at generation number: " + str(algo.stopped_at_gen))
    if algo.elite > 0:
        f.write("\nElitism activated. Number of elite genomes: " + str(algo.elite))
    else:
        f.write("\nNo elitism.")
    f.write("\nSelection Type: " + selection)
    if float(algo.no_p) > 0.0:
        f.write("\nPercentage of fittest evolved genomes: " + algo.no_p)
    if int(algo.tournament_size) > 0:
        f.write("\nNumber of competing genomes in one tournament: " + str(algo.tournament_size))
    f.write("\nCrossover type: " + crossover)
    f.write("\nMutation Type: " + mutation)
    f.write("\nMutation rate: " + algo.mutation_rate)
    f.write("\nBest Distance before: " + str(algo.distance_before))
    f.write("\nBest Distance after: " + str(algo.distance_after))
    f.write("\nBest Route: " + str(algo.best_route))
    f.write("\nImprovement score: " + str(algo.improvement_score) + "%")

    f.close()


def write_experiment_results(title, num_iterations, pop_size, num_generations,
                             elite, selection, p, tournament_size, crossover, mutation, mrate,
                             x_results, y_results):
    save_path = '../../data/experiment_graphs/'
    file_name = title + "_" + str(num_iterations) + ".txt"
    complete_name = os.path.join(save_path, file_name)
    f = open(complete_name, "w")
    f.write(title)
    f.write("\nNumber of iterations: " + str(num_iterations))
    f.write("\nPopulation size: " + str(pop_size))
    f.write("\nNumber of generations: " + str(num_generations))
    f.write("\nElite: " + str(elite))
    f.write("\nSelection: " + str(selection))
    f.write("\np: " + str(p))
    f.write("\nTournament_size: " + str(tournament_size))
    f.write("\nCrossover: " + str(crossover))
    f.write("\nMutation: " + str(mutation))
    f.write("\nMutation rate: " + str(mrate))
    f.write("\nx_results: " + str(np.array(x_results)))
    f.write("\ny_results: " + str(np.array(y_results)))

    f.close()

