import numpy as np
#import copy as cp

graph = [[]]
def initial_state(dataset):
    global graph
    graphCopy = np.array(dataset)
    graph = graphCopy.copy()
    state = {
        # "graph": dataset,
        "colors": [None for _ in range(len(dataset))]
    }
    return state


def copy(state):
    new_state = {
        # "graph": state['graph'],
        "colors": list(state['colors'])  # Es para crear listas independientes con los mismos valores.
    }
    return new_state


def colores_vecinos(A, u, state):
    """
    A: matriz de adyacencia como lista de listas (n x n)
    u: índice del nodo (0..n-1)
    """
    n = len(A)
    vecinos = []
    for v in range(n):
        if A[u][v] == 1:
            if v != u:
                color = state['colors'][v]
                if (color is not None):
                    vecinos.append(state['colors'][v])
    return vecinos

def expand(state):
    states = []  # Crea una lista vacía de estados
    # Busco el primer nodo con color a None

    for pos in range(len(state['colors'])):
        new_state = copy(state)
        color = 0
        if state['colors'][pos] is None:
            # Si el color no ha sido asignado previamente
            if color not in (state['colors']):
                new_state['colors'][pos] = color
                states.append(new_state)
            else:
                # Color ya asignado, comprobamos que no esté asignado a ningún nodo vecino al actual

                vecinos = colores_vecinos(graph,pos,state)
                color_asigned = False
                while not color_asigned:
                    if (color in vecinos):
                        color += 1
                    else:
                        color_asigned = True

                new_state['colors'][pos] = color
                states.append(new_state)

    return states  # Devolvemos una lista de estados

def is_solution(state):
    # Devuelve True si el estado es solucion, False en otro caso
    return None not in (state['colors'])


def cost(path):
    if path is None :
        return 0
    state = path[-1]
    # Crea una máscara booleana donde el valor NO sea None
    valid_colors = state['colors'][state['colors'] != None]
    return len(np.unique(valid_colors))


# El coste de un camino es el número de colores distintos empleados en el último estado del camino
# expand empeora la solución cuando genera estados cuyo coste c(P)
# , es decir, el número de colores distintos en su estado final,
# es mayor que el de otros caminos alternativos que llegan a estados “igual de buenos o mejores”.


def heuristic(state):
    # Calcula una heurística para un estado

    # ¿Cuanto coste tenemos que aportar para llegar al estado meta?

    # Si no hay heurística la consideramos a 0 :
    #return 0

    # heurística 1 : Necesitaremos tantos colores nuevos como nodos pendientes a colorear
    # Puede no ser admisible puesto que no reutilizamos colores ya asignados y por lo tanto
    # no nos lleva a una solución óptima

    # return sum(1 for x in state['colors'] if x is None)

    # heurística 2: Necesitaremos tantos colores nuevos como nodos pendientes a colorear menos el número de colores ya utilizados.
    #

    colores_validos = [c for c in state['colors'] if c is not None]
    x = len(np.unique(colores_validos))
    y = sum(1 for x in state['colors'] if x is None)
    if y < x:
       return 0
    else:
       return y - x


def eq(s1, s2):
    return np.array_equal(s1['colors'],s2['colors'])


def prune(path_list):
    # Si detecta que dos caminos llevan al mismo estado,
    # solo nos interesa aquel camino de menor coste
    # Recuerda que prune_list llega ordenada por coste
    # new_path_list = cp.deepcopy(path_list)
    # new_path_list = []
    #
    # Diccionario: Clave = Estado Final -> Valor = Camino Completo
    best_paths = {}

    for path in path_list:
        # Asumimos que el estado final es el último elemento del camino
        final_state = tuple(path[-1]['colors'])

        # Si el estado no está o encontramos un camino más barato a ese estado
        if (final_state not in best_paths) or (cost(path) < cost(best_paths[final_state])):
            best_paths[final_state] = path

    # Devolvemos solo los caminos ganadores
    return list(best_paths.values())
    # return sorted(best_paths.values(), key=lambda p: cost(p))



# *args y **kwargs son argumentos variables, si el argumento no es reconocido es almacenado en estas variables.
# Aquí se utilizan para ignorar argumentos innecesarios.

def order_astar(old_paths, new_paths, c, h, *args, **kwargs):
    # Ordena la lista de caminos segun la heuristica y el coste
    new_list = old_paths + new_paths

    def f(path):  # Me defino esta función porque key solo puede recibir funciones o None.
        if path is None :
            return 0
        #print("c: ",c(path),"h: ",h(path[-1]))
        return c(path) + h(path[-1])

    new_list.sort(key=f, reverse=False)
    new_list = prune(new_list)
#    new_list.sort(key=f, reverse=False)
    return new_list


def search(dataset, initial_state, expansion, cost, heuristic, ordering, solution):
    # Realiza una búsqueda en el espacio de estados
    paths = [[initial_state(dataset)]]  # Crea la lista de caminos, inicialmente el estado inicial
    sol = None  # Este es el estado solucion

    # 1 - Mientras haya caminos y no se haya encontrado solución
    new_paths = []
    while paths :
        # 2 - Extraer el primer camino
        # print("Numero de paths:",len(paths))

        path = paths.pop(0)
        # 3 - Comprobar si estamos ante un estado solución
        # 4.1 - Si no es solución, expandir el camino
        # 4.2 - Si es solucion, detenemos y vamos al paso END.
        # print("is_solution",path[-1])
        if (not solution(path[-1])):
            # expansion
            states = expansion(path[-1])
            # Comprobamos si es solución alguno de los nuevos estados expandidos
            for state in states:
                if solution(state):
                    sol = state
                    break

        else:
            sol = path[-1]
            break
    # 5 - Para cada estado expandido nuevo, añadirlo al camino lo que genera una lista de nuevos caminos

        arr = np.array(path)
        for state in states :
            new_path = arr.tolist()
            new_path.append(state)
            new_paths.append(tuple(new_path))
    # 6 - Ordenar los nuevos caminos y viejos caminos, y realizar poda. Volver al paso 1.
        paths = ordering(paths,new_paths,cost,heuristic)
    # END - Devolver el camino si es solución, si no devolver None

    if sol:
        return sol  # Devuelve solo la solucion, no el camino solucion
    else:
        return None


def measure_sol_search(solution):
    # cost = None
    # Mide el coste de la solucion que haya encontrado el algoritmo search
    # return solution['current'] + 1
    return len(np.unique(solution['colors'])),solution['colors']
