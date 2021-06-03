from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination
from pymoo.factory import get_problem
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
import numpy as np
import time
import sys

#for path in sys.path:
#    print(path)
##add module path if necessary 
sys.path.append(r"/Users/wuyoscar/Documents/Project/MOOP/function_files/")
#
from problems import split_X

# this function for random generating X
def random_pick_X(n_var = None, bound = None, datasize=None):
    a = bound[0]
    b = bound[1]
    X = (b-a)*np.random.random((datasize, n_var)) +a
    return X

problem_list = ['BNH', 'OSY', 'TNK', 'Truss2D', 'Welded_Beam', 'zdt1','ZDT2','ZDT3','ZDT4','ZDT5','ZDT6']

select_problem_list = ['BNH', 'OSY','TNK', 'Truss2D', 'Welded_Beam']

problem_dict = {}


for problem in select_problem_list:
    print('\n\n')
    print('-'*60)
    print('-'*60)
    
    p = get_problem(problem)
    print('problem is:\n',p)
    
    #algorithm parameters
    algorithm = NSGA2(
    pop_size= 20,
    n_offspring = 10,
    crossover=get_crossover("real_sbx", prob=0.9, eta=15),
    mutation=get_mutation("real_pm", eta=20),
    eliminate_duplicates=True 
)


    termination = get_termination("n_gen", 300)
    start = time.time()
    res = minimize(p,
            algorithm,
            termination,
            seed=1,
            save_history=True,
            verbose=False
            )
    print('\nTime elapsed for solving problem: ', time.time() - start, ' seconds\n')
    problem_dict[problem] = {'Solution':np.array(res.X), 'Obj_value':np.array(res.F), 'CV':np.array(res.CV)}
    
    print("Best solution found: {}".format(res.X.shape)) #pareto solution set 
    print("Function value: {}".format(res.F.shape)) #object function value 
    print("Constraint violation: {}".format(res.CV.shape)) 


    t = 1000 * time.time() # current time in milliseconds
    np.random.seed(int(t) % 2**32)


    #call function generate X
    lb = -np.random.randint(30)
    lp = np.random.randint(30)
    bound = np.random.uniform(lb,lp,2)
    datasize = np.random.randint(1000)
    
    print(datasize)

    X = random_pick_X(n_var = p.n_var, bound = bound, datasize=datasize)

    print('\n')
    problem_result = p.evaluate(X)
    
    split_X(X, problem_result[0], problem_result[1], lb , lp)          #problem_F = problem_result[0] #problem_CV = problem_result[1]
#print(problem_dict)




