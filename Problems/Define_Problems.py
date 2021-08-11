from pymoo.model.problem import Problem
import numpy as np


def lsp(objective_function):
    num_weight = len(objective_function)
    w = np.random.rand(num_weight)
    w=w/w.sum()
    fp = np.array(objective_function)
    lsp = np.dot(w, fp)
    print('weight is: ',w)
    return lsp



class p1(Problem):
#clarify the problem
    def __init__(self):
        super().__init__(n_var=2,
                        n_obj=2,
                        n_constr=2
                    #  xl=np.array([0,0]),  
                    # xu=np.array([5,3])
                        )

    def _evaluate(self, X, out,*args, **kwargs):  #return_values_of = ['F','G']
        f1 = 4*(X[:,0])**2 +4*(X[:,1])**2
        f2 = (X[:,0]-5)**2 + (X[:,1]-5)**2

        g1 =  (X[:,0]-5)**2 + (X[:,1])**2 - 25 
        g2 =  -((X[:,0]-8)**2  + (X[:,1]-3)**2 - 7.7)

        out["F"] = np.column_stack([f1, f2]) 
        out["G"] = np.column_stack([g1, g2])
        



#################################################################
#################problem_2#######################################
class p2(Problem):

#clarify the problem
    def __init__(self):
        super().__init__(n_var=2,
                        n_obj=2,
                        n_constr=2
                    # xl=np.array([-20,-20]), 
                    # xu=np.array([20,20])
                    )
                        #elementwise_evaluation=True)

#var_1 = X[:,0] ; var_2 = X[:,1], var_3 = X[:2]
#objetive and constraint formula
#Note: for constraint formula, convert them <= 0
###    for objective formula, convert them into minimize
    def _evaluate(self, X, *args, **kwargs):
        f1 = 2 + (X[:,0]-2)**2 + (X[:,1]-1)**2
        f2 = 9*X[:,0] - (X[:,1]-1)**2


    #constraints need to be formulated as g(xi)<=0
        g1 =  X[:,0]**2 + X[:,1]**2 -225
        g2 =  X[:,0] - 3*X[:,1] + 10

        out["F"] = np.column_stack([f1, f2]) 
        out["G"] = np.column_stack([g1, g2]) 



#################################################################
#################problem_3#######################################
class p3(Problem):

#clarify the problem
    def __init__(self):
        super().__init__(n_var=2,
                        n_obj=2,
                        n_constr=3,
        )
    def _evaluate(self, X, out,*args, **kwargs):
        f1 = X[:,0]**2 - X[:,1]
        f2 = -0.5*X[:,0] - X[:,1] -1


    #constraints need to be formulated as g(xi)<=0
        g1 =  -(6.5 - X[:,0]/6 - X[:,1])
        g2 =  -(7.5 - 0.5*X[:,0] - X[:,1])
        g3 = -(30 - 5*X[:,0] - X[:,1])

        out["F"] = np.column_stack([f1, f2]) 
        out["G"] = np.column_stack([g1, g2, g3]) 

#################################################################
#################Osyczka and kundu fucntion###########

class p4(Problem):
    def __init__(Problem):
        super().__init__(n_var=2,
                        n_constr=2
        )
    
    def _evaluate(self, X, out, *args, **kwargs):
        f1= X[:,0]
        f2 = (1+X[:,1])*np.exp(-X[:,0]/(1+X[:,1]))

        g1 = -f2/0.858*np.exp(-0.54*f1)-1
        g2 = -f2/0.72*np.exp(-0.29*f1)-1


        out["F"] = np.column_stack([f1, f2]) 
        out["G"] = np.column_stack([g1, g2])
#################################################################
#################problem_1###########
class p5(Problem):
    def __init__(self):
        super().__init__(n_var=3,
                        n_constr=3
                        )

    def _evaluate(self, X,out, *args, **kwargs):
        f1 = X[:,0]**3 + X[:,1] + X[:,2] 
        f2 =  (X[:,0]**2 - X[:,1])/4 + 5*X[:,2]
        f3 =  9 + (X[:,0]+X[:,1])**2 + (X[:,1]-X[:,2])**2


        g1 = X[:,0] - 3 + X[:,1]**2 +  X[:,2]
        g2 = X[:,1]**2 + X[:,2] -X[:,0]**4-5-5
        g3 =  -X[:,2]**3 -(X[:,1]**2)/2

        out["F"] = np.column_stack([f1, f2,f3]) 
        out["G"] = np.column_stack([g1, g2, g3]) 



#################################################################
#################problem_2###########
class p5(Problem):
    def __init__(self):
        super().__init__(n_var=2,
                        n_constr=3
                        )

    def _evaluate(self, X, out,*args,  **kwargs):
        f1 = (X[:,0]-2**2) + (X[:,1]-1)**2 + 2 
        f2 =  9*X[:,0] - (X[:,1]-1)**2
        
        g1 = (X[:,0])**2 +(X[:,1])**2 -225
        g2 = X[:,0] - 3*X[:,1] +10

        out["F"] = np.column_stack([f1, f2]) 
        out["G"] = np.column_stack([g1, g2]) 



