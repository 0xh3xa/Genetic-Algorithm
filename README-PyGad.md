#### PyGad

Is an open-source Python library for building the genetic algorithm and optimizing machine learning algorithms. It works with Keras and PyTorch. <a href="https://pygad.readthedocs.io/en/latest/">More</a>

#### GA class parameters in PyGad library

* For more information about parameters visit <a href="https://pygad.readthedocs.io/en/latest/README_pygad_ReadTheDocs.html">PyGad Parameters</a>

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
            lower and upper value of the random range from which the gene values in the initial population
        </td>
        <td>
            init_range_low = 0
            init_range_high = 6
        </td>
    </tr>
        <tr>
        <td>
            random_mutation_min_val
            random_mutation_max_val
        </td>
        <td>
            Used with random mutation they specify the min and max for the random range values
        </td>
        <td>
            random_mutation_min_val = 0
            random_mutation_max_val = 6
        </td>
    </tr>
    <tr>
        <td>
            parent_selection_type
        </td>
        <td>
            Parent selection type are:
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
            Mutation operations are:
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
            <ol>
                <li>mutation_percent_genes</li>
                <li>mutation_probability</li>
                <li>mutation_num_genes</li>
            </ol>
        </td>
        <td>
             <ol>
                <li>Percentage of genes to mutate, it must be > 0 and <=100, <span style="background:orange;">has no action if mutation_probability or mutation_num_genes exist</span></li>
                <li>probability of selecting a gene for applying the mutation operation, <span style="background:orange;">has no need for the 2 parameters mutation_percent_genes and mutation_num_genes</span></li>
                <li> Number of genes to mutate which defaults to None meaning that no number is specified, <span style="background:orange;">has no action if the parameter mutation_probability exists</span></li>
            </ol>
        </td>
        <td>
            mutation_percent_genes = 10
        </td>
    </tr>
</table>

* PyGad initialize_population with the following (init_range_low, init_range_high, allow_duplicate_genes, True, gene_type)
