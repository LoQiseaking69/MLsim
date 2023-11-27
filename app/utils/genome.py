
import random

class Genome:
    def __init__(self, genes):
        self.genes = genes

    def mutate(self):
        mutation_rate = 0.1
        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                self.genes[i] += random.choice([-1, 1])

    def crossover(self, other_genome):
        crossover_point = len(self.genes) // 2
        new_genes = self.genes[:crossover_point] + other_genome.genes[crossover_point:]
        return Genome(new_genes)
