import numpy as np
from pymoo.factory import get_problem
from pymoo.util.plotting import plot
osy_problem = get_problem('osy')

#inspect problem
print(osy_problem)

# 2-D, 2_objective values
#pareto soluation inspect
print(osy_problem.pareto_front().shape)

#visualization 
#plot(osy_problem.pareto_front(), no_fill=True)



