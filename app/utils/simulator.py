
import random
from .individual import Individual
from .genome import Genome

class Simulator:
    def __init__(self, population_size, environment):
        self.population = [Individual(Genome([0, 1, 2])) for _ in range(population_size)]
        self.environment = environment

    def run_simulation(self, generations):
        for _ in range(generations):
            self.update_environment()
            self.update_population()
            self.evaluate_fitness()
            self.reproduce_population()
            self.remove_deceased()

    def update_environment(self):
        self.environment = [random.randint(-5, 5) for _ in range(3)]

    def update_population(self):
        for individual in self.population:
            individual.update(self.environment)

    def evaluate_fitness(self):
        for individual in self.population:
            individual.calculate_fitness()

    def reproduce_population(self):
        if len(self.population) < 100:
            self.population.append(Individual(Genome([0, 1, 2])))

    def remove_deceased(self):
        self.population = [ind for ind in self.population if ind.health > 0 and ind.energy > 0]
