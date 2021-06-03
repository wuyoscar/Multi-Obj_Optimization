from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination
from pymoo.factory import get_problem
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
from pymoo.util.termination.default import MultiObjectiveDefaultTermination
import numpy as np
import time
import sys

#for path in sys.path:
#    print(path)

# this function for random generating X
def random_pick_X(n_var = None, bound = None, datasize=None):
    a = bound[0]
    b = bound[1]
    X = (b-a)*np.random.random((datasize, n_var)) +a
    return X

def split_X(X,problem_F,problem_CV, lb, lp):
    
    #filter infeasible and feasible index
    infeasible_index = np.where(problem_CV > 0)[0]
    feasible_index = [i for i in range(X.shape[0]) if i not in infeasible_index ]
    #get feasible and infeasible input
    feasible_X = X[feasible_index]         

    infeasible_X = X[infeasible_index]
    feasible_F = problem_F[feasible_index]
    infeasible_F = problem_F[infeasible_index]

    print('------problem evaluation-----')
    print('Give search domain {} ~ {}  with {} data points'.format(lb, lp, X.shape[0]))
    print('{} is feasible and {} is infeasiebl'.format(len(feasible_index), len(infeasible_index)))

    return feasible_X,infeasible_X, feasible_F,infeasible_F



problem_list = ['BNH', 'OSY', 'TNK', 'Truss2D', 'Welded_Beam', 'zdt1','ZDT2','ZDT3','ZDT4','ZDT5','ZDT6']

select_problem_list = ['BNH']

problem_dict = {}


#loop parameters population size
pop_list = [20,50,80,200,300,600,1000,1500,2000,3000,4000]

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
        n_max_gen=1000,
        n_max_evals=100000
        )

        #algorithm parameters
        algorithm = NSGA2(
        pop_size= pop,
        n_offspring = 20,
  #      crossover=get_crossover("real_sbx", prob=0.9, eta=15),
  #      mutation=get_mutation("real_pm", eta=20),
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
        datasize = np.random.randint(10000)
        print(datasize)

        X = random_pick_X(n_var = p.n_var, bound = bound, datasize=datasize)
        print('\n')
        problem_result = p.evaluate(X)

        feasible_X,infeasible_X, feasible_F,infeasible_F = split_X(X, problem_result[0], problem_result[1], lb , lp)          #problem_F = problem_result[0] #problem_CV = problem_result[1]








