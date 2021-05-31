
from pymoo.model.problem import Problem
import numpy as np
    

#reference for input define using np.random
#rng.random --uniform distribution [0,1)
#rng.uniform(a,b) --uniform distribution [a,b, size]
#rng.gauss(mu, sigma)
#rng = np.random.default_rng(seed=22)
#x = 40*rng.random((10000,1))-20 #[-20,20]
#y = 40*rng.random((10000,1))-20 #[-20,20]
#X = np.concatenate([x,y],axis=1)

####################################################
def aval_problems():
    p_list = ['binh_and_korn_Problem', 'changkong_and_haimes_problem', 'test_problem','constr_ex_problem' ]
        
    print('The multiple obejective problems:')
    print('-'*40)
    for i in p_list:
        print('\n')
        print(i)
    print('\n-----------------------\n')
    print('Call problem by name')
    


    print('\n\n*****\n')
    print('split_X(given_design_space,given_problem):\n')
    
    print('feasible_X,infeasible_X, feasible_F,infeasible_F,feasible_G,infeasible_G')

    return 'Updating more problems'
aval_problems()
####################################################
#################problem_1#######################################
class binh_and_korn_Problem(Problem):

#clarify the problem
    def __init__(self):
        super().__init__(n_var=2,
                        n_obj=2,
                        n_constr=2,
                        xl=np.array([0,0]), 
                        xu=np.array([5,3]))
                        #elementwise_evaluation=True)

#var_1 = X[:,0] ; var_2 = X[:,1], var_3 = X[:2]
#objetive and constraint formula
#Note: for constraint formula, convert them <= 0
###    for objective formula, convert them into minimize
    def _evaluate(self, X, out, *args, **kwargs):
        f1 = 4*(X[:,0])**2 +4*(X[:,1])**2
        f2 = (X[:,0]-5)**2 + (X[:,1]-5)**2


    #constraints need to be formulated as g(xi)<=0
        g1 =  (X[:,0]-5)**2 + (X[:,1])**2 - 25 
        g2 =  -((X[:,0]-8)**2  + (X[:,1]-3)**2 - 7.7)

        out["F"] = np.column_stack([f1, f2]) 
        out["G"] = np.column_stack([g1, g2]) 
    



#################################################################
#################problem_2#######################################
class changkong_and_haimes_problem(Problem):

#clarify the problem
    def __init__(self):
        super().__init__(n_var=2,
                        n_obj=2,
                        n_constr=2,
                        xl=np.array([-20,-20]), 
                        xu=np.array([20,20]))
                        #elementwise_evaluation=True)

#var_1 = X[:,0] ; var_2 = X[:,1], var_3 = X[:2]
#objetive and constraint formula
#Note: for constraint formula, convert them <= 0
###    for objective formula, convert them into minimize
    def _evaluate(self, X, out, *args, **kwargs):
        f1 = 2 + (X[:,0]-2)**2 + (X[:,1]-1)**2
        f2 = 9*X[:,0] - (X[:,1]-1)**2


    #constraints need to be formulated as g(xi)<=0
        g1 =  X[:,0]**2 + X[:,1]**2 -225
        g2 =  X[:,0] - 3*X[:,1] + 10

        out["F"] = np.column_stack([f1, f2]) 
        out["G"] = np.column_stack([g1, g2]) 
    


#################################################################
#################problem_3#######################################
class test_problem(Problem):

#clarify the problem
    def __init__(self):
        super().__init__(n_var=2,
                        n_obj=2,
                        n_constr=3,
                        xl=np.array([-7,-7]), 
                        xu=np.array([4,4]))
                        #elementwise_evaluation=True)

#var_1 = X[:,0] ; var_2 = X[:,1], var_3 = X[:2]
#objetive and constraint formula
#Note: for constraint formula, convert them <= 0
###    for objective formula, convert them into minimize
    def _evaluate(self, X, out, *args, **kwargs):
        f1 = X[:,0]**2 - X[:,1]
        f2 = -0.5*X[:,0] - X[:,1] -1


    #constraints need to be formulated as g(xi)<=0
        g1 =  -(6.5 - X[:,0]/6 - X[:,1])
        g2 =  -(7.5 - 0.5*X[:,0] - X[:,1])
        g3 = -(30 - 5*X[:,0] - X[:,1])

        out["F"] = np.column_stack([f1, f2]) 
        out["G"] = np.column_stack([g1, g2, g3]) 
    




####################################################
#################problem_4##########################

class constr_ex_problem(Problem):
#clarify the problem
    def __init__(self):
        super().__init__(n_var=2,
                        n_obj=2,
                        n_constr=2,
                        xl=np.array([0.1,1]), 
                        xu=np.array([1,5]))
                        #elementwise_evaluation=True)

#var_1 = X[:,0] ; var_2 = X[:,1], var_3 = X[:2]
#objetive and constraint formula
#Note: for constraint formula, convert them <= 0
###    for objective formula, convert them into minimize
    def _evaluate(self, X, out, *args, **kwargs):
        f1 = X[:,0]
        f2 = (1+X[:,1])/X[:,0]


    #constraints need to be formulated as g(xi)<=0
        g1 =  -(X[:,1] + 9*X[:,0] -6)
        g2 =  -(-X[:,1] + 9*X[:,0] -1)


        out["F"] = np.column_stack([f1, f2]) 
        out["G"] = np.column_stack([g1, g2]) 



# filter input
#problem = problem_1()

#rng = np.random.default_rng(seed=42)
#x = 5*rng.random((10000,1)) #[0,5]
#y = 3*rng.random((10000,1)) #[0,3]

#X = np.concatenate([x,y],axis=1)
##############################################################################
##############################################################################

def split_X(X,problem):
    result = problem.evaluate(X, return_as_dictionary=True)
    #filter infeasible and feasible index
    infeasible_index = np.where(result['CV'] > 0)[0]
    feasible_index = [i for i in range(X.shape[0]) if i not in infeasible_index ]
    #get feasible and infeasible input
    feasible_X = X[feasible_index]         
    #result include three types of oupt 
    # result['F'] == objective values
    # result['CV'], if CV ==0, feasible; otherwise, infeasible 
    # result['G'] == constraint value
    infeasible_X = X[infeasible_index]
    feasible_F = result['F'][feasible_index]
    infeasible_F = result['F'][infeasible_index]
    feasible_G = result['G'][feasible_index]
    infeasible_G = result['G'][infeasible_index]

    print('{} data points and {} n_vars in Receive X:'.format(X.shape[0], X.shape[1]))
    print('\n{}--feasible\n{}--infesiable'.format(len(feasible_index), len(infeasible_index)))


    print('\n*****\n')
    print('plot_problem(X, problem)')
    return feasible_X,infeasible_X, feasible_F,infeasible_F,feasible_G,infeasible_G

from matplotlib import pyplot as plt
def plot_problem(X, problem):
    feasible_X,infeasible_X, feasible_F,infeasible_F,feasible_G,infeasible_G= split_X(X, problem=problem)
    figure, ax = plt.subplots(1,2)
    #figure for feasible input
    ax[0].scatter(feasible_F[:,0],feasible_F[:,1], alpha=0.3, color = 'blue', edgecolor= 'black') #alpha change color tranparent
    ax[0].set_xlabel("min $f(1)$")
    ax[0].set_ylabel("min $f(2)$")
    ax[0].set_title('{} feasible input out of {}'.format(feasible_F.shape[0], feasible_F.shape[0]+infeasible_F.shape[0]))
    #figure for infeasible input
    ax[1].scatter(infeasible_F[:,0], infeasible_F[:,1],alpha=0.3, color = 'blue', edgecolor= 'black')
    ax[1].set_xlabel("min $f(1)$")
    ax[1].set_ylabel("min $f(2)$")
    ax[1].set_title('{} infeasible input out of {}'.format(feasible_F.shape[0],feasible_F.shape[0]+infeasible_F.shape[0]))
    plt.tight_layout()
    plt.show()




#define input here

########################################################################################################
###########################################################################################

##############################################################################
#################################################################






