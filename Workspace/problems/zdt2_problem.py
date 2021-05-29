from pymoo.factory import get_problem
from pymoo.util.plotting import plot

problem = get_problem("zdt2")
plot(problem.pareto_front(), no_fill=True)