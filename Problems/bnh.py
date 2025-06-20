
from pymoo.core.problem import Problem
import numpy as np
import autograd.numpy as anp


class BNH(Problem):

    def __init__(self):
        super().__init__(n_var=2, n_obj=2, n_constr=2, type_var=np.double)
        self.xl = anp.zeros(self.n_var)
        self.xu = anp.array([5.0, 3.0])
        
    def _evaluate(self, x, out, *args, **kwargs):
        f1 = 4 * x[:, 0] ** 2 + 4 * x[:, 1] ** 2
        f2 = (x[:, 0] - 5) ** 2 + (x[:, 1] - 5) ** 2
        g1 = (1 / 25) * ((x[:, 0] - 5) ** 2 + x[:, 1] ** 2 - 25)
        g2 = -1 / 7.7 * ((x[:, 0] - 8) ** 2 + (x[:, 1] + 3) ** 2 - 7.7)

        out["F"] = anp.column_stack([f1, f2])
        out["G"] = anp.column_stack([g1, g2])

    def _calc_pareto_front(self, n_points=100):
        x1 = anp.linspace(0, 5, n_points)
        x2 = anp.linspace(0, 5, n_points)
        x2[x1 >= 3] = 3

        X = anp.column_stack([x1, x2])
        return self.evaluate(X, return_values_of=["F"])