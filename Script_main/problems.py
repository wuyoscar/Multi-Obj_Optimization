
from pymoo.model.problem import Problem
import numpy as np


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
    
def binh_and_korn():
    binh_and_korn = binh_and_korn_Problem()
    return binh_and_korn


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
    
def changkong_and_haimes():
    changkong_and_haimes = changkong_and_haimes_problem()
    return changkong_and_haimes

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
    
def test():
    test = test_problem()
    return test



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
    
def constr_ex():
    constr_ex = constr_ex_problem()
    return constr_ex


# filter input
#problem = problem_1()

#rng = np.random.default_rng(seed=42)
#x = 5*rng.random((10000,1)) #[0,5]
#y = 3*rng.random((10000,1)) #[0,3]

#X = np.concatenate([x,y],axis=1)
##############################################################################
##############################################################################
def filter_input(X,problem):
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

    return feasible_X,infeasible_X, feasible_F,infeasible_F,feasible_G,infeasible_G


#result_1 = bk_problem.evaluate(np.array([5,8]), return_as_dictionary= True)
#print(result)


#reference for input define using np.random
#rng.random --uniform distribution [0,1)
#rng.uniform(a,b) --uniform distribution [a,b, size]
#rng.gauss(mu, sigma)

#define input here

########################################################################################################
###########################################################################################
def visual_algorithms(feasible_f_new, feasible_f_old, infeasible_F_old, algorithmns_name = 'Algorithmn'):
    from matplotlib import pyplot as plt
    fig, ax = plt.subplots(nrows=2, ncols=2)
    ax = ax.flatten()
    #figure for feasible input
    ax[0].scatter(feasible_f_new[:,0],feasible_f_new[:,1], alpha=0.3, color = 'blue', edgecolor= 'black',label = 'pareto front') #alpha change color tranparent
    ax[0].set_xlabel("$minf(1)$")
    ax[0].set_ylabel("$minf(2)$")
    ax[0].set_title('{}-{}data points'.format(algorithmns_name, feasible_f_new.shape[0]))
    ax[0].legend()
    #figure for infeasible input
    ax[1].scatter(feasible_f_old[:,0], feasible_f_old[:,1], alpha=0.2, color = 'blue',edgecolor= 'black', label = 'feasible_obejct_space' )
    ax[1].scatter(infeasible_F_old[:,0], infeasible_F_old[:,1], alpha=0.2, color = 'orange',  label = 'infeasible_obejct_space')
    ax[1].set_xlabel("$minf(1)$")
    ax[1].set_ylabel("$minf(2)$")
    ax[1].set_title('Random Pick {} data points'.format(feasible_f_old.shape[0]+infeasible_F_old.shape[0]))
    ax[1].legend()

    ax[2].scatter(feasible_f_old[:,0], feasible_f_old[:,1],alpha=0.3, color = 'blue', edgecolor= 'black', label='feasible_obejct_space')
    ax[2].set_xlabel("$minf(1)$")
    ax[2].set_ylabel("$minf(2)$")
    ax[2].set_title('{} feasible input out of {}'.format(feasible_f_old.shape[0],feasible_f_old.shape[0]+infeasible_F_old.shape[0]))
    ax[2].legend()

    ax[3].scatter(infeasible_F_old[:,0], infeasible_F_old[:,1],alpha=0.17, color = 'orange',  label='infeasible_obejct_space')
    ax[3].set_xlabel("$minf(1)$")
    ax[3].set_ylabel("$minf(2)$")
    ax[3].set_title('{} infeasible input out of {}'.format(infeasible_F_old.shape[0],feasible_f_old.shape[0]+infeasible_F_old.shape[0]))
    ax[3].legend()
    plt.tight_layout()
    plt.legend()
    plt.show()

##############################################################################
#################################################################
from matplotlib import pyplot as plt
def visual_problems(feasible_f, infeasible_f):
    figure, ax = plt.subplots(1,2)
    #figure for feasible input
    ax[0].scatter(feasible_f[:,0],feasible_f[:,1], alpha=0.3, color = 'blue', edgecolor= 'black') #alpha change color tranparent
    ax[0].set_xlabel("$minf(1)$")
    ax[0].set_ylabel("$minf(2)$")
    ax[0].set_title('{} feasible input out of {}'.format(feasible_f.shape[0], feasible_f.shape[0]+infeasible_f.shape[0]))

    #figure for infeasible input
    ax[1].scatter(infeasible_f[:,0], infeasible_f[:,1],alpha=0.3, color = 'blue', edgecolor= 'black')
    ax[1].set_xlabel("$minf(1)$")
    ax[1].set_ylabel("$minf(2)$")
    ax[1].set_title('{} infeasible input out of {}'.format(infeasible_f.shape[0],feasible_f.shape[0]+infeasible_f.shape[0]))


    plt.show()





