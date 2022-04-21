# This script shows the GA using PyGad for this max function:
# y = x^2

import pygad
import numpy
import random

val = random.random()

desired_output = 64

def fitness_func(solutions, solution_idx):
    output = solutions[0]
    output *= output
    return 1.0/numpy.abs(output - desired_output)

# Parameters
fitness_function = fitness_func

num_generations = 50
num_parents_mating = 2

sol_per_pop = 8

num_genes = 1

init_range_low = 0
init_range_high = 10

parent_selection_type = "rank"

keep_parents = 1

crossover_type = "single_point"

mutation_type = "random"

mutation_percent_genes = 10

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       init_range_low=init_range_low,
                       init_range_high=init_range_high,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

# ga_instance.plot_result()

print("-------------------------------Result--------------------------------")

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

prediction = solution
print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))
