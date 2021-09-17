from src.Utilities import bcolors, random
from src.TSPlibReader import TSPlibReader

class TSP():
    """
    Clase que lee una instancia, evalua soluciones del TSP y provee metodos para crear soluciones

    Attributes
    ----------
    nodes : int
        Numero de Nodos
    distances : list[list]
        Matriz con la distacia
    neighbours : int
        Matriz con vecinos mas cercanos
    tsplib_instance : TSPlibReader
        Instancia TSP
    options : AlgorithmsOptions
        Opciones
    

    Methods
    -------
    __init__(args, opciones)
        Clase constructora, lee todas las opciones que pueda tener el problema
   
    """

    # Numero de Nodos
    nodes = 0

    # Matriz con las distacias
    distances = [[]]

    # Matriz con vecinos mas cercanos 
    neighbours = [[]]

    # Instancia TSPlibReader
    instance :TSPlibReader


    def __init__(self, filename: str) -> None:

        # leer instancia desde un archivo TSPlib
        self.instance = TSPlibReader(filename)

        # obtener matriz de distancia
        self.distances = self.instance.distance

        # obtener vecinos mas cercanos
        self.neighbours = self.instance.nn_list
        
        # obtener tamano de la instancia 
        self.nodes = self.instance.n
        #print(self.compute_tour_length([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11, 13, 0]))
        #self.print_solution_and_cost([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11, 13, 0])

        #self.print_distances()


    def getSize(self) -> int:
        """ Obtener numero de nodos"""
        return self.nodes

    def print_distances(self) -> None:
        """ Imprimir matriz de distancia entre nodos """
        print(f"{bcolors.BOLD}Distancia entre Nodos: {bcolors.ENDC}")
        for fila in self.distances:
            for valor in fila:
                print(f"{bcolors.OKCYAN}{valor} {bcolors.ENDC}",end=" ")
            if fila: print()      

    def get_distance(self, i: int, j: int) -> int:
        """ Obtener distancia entre los nodos por su indice i y j"""
        return self.distances[i][j]

    def compute_tour_length(self, tour: list) -> int:
        """ Computar y retornar el costo de un tour """
        tour_length = 0
        for i in range(self.nodes):
            tour_length += self.distances[tour[i]][tour[i + 1]]
        return tour_length

    def tsp_check_tour(self, tour: list) -> bool:
        """ Revisa la correctitud de una solucion del TSP """
        
        error = False
        used = [0] * self.nodes

        # Si no se recibio el tour 
        if (not tour):
            print(f"{bcolors.FAIL}Error: permutacion no esta inicializada! {bcolors.ENDC}")
            exit()

        for i in range(self.nodes):
            if used[tour[i]] != 0:
                print(f"{bcolors.FAIL}Error: la solucion tiene dos veces el valor {tour[i]} (ultima posicion: {i}) {bcolors.ENDC}")
                error = True
            else:
                used[tour[i]] = 1

        if (not error):
            for i in range(self.nodes):
                if (used[i] == 0):
                    print(f"{bcolors.FAIL}Error: posicion {i} en la solucion no esta ocupada{bcolors.ENDC}")
                    error = True
        if (not error):
            if (tour[0] != tour[self.nodes]):
                print(f"{bcolors.FAIL}Error: la permutacion no es un tour cerrado.{bcolors.ENDC}")
                error = True;
            
        if (not error):
            return True

        print(f"{bcolors.FAIL}Error: vector solucion:{bcolors.ENDC} ", end='')
        for elem in tour:
            print(f"{bcolors.FAIL}{elem}{bcolors.ENDC}", end=" ")
        print()
        return False
        
    def print_solution_and_cost(self, tour: list) -> None:
        """ Muestra la solucion y costo """

        print(f"{bcolors.BOLD}Solucion: {bcolors.ENDC}", end='')
        for elem in tour:
            print(f"{bcolors.OKCYAN}{elem}{bcolors.ENDC}", end=' ')
        print(f"{bcolors.BOLD}\nCosto: {bcolors.ENDC}{bcolors.OKCYAN}{self.compute_tour_length(tour)}{bcolors.ENDC}")

    def random_tour(self) -> list:
        """ Generar una solucion aleatoria """

        # crear lista con tour a reordenar
        tour = list(range(self.nodes))
        # reordenar aleatoriamente el tour
        random.shuffle(tour)
        # asignar que el ultimo nodo sea igual al primero
        tour.append(tour[0])

        return tour
    
    def greedy_nearest_n(self, start: int) -> list:
        """ Generar una solucion del tsp usando la heuristica del nodo mas cercano comenzando del nodo start """

        tour = [0] * self.nodes
        selected = [False] * self.nodes

        # Si el nodo inicial es menor que 0
        if (start < 0):
            start = random.randint(0, self.nodes-1)
        tour[0] = start
        selected[start] = True

        # Ciclo para los nodos del tour
        for i in range(1,self.nodes):            
            for j in range(self.nodes):
                if (not selected[self.neighbours[tour[i-1]][j]]):
                    tour[i] = self.neighbours[tour[i-1]][j]
                    selected[self.neighbours[tour[i-1]][j]] = True
                    break
        tour.append(tour[0])
        return tour
    
    def deterministic_tour(self) -> list:
        """ Generar una solucion deterministica """

        # Crear lista deterministica (rango secuencial 0 al numero de nodos)
        tour = list(range(self.nodes))
        # Retornar al inicio
        tour.append(tour[0])

        return tour
