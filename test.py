from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination
from pymoo.optimize import minimize
from pymoo.util.termination.default import MultiObjectiveDefaultTermination
from pymoo.factory import get_performance_indicator
import numpy as np
import time
import sys
import os 
import argparse
from problems.Define_Problems import *

parser = argparse.ArgumentParser(description='''parameters description''')
parser.add_argument('-p','--problem', type=str, required=True,choices=['bnh','carside',
                            'clutch','kursawe','weldebeam',
                            'truss2d', 'tnk', 'osy', 'chankong','test', 
                            'ctp1', 'pro1','zdt1','zdt2','zdt3','zdt3',
                            'zdt4','zdt5','zdt6', 'kur1'],help="This is specific problem")
parser.add_argument('-a', '--algorithm', type = str)
parser.add_argument('-ob','--objectives', type=int,help="This is number of objetives")                            
parser.add_argument('-gen', '--generation', type=int,help='# of generation NSGAII')
parser.add_argument('-lb', '--lb',type=float, nargs= '+', help='Integer or np.ndarray of length n_var representing the lower bounds of the design variables.')
parser.add_argument('-ub', '--ub',type=float,nargs= '+', help ='Integer or np.ndarray of length n_var representing the upper bounds of the design variables.')
parser.add_argument('-n', '-nvar', type = int, help= 'Number of variables')
args = parser.parse_args()


if __name__ == "__main__":
    p = input_problem(args.problem)
    



