
from problems import *
from algorithms import *
import numpy as np





#give random input

rng = np.random.default_rng(seed=22)

x = 40*rng.random((10000,1))-20 #[-20,20]
y = 40*rng.random((10000,1))-20 #[-20,20]

X = np.concatenate([x,y],axis=1)


#evaluation
#feasible_X_old, infeasible_X_old, feasible_F_old,infeasible_F_old,feasible_G_old,infeasible_G_old = split_X(X= X, problem= )

#visual_problems(feasible_F_old,infeasible_F_old)

#feasible_X, infeasible_X, feasible_F,infeasible_F,feasible_G,infeasible_G = filter_input(X=X, problem=ch_problem)
#visual_problems(feasible_F,infeasible_F)


#apply algorithm

from algorithms import nsga2, generation_history
res= nsga2(ch_problem)

feasible_X,infeasible_X, feasible_F,infeasible_F,feasible_G,infeasible_G = filter_input(X=res.X,problem= ch_problem)


n_evals, F, cv =  generation_history(res)


#compare algrotihmns

#visual_algorithms(feasible_F, feasible_F_old, infeasible_F_old,'NSGA-II')










########
##############output

#import os
#print(os.getcwd())

#path = '/Users/wuyoscar/Documents/Project/MOOP/Result/'w =


#received_X_file = path+'NSGA-ch_problem_X.txt'
#input_infeas_file=path+'NSGA-ch_problem_infeasible_X.txt'
#input_feas_file=path+'NSGA-ch_problem_feasible_X.txt'

#optimal_solution_set = path + 'NSGA-ch_problem_ps_X.txt'


#np.savetxt(received_X_file, X)
#np.savetxt(input_infeas_file, infeasible_X_old)
#np.savetxt(optimal_solution_set, res.X)





n_evals = []    # corresponding number of function evaluations\
F = []          # the objective space values in each generation
cv = []         # constraint violation in each generation


# iterate over the deepcopies of algorithms
for algorithm in res.history:

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
