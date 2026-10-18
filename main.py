from genetic import genetic_algorithm, measure_sol_genetic, generate_initial_population, fitness, generation_stop, \
    roulette_selection, one_point_crossover, uniform_mutation, elitism
from search import search, initial_state, expand, cost, order_astar, is_solution, measure_sol_search, heuristic

################################# NO TOCAR #################################
#                                                                          #
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print("Execution time: ", end - start, " seconds")
        return res

    return wrapper


#                                                                          #
################################# NO TOCAR #################################

# Este codigo temporiza la ejecución de una función cualquiera

################################# NO TOCAR #################################
#                                                                          #
@timer
def search_run(dataset, heuristic):
    output = search(dataset, initial_state, expand, cost, heuristic, order_astar, is_solution)
    return measure_sol_search(output)


@timer
def genetic_run(generate_population, pop_size, fitness_function, stopping_criteria,
                offspring_size, selection, crossover, p_cross, mutation, p_mut,
                environmental_selection, dataset, *args, **kwargs):
    output = genetic_algorithm(generate_population,
                               pop_size,
                               fitness_function,
                               stopping_criteria,
                               offspring_size,
                               selection,
                               crossover,
                               p_cross,
                               mutation,
                               p_mut,
                               environmental_selection,
                               dataset=dataset,
                               *args, **kwargs)
    return measure_sol_genetic(output)


#                                                                          #
################################# NO TOCAR #################################
# Grafo de 4 vértices
problem_4 = ((0, 1, 1, 0),
             (1, 0, 1, 0),
             (1, 1, 0, 1),
             (0, 0, 1, 0),
             )
# Grafo de 5 vértices:
problem_5 = (
    (0, 1, 1, 1, 1),
    (1, 0, 1, 1, 1),
    (1, 1, 0, 1, 1),
    (1, 1, 1, 0, 1),
    (1, 1, 1, 1, 0),
)

# Grafo de 8 vértices:
problem_8 = (
    (0, 1, 1, 1, 1, 1, 0, 1),
    (1, 0, 1, 1, 1, 0, 1, 1),
    (1, 1, 0, 1, 0, 1, 1, 0),
    (1, 1, 1, 0, 1, 0, 0, 1),
    (1, 1, 0, 1, 0, 1, 1, 1),
    (1, 0, 1, 0, 1, 0, 1, 1),
    (0, 1, 1, 0, 1, 1, 0, 1),
    (1, 1, 0, 1, 1, 1, 1, 0),
)

# Grafo de 12 vértices:
problem_12 = (
    (0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1),
    (1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1),
    (1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1),
    (1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0),
    (1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1),
    (1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0),
    (1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0),
    (1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0),
    (0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1),
    (1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0),
    (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1),
    (1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0),
)

# Grafo de 18 vértices:
problem_18 = (
    (0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1),
    (1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1),
    (0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0),
    (0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0),
    (0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1),
    (1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0),
    (0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0),
    (1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0),
    (0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0),
    (0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0),
    (1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1),
    (0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1),
    (0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1),
    (1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0),
    (1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1),
    (0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0),
    (0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1),
    (1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0),
)

# Grafo de 25 vértices:
problem_25 = (
    (0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1),
    (1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0),
    (0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0),
    (0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0),
    (0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0),
    (0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0),
    (0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
    (0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0),
    (0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1),
    (0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0),
    (1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1),
    (0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0),
    (0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1),
    (0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0),
    (1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0),
    (0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0),
    (0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1),
    (1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0),
    (0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0),
    (0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0),
    (0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0),
    (0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0),
)
#problems = [problem_4]
#problems = [problem_5]
#problems = [problem_8]
#problems = [problem_12]
#problems = [problem_25]
problems = [problem_5,problem_8, problem_12, problem_18, problem_25]

# @title Ejemplo de ejecución completa
def main():
    for i, problem in enumerate(problems):
        print(f"Problem: {i}")
        search_benefit = search_run(problem, heuristic=heuristic)
        print(f"Search: {search_benefit}")
        ga_benefit = genetic_run(generate_population=generate_initial_population, pop_size=500,
                                  fitness_function=fitness,
                                  stopping_criteria=generation_stop,
                                  offspring_size=500,
                                  selection=roulette_selection,
                                  crossover=one_point_crossover, p_cross=0.8,
                                  mutation=uniform_mutation, p_mut=1 / len(problem),
                                  environmental_selection=elitism,
                                  dataset=problem,
                                  max_gen=100,
                                  elite_n=1)
        print(f"Genetic: {ga_benefit}")
        print("-----")

    # Ten en cuenta que genetic_run y search_run devuelven su tiempo de ejecucion automaticamente
    # por pantalla, un print tras ejecutarlos.
if __name__ == "__main__":
    main()