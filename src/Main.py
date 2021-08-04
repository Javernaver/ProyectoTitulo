from src.Tour import Tour
from src.AlgorithmsOptions import AlgorithmsOptions, MHType, TSPMove
from src.TSP import TSP
from src.SimulatedAnnealing.SimulatedAnnealing import SimulatedAnnealing
import sys


class Main():
    """
    Clase principal que implementa algoritmos metaheristicos para resolver el problema del vendedor viajero (TSP)

    Methods
    -------
    __init__(argv=sys.argv)
        Clase principal que recibe los argumentos que puedan haber sido incluidos al ejecutar el script en la consola
    """
    def __init__(self, argv=sys.argv) -> None:
        """
        Clase principal que recibe los argumentos que puedan haber sido incluidos al ejecutar el script en la consola

        Parameters
        ----------
        argv : list of str, optional
            Lista con los argumentos que pueda tener al inicializar la clase

        """
        
        # leer e inicializar las opciones 
        options = AlgorithmsOptions(argv)

        # leer e interpretar el problema TSP leido desde la instancia definida
        problem = TSP(options)
        #print(problema.random_tour())

        initial_solution = Tour(initial_sol=options.initial_solution, problem=problem)
        #print(solucion_inicial.actual, solucion_inicial.costo)
        #solucion_inicial.randomNeighbor(TSPMove.TWO_OPT)
        #print(solucion_inicial.actual, solucion_inicial.costo)

        # Ejecutar Metaheuristica
        if (options.metaheuristic == MHType.SA):
            # Crear solver
            solver = SimulatedAnnealing(problem, options)
            