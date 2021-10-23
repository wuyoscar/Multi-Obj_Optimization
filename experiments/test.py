from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination,get_performance_indicator
from pymoo.optimize import minimize
from pymoo.util.termination.default import MultiObjectiveDefaultTermination
import numpy as np
import os, sys,argparse,time


currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from problems.Define_Problems import *



parser = argparse.ArgumentParser(description='''parameters description''')
parser.add_argument('-p','--problem', type=str, required=True,choices=['bnh','carside',
                            'clutch','kursawe','weldebeam',
                            'truss2d', 'tnk', 'osy', 'chankong', 
                            'ctp1', 'pro1','zdt1','zdt2','zdt3','zdt3',
                            'zdt4','zdt5','zdt6', 
                            'kur1', 'vu1', 'vu2', 'sk1','sk2','tkly1','ltdz1'],help="This is specific problem")
parser.add_argument('-a', '--algorithm', type = str)
parser.add_argument('-ob','--objectives', type=int,help="This is number of objetives")                            
parser.add_argument('-gen', '--generation', type=int,help='# of generation NSGAII')
parser.add_argument('-lb', '--lb', nargs= '+', help='Integer or np.ndarray of length n_var representing the lower bounds of the design variables.')
parser.add_argument('-ub', '--ub', nargs= '+', help ='Integer or np.ndarray of length n_var representing the upper bounds of the design variables.')
parser.add_argument('-n', '--var', type = int, help= 'Number of variables')
args = parser.parse_args()


if __name__ == "__main__":
    if args.var is None:
        p = input_problem(problem_name = args.problem)
    elif args.var and args.lb is not None:
        p = input_problem(problem_name = args.problem, n_var = args.var, xl= args.lb, xu = args.ub)
    elif args.var is not None:
        p = input_problem(problem_name = args.problem, n_var = args.var)
#python test.py -p vu1