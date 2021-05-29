from pymoo.factory import get_problem
import numpy as np
# here using zdt1 as example
#2_obejct, 
zdt1_problem = get_problem('zdt1')
print(zdt1_problem)
rng = np.random.default_rng(seed=42)
X = rng.random((10000,30))
result = zdt1_problem.evaluate(X)



#NSGA II algorithm
def nsga_2_algorithm(zdt1_problem):
    from pymoo.algorithms.nsga2 import NSGA2
    from pymoo.factory import get_sampling, get_crossover, get_mutation,get_termination, get_reference_directions, get_visualization,get_problem_options
    from pymoo.optimize import minimize
    from pymoo.util.termination.default import MultiObjectiveDefaultTermination
    
    
    algorithm = NSGA2(
        pop_size=40,
        n_offsprings=10,
        sampling=get_sampling("real_random"),
        crossover=get_crossover("real_sbx", prob=0.9, eta=15),
        mutation=get_mutation("real_pm", eta=20),
        eliminate_duplicates=True
    )
    termination = MultiObjectiveDefaultTermination(n_max_gen=1000,n_max_evals=100000)
    
    res = minimize(zdt1_problem,
            algorithm,
            termination,
            seed=1,
            save_history=True,
            pf = True,
            verbose=True)
    return res




