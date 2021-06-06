from pymoo.algorithms.rnsga2 import RNSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination
from pymoo.factory import get_problem
from pymoo.optimize import minimize
from pymoo.util.termination.default import MultiObjectiveDefaultTermination
from pymoo.factory import get_performance_indicator
import numpy as np
import time
import sys
import os 

#for path in sys.path:
#    print(path)

problem_list = ['BNH', 'OSY', 'TNK', 'Truss2D', 'Welded_Beam', 'zdt1','ZDT2','ZDT3','ZDT4','ZDT5','ZDT6']

select_problem_list = ['BNH']

problem_dict ={}


def generate_weight():
    a = np.random.random(1)
    b = 1-a
    weight = np.concatenate([a,b])
    return weight

weight_list = [generate_weight() for i in range(5)]  #!!! set weight parameters here by change number 


for problem_name in select_problem_list:
    p_dict ={}
    for weight in weight_list:
        print('\n\n')
        print('-'*60)
        print('-'*60)
        
        p = get_problem(problem_name)
        pf = p.pareto_front()
        gd = get_performance_indicator("gd",pf )
        print('problem is:\n',p)

        # Define reference points
        ref_points = np.array([[0.5, 0.2], [0.1, 0.6]])
        
        #algorithm parameters
        algorithm = RNSGA2(
            ref_points=ref_points,
            
            epsilon=0.01,
            normalization='front',
            extreme_points_as_reference_points=False,
            weights=weight)
        start = time.time()
        res = minimize(p,
                algorithm,
                ('n_gen', 900),
                seed=1,
                save_history=True,
                verbose=False)

        print('Time elapsed for solving problem: ', time.time() - start, ' seconds\n')
        

        print('weight is ',weight)
        print("Best solution found: {}".format(res.X.shape)) #pareto solution set 
        print("Function value: {}".format(res.F.shape)) #object function value 
        print("Constraint violation: {}".format(res.CV.shape)) 
        if pf is not None:
            p_dict[str(weight)] = gd.calc(res.F)
            print("GD", gd.calc(res.F))
        #join directory 

        path = os.path.join(os.getcwd(), 'Result','Algorithmn_Result', 'RNSGA2' )
        print(path)
        try:
            os.makedirs(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s" % path)
        best_solution_path = path + '/RNSGA2_' + str(problem_name)+'_weight' + str(weight) + '_X'
        objective_value_path= path + '/RNSGA2_' + str(problem_name) + '_weight' +str(weight) + '_F'
        constraint_viloation_path = path + '/RNSGA2_' + str(problem_name)+ '_weight' + str(weight) + '_CV'
        
        with open(best_solution_path, 'w+') as f:  # infeasible point, outside feasible domain
            print(res.X, sep=' ', file=f)
        with open(objective_value_path, 'w+') as f:  # infeasible point, outside feasible domain
            print(res.F, sep=' ', file=f)
        with open(constraint_viloation_path, 'w+') as f:  # infeasible point, outside feasible domain
            print(res.CV, sep=' ', file=f)
    
    sorted_dict = dict(sorted(p_dict.items(),
                        key=lambda item: item[1],
                        reverse=False)) 
    problem_dict[problem_name] = sorted_dict
print('-'*60)
print(problem_dict)






