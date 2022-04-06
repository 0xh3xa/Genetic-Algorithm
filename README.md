### Genetic Algorithm GA class

This repository contains the practical for the Genetic Algorithm (GA) class
[![hello_genetic](https://img.shields.io/static/v1?label=Genetic&message=Algorithms&color=blue&style=flat)](https://github.com/EbGazar/Genetic-Algorithm)
[![Python](https://img.shields.io/static/v1?label=Language&message=Python&color=lightblue&style=flat)](https://github.com/EbGazar/Genetic-Algorithm)

### What is Genetic Algorithm (GA)

### Pros and Cons of Genetic Algorithm (GA)

### Application of Genetic Algorithm (GA)

### Machine Learning vs. Neural Networks vs. Deep Learning vs. Genetic Genetic Algorithm (GA)

### Environment Setup

1. VS Code
2. Python-3
3. Anaconda (Optional)
4. PyGad
5. PyGame

### Technologies

Some solutions are using libraries like PyGad while others not (Pure Python implementation). Some problems' solutions are both using libraries and Pure Python.

The Libraries which are used

1. PyGad
2. PyGame

### Problems

1. Linear Model
2. Square function
3. Traveling salesman problem (TSP)
4. Simple Linear Regression

#### PyGad

Is an open-source Python library for building the genetic algorithm and optimizing machine learning algorithms. It works with Keras and PyTorch. <a href="https://pygad.readthedocs.io/en/latest/">More</a>

#### GA class parameters in PyGad library

These variables are assigned values and passed to GA class

<table border="2">
    <tr>
        <th>
            Parameter
        </th>
        <th>
            Description
        </th>
        <th>
            Usage Example
        </th>
    </tr>
    <tr>
        <td>
            fitness_function
        </td>
        <td>
            Declare your fitness function and assign it to 
        </td>
        <td>
            fitness_function = fitness_func
        </td>
    </tr>
    <tr>
        <td>
            num_generations
        </td>
        <td>
            Declare number of generation
        </td>
        <td>
            num_generations = 50
        </td>
    </tr>
    <tr>
        <td>
            num_parents_mating
        </td>
        <td>
            Declare number of parents mating
        </td>
        <td>
            num_parents_mating = 4
        </td>
    </tr>
    <tr>
        <td>
            sol_per_pop
        </td>
        <td>
            Number of solutions (i.e. chromosomes) within the population. This parameter has no action if initial_population parameter exists
        </td>
        <td>
            sol_per_pop = 8
        </td>
    </tr>
    <tr>
        <td>
            num_genes
        </td>
        <td>
            Number of genes in the solution/chromosome. It is not needed if the user feeds the initial population to the initial_population parameter
        </td>
        <td>
            num_genes = 4
        </td>
    </tr>
    <tr>
        <td>
            init_range_low
            init_range_high
        </td>
        <td>
            mutation value is selected randomly init_range_low and init_range_high from the range specified by the
        </td>
        <td>
            init_range_low = 0
            init_range_high = 6
        </td>
    </tr>
    <tr>
        <td>
            parent_selection_type
        </td>
        <td>
            parent selection type are:
            <ol>
                <li>steady-state selection (sss)</li>
                <li>roulette wheel selection (rws)</li>
                <li>stochastic universal selection (sus)</li>
                <li>rank selection (rank selection)</li>
                <li>random selection (random)</li>
                <li>tournament selection (tournament)</li>
            </ol>
        </td>
        <td>
            parent_selection_type = "sss"
        </td>
    </tr>
    <tr>
        <td>
            keep_parents
        </td>
        <td>
            Number of parents to keep in the current population
-1 (default) means to keep all parents in the next population
0 means keep no parents in the next population
        </td>
        <td>
            keep_parents = 1
        </td>
    </tr>
    <tr>
        <td>
            crossover_type
        </td>
        <td>
            Types of the crossover operation are:
            <ol>
                <li>single-point crossover (single_point)</li>
                <li>two points crossover (two_points)</li>
                <li>uniform crossover (uniform)</li>
                <li>scattered crossover (scattered)</li>
            </ol>
        </td>
        <td>
            crossover_type = "single_point"
        </td>
    </tr>
    <tr>
        <td>
            mutation_type
        </td>
        <td>
            mutation operation are:
            <ol>
                <li>random mutation (random)</li>
                <li>swap mutation (swap)</li>
                <li>inversion mutation (inversion)</li>
                <li>scramble mutation (scramble)</li>
                <li>adaptive mutation (adaptive)</li>
            </ol>
        </td>
        <td>
            mutation_type = "random"
        </td>
    </tr>
    <tr>
        <td>
            mutation_percent_genes
        </td>
        <td>
            Percentage of genes to mutate
10% of the genes will be mutated
It must be >0 and <=100
        </td>
        <td>
            mutation_percent_genes = 10
        </td>
    </tr>
</table>

* PyGad initialize_population with the following (init_range_low, init_range_high, allow_duplicate_genes, True, gene_type)

* For more information about parameters visit <a href="">PyGad Documentation</a>


### GA Pattern

The pattern for any GA are theses steps:

1. Declare input(s)
2. Declare output
3. Fitness_function
4. Crossover and/or mutation

### Crossover types


### Mutation types
