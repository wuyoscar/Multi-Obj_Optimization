from pymoo.core.problem import Problem
import numpy as np 
class LTDZ1(Problem):
  # this is maximun problem 
    def __init__(self,**kwargs):
        super().__init__(n_var=3,n_obj=3, n_constr=0,**kwargs)
    #define bound here
        self.xl= np.array([0,0,0])
        self.xu = np.array([1,1,1])
        assert len(self.xl) == self.n_var
        assert len(self.xu) == self.n_var
        
    def _evaluate(self,x, out, *args, **kwargs):
        
        f1 = -(3-(1+x[:,2])*np.cos(x[:,0]*np.pi/2)*np.cos(x[:,1]*np.pi/2))
        f2 = -(3-(1+x[:,2])*np.cos(x[:,0]*np.pi/2)*np.sin(x[:,1]*np.pi/2))
        f3 = -(3-(1+x[:,2])*np.sin(x[:,0]*np.pi/2))
        #exporting objective value     
        out['F'] = np.column_stack([f1,f2,f3])