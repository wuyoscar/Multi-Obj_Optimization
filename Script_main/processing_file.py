from problems import binh_and_korn, test, constr_ex, changkong_and_haimes, filter_input
import numpy as np
import time

#call problems from problems files 
ch_problem = changkong_and_haimes()
#inspect problem
print(ch_problem)

#call NSGAII from packages
#! lack of tuning algorithms parameters code here:
from pymoo.algorithms.nsga2 import NSGA2
from pymoo.util.termination.f_tol import MultiObjectiveSpaceToleranceTermination
from pymoo.optimize import minimize

algorithm = NSGA2()
#define termination criterion
#recommend supplying a maximum number of generations n_max_gen or function evaluations n_max_evals
termination = MultiObjectiveSpaceToleranceTermination(#tol=0.0025,
                                                #n_last=30,
                                                #nth_gen=5,
                                                n_max_gen=10000,
                                                n_max_evals=100000)
#process algorithm
start = time.time()
res = minimize(problem = ch_problem, # define ch_problem, here bk_ch_problem
        algorithm = algorithm, # pass algorithm, here NSGA-II
        termination= termination, #define algorithmn terminations
        seed=1, #random seed
        verbose = False # define whether ouput should print out 
)
print('\nTime elapsed for solving ch_problem: ', time.time() - start, ' seconds\n')
print("Generations", res.algorithm.n_gen)
print("Design space", res.X.shape)
print("Object values space", res.F.shape)
print('Constraint values', res.G.shape)
print("Aggregated constraint violation", res.CV.shape) #base on this value, we can filtering feasible and infeasible
print('Final population object',res.pop.shape)
