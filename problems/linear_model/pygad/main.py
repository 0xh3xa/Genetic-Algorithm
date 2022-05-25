# This script shows the GA using PyGad for this Linear:
# y = w1x1 + w2x2 + w3x3 + w4x4 + w5x5 + w6x6

import pygad
import numpy

# represents x's
inputs = [4,-2,3.5,5,-11,-4.7]
desired_output = 44

def fitness_func(weights, weight_idx):
    output = numpy.sum(weights*inputs)
    return 1.0/numpy.abs(output - desired_output)

# Parameters
fitness_function = fitness_func

ga_instance = pygad.GA(num_generations=50,
                       num_parents_mating=4,
                       fitness_func=fitness_function,
                       sol_per_pop=8,
                       num_genes=len(inputs),
                       init_range_low=-2,
                       init_range_high=5,
                       parent_selection_type="sss",
                       keep_parents=1,
                       crossover_type="single_point",
                       mutation_type="random",
                       mutation_percent_genes=10)

ga_instance.run()

# ga_instance.plot_result()

print("-------------------------------Result--------------------------------")

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best weights : {solution}".format(solution=solution))
print("Fitness value of the best weightes = {solution_fitness}".format(solution_fitness=solution_fitness))

prediction = numpy.sum(numpy.array(inputs)*solution)
print("Predicted output based on the best weights : {prediction}".format(prediction=prediction))
