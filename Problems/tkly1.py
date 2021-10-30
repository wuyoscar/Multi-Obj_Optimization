from pymoo.core.problem import Problem
import numpy as np 
class TKLY1(Problem):
    def __init__(self,**kwargs):
        super().__init__(n_var=4,n_obj=2, n_constr=0,**kwargs)
    #define bound here
        self.xl= np.array([0,0,0,0])
        self.xu = np.array([1,1,1,1])

        
    def _evaluate(self,x, out, *args, **kwargs):
        
        f1 = x[:,0]+0.1
        f2 = np.prod(2-np.exp(-np.power((x[:,1:]-0.1)/0.004,2))-0.8*np.exp(-np.power((x[:,1:]-0.9)/0.4,2)),axis=1)/(x[:,0]+0.1)
        #exporting objective value     
        out['F'] = np.column_stack([f1,f2])