from deap import benchmarks
from platypus import algorithms, problems
from platypus.core import Algorithm
from pymoo.optimize import minimize #import minimize to find optimal solution
from pymoo.model.problem import Problem
from pymoo.algorithms.nsga2 import NSGA2
from matplotlib import pyplot as plt
import numpy as np

#print(benchmarks.kursawe([1,0]))
#test multiobject function --kursawe

###steps
# - Problem
# - Algorithm
# - Stop criteria


class ProblemWrapper(Problem):

    def _evaluate(self, designs, out, *args, **kwargs):
        res = []  #define list to save result

        for design in designs:    # designs is our input 
            res.append(benchmarks.kursawe(design)) # for each input, test kursawe function
            out['F'] = np.array(res)     #np.array convert result into array in order to computation


# step1 define problem
problem = ProblemWrapper(n_var=2, n_obj=2, xl=[-5.,-5.], xu=[5.,5.])

# step2 define algorithm
algorithm = NSGA2(pop_size=200)

# step3 stop criteria

stop_criteria = ('n_gen', 100)   #100 generation

results = minimize(
    problem= problem,
    algorithm= algorithm,
    termination= stop_criteria
)


#call pareto result

results_data = results.F.T

plt.scatter(results_data[0], results_data[1], alpha=.4,)
plt.title('Kursawe function -- NSGA2 algorithm')
plt.xlabel('$x1$')
plt.ylabel('$x2$')
plt.show()

