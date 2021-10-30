from pymoo.core.problem import Problem
import numpy as np 
class SK1(Problem):
    def __init__(self,n_var=1,**kwargs):
        super().__init__(n_var=n_var,xl=-10, xu = 10,n_obj=2 ,type_var= np.double,n_constr=0,**kwargs)
    #define bound here
        
    def _evaluate(self,x, out, *args, **kwargs):
        
        f1 = -(-np.power(x,4)-3*np.power(x,3)+10*np.power(x,2)+10*x+10)
        f2 = -(-0.5*np.power(x,4)+2*np.power(x,3)+10*np.power(x,2)-10*x+5)
        #exporting objective value     
        out['F'] = np.column_stack([f1,f2])

class SK2(Problem):
    def __init__(self,n_var=4,**kwargs):
        super().__init__(n_var=n_var,xl=-10, xu = 10,n_obj=2, n_constr=0,**kwargs)

    def _evaluate(self,x, out, *args, **kwargs):
        f1 = -(-np.power(x[:,0]-2,2)-np.power(x[:,1]+3,2)-np.power(x[:,2]-5,2)-np.power(x[:,3]-4,2)+5)
        f2 = -(np.sum(np.sin(x),axis=1)/(np.sum(np.power(x,2),axis=1)*0.01+1))
        #exporting objective value     
        out['F'] = np.column_stack([f1,f2])

class SK2_typo(Problem):
    def __init__(self,n_var=4,**kwargs):
        super().__init__(n_var=n_var,xl=-10, xu = 10,n_obj=2, n_constr=0,**kwargs)
    #define bound here
        #assert len(self.xl) == self.n_var
        #assert len(self.xu) == self.n_var
        
    def _evaluate(self,x, out, *args, **kwargs):
        f1 = -(-np.power(x[:,0]-2,2)-np.power(x[:,1]-3,2)-np.power(x[:,2]-5,2)-np.power(x[:,3]-4,2)+5)
        f2 = -(np.sum(np.sin(x),axis=1)/(np.sum(np.power(x,2),axis=1)*0.01+1))
        #exporting objective value     
        out['F'] = np.column_stack([f1,f2])