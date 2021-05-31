import numpy as np
import time
from pymoo.algorithms.nsga2 import NSGA2
from pymoo.util.termination.f_tol import MultiObjectiveSpaceToleranceTermination
from pymoo.optimize import minimize
import matplotlib.pyplot as plt
from pymoo.performance_indicator.hv import Hypervolume
from problems import split_X

#call NSGAII from packages
#! lack of tuning algorithms parameters code here:
print('algorithmn:')
print('nsga2')


print('\n******\n')

print('n_evals, F, cv = gen_res(res)')
print('plot_cv(res)')
print('plot_hv(res, ref_point =np.array([1.0, 1.0]))')
print('plot_cc(res,problem, X ,algorithmns_name = \'Algorithmn\')')


#################################################
####################################################
def nsga2(problem):
    algorithm = NSGA2()
    #define termination criterion
    #recommend supplying a maximum number of generations n_max_gen or function evaluations n_max_evals
    termination = MultiObjectiveSpaceToleranceTermination(#tol=0.0025,
                                                    #n_last=30,
                                                    #nth_gen=5,
                                                    n_max_gen=10000,
                                                    n_max_evals=100000)

    #process algorithm
    start = time.time()

    res = minimize(problem = problem, # define problem, here bk_problem
            algorithm = algorithm, # pass algorithm, here NSGA-II
            termination= termination, #define algorithmn terminations
            seed=1, #random seed
            verbose = True,
            save_history= True # define whether ouput should print out 
    )



    # what avaible methods can be called from result
    # get values by deleting shape
    print('\nTime elapsed for solving problem: ', time.time() - start, ' seconds\n')
    print("Generations", res.algorithm.n_gen)
    #  print('Number of functions evaluation',res.algorithm.n_eval)
    print("Design space", res.X.shape)
    print("Object values space", res.F.shape)
    print('Constraint values', res.G.shape)
    print("Aggregated constraint violation", res.CV.shape) #base on this value, we can filtering feasible and infeasible
    print('Final population object',res.pop.shape)
    return res


####################################################
########################evluation visualization############################    





def gen_res(res):
    # iterate over the deepcopies of algorithms
    for algorithm in res.history:
        n_evals = []    # corresponding number of function evaluations\
        F = []          # the objective space values in each generation
        cv = []         # constraint violation in each generation

        # store the number of function evaluations
        n_evals.append(algorithm.evaluator.n_eval)

        # retrieve the optimum from the algorithm
        opt = algorithm.opt

        # store the least contraint violation in this generation
        cv.append(opt.get("CV").min())

        # filter out only the feasible and append
        feas = np.where(opt.get("feasible"))[0]
        _F = opt.get("F")[feas]
        F.append(_F)   
    
    
    return n_evals, F, cv




def plot_cv(res):
    n_evals, F, cv = gen_res(res)
    k = min([i for i in range(len(cv)) if cv[i] <= 0])
    first_feas_evals = n_evals[k]
    print(f"First feasible solution found after {first_feas_evals} evaluations")

    plt.plot(n_evals, cv, '--', label="CV")
    plt.scatter(first_feas_evals, cv[k], color="red", label="First Feasible")
    plt.xlabel("Function Evaluations")
    plt.ylabel("Constraint Violation (CV)")
    plt.legend()
    plt.show()



def plot_hv(res, ref_point =np.array([1.0, 1.0])):
    n_evals, F, cv = gen_res(res)
    # MODIFY - this is problem dependend
    
    # create the performance indicator object with reference point
    metric = Hypervolume(ref_point=ref_point, normalize=False)

    # calculate for each generation the HV metric
    hv = [metric.calc(f) for f in F]

    # visualze the convergence curve
    plt.plot(n_evals, hv, '-o', markersize=4, linewidth=2)
    plt.title("Convergence")
    plt.xlabel("Function Evaluations")
    plt.ylabel("Hypervolume")
    plt.show()


def plot_cc(res,problem, X ,algorithmns_name = 'Algorithmn'):
    feasible_X,infeasible_X, feasible_F,infeasible_F,feasible_G,infeasible_G= split_X(X, problem)

    feasible_f_old = feasible_F
    infeasible_F_old = infeasible_F
    
    from matplotlib import pyplot as plt
    fig, ax = plt.subplots(nrows=2, ncols=2)
    ax = ax.flatten()
    #figure for feasible input
    ax[0].scatter(res.F[:,0],res.F[:,1], alpha=0.3, color = 'blue', edgecolor= 'black',label = 'pareto front') #alpha change color tranparent
    ax[0].set_xlabel("$min f(1)$")
    ax[0].set_ylabel("$min f(2)$")
    ax[0].set_title('{}-{}data points'.format(algorithmns_name, res.F.shape[0]))
    ax[0].legend()
    #figure for infeasible input
    ax[1].scatter(feasible_f_old[:,0], feasible_f_old[:,1], alpha=0.2, color = 'blue',edgecolor= 'black', label = 'feasible_obejct_space' )
    ax[1].scatter(infeasible_F_old[:,0], infeasible_F_old[:,1], alpha=0.2, color = 'orange',  label = 'infeasible_obejct_space')
    ax[1].set_xlabel("$min f(1)$")
    ax[1].set_ylabel("$min f(2)$")
    ax[1].set_title('Random Pick {} data points'.format(feasible_f_old.shape[0]+infeasible_F_old.shape[0]))
    ax[1].legend()

    ax[2].scatter(feasible_f_old[:,0], feasible_f_old[:,1],alpha=0.3, color = 'blue', edgecolor= 'black', label='feasible_obejct_space')
    ax[2].set_xlabel("$min f(1)$")
    ax[2].set_ylabel("$min f(2)$")
    ax[2].set_title('{} feasible input out of {}'.format(feasible_f_old.shape[0],feasible_f_old.shape[0]+infeasible_F_old.shape[0]))
    ax[2].legend()

    ax[3].scatter(infeasible_F_old[:,0], infeasible_F_old[:,1],alpha=0.17, color = 'orange',  label='infeasible_obejct_space')
    ax[3].set_xlabel("$min f(1)$")
    ax[3].set_ylabel("$min f(2)$")
    ax[3].set_title('{} infeasible input out of {}'.format(infeasible_F_old.shape[0],feasible_f_old.shape[0]+infeasible_F_old.shape[0]))
    ax[3].legend()
    plt.tight_layout()
    plt.legend()
    plt.show()


























