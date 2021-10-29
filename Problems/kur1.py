from pymoo.core.problem import Problem
import numpy as np 
class Kur1(Problem):
    def __init__(self, n_var=None, xl=None, xu = None,**kwargs):
        super().__init__(n_obj=2, n_constr=0,**kwargs)
    #define bound here
        self.xl= np.ones(n_var)*xl
        self.xu = np.ones(n_var)*xu
        self.n_var = n_var

        assert self.xl is not None, "Provide Search Domain"
        assert len(self.xu) == self.n_var
        
    def _evaluate(self,x, out, *args, **kwargs):
        #from i=1 to n-1
        #here, i would like to use vectorization to save cost
        power = np.column_stack([(-0.2)*np.sqrt(np.power(x[:,i],2))+(np.power(x[:,i+1],2)) for i in range(self.n_var-1)])
        f1 = np.sum(-10*np.exp(power),axis=1)
        f2 = np.sum(np.power(abs(x),0.8) +5* np.power(np.sin(x),3),axis=1)
        #exporting objective value     
        out['F'] = np.column_stack([f1,f2])