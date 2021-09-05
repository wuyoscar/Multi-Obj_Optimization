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

#module_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
#path = os.path.join(module_path, 'Problems/')
#module_path = os.getcwd()+'/Problems/'
#sys.path.append(module_path)
#sys.path.append(path)
sys.path.append('/scratch/lk32/ow6835/MOOP')
sys.path.append('/scratch/lk32/ow6835/MOOP/Problems')
from Problems.Define_Problems import *   # python file in Problems/Define_Problems

# add parameters
parser = argparse.ArgumentParser(description='''parameters description''')
parser.add_argument('-p','--problem', type=str, required=True,choices=['bnh','carside',
                            'clutch','kursawe','weldebeam',
                            'truss2d', 'tnk', 'osy', 'chankong','test', 
                            'ctp1', 'pro1','zdt1','zdt2','zdt3','zdt3',
                            'zdt4','zdt5','zdt6'],help="This is specific problem")
parser.add_argument('-d','--dimension', type=int,help="This is dimension of problem")
parser.add_argument('-o','--objectives', type=int,help="This is number of objetives")
parser.add_argument('-lb', '--lb',type=float, nargs= '+', help='Integer or np.ndarray of length n_var representing the lower bounds of the design variables.')
parser.add_argument('-ub', '--ub',type=float,nargs= '+', help ='Integer or np.ndarray of length n_var representing the upper bounds of the design variables.')
parser.add_argument('-s', '--size', type=int,help='# of data points' )
parser.add_argument('-f', '--filename', type=str,help='this is filename' ) #construct filename base on above parameters
parser.add_argument('-n_eval', '--evaluation', type=int,help='# of evaluation NSGAII' )
#parser.add_argument('-gen', '--generation', type=int,help='# of generation NSGAII' )


args = parser.parse_args()

current_path = os.getcwd()


xl =np.array(args.lb)
xu =np.array(args.ub)

# select problem from parameter
if __name__ == "__main__":

    problem = input_problem(args.problem, args.dimension)
    
    
    
    input_X = np.random.uniform(low=xl,high=xu, size=args.size*args.dimension).reshape(-1,args.dimension)


    print('According input, design variable bound is as below')
    print('\nfrom bound given below, generating  data points {} successfully'.format(input_X.shape))
    #print(search_domain)
    print('\n********************\n')
    #!!!! evaluateing input_X data by _valuate, filtering datasets
    ## based on codes constraints
    input_X_objective_value, input_X_constraint_value, input_X_violating_value =problem.evaluate(input_X, return_values_of = ['F','G','CV'])
    #print(input_X,input_X_objective_value)
    #spliting feasible /infeasible
    feasible_X,infeasible_X, feasible_F,infeasible_F = split_X(input_X,input_X_objective_value,input_X_violating_value)
    
    #print(feasible_X,infeasible_X, feasible_F,infeasible_F )

    # construct filename 
    path = '/scratch/lk32/ow6835/MOOP_Result/Result/'

    #create output subfolder based on dimension 
    

    try:
        os.makedirs(path +'feasible_X/')
        os.makedirs(path +'infeasible_X/')
        os.makedirs(path +'feasible/_F/')
        os.makedirs(path +'infeasib/le_F/')
        os.makedirs(path +'input_X/')
        os.makedirs(path +'output_X/')
        os.makedirs(path +'NSGA-II_X/')
        os.makedirs(path +'NSGA-II_F/')

    except OSError:
        pass
    else:
        print ("Successfully created the directory %s" % path)
    
    # problem dimension, #objectives, data size, lb, ub, #evaluation
    #${p}_nsga2.job_2_${s}_${lb}_$(($lb+$ub))_${n_eval}
    pref_path = args.filename
    
    try:
        feasible_X_path= path+ '/feasible_X/'+pref_path
        infeasible_X_path =path+  '/infeasible_X/'+pref_path
        feasible_objective_path =path+  '/feasible/_F/'+pref_path
        infeasible_objective_path = path+  '/infeasib/le_F/'+pref_path
        input_X_path= path+ '/input_X/'+pref_path
        output_X_path = path+ '/output_X/'+pref_path
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
    
    with open(input_X_path, 'a') as f:  # infeasible point, outside feasible domain
            np.savetxt(f,input_X, delimiter=",")
    
    with open(output_X_path, 'a') as f:  # infeasible point, outside feasible domain
            np.savetxt(f,input_X_objective_value, delimiter=",")
    
    



    algorithm = NSGA2(pop_size=500)


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

    algorithm_X_path = path+ '/NSGA-II_X/'+ pref_path 
    algorithm_F_path = path+ '/NSGA-II_F/'+ pref_path


    with open(algorithm_X_path, 'a') as f:  
            np.savetxt(f,res.X, delimiter=",")

    with open(algorithm_F_path, 'a') as f:  
            np.savetxt(f,res.F, delimiter=",")
    

    
    print('\n\n---------')
    print('input X path is ', input_X_path)
    print('output X path is ', output_X_path)
    print('------------')
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

# store result of each run into table 
    import csv 

    fieldnames = ['problem', 'problem dimension', '#_objectives', 
                    'lb', 'ub', 'input data size', 
                    '#_feasible', '#_infeasible','#_evaluations',
                    'algorithmn','#solutions algorithmns produce','Time elapsed by algorithm',
                    'input X path', 'obejctive value of input X path',
                    'feasible_X_path', 'infeasible_X_path',
                    'feasible_objective_path', 'infeasible_objective_path',
                    'algorihtmn_X_path',
                    'algorithmn_F_path']
    rows = {'problem': args.problem,
        'problem dimension': args.dimension,
        '#_objectives': args.objectives,
        'lb': args.lb,
        'ub': args.ub,
        'input data size': args.size,
        '#_feasible': feasible_X.shape[0],
        '#_infeasible': infeasible_X.shape[0],
        'algorithmn': 'NSGA-II',
        '#solutions algorithmns produce': res.X.shape[0],
        '#_evaluations': args.evaluation,
        'Time elapsed by algorithm':time.time() - start ,
        'input X path':  input_X_path,
        'obejctive value of input X path':output_X_path ,
        'feasible_X_path': feasible_X_path,
        'infeasible_X_path': infeasible_X_path ,
        'feasible_objective_path': feasible_objective_path ,
        'infeasible_objective_path':infeasible_objective_path,
        'algorihtmn_X_path':algorithm_X_path ,
        'algorithmn_F_path':algorithm_F_path}
    
    file_exists = os.path.isfile('/scratch/lk32/ow6835/MOOP_Result/Result/table.csv')
    with open('/scratch/lk32/ow6835/MOOP_Result/Result/table.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
                writer.writeheader()
        writer.writerows(rows)

