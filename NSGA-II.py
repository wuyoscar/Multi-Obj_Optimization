from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination
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
from Problems.Define_Problems import *  # python file in Problems/Define_Problems

# add parameters
parser = argparse.ArgumentParser(description='''parameters description''')
parser.add_argument('-p','--problem', type=str, required=True,choices=['bnh','carside',
                            'clutch','kursawe','weldebeam',
                            'truss2d', 'tnk', 'osy', 'chankong','test', 
                            'ctp1', 'pro1','zdt1','zdt2','zdt3','zdt3',
                            'zdt4','zdt5','zdt6'],help="This is specific problem")
parser.add_argument('-d','--dimension', type=int,help="This is dimension of input")
parser.add_argument('-lb', '--lb',type=float, nargs= '+', help='Integer or np.ndarray of length n_var representing the lower bounds of the design variables.')
parser.add_argument('-ub', '--ub',type=float,nargs= '+', help ='Integer or np.ndarray of length n_var representing the upper bounds of the design variables.')
parser.add_argument('-s', '--size', type=int,help='# of data points' )
parser.add_argument('-f', '--filename', type=str,help='this is filename' ) #construct filename base on above parameters
parser.add_argument('-eval', '--evaluation', type=int,help='# of evaluation NSGAII' )
#parser.add_argument('-gen', '--generation', type=int,help='# of generation NSGAII' )


args = parser.parse_args()

current_path = os.getcwd()


xl =np.array(args.lb)
xu =np.array(args.ub)
if args.dimension is not None:
    n_var = args.dimension
else:
    print('plz input dimension')

# select problem from parameter
if __name__ == "__main__":

    problem = input_problem(args.problem, n_var)
    search_domain = np.column_stack([np.array(args.lb),np.array(args.ub)])
    
    if args.size is None:
        input_X = random_pick_X(sd= search_domain, size = 50) 
        print('\n\n********************')
        print('*user did not input require data size,using default data point size 50*')
    else:
        input_X = random_pick_X(sd= search_domain, size = args.size)
        print('\n\n********************')
    print('According input, design variable bound is as below')
    print('\nfrom bound given below, generating  data points {} successfully'.format(input_X.shape))
    print(search_domain)
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
    pref_path = "NSGAII_" + pref_path
    try:
        feasible_X_path= os.path.join(path, pref_path + '_feasible_X.txt')
        infeasible_X_path =os.path.join(path,  pref_path + '_infeasible_X.txt')
        feasible_objective_path =os.path.join(path, pref_path + '_feasible_F.txt')
        infeasible_objective_path = os.path.join(path,  pref_path + '_infeasible_F.txt')
    except Exception:
        print('\n****plz input a filename argument***')

    with open( feasible_X_path, 'a') as f:  # infeasible point, outside feasible domain
            np.savetxt(f,feasible_X, delimiter=",")

    with open(infeasible_X_path, 'a') as f:  # infeasible point, outside feasible domain
            np.savetxt(f,infeasible_X, delimiter=",")

    with open(feasible_objective_path, 'a') as f:  # infeasible point, outside feasible domain
            np.savetxt(f,feasible_F, delimiter=",")

    with open(infeasible_objective_path, 'a') as f:  # infeasible point, outside feasible domain
            np.savetxt(f,infeasible_F, delimiter=",")



    algorithm = NSGA2(pop_size=100)


    start = time.time()

    if args.evaluation is None:

        termination = get_termination("n_eval", 2000)
        print('\n\n***user did not inputing number of evaluation, using default value 2000***')
    else:
        termination = get_termination("n_eval", args.evaluation)

    res = minimize(problem= problem,
            algorithm = algorithm,
            termination=termination,
            seed=1,
            verbose=True)
    print('\nTime elapsed for solving problem: ', time.time() - start, ' seconds\n')

    algorithm_X_path = os.path.join(path, pref_path + '_NSGA-II_X.txt')
    algorithm_F_path = os.path.join(path, pref_path + '_NSGA-II_F.txt')


    with open(algorithm_X_path, 'a') as f:  
            np.savetxt(f,res.X, delimiter=",")

    with open(algorithm_F_path, 'a') as f:  
            np.savetxt(f,res.F, delimiter=",")
    
    print('\n\n---------')
    print('feasible_X path is: ',feasible_X_path)
    print('------------')
    print('infeasible_X path is: ',infeasible_X_path)
    print('------------')
    print('feasible_F path is: ',feasible_objective_path)
    print('------------')
    print('infeasible_F path is: ',infeasible_objective_path)
    print('------------')
    print('NSGAII optimal X path is : ',algorithm_X_path)
    print('------------')
    print('NSGAII optimal objective value path is: ',algorithm_F_path)
