from problems import binh_and_korn, test, constr_ex, changkong_and_haimes, filter_input
import numpy as np
import time
from pymoo.algorithms.nsga2 import NSGA2
from pymoo.util.termination.f_tol import MultiObjectiveSpaceToleranceTermination
from pymoo.optimize import minimize

#call NSGAII from packages
#! lack of tuning algorithms parameters code here:


#################################################
####################################################
def nsga2(problem):
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

    res = minimize(problem = problem, # define problem, here bk_problem
            algorithm = algorithm, # pass algorithm, here NSGA-II
            termination= termination, #define algorithmn terminations
            seed=1, #random seed
            verbose = True,
            save_history= True # define whether ouput should print out 
    )



    # what avaible methods can be called from result
    # get values by deleting shape
    print('\nTime elapsed for solving problem: ', time.time() - start, ' seconds\n')
    print("Generations", res.algorithm.n_gen)
    #  print('Number of functions evaluation',res.algorithm.n_eval)
    print("Design space", res.X.shape)
    print("Object values space", res.F.shape)
    print('Constraint values', res.G.shape)
    print("Aggregated constraint violation", res.CV.shape) #base on this value, we can filtering feasible and infeasible
    print('Final population object',res.pop.shape)
    return res


####################################################
####################################################    
def generation_history(res):
    # iterate over the deepcopies of algorithms
    for algorithm in res.history:
        n_evals = []    # corresponding number of function evaluations\
        F = []          # the objective space values in each generation
        cv = []         # constraint violation in each generation

        # store the number of function evaluations
        n_evals.append(algorithm.evaluator.n_eval)

        # retrieve the optimum from the algorithm
        opt = algorithm.opt

        # store the least contraint violation in this generation
        cv.append(opt.get("CV").min())

        # filter out only the feasible and append
        feas = np.where(opt.get("feasible"))[0]
        _F = opt.get("F")[feas]
        F.append(_F)   
    
    
    return n_evals, F, cv
























