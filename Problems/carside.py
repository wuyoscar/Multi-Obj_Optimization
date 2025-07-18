
import autograd.numpy as anp

from pymoo.core.problem import Problem


class Carside(Problem):
    def __init__(self):
        super().__init__(n_var=7, n_obj=3, n_constr=10, type_var=anp.double)
        self.xl = anp.array([0.5, 0.45, 0.5, 0.5, 0.875, 0.4, 0.4])
        self.xu = anp.array([1.5, 1.35, 1.5, 1.5, 2.625, 1.2, 1.2])

    def _evaluate(self, x, out, *args, **kwargs):
        g1 = 1.16 - 0.3717 * x[:,1] * x[:,3] - 0.0092928 * x[:,2]
        g2 = 0.261 - 0.0159 * x[:,0] * x[:,1] - 0.188 * x[:,0] * 0.345 - 0.019 * x[:,1] * x[:,6] + 0.0144 * x[:,2] * x[:,4] + 0.08045 * x[:,5] * 0.192
        g3 = 0.214 + 0.00817 * x[:,4] - 0.131 * x[:,0] * 0.345 - 0.0704 * x[:,0] * 0.192 + 0.03099 * x[:,1] * x[:,5] - 0.018 * x[:,1] * x[:,6] + 0.0208 * x[:,2] * 0.345 + 0.121 * x[:,2] * 0.192 - 0.00364 * x[:,4] * x[:,5] - 0.018 * x[:,1] ** 2
        g4 = 0.74 - 0.61 * x[:,1] - 0.031296 * x[:,2] - 0.166 * x[:,6] * 0.192 + 0.227 * x[:,1] ** 2
        g5 = 28.98 + 3.818 * x[:,2] - 4.2 * x[:,0] * x[:,1] + 6.63 * x[:,5] * 0.192 - 7.77 * x[:,6] * 0.345
        g6 = 33.86 + 2.95 * x[:,2] - 5.057 * x[:,0] * x[:,1] - 11 * x[:,1] * 0.345 - 9.98 * x[:,6] * 0.345 + 22 * 0.345 * 0.192
        g7 = 46.36 - 9.9 * x[:,1] - 12.9 * x[:,0] * 0.345
        g8 = 4.72 - 0.5 * x[:,3] - 0.19 * x[:,1] * x[:,2]
        g9 = 10.58 - 0.674 * x[:,0] * x[:,1] - 1.95 * x[:,1] * 0.345
        g10 = 16.45 - 0.489 * x[:,2] * x[:,6] - 0.843 * x[:,4] * x[:,5]

        f1 = 1.98 + 4.9 * x[:,0] + 6.67 * x[:,1] + 6.98 * x[:,2] + 4.01 * x[:,3] + 1.78 * x[:,4] + 0.00001 * x[:,5] + 2.73 * x[:,6]
        f2 = g8
        f3 = (g9 + g10) / 2.0

        g1 = - 1 + g1 / 1.0
        g2 = -1 + g2 / 0.32
        g3 = -1 + g3 / 0.32
        g4 = -1 + g4 / 0.32
        g5 = -1 + g5 / 32.0
        g6 = -1 + g6 / 32.0
        g7 = -1 + g7 / 32.0
        g8 = -1 + g8 / 4.0
        g9 = -1 + g9 / 9.9
        g10 = -1 + g10 / 15.7

        out["F"] = anp.column_stack([f1, f2, f3])
        out["G"] = anp.column_stack([g1, g2, g3, g4, g5, g6, g7, g8, g9, g10])
