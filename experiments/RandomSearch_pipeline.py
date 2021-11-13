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
from problems.Define_Problems import *
from algorithms.algorithm import * 
from matplotlib import pyplot as plt 
import pygmo as pg





parser = argparse.ArgumentParser(description='''parameters description''')

# problem parameters

parser.add_argument('-p','--problem', type=str, required=True,
                        choices=[
                            'bnh','carside',
                            'clutch','kursawe','weldebeam',
                            'truss2d', 'tnk', 'osy', 'chankong', 
                            'ctp1', 'pro1','zdt1','zdt2','zdt3','zdt3',
                            'zdt4','zdt5','zdt6', 'sk2_typo',
                            'kur1', 'vu1', 'vu2', 'sk1','sk2','tkly1','ltdz1'])
parser.add_argument('-ob','--objectives', type=int,help="This is number of objetives") 
parser.add_argument('-n', '--var', type = int, help= 'Number of variables')


parser.add_argument('-pop', '--pop_size', default=100,type=int,help='#population size')   


args = parser.parse_args()

if __name__ == "__main__":
#get problem first
    print("/n/n")
    problem = input_problem(problem_name = args.problem, n_var = args.var)
    assert problem.n_var == args.var, "Variables dimension inconsistent"
    print(f'problem name is: {args.problem.upper()}')
    print(f'number of objetives {problem.n_obj}')
    print(f'number of variables {problem.n_var}')
    

#random generating data points give domain 
    data_point = generate_data(p=problem, size=args.pop_size) #this function coding at "problems/Define_Problems.py"
    print(data_point.shape)

    #compare data point domain with problem domain, ensure they are within same bound, data point size according to algorithm population_size previously
    print(f'--test problem--- xl is {problem.xl} amd xu is {problem.xu}')
    print(f'--data point--- xl is {np.min(data_point,axis=0)} amd xu is {np.max(data_point,axis=0)}')

#**note**: this pipeline only for test problem which does not have constraints
#now we have input data, we can a)count feasible/infeasible set, b) dominated/non-dominated set, c)calculate hv and igd+ in notebook under "Result/result_factory"

    result = problem.evaluate(data_point,return_as_dictionary=True)
    total_solution = result['F']
    ndf, dl, dc, ndr = pg.fast_non_dominated_sorting(total_solution)
#ndf (list of 1D NumPy int array): the non dominated fronts
#dl (list of 1D NumPy int array): the domination list
#dc (1D NumPy int array): the domination count
#ndr (1D NumPy int array): the non domination ranks
    non_donmiated_solution = total_solution[dl[0]]
    print(f'Non dominated solution shape is :{non_donmiated_solution.shape} given data points {args.pop_size}')

    # if can't find non-dominated set
    if non_donmiated_solution.shape[0] ==0:
        
        fieldnames = ['Problem', 'Objectives', 'n_variables','xl', 'xu','pf_shape', 'data_point_shape','path','image_location']
        rows = { 'Problem':args.problem.upper(),
                'Objectives':problem.n_obj,
                'n_variables': problem.n_var,
                'xl': np.min(data_point,axis=0), # this is search domain of input data from uniform distribution 
                'xu': np.max(data_point,axis=0),
                'pf_shape': 0,
                'data_point_shape':args.pop_size,
                'path': "None",
                'image_location': "None"
        }  
        table_path = os.path.join(currentdir,'Result','Random_Search_Result')
        file_exists = os.path.isfile(table_path)
        with open(table_path, 'a+', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(rows)
        print(f'table path is {table_path}')




    else:
    # constructing file name 
        currentdir = os.path.dirname(os.getcwd())
        result_folder = os.path.join(currentdir,'Result','Random_Search' ,args.problem.upper())
        try:
            os.makedirs(result_folder)
        except OSError:
            pass
        #file name $problem_#non_dominated_shape
        id = uuid.uuid4()
        filename = [args.problem.upper(), 'Obj-'+str(problem.n_obj),'Var-'+str(problem.n_var)]
        file_unique_name_1 = "_".join(filename)
        file_unique_name = file_unique_name_1 +"."+str(id)
        #objective location 
        output_location = os.path.join(result_folder, file_unique_name) #objective export locaton
        print(output_location)
        np.savetxt(output_location, non_donmiated_solution)



        #save image 
        images_folder = os.path.join(currentdir,'Result','Images','Random_Search' ,args.problem.upper())
        try:
            os.makedirs(images_folder)
        except OSError:
            pass
        image_name = file_unique_name_1+str(id)
        image_location = os.path.join(images_folder, image_name)

    #visualization 

        approx_ideal = np.min(non_donmiated_solution,axis=0)
        approx_nadir = np.max(non_donmiated_solution,axis=0)
        plt.figure(figsize=(7, 5))
        plt.scatter(non_donmiated_solution[:, 0], non_donmiated_solution[:, 1], alpha=0.4,s=30, facecolors='none', edgecolors='blue')
        plt.scatter(approx_ideal[0], approx_ideal[1], facecolors='none', edgecolors='red', marker="*", s=100, label="Ideal Point (Approx)")
        plt.scatter(approx_nadir[0], approx_nadir[1], facecolors='none', edgecolors='black', marker="p", s=100, label="Nadir Point (Approx)")
        plt.title(f"Objective Space with pop_size {non_donmiated_solution.shape[0]}")
        plt.xlabel("$f1$")
        plt.ylabel("$f2$")
        plt.legend()
        plt.savefig(f"{image_location}")
        print(f"image location {image_location}")

    #summary table for record jobs 
        fieldnames = ['Problem', 'Objectives', 'n_variables','xl', 'xu','pf_shape', 'data_point_shape','path','image_location']
        rows = { 'Problem':args.problem.upper(),
                'Objectives':problem.n_obj,
                'n_variables': problem.n_var,
                'xl': np.min(data_point,axis=0),
                'xu': np.max(data_point,axis=0),
                'pf_shape': str(non_donmiated_solution.shape[0]),
                'data_point_shape':args.pop_size,
                'path': output_location,
                'image_location':image_location
        }  
        table_path = os.path.join(currentdir,'Result','Random_Search_Result')
        file_exists = os.path.isfile(table_path)
        with open(table_path, 'a+', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(rows)
        print(f'table path is {table_path}')