import random
from tsp.Tour import Tour


def one_point_cut(genes, parent1, parent2):
    child = Tour(genes)
    genome_size = len(genes)
    # random cutting point
    cutting_point = int(random.random() * genome_size)
    for i in range(0, cutting_point):
        child.set_city(i, parent1.get_city(i))

    return fill_rest(genome_size, child, parent2)


def two_point_cut(genes, parent1, parent2):
    child = Tour(genes)
    genome_size = len(genes)

    # randomly generate start/end positions of one parent:
    start_pos = int(random.random() * genome_size)
    end_pos = int(random.random() * genome_size)

    # within a part of a sequence exchange all the genes with the ones from 1st parent
    for i in range(0, genome_size):
        if start_pos < end_pos and start_pos < i < end_pos:
            child.set_city(i, parent1.get_city(i))
        elif start_pos > end_pos:
            if not (start_pos > i > end_pos):
                child.set_city(i, parent1.get_city(i))

    return fill_rest(genome_size, child, parent2)


# fill remaining missing genes in child with genes from 2nd parent
def fill_rest(genome_size, child, parent2):
    for i in range(0, genome_size):
        if not child.has_city(parent2.get_city(i)):
            for j in range(0, genome_size):
                if child.get_city(j) is None:
                    child.set_city(j, parent2.get_city(i))
                    break
    return child  # returns only one child!
