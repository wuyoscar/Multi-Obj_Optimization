from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.algorithms.moo.rnsga2 import RNSGA2
from pymoo.algorithms.moo.moead import MOEAD, ParallelMOEAD
from pymoo.algorithms.moo.age import AGEMOEA
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.factory import get_problem, get_visualization, get_reference_directions

def NSGA2_f(pop_size = None):
    algorithm = NSGA2(
        pop_size= pop_size,
        eliminate_duplicates=True)
    return algorithm

def NSGA3_f(pop_size = None, m = None, n_partitions = None):
    ref_dirs = get_reference_directions("energy", m, n_partitions,seed=1)
    algorithm = NSGA3(pop_size=pop_size,
                ref_dirs=ref_dirs,
                eliminate_duplicates=True)
    return algorithm


def MOEAD_f(m = None, n_partitions = None):
    #m is number of objectives 
    ref_dirs = get_reference_directions("energy", m, n_partitions,seed=1)

    algorithm = MOEAD(
    ref_dirs = ref_dirs,
    n_neighbors=15,
    prob_neighbor_mating=0.7)
    return algorithm

def AGEMOEA_f(pop_size = None):
    algorithm = AGEMOEA(pop_size=100,
            eliminate_duplicates=True)
    return algorithm

def RNSGA2_f(pop_size = None, m = None, n_partitions = None):
    ref_dirs = get_reference_directions("energy", m, n_partitions,seed=1)
    algorithm = RNSGA2(
    ref_points=ref_dirs,
    pop_size=pop_size,
    epsilon=0.01,
    normalization='front',
    extreme_points_as_reference_points=False)

    return algorithm




def input_algorithm(algorithm_name, **kwargs):

    if algorithm_name=='nsga2':
        algorithm = NSGA2_f(pop_size= kwargs['pop_size'])
        return algorithm
    
    elif algorithm_name == 'nsga3':
        algorithm = NSGA3_f(pop_size= kwargs['pop_size'],m = kwargs['m'], n_partitions = kwargs['n_partitions'])
        return algorithm
    
    elif algorithm_name == 'agnomen':
        algorithm= AGEMOEA_f(pop_size= kwargs['pop_size'])
        return algorithm

    elif algorithm_name=='moead':
        algorithm = MOEAD_f(m = kwargs['m'], n_partitions = kwargs['n_partitions'])
        return algorithm
    elif algorithm_name=='rnsga2':

        algorithm = RNSGA2_f(pop_size= kwargs['pop_size'],m = kwargs['m'], n_partitions = kwargs['n_partitions'])


input_algorithm(algorithm_name='nsga3',pop_size=100, m =3, n_partitions = 12)

