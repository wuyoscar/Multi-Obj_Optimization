from pymoo.model.problem import Problem
import numpy as np
import autograd.numpy as anp



class PRO1(Problem):
    def __init__(self):
        self.xl = np.array([0,0,0])
        self.xu = np.array([4,4,4])

        super().__init__(n_var=3,
                        n_constr=3,
                        n_obj=3
                        )

    def _evaluate(self, X,out, *args, **kwargs):
        f1 = X[:,0]**3 + X[:,1] + X[:,2] 
        f2 =  (X[:,0]**2 - X[:,1])/4 + 5*X[:,2]
        f3 =  9 + (X[:,0]+X[:,1])**2 + (X[:,1]-X[:,2])**2


        g1 = X[:,0] - 3 + X[:,1]**2 +  X[:,2]
        g2 =1/5*( X[:,1]**2 + X[:,2] -X[:,0]**4-5)
        g3 =  -X[:,2]**3 -(X[:,1]**2)/2

        out["F"] = np.column_stack([f1, f2,f3]) 
        out["G"] = np.column_stack([g1, g2, g3]) 