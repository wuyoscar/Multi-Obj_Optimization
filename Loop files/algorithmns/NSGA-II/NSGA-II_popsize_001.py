from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination
from pymoo.factory import get_problem
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
from pymoo.util.termination.default import MultiObjectiveDefaultTermination
import numpy as np
import time
import sys
import os 

#for path in sys.path:
#    print(path)






problem_list = ['BNH', 'OSY', 'TNK', 'Truss2D', 'Welded_Beam', 'zdt1','ZDT2','ZDT3','ZDT4','ZDT5','ZDT6']

select_problem_list = ['BNH', 'OSY']

problem_dict = {}

pop_list = [10,50]
for pop in pop_list:

    for problem in select_problem_list:
        print('\n\n')
        print('-'*60)
        print('-'*60)

        p = get_problem(problem)
        print('problem is:\n',p)

        termination = MultiObjectiveDefaultTermination(
        x_tol=1e-8,
        cv_tol=1e-6,
        f_tol=0.0025,
        nth_gen=5,
        n_last=30,
        n_max_gen=1000,
        n_max_evals=100000
        )

        #algorithm parameters
        algorithm = NSGA2(
        pop_size= pop, #! parameters
        n_offspring = 20,
        crossover=get_crossover("real_sbx", prob=0.9, eta=15),
        mutation=get_mutation("real_pm", eta=20),
        eliminate_duplicates=True,
        termination = termination 
    )

        start = time.time()
        res = minimize(p,
                algorithm,
                termination,
                seed=1,
                save_history=True,
                verbose=False,

                )
        print('Time elapsed for solving problem: ', time.time() - start, ' seconds\n')
        problem_dict[problem] = {'Solution':np.array(res.X), 'Obj_value':np.array(res.F), 'CV':np.array(res.CV)}

        print("Best solution found: {}".format(res.X.shape)) #pareto solution set 
        print("Function value: {}".format(res.F.shape)) #object function value 
        print("Constraint violation: {}".format(res.CV.shape)) 




        t = 1000 * time.time() # current time in milliseconds

        np.random.seed(int(t) % 2**32)
        #call function generate X
        lb = -np.random.randint(20)
        lp = np.random.randint(20)
        bound = np.random.uniform(lb,lp,2)
        datasize = pop
        print(datasize)


        #np.savetxt(path + '/X_' + problem + '_popsize_' + str(pop) , X)
        #file_name = path+problem+'_'+ str(pop)
        #np.savetxt(file_name + 'received_X', X)
        
path = os.path.join(os.getcwd(),'Result', 'NSGA-II'
print(path + '/X_' + problem + '_popsize_' + str(pop))
problem
pop

#import os
#print(os.getcwd())

#path = '/Users/wuyoscar/Documents/Project/MOOP/Result/'


#received_X_file = path+'NSGA-ch_problem_X.txt'
#input_infeas_file=path+'NSGA-ch_problem_infeasible_X.txt'
#input_feas_file=path+'NSGA-ch_problem_feasible_X.txt'

#optimal_solution_set = path + 'NSGA-ch_problem_ps_X.txt'


#np.savetxt(received_X_file, X)
#np.savetxt(input_infeas_file, infeasible_X_old)
#np.savetxt(optimal_solution_set, res.X)

#print(problem_dict)




