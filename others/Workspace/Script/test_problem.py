
#n_var: number of variables
#n_job: number of object
#x1: lower bounds
#xu: upper bounds

# F: function
# G: constrains

import numpy as np
from pymoo.model.problem import Problem

class MyProblem(Problem):

    def __init__(self):
        super().__init__(n_var=2, # two variables
                         n_obj=2, # two obejctive
                         n_constr=2, # two constrains
                         xl=np.array([-2,-2]), # bound
                         xu=np.array([2,2])) # bound

    def _evaluate(self, X, out, *args, **kwargs):
        f1 = X[:,0]**2 + X[:,1]**2 #objective formula
        f2 = (X[:,0]-1)**2 + X[:,1]**2 

        g1 = 2*(X[:, 0]-0.1) * (X[:, 0]-0.9) / 0.18 #constrain formulat
        g2 = - 20*(X[:, 0]-0.4) * (X[:, 0]-0.6) / 4.8

        out["F"] = np.column_stack([f1, f2])
        out["G"] = np.column_stack([g1, g2])


vectorized_problem = MyProblem()

'''





'''
from pymoo.factory import get_problem, get_reference_directions, get_visualization
from pymoo.util.plotting import plot

ref_dirs = get_reference_directions("das-dennis", 3, n_partitions=12)

pf = get_problem("dtlz1").pareto_front(ref_dirs)
get_visualization("scatter", angle=(45,45)).add(pf).show()



a = 2*2*2*2*4*3*2-1
print(a)
