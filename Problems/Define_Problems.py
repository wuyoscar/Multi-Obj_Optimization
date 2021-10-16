from pymoo.model.problem import Problem
import numpy as np
import autograd.numpy as anp
import os 
import sys

sys.path.append('/scratch/lk32/ow6835/MOOP/Problems')

from carside    import *
from ctp        import *
from kursawe    import *
from bnh        import *
from chankong   import *
from clutch     import *
from osy        import *
from test_      import *
from tnk        import *
from truss2d    import *
from weldebeam  import *
from zdt        import *


def lsp(objective_function):
    num_weight = len(objective_function)
    w = np.random.rand(num_weight)
    w=w/w.sum()
    fp = np.array(objective_function)
    lsp = np.dot(w, fp)
    print('weight is: ',w)
    return lsp




def split_X(X,problem_F,problem_CV):
    
    #filter infeasible and feasible index
    infeasible_index = np.where(problem_CV > 0)[0]
    feasible_index = [i for i in range(X.shape[0]) if i not in infeasible_index ]
    #get feasible and infeasible input
    feasible_X = X[feasible_index]         

    infeasible_X = X[infeasible_index]
    feasible_F = problem_F[feasible_index]
    infeasible_F = problem_F[infeasible_index]

    print('------problem evaluation-----')
    print('{} is feasible and {} is infeasible among {} data points'.format(len(feasible_index), len(infeasible_index), len(X)))

    return feasible_X,infeasible_X, feasible_F,infeasible_F



def input_problem(problem_name):

    problems_set_1 = ['bnh','carside','clutch','kursawe','weldebeam',"truss2d","tnk",'osy',  "chankong",'test','ctp1','pro1']
    if problem_name in problems_set_1:
        p_dict = {'bnh':BNH(), 
            'carside':Carside(), 
            'clutch':Clutch(), 
            'kursawe':Kursawe(), 
            'weldebeam':WeldedBeam(),
            "truss2d":Truss2D(),
            "tnk": TNK(), 
            'osy':OSY(),
            "chankong":Chankong(),
            'test':Test(),
            'ctp1':CTP1()
            }
        problem = p_dict[problem_name]
        print('\n\n***********')
        print('probelm is :')
        print(problem)
        return problem
    
    elif problem_name in ['zdt1','zdt2','zdt3','zdt4','zdt5','zdt6']:
        p_dict  = {'zdt1':ZDT1(n_var=n_var),
            'zdt2':ZDT2(n_var=n_var),
            'zdt3':ZDT3(n_var=n_var),
            'zdt4':ZDT4(n_var=n_var),
            'zdt5':ZDT5(),
            'zdt6':ZDT6(n_var=n_var) }
        problem = p_dict[problem_name]
        print('\n\n***********')
        print('probelm is :')
        print(problem)
        return problem
    
    else:
        print('Plz select correct problem')

def generate_data(p = None,size = None):
    data_point = []
    for i in np.column_stack([p.xl,p.xu]):
        data_point.append(np.random.uniform(low=i[0],high=i[1], size=500))
    data_point = np.array(data_point)
    data_point = data_point.T
    return data_point
