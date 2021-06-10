from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination
from pymoo.factory import get_problem
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
from pymoo.util.termination.default import MultiObjectiveDefaultTermination
from pymoo.factory import get_performance_indicator
import numpy as np
import time
import sys
import os 



'''
This loop file to evaluating performance of NSGA-II by selecting problems and pop_size 
'''

#for path in sys.path:
#    print(path)

#!select problems here 
problem_list = ['BNH', 'OSY', 'TNK', 'Truss2D', 'Welded_Beam', 'zdt1','ZDT2','ZDT3','ZDT4','ZDT5','ZDT6']
select_problem_list = ['BNH', 'OSY', 'TNK','Truss2D','Welded_Beam']


problem_dict = {}

#! set pop_size list here
pop_list = list(range(10,1500,10)) ####!!!!!!!!!!!


for problem_name in select_problem_list:
    pop_dict = {}
    for pop_name in pop_list:
        print('\n\n')
        print('-'*60)
        print('-'*60)

        p = get_problem(problem_name)
        print('problem is:\n',p)
        
        #default setting for termination
        termination = MultiObjectiveDefaultTermination(

        n_max_gen=1500,
        n_max_evals=1500
        )
        #algorithm parameters
        algorithm = NSGA2(
        pop_size= pop_name, #! parameters
        n_offspring = 20,
    #    crossover=get_crossover("real_sbx", prob=0.9, eta=15),
    #    mutation=get_mutation("real_pm", eta=20),
        eliminate_duplicates=True,
        termination = termination 
    )

        start = time.time()
        res = minimize(p,
                algorithm,
                termination,
                seed=1,
                save_history=True,
                verbose=False)

        print('Time elapsed for solving problem: ', time.time() - start, ' seconds\n')
        
        print('population size',pop_name)
        print("Best solution found: {}".format(res.X.shape)) #pareto solution set 
        print("Function value: {}".format(res.F.shape)) #object function value 
    # print("Constraint violation: {}".format(res.CV.shape)) 
        #join directory 
        
        pf = p.pareto_front()
        gd = get_performance_indicator("gd",pf ) 
        if pf is not None:
            pop_dict[str(pop_name)] = gd.calc(res.F)
            print("GD", gd.calc(res.F))
        
        path = os.path.join(os.getcwd(), 'Result','Algorithmn_Result', 'NAGA-II' )

        print(path)
        try:
            os.makedirs(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s" % path)


        best_solution_path = path + '/NSGA-II_' + str(problem_name)+'_popsize_' + str(pop_name) + '_X'
        objective_value_path= path + '/NSGA-II_' + str(problem_name) + '_popsize_' +str(pop_name) + '_F'
        

        with open(best_solution_path, 'w+') as f:  # infeasible point, outside feasible domain
            print(res.X, sep=' ', file=f)

        with open(objective_value_path, 'w+') as f:  # infeasible point, outside feasible domain
            print(res.F, sep=' ', file=f)

    sorted_dict = dict(sorted(pop_dict.items(),
                        key=lambda item: item[1],
                        reverse=False))      

    problem_dict[problem_name] = sorted_dict

print('-'*60)

for i in problem_dict.keys():
    print(i,problem_dict[i])
    print('\n')


        
        




        





