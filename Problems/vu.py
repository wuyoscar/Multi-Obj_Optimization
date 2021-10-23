from pymoo.core.problem import Problem
import numpy as np 
class Vu1(Problem):
    def __init__(self,  xl=None, xu = None,**kwargs):
        super().__init__(n_var = 2,n_obj=2, n_constr=0,**kwargs)
    #define bound here
        self.xl= np.array([-3,-3])
        self.xu = np.array([3,3])

        assert len(self.xl) == self.n_var
        assert len(self.xu) == self.n_var
        
    def _evaluate(self,x, out, *args, **kwargs):
        f1 = 1/(np.sum(np.power(x,2), axis=1)+1)
        f2 = np.sum(np.column_stack([np.power(x[:,0],2), 3*np.power(x[:,1],2)]), axis =1)+1
        #exporting objective value     
        out['F'] = np.column_stack([f1,f2])


class Vu2(Problem):
    def __init__(self,  xl=None, xu = None,**kwargs):
        super().__init__(n_var = 2,n_obj=2, n_constr=0,**kwargs)
    #define bound here
        self.xl= np.array([-3,-3])
        self.xu = np.array([3,3])

        assert len(self.xl) == self.n_var
        assert len(self.xu) == self.n_var
        
    def _evaluate(self,x, out, *args, **kwargs):
        
        f1 = np.sum(x, axis=1)+1
        f2 = np.sum(np.column_stack([np.power(x[:,0],2), 2*x[:,1]]), axis =1)-1
        #exporting objective value     
        out['F'] = np.column_stack([f1,f2])