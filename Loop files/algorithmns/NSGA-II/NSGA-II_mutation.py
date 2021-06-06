from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination, get_selection
from pymoo.factory import get_problem
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
from pymoo.util.termination.default import MultiObjectiveDefaultTermination
from pymoo.factory import get_performance_indicator
import numpy as np
import time
import sys
import os 

#for path in sys.path:
#    print(path)

problem_list = ['BNH', 'OSY', 'TNK', 'Truss2D', 'Welded_Beam', 'zdt1','ZDT2','ZDT3','ZDT4','ZDT5','ZDT6']

#!select problem here
select_problem_list = ['BNH','TNK']

eta_list = [1,2,5,7,9,10,13,16,18,20,25,27,30 ]
problem_parameter_dict = {}

for problem_name in select_problem_list:
    res_dict = {}

    for eta in eta_list:
        print('\n\n')
        print('='*60)

        p = get_problem(problem_name)
        print('problem is:\n',p)
        
        #algorithm parameters
        algorithm = NSGA2( 
        n_offspring = 5,
        crossover=get_crossover("real_sbx", prob=0.4, eta=15),
        mutation=get_mutation("real_pm", eta=eta),
        
        eliminate_duplicates=True
    )

    #set time 
        start = time.time()
        res = minimize(p,
                algorithm,
                seed=1,
                save_history=True,
                verbose=False)
                
        print('Time elapsed for solving problem: ', time.time() - start, ' seconds\n')
        #problem_dict[problem_name] = {'Solution':np.array(res.X), 'Obj_value':np.array(res.F), 'CV':np.array(res.CV)}
        
        
    #    print("Best solution found: {}".format(res.X.shape)) #pareto solution set 
    #    print("Function value: {}".format(res.F.shape)) #object function value 
    #    print("Constraint violation: {}".format(res.CV.shape)) 
        #join directory 
        
        path = os.path.join(os.getcwd(), 'Result','Algorithmn_Result', 'NAGA-II' )
        
        pf = p.pareto_front()
        if pf is not None:
            gd = get_performance_indicator("gd", pf)
            print("GD", gd.calc(res.F))
            res_dict[str(eta)] = gd.calc(res.F)
        
        try:
            os.makedirs(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s" % path)
        
        best_solution_path = path + '/NSGA-II_' + str(problem_name)+'_mutation_' + str(eta) + '_X'
        objective_value_path= path + '/NSGA-II_' + str(problem_name) + '_mutation_' +str(eta) + '_F'
        
        

        print(best_solution_path)

        with open(best_solution_path, 'w+') as f:  # infeasible point, outside feasible domain
            print(res.X, sep=' ', file=f)

        with open(objective_value_path, 'w+') as f:  # infeasible point, outside feasible domain
            print(res.F, sep=' ', file=f)


    sorted_dict = dict(sorted(res_dict.items(),
                        key=lambda item: item[1],
                        reverse=False)) 
    problem_parameter_dict[problem_name] = sorted_dict
    print('eta is ', eta)
    print('\n!!!!!!Find the best parameter here !!!!!\n')
    print(sorted_dict)

print('-'*60)
print(problem_parameter_dict)




        





