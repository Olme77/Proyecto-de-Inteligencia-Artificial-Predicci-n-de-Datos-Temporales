import random

import numpy as np

problem_example = (
    (0, 1, 1, 0, 1),
    (1, 0, 1, 0, 0),
    (1, 1, 0, 1, 1),
    (0, 0, 1, 0, 0),
    (1, 0, 1, 0, 0)
)

def generate_random_array(length):
    random_array = []
    # Genera un array de elementos aleatorios dado el alfabeto
    random_array = [random.randint(0,i) for i in range(length)]
    return random_array

def generate_initial_population(pop_size, *args, **kwargs):
    dataset = kwargs['dataset'] # Dataset con la misma estructura que el ejemplo
    # Obtener el alfabeto y la longitud a partir del dataset
    # Genera una población inicial de tamaño pop_size
    initial_pop = [generate_random_array(len(dataset)) for i in range(pop_size)]
    return initial_pop

def matriz_a_aristas(adj):
    n = len(adj)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):  # solo mitad superior para no duplicar
            if adj[i][j]:
                edges.append((i, j))
    return edges

def fitness(solution, *args, **kwargs):
    # dataset = kwargs['dataset']
    edges = kwargs['edges']
    # Calcula el beneficio representado en 'solution'
    # Considera que p es al menos 1 para evitar dividir entre 0
    # Utilizo una lista de aristas que es más eficiente para el cálculo del fitness
    c = len(set(solution))
    p = 0
    for edge in edges :
        if solution[edge[0]] == solution[edge[1]] :
            p += 1
    # Set te elimina los elementos repetidos

    q = 1 / (c * (p + 1))
    return q

def roulette_selection(population, fitness, number_parents, *args, **kwargs):
    # Selecciona number_parents individuos de la población mediante selección por ruleta
    parents = []
    acum_fitness = sum(fitness)
    probabilites = [ fitness[i] / acum_fitness for i in range(len(population))]
    acum_probabilities = [sum(probabilites[0:i]) for i in range(1,len(population))]
    # Realiza una elección aleatoria no equiprobable sobre los individuos
    for i in range(number_parents) :
        r = random.uniform(0,1)
        index = np.digitize(r,acum_probabilities) - 1
        parents.append(population[index])

    return parents

def copy(item):
    new_item = list(item)  # Es para crear listas independientes con los mismos valores.
    return new_item

def one_point_crossover(parent1, parent2, p_cross, *args, **kwargs):
    # Realiza el cruce de dos padres con una probabilidad p_cross
    child1 = []
    child2 = []
    r1 = random.uniform(0,1)
    if r1 < p_cross :
        # Se selecciona el punto de corte del cromosoma mediante elección
        # equiprobable entre 1 y L − 1 siendo L el número de elementos del cromosoma
        r2 = random.uniform(0,1)
        probabilities = [i / (len(parent1) - 1) for i in range(len(parent1))]
        cross_point = np.digitize(r2,probabilities)
        child1 = copy(parent1)
        child1[cross_point:] = parent2[cross_point:]
        child2 = copy(parent2)
        child2[cross_point:] = parent1[cross_point:]
    return child1, child2

def uniform_mutation(chromosome, p_mut, *args, **kwargs):
    dataset = kwargs['dataset'] # Dataset con la misma estructura que el ejemplo
    # Realiza la mutación gen a gen con una probabilidad p_mut
    for i in range(len(chromosome)) :
        p1 = random.uniform(0,1)
        if p1 < p_mut :
            probabilities = [j / (i + 1) for j in range(0,i + 2)]
            p2 = random.uniform(0,1)
            chromosome[i] = int(np.digitize(p2,probabilities) - 1)
    return chromosome

def elitism(population, fitness, offspring, fitness_offspring, *args, **kwargs):

    # Realiza la sustitución generacional de la población con elitismo
    # Debe devolver tanto la nueva población como el fitness de la misma

    elite = kwargs['elite_n']

    # elite_n número de mejores descendientes a añadir a la nueva población
    # offspring es el número de descendientes
    # fitness_offspring lista ordenada de los descendientes según su fitness

    # Ordenamos la población de padres según su fitness
    parents_sorted = sorted(population, key= lambda t : fitness(t,*args,**kwargs), reverse=True)

    # Añadimos los elite mejores padres a la nueva lista
    new_pop = [parents_sorted[i] for i in range(0,elite)]

    #Añadimos el resto de descendientes hasta completar offspring elementos
    for i in range(elite,offspring) :
        new_pop.append(fitness_offspring[i - elite])

    new_fit = [fitness(item, *args, **kwargs) for item in new_pop]

    return new_pop, new_fit

def generation_stop(generation, fitness, *args, **kwargs):
    max_gen=kwargs['max_gen']
    # Comprueba si se cumple el criterio de parada (máximo número de generaciones)
    return generation >= max_gen


def copy(population):
    new_population =  list(population)  # Es para crear listas independientes con los mismos valores.
    return new_population

def calculate_best_fitness(population,fitness_list,best_fitness,fitness_function,*args,**kwargs) :
    # fitness_list: lista con los valores de fitness de cada cromosoma de population
    # best_fitness: lista con los cromosomas con mejor fitness de cada generación
    # Calcula la lista de cromosomas con mejor fitness de population y lo añade a best_fitness
    best_value = max(fitness_list)
    best_value_elements = []
    for i, value in enumerate(fitness_list) :
        if value == best_value :
            best_value_elements.append(population[i])

    #Añado la lista a best_fitness
    best_fitness += best_value_elements

    #Elimino elementos repetidos
    best_fitness = np.unique(best_fitness, axis=0).tolist()

    #Ordeno por fitness
    best_fitness = sorted(best_fitness, key= lambda t : fitness_function(t,*args,**kwargs), reverse= True)

    return best_fitness


def genetic_algorithm(generate_population, pop_size, fitness_function, stopping_criteria, offspring_size,
                      selection, crossover, p_cross, mutation, p_mut, environmental_selection, *args, **kwargs):
    # test
    dataset = kwargs['dataset']
    # convierto matriz de adyacencias a una lista de aristas
    edges = matriz_a_aristas(dataset)
    kwargs['edges'] = edges
    # Aplica un algoritmo genético a un problema de maximización
    best_fitness = [] # Guarda el mejor fitness de cada generación
    mean_fitness = [] # Guarda el fitness medio de cada generación
    generation = 0 # Contador de generaciones

    # 1 - Inicializa la población con la función generate_population
    population = generate_population(pop_size, *args, **kwargs) # Crea la población de individuos de tamaño pop_size
    # 2 - Evalúa la población con la función fitness_function
    fitness = [fitness_function(item, *args, **kwargs) for item in population] # Contiene la evaluación de la población
    # 3 - Mientras no se cumpla el criterio de parada stopping_criteria
    while not stopping_criteria(generation,fitness,*args,**kwargs) :
        new_population = []
        while offspring_size > len(new_population) :
            # 4 - Selección de padres con la función selection
            parents = selection(population, fitness, 2, *args, **kwargs)
            # 5 - Cruce de padres mediante la función crossover con probabilidad p_cross
            child1, child2 = crossover(parents[0], parents[1], p_cross, *args, **kwargs)
            # 6 - Mutación de los descendientes con la función mutation con probabilidad p_mut
            if child1 :
                child1 = mutation(child1,p_mut,*args,**kwargs)
                child2 = mutation(child2,p_mut,*args,**kwargs)
                new_population.append(child1)
                new_population.append(child2)

        # 7 - Evaluación de los descendientes
        fitness_offspring = sorted(new_population, key= lambda t : fitness_function(t,*args,**kwargs), reverse = True)

        # 8 - Generación de la nueva población con la función environmental_selection
        new_population, new_fit = environmental_selection(population,fitness_function,offspring_size,fitness_offspring,*args,**kwargs)
        population = copy(new_population)
        fitness = [fitness_function(item, *args, **kwargs) for item in population]

        # Calculo lista de elementos con el mejor fitness de la generación actual y lo añado a la lista best_fitness
        best_fitness = calculate_best_fitness(population,new_fit,best_fitness,fitness_function,*args, **kwargs)

        # Calculo fitness medio de la nueva generación y lo añado a mean_fitness
        mean_fitness.append(np.mean(new_fit))

        generation += 1

    # Utilizo la variable fitness para almacenar el valor de fitness de cada cromosoma de best_fitness
    fitness = [fitness_function(item,*args,**kwargs) for item in best_fitness]

    return population, fitness, generation, best_fitness, mean_fitness, edges

def measure_sol_genetic(output):
    # output es la salida de genetic_algorithm. Es decir := (population, fitness, generation, best_fitness, mean_fitness)
    # best_fitness: lista con los cromosomas con mejor fitness de cada generación
    best_fitness = output[3]
    # fitness almacena el valor de fitness de cada cromosoma de best_fitness
    fitness = output[1]
    # obtengo la lista de aristas correspondiente a la matriz de adyacencia para comprobar los cromosomas solución
    edges = output[5]

    candidates = []
    best_value = max(fitness)

    for i,value in enumerate(fitness) :
        if value == best_value :
            candidates.append(best_fitness[i])

    benefit = best_value
    solutions = []
    for candidate in candidates :
        for edge in edges :
            if candidate[edge[0]] == candidate[edge[1]] :
                break
        else : # Se ejecuta si el bucle for finaliza sin break
            solutions.append(candidate)

    return benefit,solutions