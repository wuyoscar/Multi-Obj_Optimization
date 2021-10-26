
from pymoo.optimize import minimize
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination
import numpy as np
from pymoo.indicators.hv import Hypervolume
import os, sys,argparse,time,csv,uuid


currentdir = os.path.dirname(os.getcwd())
parentdir = os.path.dirname(currentdir)
sys.path.append(currentdir)
sys.path.append(parentdir)
from Problems.Define_Problems import *
from algorithms.algorithm import * 



parser = argparse.ArgumentParser(description='''parameters description''')

# problem parameters
parser.add_argument('-a', '--algorithm', type = str, required=True)
parser.add_argument('-p','--problem', type=str, required=True,
                        choices=[
                            'bnh','carside',
                            'clutch','kursawe','weldebeam',
                            'truss2d', 'tnk', 'osy', 'chankong', 
                            'ctp1', 'pro1','zdt1','zdt2','zdt3','zdt3',
                            'zdt4','zdt5','zdt6', 
                            'kur1', 'vu1', 'vu2', 'sk1','sk2','tkly1','ltdz1'])
parser.add_argument('-ob','--objectives', type=int,help="This is number of objetives") 
parser.add_argument('-xl', '--lb', type=float,nargs= '+')
parser.add_argument('-xu', '--ub', type=float,nargs= '+')
parser.add_argument('-n', '--var', type = int, help= 'Number of variables')


#!-------algorithm parameters  
parser.add_argument('-pop', '--pop_size', default=200,type=int,help='#population size')   
parser.add_argument('-np', '--n_partitions', default=100,type=int)                         
parser.add_argument('-gen', '--generation', type=int,help='# of generation NSGAII')





args = parser.parse_args()


if __name__ == "__main__":

#initial problem, filtering problem base on condition 
    if args.var is None:
        problem = input_problem(problem_name = args.problem)
    elif (args.var is not None )and (args.lb is None):
        problem = input_problem(problem_name = args.problem, n_var = args.var)
    elif args.var and args.lb is not None:
        problem = input_problem(problem_name = args.problem, n_var = args.var, xl= args.lb, xu = args.ub)
    print(f'problem name is: {args.problem.upper()}')
    print(f'number of objetives {problem.n_obj}')
    print(f'number of variables {problem.n_var}')
#initial algorithm
    algorithm = input_algorithm(algorithm_name = args.algorithm, m = problem.n_obj, pop_size = args.pop_size, n_partitions = args.n_partitions)

# initial termination 
    assert args.generation, "Define termination"
    termination = get_termination("n_gen", args.generation)
    print(f'algorithm name is: {args.algorithm.upper()}')

# start execution

    res = minimize(problem= problem,
            algorithm = algorithm,
            termination=termination,
            seed=1,
            verbose=False)
    print(f"--- exec_time --: {res.exec_time}s")
    
# now we have result 
    F = res.F
    

#performance indicator 
    #ref_point = np.array([1,1])
    #metric = Hypervolume(nds=True,ref_point = ref_point,norm_ref_point=False)
    #hv = metric.do(F)
    

#recording info of this job
    print('solution shape:',F.shape)
    print(f'generation is: {args.generation}')
    print(f'lower bound is:{problem.xl} and upper bound is {problem.xu}')



#construct output file:
    result_folder = os.path.join(currentdir,'Result',args.problem.upper(),args.algorithm.upper()+'_' +args.problem.upper())
    try:
        os.makedirs(result_folder)
    except OSError:
        pass
    id = uuid.uuid4()
    filename = [args.problem.upper(), args.algorithm.upper(),"Iteration-"+str(args.generation),'Obj-'+str(problem.n_obj),'Var-'+str(problem.n_var)]
    file_unique_name = "_".join(file_unique_name)
    file_unique_name = filename +"."+str(id)

    output_location = os.path.join(result_folder, file_unique_name) #objective export locaton
    print("folder name",result_folder)
    print("filename",filename)
    print('Output location:', output_location)
    np.savetxt(output_location, F)


#summary table:


    fieldnames = ['filename', 'lower bound', 'upper bound', 'exec_time','solutions','path']
    rows = { 'filename':filename,
            'lower bound': list(problem.xl),
            'upper bound': list(problem.xu),
            'exec_time':res.exec_time,
            'solutions': str(F.shape[0]),
            'path': output_location
    }

    table_path = os.path.join(currentdir,'Result','Jobs_record')
    file_exists = os.path.isfile(table_path)
    with open(table_path, 'a+', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(rows)
