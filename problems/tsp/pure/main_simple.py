import random
import math


total_cities = 4 # total number of cities 
pop_size = 50
PERCENTAGE = 0.5 # how much of the current pop_routes to crossover for the next generation

# ----------------------------------------------
class Route:
    def __init__(self):
        self.distance = 0
        self.path = random.sample(list(range(total_cities)), total_cities) # list of paths

    # euclidean Distance
    def calcDistance(self):
        distance = 0
        for i, cityNum in enumerate(self.path):
            distance += math.sqrt((cities[self.path[i]][0] - cities[self.path[i-1]][0])**2 + \
                                 (cities[self.path[i]][1] - cities[self.path[i-1]][1])**2)
        self.distance = distance
        return distance
# ----------------------------------------------

# randomly initializing the coordinates of the cities
cities = [(random.randint(0, 100), random.randint(0, 200)) for i in range(total_cities)] 

# population is list of routes
pop_routes = [Route() for i in range(pop_size)]

# sorts the pop_routes on the basis of the fitness function, ie, the distance of the route
def sortPop():
    global pop_routes
    pop_routes.sort(key = lambda route : route.distance, reverse = False)
    return

def crossover():
    global pop_routes

    updated_pop = []

    # select pop_routes based on the percentage
    updated_pop.extend(pop_routes[: int(pop_size*PERCENTAGE)])
    
    # parent selection is random
    for i in range(pop_size - len(updated_pop)):
        index1 = random.randint(0, len(updated_pop) - 1)
        index2 = random.randint(0, len(updated_pop) - 1)

        # loop until getting different indices for the parents
        while index1 == index2:
            index2 = random.randint(0, len(updated_pop) - 1)

        parent1 = updated_pop[index1]
        parent2 = updated_pop[index2]

        rand_index = random.randint(0, total_cities - 1)

        # declare new child from mating parent1 + parent2
        # mutation is random
        child = Route()
        child.path = parent1.path[:rand_index]

        # start:rand_index from first parent1 and rand_index:end from parent2
        # select paths from parent2 when not in child path
        # add other paths
        notInChild = [path for path in parent2.path if not path in child.path]

        child.path.extend(notInChild)
        
        # add the child to the updated pop_routes
        updated_pop.append(child)

    pop_routes = updated_pop
    return


def main():
    global pop_routes
    counter = 0

    best_route = random.choice(pop_routes)

    minDistance = best_route.calcDistance()

    while counter <= pop_size:
        # for each route in pop_routes
        # calc distance between cities in this route
        for element in pop_routes:
            element.calcDistance()

        sortPop()
        crossover()
        
        for element in pop_routes:
            if element.distance < minDistance:
                minDistance = element.calcDistance()
                best_route = element
            elif element.distance == minDistance:
                counter += 1


    print("-------------------------------Result--------------------------------")
    print("cities: {}".format(cities))
    print("The minimum distance is : {}".format(minDistance))
    print("A feasible path : {}".format(best_route.path))

if __name__ == "__main__":
    main()
