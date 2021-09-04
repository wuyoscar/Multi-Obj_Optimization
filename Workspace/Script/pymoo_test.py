
from pymoo.factory import  get_crossover, get_mutation, get_sampling
from pymoo.algorithms.nsga2 import NSGA2
from pymoo.model.problem import Problem
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter

import numpy as np
import pandas as pd
from numpy import empty
import time


path='C:/Users/LearningPython/'

input_infeas_file=path+'thupymoo_input_infeasible.txt'
input_feas_file=path+'thupymoo_input_feasible.txt'
output_scalar_file=path+'thupymoo_output_scalar.txt'
output_vector_file=path+'thupymoo_output_vector.txt'

# define function to call later
def my_function(input_vector):
# this is where you implement your test functions
    f1=input_vector[0]+input_vector[1]
	f2=input_vector[0]-input_vector[1]
    return [f1, f2]


w = np.random.rand(2)
w=w/w.sum()

print("weighted-sum vector w=:",w)

# define a scalarization function of 18-objectives and
def scalar_function(w,obj_vector):
    scalar = np.dot(w,obj_vector)
    return scalar

class MyProblem(Problem):

    def __init__(self): #setting some init parameters, unsure what it does here
        super().__init__(n_var=2, #dimension
                         n_obj=1, #how many objectives
                         n_constr=0, # no otehr constraints
                         xl=np.array([1]*16), # domain boundaries
                         xu=np.array([4]*16),
                         type_var=np.int,  # are variables integer or reals (i Guess you need reals)
                         elementwise_evaluation=True) #???

    def _evaluate(self, x, out, *args, **kwargs):
        fsr = my_function(x)
        fs = scalar_function(w, fsr)  #scalarising function
        out["F"] = fs  #I think this is the output, see pyMOO manual how to do multiobjective problems
		
		# now we write inputs and outputs into respective files. The below part may be implemented better, without opening files all he time
        if sum(fsr[i] for i in range(n_var)) >= 0:
            with open(input_infeas_file, 'a') as f:  # infeasible point, outside feasible domain
                print(x, sep=' ', file=f)
        else:
            with open(input_feas_file, 'a') as f:  # ifeasible point
                print(x, sep=' ', file=f)
            with open(output_scalar_file, 'a') as f:
                print(fs, sep=' ', file=f)
            with open(output_vector_file, 'a') as f:
                print(fsr, sep=' ', file=f)



problem = MyProblem()
start = time.time()


ref_starting = np.random.randint(1,5,2)
# print starting point
print("starting point random:", ref_starting)

algorithm = NSGA2(x0=ref_starting,pop_size=100,sampling=get_sampling("int_random"),
                       crossover=get_crossover("int_sbx", prob=1.0, eta=3.0),
                       mutation=get_mutation("int_pm", eta=3.0),
                       eliminate_duplicates=True,)

res = minimize(problem,
               algorithm,
               ("n_iter", 15),
               verbose=True,
               seed=1)

print("Best solution found: %s" % res.X)
#print("Best solution found:\n")



#print("Best solution found: %s" % res.X.astype(np.int))
print("Function value: %s" % res.F)

print('\nTime elapsed for solving problem: ', time.time() - start, ' seconds\n')