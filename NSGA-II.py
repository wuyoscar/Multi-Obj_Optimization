from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination, get_problem
from pymoo.optimize import minimize
from pymoo.util.termination.default import MultiObjectiveDefaultTermination
from pymoo.factory import get_performance_indicator
import numpy as np
import time
import sys
import os 
import argparse



module_path = os.getcwd()+'/Problems/'
sys.path.append(module_path)
import Define_Problems 


parser = argparse.ArgumentParser(description='''problem, one set of bounds and dimensions, 
                            one set of output file names,one set of algorithm parameters''')
parser.add_argument('-p','--problem', type=str, choices=['p1','p2','p3','p4','p5'],help="This is specific problem")
parser.add_argument('-d','--dimension', type=int,help="This is dimension of input")
parser.add_argument('-lb','--lb', type=float, nargs= '+', help='lower bound')
parser.add_argument('-ub','--ub', type=float,nargs= '+', help ='upper bound')


args = parser.parse_args()


print(args)

def design_problem():
    return




def design_nsga_2():

    return 





