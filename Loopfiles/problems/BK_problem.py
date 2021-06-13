from pymoo.model.problem import Problem
import numpy as np
import os



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




# this function for random generating X
def random_pick_X(n_var = None, bound = None, datasize=None):
    a = bound[0]
    b = bound[1]
    X = (b-a)*np.random.random((datasize, n_var)) +a
    return X

def split_X(X,problem_F,problem_CV, lb, lp):
    
    #filter infeasible and feasible index
    infeasible_index = np.where(problem_CV > 0)[0]
    feasible_index = [i for i in range(X.shape[0]) if i not in infeasible_index ]
    #get feasible and infeasible input
    feasible_X = X[feasible_index]         

    infeasible_X = X[infeasible_index]
    feasible_F = problem_F[feasible_index]
    infeasible_F = problem_F[infeasible_index]

    print('------problem evaluation-----')
    print('Give search domain {} ~ {}  with {} data points'.format(lb, lp, X.shape[0]))
    print('{} is feasible and {} is infeasiebl'.format(len(feasible_index), len(infeasible_index)))

    return feasible_X,infeasible_X, feasible_F,infeasible_F


#get problem 

p = 'BK_problem'

problem = binh_and_korn_Problem()

#!define bound here
ub = np.random.randint(20) #upper bound
lb = - np.random.randint(20) # Lower bound

X = random_pick_X(n_var = problem.n_var, bound = [lb,ub], datasize=300) #! define data size here
print('\n')


problem_result = problem.evaluate(X)
feasible_X,infeasible_X, feasible_F,infeasible_F = split_X(X, problem_result[0], problem_result[1], lb , ub)  


#join directory 
path = os.path.join(os.getcwd(), 'Result','Problem', p )

print(path)
try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)

feasible_X_path = path + '/' + str(lb) + '~' + str(ub) + '_fesasible_X'
infeasible_X_path = path + '/' +str(lb) + '~' + str(ub) + '_infesasible_X'
feasible_F_path = path + '/' + str(lb) + '~' + str(ub) + '_fesasible_F'
infeasible_F_path = path + '/' + str(lb) + '~' + str(ub) + '_infesasible_F'

print(feasible_X_path, infeasible_X_path, feasible_F_path, infeasible_F_path)



#np.savetxt(feasible_X_path, feasible_X)
#np.savetxt(infeasible_X_path, infeasible_X)
#np.savetxt(feasible_F_path, feasible_F)
#np.savetxt(infeasible_F_path, infeasible_F)


with open(feasible_X_path, 'a') as f:  # infeasible point, outside feasible domain
        print(feasible_X, sep=' ', file=f)

with open(infeasible_X_path, 'a') as f:  # infeasible point, outside feasible domain
        print(infeasible_X, sep=' ', file=f)

with open(feasible_F_path, 'a') as f:  # infeasible point, outside feasible domain
        print(feasible_F, sep=' ', file=f)

with open(infeasible_F_path, 'a') as f:  # infeasible point, outside feasible domain
        print(infeasible_F, sep=' ', file=f)

