import random

problem_example = (
    (0, 1, 1, 0, 1),
    (1, 0, 1, 0, 0),
    (1, 1, 0, 1, 1),
    (0, 0, 1, 0, 0),
    (1, 0, 1, 0, 0)
)

def generate_random_array(length):
    # Genera un array de elementos aleatorios dado el alfabeto
    random_array = []
    return random_array

def generate_initial_population(pop_size, *args, **kwargs):
    dataset = kwargs['dataset'] # Dataset con la misma estructura que el ejemplo
    # Obtener el alfabeto y la longitud a partir del dataset
    # Genera una población inicial de tamaño pop_size
    initial_pop = []
    return initial_pop

def fitness(solution, *args, **kwargs):
    dataset = kwargs['dataset']
    # Calcula el beneficio representado en 'solution'
    # Considera que p es al menos 1 para evitar dividir entre 0
    q = 0
    return q

def roulette_selection(population, fitness, number_parents, *args, **kwargs):
    # Selecciona number_parents individuos de la población mediante selección por ruleta
    parents = []
    return parents

def one_point_crossover(parent1, parent2, p_cross, *args, **kwargs):
    # Realiza el cruce de dos padres con una probabilidad p_cross
    child1, child2 = [], []
    return child1, child2

def uniform_mutation(chromosome, p_mut, *args, **kwargs):
    dataset = kwargs['dataset'] # Dataset con la misma estructura que el ejemplo
    # Realiza la mutación gen a gen con una probabilidad p_mut
    chromosome = []
    return chromosome

def elitism(population, fitness, offspring, fitness_offspring, *args, **kwargs):
    elite = kwargs['elite_n']
    # Realiza la sustitución generacional de la población con elitismo
    # Debe devolver tanto la nueva población como el fitness de la misma
    new_pop, new_fit = [], []
    return new_pop, new_fit

def generation_stop(generation, fitness, *args, **kwargs):
    max_gen=kwargs['max_gen']
    # Comprueba si se cumple el criterio de parada (máximo número de generaciones)
    return False

def genetic_algorithm(generate_population, pop_size, fitness_function, stopping_criteria, offspring_size,
                      selection, crossover, p_cross, mutation, p_mut, environmental_selection, *args, **kwargs):
    # Aplica un algoritmo genético a un problema de maximización
    population = generate_population(pop_size, *args, **kwargs) # Crea la población de individuos de tamaño pop_size
    fitness = [fitness_function(item, *args, **kwargs) for item in population] # Contiene la evaluación de la población
    best_fitness = [] # Guarda el mejor fitness de cada generación
    mean_fitness = [] # Guarda el fitness medio de cada generación
    generation = 0 # Contador de generaciones

    # 1 - Inicializa la población con la función generate_population
    # 2 - Evalúa la población con la función fitness_function
    # 3 - Mientras no se cumpla el criterio de parada stopping_criteria
    # 4 - Selección de padres con la función selection
    # 5 - Cruce de padres mediante la función crossover con probabilidad p_cross
    # 6 - Mutación de los descendientes con la función mutation con probabilidad p_mut
    # 7 - Evaluación de los descendientes
    # 8 - Generación de la nueva población con la función environmental_selection

    return population, fitness, generation, best_fitness, mean_fitness

def measure_sol_genetic(output):
    # output es la salida de genetic_algorithm. Es decir := (population, fitness, generation, best_fitness, mean_fitness)
    benefit = None
    # Mide el MEJOR fitness que haya encontrado el algoritmo genético
    # get index from fitness
    return benefit