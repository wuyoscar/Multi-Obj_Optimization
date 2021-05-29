from pymoo.factory import get_problem, get_reference_directions, get_visualization
from pymoo.util.plotting import plot

pf = get_problem("zdt1").pareto_front()
get_visualization("scatter", angle=(45,45)).add(pf).show()