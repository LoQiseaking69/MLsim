
class Individual:
    def __init__(self, genome):
        self.genome = genome
        self.fitness = 0
        self.energy = 100
        self.health = 100

    def update(self, environmental_data):
        decision = self.simple_decision_process(environmental_data)
        self.execute_decision(decision)
        self.calculate_fitness()

    def simple_decision_process(self, data):
        decision = sum(data) > 0
        return decision

    def execute_decision(self, decision):
        if decision:
            self.energy -= 10
        else:
            self.energy -= 5

    def calculate_fitness(self):
        self.fitness = self.energy + self.health
