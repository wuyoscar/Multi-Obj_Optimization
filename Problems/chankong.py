from pymoo.model.problem import Problem
import numpy as np
import autograd.numpy as anp

class Chankong(Problem):

#clarify the problem
    def __init__(self):

        super().__init__(n_var=2, n_obj=2,n_constr=2,type_var=np.double)
        self.xl = anp.array([-20,-20])
        self.xu = anp.array([20,20])
    def _evaluate(self, X, out,*args, **kwargs):
        f1 = 2 + (X[:,0]-2)**2 + (X[:,1]-1)**2
        f2 = 9*X[:,0] - (X[:,1]-1)**2


    #constraints need to be formulated as g(xi)<=0
        g1 =  1/225*(X[:,0]**2 + X[:,1]**2 -225)
        g2 =  X[:,0] - 3*X[:,1] + 10

        out["F"] = np.column_stack([f1, f2]) 
        out["G"] = np.column_stack([g1, g2]) 