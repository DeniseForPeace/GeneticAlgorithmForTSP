class Options:
    def __init__(self):
        self.elite = 0
        self.elitism_options = ["Yes", "No"]

        self.selection = None
        self.selection_options = ["Deterministic_Truncation",
                                  "Tournament",
                                  "Roulette_Wheel",
                                  "Rank_Based_Roulette_Wheel"]
        self.p = 0.0
        self.tournament_size = 0

        self.crossover = None
        self.crossover_options = ["one_point_cut", "two_point_cut"]

        self.mutation = None
        self.mutation_options = ["Scramble", "Invert", "Swap"]
        self.mutation_rate = 0

    @staticmethod
    def interact(string, method):
        print(string)
        for idx, element in enumerate(method):
            print("{}) {}".format(idx + 1, element))
        i = input("Enter number: ")
        if 0 < int(i) <= 4:
            return int(i)
        else:
            raise ValueError('Your input does not correspond with any of the options, try again')

    def summarize(self):
        elitism = self.interact("Do you want elitism?", self.elitism_options)
        if elitism == 1:
            self.elite = int(input("How many of the fittest genomes shall pass on as is? (int, usually 1) "))
        print()
        self.selection = self.interact("Please choose the selection:", self.selection_options)
        if self.selection == 1:
            self.p = float(input("How many genomes shall evolve? (percentage as float) "))
        elif self.selection == 2:
            self.tournament_size = int(input("How many genomes shall compete in one tournament? (int, e.g. 5) "))
        print()
        self.crossover = self.interact("Please choose the crossover method:", self.crossover_options)
        print()
        self.mutation = self.interact("Please choose the mutation:", self.mutation_options)
        print()
        self.mutation_rate = float(input("Please choose the mutation rate? (percentage as float) "))

    def selection_to_string(self):
        if self.selection == 1:
            return self.selection_options[0]
        if self.selection == 2:
            return self.selection_options[1]
        if self.selection == 3:
            return self.selection_options[2]
        if self.selection == 4:
            return self.selection_options[3]

    def crossover_to_string(self):
        if self.crossover == 1:
            return self.crossover_options[0]
        if self.crossover == 2:
            return self.crossover_options[1]

    def mutation_to_string(self):
        if self.mutation == 1:
            return self.mutation_options[0]
        if self.mutation == 2:
            return self.mutation_options[1]
        if self.mutation == 3:
            return self.mutation_options[2]
