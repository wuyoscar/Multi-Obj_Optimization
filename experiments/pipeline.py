
from pymoo.optimize import minimize
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination
import numpy as np
from pymoo.indicators.hv import Hypervolume
import os, sys,argparse,time,csv,uuid
from datetime import datetime

currentdir = os.path.dirname(os.getcwd())
parentdir = os.path.dirname(currentdir)
sys.path.append(currentdir)
sys.path.append(parentdir)
from Problems.Define_Problems import *
from algorithms.algorithm import * 
from matplotlib import pyplot as plt 



parser = argparse.ArgumentParser(description='''parameters description''')

# problem parameters
parser.add_argument('-a', '--algorithm', type = str, required=True)
parser.add_argument('-p','--problem', type=str, required=True,
                        choices=[
                            'bnh','carside',
                            'clutch','kursawe','weldebeam',
                            'truss2d', 'tnk', 'osy', 'chankong', 
                            'ctp1', 'pro1','zdt1','zdt2','zdt3','zdt3',
                            'zdt4','zdt5','zdt6', 'sk2_typo',
                            'kur1', 'vu1', 'vu2', 'sk1','sk2','tkly1','ltdz1'])
parser.add_argument('-ob','--objectives', type=int,help="This is number of objetives") 
parser.add_argument('-xl', '--lb', type=float,nargs= '+')
parser.add_argument('-xu', '--ub', type=float,nargs= '+')
parser.add_argument('-n', '--var', type = int, help= 'Number of variables')


#!-------algorithm parameters  
parser.add_argument('-pop', '--pop_size', default=100,type=int,help='#population size')   
parser.add_argument('-np', '--n_partitions', default=500,type=int)                         
parser.add_argument('-e_val', '--evaluation', type=int,help='# of evaluations')





args = parser.parse_args()


if __name__ == "__main__":

#initial problem, filtering problem base on condition 
    problem = input_problem(problem_name = args.problem, n_var = args.var)
    assert problem.n_var == args.var, "Variables dimension inconsistent"
    print(f'problem name is: {args.problem.upper()}')
    print(f'number of objetives {problem.n_obj}')
    print(f'number of variables {problem.n_var}')
#initial algorithm
    algorithm = input_algorithm(algorithm_name = args.algorithm, m = problem.n_obj, pop_size = args.pop_size, n_partitions = args.n_partitions)

# initial termination 
    assert args.evaluation, "Define termination"
    termination = get_termination("n_eval", args.evaluation)
    print(f'algorithm name is: {args.algorithm.upper()}')

# start execution

    res = minimize(problem= problem,
            algorithm = algorithm,
            termination=termination,
            save_history=True,
            seed=1,
            verbose=False)
    print(f"--- exec_time --: {res.exec_time}s")
    
# now we have result 
    F = res.F
    iteration = len(res.history)

#recording info of this job
    print('solution shape:',F.shape)
    print(f'evaluation is: {res.history[-1].evaluator.n_eval}')
    print(f'lower bound is:{problem.xl} and upper bound is {problem.xu}')



#construct output file:
    result_folder = os.path.join(currentdir,'Result',args.problem.upper(),args.algorithm.upper()+'_' +args.problem.upper()+'_'+str(args.var))
    try:
        os.makedirs(result_folder)
    except OSError:
        pass
    id = uuid.uuid4()
    filename = [args.problem.upper(), args.algorithm.upper(),"Iteration-"+str(iteration),'Obj-'+str(problem.n_obj),'Var-'+str(problem.n_var)]
    file_unique_name = "_".join(filename)
    file_unique_name = file_unique_name +"."+str(id)

    output_location = os.path.join(result_folder, file_unique_name) #objective export locaton
    print("folder name",result_folder)
    print("filename",filename)
    print('Output location:', output_location)
    np.savetxt(output_location, F)




#construct image file:
    images_folder = os.path.join(currentdir,'Result', 'Images',args.problem.upper(),args.algorithm.upper()+'_'+args.problem.upper()+'Var-'+str(problem.n_var))
    #images_folder = os.path.join(currentdir,'Result', 'Images',args.problem.upper(),args.algorithm.upper()+'_' +args.problem.upper())
    try:
        os.makedirs(images_folder)
    except OSError:
        pass
    image_name = [args.problem.upper(), args.algorithm.upper(),"Iteration-"+str(iteration),'Obj-'+str(problem.n_obj),'Var-'+str(problem.n_var), 'Pop_size'+str(args.pop_size)]
    image_name_unique_name = "_".join(image_name)
    image_location = os.path.join(images_folder, image_name_unique_name) #objective export locaton


#visualization 
    approx_ideal = F.min(axis=0)
    approx_nadir = F.max(axis=0)
    plt.figure(figsize=(7, 5))
    plt.scatter(F[:, 0], F[:, 1], alpha=0.4,s=30, facecolors='none', edgecolors='blue')
    plt.scatter(approx_ideal[0], approx_ideal[1], facecolors='none', edgecolors='red', marker="*", s=100, label="Ideal Point (Approx)")
    plt.scatter(approx_nadir[0], approx_nadir[1], facecolors='none', edgecolors='black', marker="p", s=100, label="Nadir Point (Approx)")
    plt.title(f"Objective Space with pop_size {args.pop_size}")
    plt.xlabel("$f1$")
    plt.ylabel("$f2$")
    plt.legend()
    plt.savefig(f"{image_location}")
    print(f"image location {image_location}")



#summary table:
    fieldnames = ['Problem', 'Alg_name', 'Iteration', 'Evaluations','Objectives', 'n_variables',
        'xl', 'xu', 'exec_time', 'approx_nadir','solutions_shape', 'pop_size','path','image_location']

    rows = { 'Problem':args.problem.upper(),
            'Alg_name': args.algorithm.upper(),
            'Iteration': iteration,
            'Evaluations':res.history[-1].evaluator.n_eval,
            'Objectives':problem.n_obj,
            'n_variables': problem.n_var,
            'xl': problem.xl,
            'xu': problem.xu,
            'exec_time': res.exec_time,
            'approx_nadir':approx_nadir,
            'solutions_shape': str(res.F.shape[0]),
            'pop_size':args.pop_size,
            'path': output_location,
            'image_location':image_location
    }   

    table_path = os.path.join(currentdir,'Result','result_23Nov')
    file_exists = os.path.isfile(table_path)
    with open(table_path, 'a+', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(rows)
    print(f'table path is {table_path}')
