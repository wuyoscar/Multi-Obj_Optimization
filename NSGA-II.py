from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination, get_problem
from pymoo.optimize import minimize
from pymoo.util.termination.default import MultiObjectiveDefaultTermination
from pymoo.factory import get_performance_indicator
import numpy as np
import time
import sys
import os 
import argparse



module_path = os.getcwd()+'/Problems/'
sys.path.append(module_path)
from Define_Problems import *

# add parameters
parser = argparse.ArgumentParser(description='''parameters description''')
parser.add_argument('-p','--problem', type=str, required=True,choices=['p1','p2','p3','p4','p5'],help="This is specific problem")
parser.add_argument('-d','--dimension', type=int,help="This is dimension of input")
parser.add_argument('-lb','--lb', type=float, nargs= '+', help='Integer or np.ndarray of length n_var representing the lower bounds of the design variables.')
parser.add_argument('-ub','--ub', type=float,nargs= '+', help ='Integer or np.ndarray of length n_var representing the upper bounds of the design variables.')
parser.add_argument('-s', '--size', type=int,help='# of data points' )
parser.add_argument('-f', '--filename', type=str,help='this is filename' )

#algorithms paramters 
parser.add_argument('-eval', '--evaluation', type=int,help='# of evaluation NSGAII' )
#parser.add_argument('-gen', '--generation', type=int,help='# of generation NSGAII' )


args = parser.parse_args()

current_path = os.getcwd()
'''


nsga2_algorithmn_X
nsga2_algorithmn_objective_X

'''

xl =np.array(args.lb)
xu =np.array(args.ub)

# select problem from parameter
if __name__ == "__main__":
    p_dict = {'p1':p1(xl,xu), 'p2':p2(xl,xu), 'p3':p3(xl,xu), 'p4':p4(xl,xu), 'p5':p5(xl,xu)}
    
    if args.problem in p_dict.keys():

        problem = p_dict[args.problem]
        print('\n\n***********')
        print('probelm is :')
        print(problem)
    else:
        print('Plz select correct problem')

    #sd: search domain
    search_domain = np.column_stack([np.array(args.lb),np.array(args.ub)])
    input_X = random_pick_X(sd= search_domain, size = args.size)    

    print('\n\n********************')

    print('According input, design variable bound is as below')
    print(search_domain)
    print('\n')
    print('from bound give above, generating  data points {} successfully'.format(input_X.shape))
    print('\n********************\n')
    #!!!! evaluateing input_X data by _valuate, filtering datasets
    ## based on codes constraints
    input_X_objective_value, input_X_constraint_value, input_X_violating_value =problem.evaluate(input_X, return_values_of = ['F','G','CV'])
    #print(input_X,input_X_objective_value)
    #spliting feasible /infeasible
    feasible_X,infeasible_X, feasible_F,infeasible_F = split_X(input_X,input_X_objective_value,input_X_violating_value)
    
    #print(feasible_X,infeasible_X, feasible_F,infeasible_F )

    # construct filename 
    path = os.path.join(os.getcwd(), 'Result')
    try:
        os.makedirs(path)
    except OSError:
        pass
    else:
        print ("Successfully created the directory %s" % path)
    pref_path = args.filename


    feasible_X_path= os.path.join(path, pref_path + 'feasible_X.txt')
    infeasible_X_path =os.path.join(path,  pref_path + 'infeasible_X.txt')
    feasible_objective_path =os.path.join(path, pref_path + 'feasible_F.txt')
    infeasible_objective_path = os.path.join(path,  pref_path + 'infeasible_F.txt')

    with open( feasible_X_path, 'a') as f:  # infeasible point, outside feasible domain
            np.savetxt(f,feasible_X, delimiter=",")

    with open(infeasible_X_path, 'a') as f:  # infeasible point, outside feasible domain
            np.savetxt(f,infeasible_X, delimiter=",")

    with open(feasible_objective_path, 'a') as f:  # infeasible point, outside feasible domain
            np.savetxt(f,feasible_F, delimiter=",")

    with open(infeasible_objective_path, 'a') as f:  # infeasible point, outside feasible domain
            np.savetxt(f,infeasible_F, delimiter=",")

    print('\n\n---------')
    print('feasible_X path is: ',feasible_X_path)
    print('------------')
    print('infeasible_X path is: ',infeasible_X_path)
    print('------------')
    print('feasible_F path is: ',feasible_objective_path)
    print('------------')
    print('infeasible_F path is: ',infeasible_objective_path)

    algorithm = NSGA2(pop_size=100)


    start = time.time()


    termination = get_termination("n_eval", args.evaluation)

    res = minimize(problem= problem,
            algorithm = algorithm,
            termination=termination,
            seed=1,
            verbose=True)
    print('\nTime elapsed for solving problem: ', time.time() - start, ' seconds\n')

    