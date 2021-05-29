
from pymoo.factory import get_problem, get_reference_directions, get_visualization
from pymoo.util.plotting import plot

ref_dirs = get_reference_directions("das-dennis", 3, n_partitions=12)
#pf = get_problem("dtlz4").pareto_front(ref_dirs)

p = get_problem("dtlz4")
pf = p.pareto_front(ref_dirs)
print(p)
get_visualization("scatter", angle=(45,45)).add(pf).show()