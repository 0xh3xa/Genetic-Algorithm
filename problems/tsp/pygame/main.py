import random
import pygame
import sys
import math
import time

pygame.init()
font = pygame.font.Font('freesansbold.ttf', 15)
WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Travelling Salesman Problem")


total_cities = 15 # total number of cities 
pop_size = 5000
PERCENTAGE = 0.5 # how much of the current pop_routes to crossover for the next generation

# ----------------------------------------------
class City:
    def __init__(self, x, y, i):
        self.x = x
        self.y = y
        self.num = i
        self.text = font.render(str(self.num), False, (255, 0, 0))

    def display(self):
        pygame.draw.circle(screen, (0, 250, 0), (self.x, self.y), 5)

# ----------------------------------------------
class Route:
    def __init__(self):
        self.distance = 0
        self.cityPath = random.sample(list(range(total_cities)), total_cities) # list of paths

    def display(self):
        for i, cityNum in enumerate(self.cityPath):
            pygame.draw.line(screen, (255, 255, 255), (cities[self.cityPath[i]].x, cities[self.cityPath[i]].y), \
                            (cities[self.cityPath[i-1]].x, cities[self.cityPath[i-1]].y))

    # euclidean Distance
    def calcDistance(self):
        distance = 0
        for i, cityNum in enumerate(self.cityPath):
            distance += math.sqrt((cities[self.cityPath[i]].x - cities[self.cityPath[i-1]].x)**2 + \
                                 (cities[self.cityPath[i]].y - cities[self.cityPath[i-1]].y)**2)
        self.distance = distance
        return distance
# ----------------------------------------------

# randomly initializing the coordinates of the cities
cities = [City(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), i) for i in range(total_cities)] 

# population is list of routes
pop_routes = [Route() for i in range(pop_size)]

# sorts the pop_routes on the basis of the fitness function, ie, the distance of the route
def sortPop():
    global pop_routes
    pop_routes.sort(key = lambda route : route.distance, reverse = False)
    return
'''
Takes the top PERCENTAGE of the pop_routes for a particular generation and 
produces a new pop_routes replacing the non essential members with new ones
'''
def crossover():
    global pop_routes

    updated_pop = []

    # select pop_routes based on the percentage
    updated_pop.extend(pop_routes[: int(pop_size*PERCENTAGE)])

    for i in range(pop_size - len(updated_pop)):
        index1 = random.randint(0, len(updated_pop) - 1)
        index2 = random.randint(0, len(updated_pop) - 1)

        # loop until getting different indices for the parents
        while index1 == index2:
            index2 = random.randint(0, len(updated_pop) - 1)

        parent1 = updated_pop[index1]
        parent2 = updated_pop[index2]

        rand_index = random.randint(0, total_cities - 1)

        # declare new child from this parents
        # using random mutaiton
        child = Route()
        child.cityPath = parent1.cityPath[:rand_index]

        # start:rand_index from first parent1 and rand_index:end from parent2
        # select paths from parent2 when not in child path
        # add other paths
        notInChild = [path for path in parent2.cityPath if not path in child.cityPath]

        child.cityPath.extend(notInChild)
        
        # add the child to the updated pop_routes
        updated_pop.append(child)

    pop_routes = updated_pop
    return


def main():
    global pop_routes
    counter = 0

    best_route = random.choice(pop_routes)

    minDistance = best_route.calcDistance()

    clock = pygame.time.Clock()
    
    while True:
        best_route.display()
        if counter >= pop_size:
            break
        clock.tick(60)
        pygame.display.update()
        screen.fill((0, 0, 0))
        for city in cities:
            city.display()
            screen.blit(city.text, (city.x - 20, city.y - 20))
      
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    print("-------------------------------Result--------------------------------")
    print("The minimum distance is : {}".format(minDistance))
    print("A feasible path : {}".format(best_route.cityPath))
    best_route.display()
    pygame.display.update()
    time.sleep(5)

if __name__ == "__main__":
    main()
