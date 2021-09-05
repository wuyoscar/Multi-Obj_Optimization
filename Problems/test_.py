from pymoo.model.problem import Problem
import numpy as np
import autograd.numpy as anp


class Test(Problem):

#clarify the problem
    def __init__(self):

        super().__init__(n_var=2,
                        n_obj=2,
                        n_constr=3,type_var=np.double)
        self.xl = anp.array([-7,-7])
        self.xu = anp.array([4,4])

    def _evaluate(self, X, out,*args, **kwargs):
        f1 = X[:,0]**2 - X[:,1]
        f2 = -0.5*X[:,0] - X[:,1] -1
        g1 =  -(6.5 - X[:,0]/6 - X[:,1])
        g2 =  -(7.5 - 0.5*X[:,0] - X[:,1])
        g3 = -(30 - 5*X[:,0] - X[:,1])

        out["F"] = np.column_stack([f1, f2]) 
        out["G"] = np.column_stack([g1, g2, g3])