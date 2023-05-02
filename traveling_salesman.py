import numpy as np
import random

# Define the distance matrix between cities
distance_matrix = np.array([
    [0, 2, 3, 4],
    [2, 0, 5, 6],
    [3, 5, 0, 7],
    [4, 6, 7, 0]
])

# Define the parameters for the genetic algorithm
population_size = 50
mutation_probability = 0.01
generations = 100

# Define a function to calculate the fitness of a candidate solution
def calculate_fitness(solution):
    total_distance = 0
    for i in range(len(solution)):
        total_distance += distance_matrix[solution[i-1], solution[i]]
    return 1 / total_distance

# Define a function to generate an initial population of candidate solutions
def generate_initial_population():
    population = []
    for _ in range(population_size):
        solution = list(range(len(distance_matrix)))
        random.shuffle(solution)
        population.append(solution)
    return population

# Define a function to perform mutation on a candidate solution
def mutate(solution):
    if random.random() < mutation_probability:
        i, j = random.sample(range(len(solution)), 2)
        solution[i], solution[j] = solution[j], solution[i]
    return solution

# Define a function to perform crossover on two parent solutions
def crossover(parent1, parent2):
    i, j = random.sample(range(len(parent1)), 2)
    if i > j:
        i, j = j, i
    child = [-1] * len(parent1)
    for k in range(i, j+1):
        child[k] = parent1[k]
    index = 0
    for k in range(len(parent2)):
        if parent2[k] not in child:
            if index == i:
                index = j+1
            child[index] = parent2[k]
            index += 1
    return child

# Define the main genetic algorithm function
def genetic_algorithm():
    population = generate_initial_population()
    for _ in range(generations):
        population_fitness = []
        for solution in population:
            population_fitness.append(calculate_fitness(solution))
        elite_index = np.argmax(population_fitness)
        elite_solution = population[elite_index]
        new_population = [elite_solution]
        while len(new_population) < population_size:
            parent1, parent2 = random.choices(population, weights=population_fitness, k=2)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        population = new_population
    return elite_solution

# Run the genetic algorithm and print the best solution
best_solution = genetic_algorithm()
print("Best solution: ", best_solution)