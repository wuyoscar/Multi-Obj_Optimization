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

#for path in sys.path:
#    print(path)

problem_list = ['BNH', 'OSY', 'TNK', 'Truss2D', 'Welded_Beam', 'zdt1','ZDT2','ZDT3','ZDT4','ZDT5','ZDT6']

select_problem_list = ['BNH', 'OSY', 'TNK','Truss2D','Welded_Beam']

problem_dict = {}



#! set pop_size list here
####!!!!!!!!!!!
n_evals_list = list(range(10,3000,50))


for problem_name in select_problem_list:
    GD_list = {}

    for n_evals in n_evals_list:  
        print('\n\n')
        print('-'*60)
        print('-'*60)

        p = get_problem(problem_name)
        print('problem is:\n',p)
        pf = p.pareto_front()
        gd = get_performance_indicator("gd",pf )

        #algorithm parameters
        algorithm = NSGA2(
        n_offspring = 20,
        crossover=get_crossover("real_sbx", prob=0.9, eta=15),
        mutation=get_mutation("real_pm", eta=20),
        eliminate_duplicates=True
        
    )
        termination = get_termination("n_eval", n_evals)
        start = time.time()
        res = minimize(p,
                algorithm,
                termination = termination,
                seed=1,
                save_history=True,
                verbose=False)
                
        print('Time elapsed for solving problem: ', time.time() - start, ' seconds\n')
        problem_dict[problem_name] = {'Solution':np.array(res.X), 'Obj_value':np.array(res.F), 'CV':np.array(res.CV)}

        print('Evaluation times:', n_evals)
        print("Best solution found: {}".format(res.X.shape)) #pareto solution set 
        if pf is not None:
            GD_list[str(n_evals)] = gd.calc(res.F)
            print("GD", gd.calc(res.F))

        print("Function value: {}".format(res.F.shape)) #object function value 
        print("Constraint violation: {}".format(res.CV.shape)) 
        #join directory 
        
        path = os.path.join(os.getcwd(), 'Result','Algorithmn_Result', 'NAGA-II' )

        print(path)
        try:
            os.makedirs(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s" % path)


        best_solution_path = path + '/NSGA-II_' + str(problem_name)+'_evals_' + str(n_evals) + '_X'
        objective_value_path= path + '/NSGA-II_' + str(problem_name) + '_evals_' +str(n_evals) + '_F'
        

        with open(best_solution_path, 'w+') as f:  # infeasible point, outside feasible domain
            print(res.X, sep=' ', file=f)

        with open(objective_value_path, 'w+') as f:  # infeasible point, outside feasible domain
            print(res.F, sep=' ', file=f)
    
    
    
    sorted_dict = dict(sorted(GD_list.items(),
                        key=lambda item: item[1],
                        reverse=False))      


    problem_dict[problem_name] = sorted_dict

print('-'*60)

for i in problem_dict.keys():
    print(i,problem_dict[i])
    print('\n')
        





