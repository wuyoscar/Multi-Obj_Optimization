
from pymoo.factory import get_problem, get_reference_directions, get_visualization
from pymoo.util.plotting import plot



pf = get_problem("dtlz5").pareto_front()
get_visualization("scatter", angle=(20,20)).add(pf).show()