from pymoo.core.problem import Problem
import numpy as np 
class Kur1(Problem):
    def __init__(self,n_var= None,**kwargs):
        super().__init__(n_obj=2, n_var=n_var, xl=-5.05, xu = 5,type_var= np.double, n_constr=0,**kwargs)

        
    def _evaluate(self,x, out, *args, **kwargs):
        #for i in range self.var-1
        power = np.column_stack([(-0.2)*np.sqrt(np.power(x[:,i],2)+np.power(x[:,i+1],2)) for i in range(self.n_var-1)])
        f1 = np.sum(-10*np.exp(power),axis=1)
        f2 = np.sum(np.power(abs(x),0.8) +5*np.sin(np.power(x,3)),axis=1)
        #exporting objective value     
        out['F'] = np.column_stack([f1,f2])