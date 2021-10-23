from pymoo.core.problem import Problem
import numpy as np 
class SK1(Problem):
    def __init__(self,  xl=None, xu = None,**kwargs):
        super().__init__(n_var=1,n_obj=2, n_constr=0,**kwargs)
    #define bound here
        self.xl= np.array(xl)
        self.xu = np.array(xu)

        #assert len(self.xl) == self.n_var
        #assert len(self.xu) == self.n_var
        
    def _evaluate(self,x, out, *args, **kwargs):
        
        f1 = -(-np.power(x,4)-3*np.power(x,3)+10*np.power(x,2)+10*x+10)
        f2 = -(-0.5*np.power(x,4)+2*np.power(x,3)+10*np.power(x,2)-10*x+5)
        #exporting objective value     
        out['F'] = np.column_stack([f1,f2])

class SK2(Problem):
    def __init__(self, xl=None, xu = None,**kwargs):
        super().__init__(n_var=4,n_obj=2, n_constr=0,**kwargs)
    #define bound here
        self.xl= np.array(xl)
        self.xu = np.array(xu)

        #assert len(self.xl) == self.n_var
        #assert len(self.xu) == self.n_var
        
    def _evaluate(self,x, out, *args, **kwargs):
        f1 = -(-np.power(x[:,0]-2,2)-np.power(x[:,1]+3,2)-np.power(x[:,2]-5,2)-np.power(x[:,3]-4,2)+5)
        f2 = -(np.sum(np.sin(x),axis=1)/(np.sum(np.power(x,2),axis=1)/100+1))
        #exporting objective value     
        out['F'] = np.column_stack([f1,f2])