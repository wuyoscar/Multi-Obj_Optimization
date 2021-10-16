from pymoo.model.problem import Problem
import numpy as np
import autograd.numpy as anp


class CTP(Problem):

    def __init__(self, n_var=2, n_constr=1, option="linear"):
        super().__init__(n_var=n_var, n_obj=2, n_constr=n_constr,  type_var=anp.double)
        self.xu = np.array([0,0])
        self.xp = np.array([1,1])

        def g_linear(x):
            return 1 + anp.sum(x, axis=1)

        def g_multimodal(x):
            A = 10
            return 1 + A * x.shape[1] + anp.sum(x ** 2 - A * anp.cos(2 * anp.pi * x), axis=1)

        if option == "linear":
            self.calc_g = g_linear

        elif option == "multimodal":
            self.calc_g = g_multimodal
            self.xl[:, 1:] = -5.12
            self.xu[:, 1:] = 5.12

        else:
            print("Unknown option for CTP single.")

    def calc_objectives(self, x):
        f1 = x[:, 0]
        gg = self.calc_g(x[:, 1:])
        f2 = gg * (1 - anp.sqrt(f1 / gg))
        return f1, f2

    def calc_constraint(self, theta, a, b, c, d, e, f1, f2):
        return - (anp.cos(theta) * (f2 - e) - anp.sin(theta) * f1 -
                  a * anp.abs(anp.sin(b * anp.pi * (anp.sin(theta) * (f2 - e) + anp.cos(theta) * f1) ** c)) ** d)

class CTP1(CTP):

    def __init__(self,n_var=2, n_constr=2,**kwargs):
        super().__init__()

        a, b = anp.zeros(n_constr + 1), anp.zeros(n_constr + 1)
        a[0], b[0] = 1, 1
        delta = 1 / (n_constr + 1)
        alpha = delta

        for j in range(n_constr):
            beta = a[j] * anp.exp(-b[j] * alpha)
            a[j + 1] = (a[j] + beta) / 2
            b[j + 1] = - 1 / alpha * anp.log(beta / a[j + 1])

            alpha += delta

        self.a = a[1:]
        self.b = b[1:]


    def _evaluate(self, x, out, *args, **kwargs):
        f1 = x[:, 0]
        gg = self.calc_g(x[:, 1:])
        f2 = gg * anp.exp(-f1 / gg)
        out["F"] = anp.column_stack([f1, f2])

        a, b = self.a, self.b
        g = []
        for j in range(self.n_constr):
            _g = - (f2 - (a[j] * anp.exp(-b[j] * f1)))
            g.append(_g)
        out["G"] = anp.column_stack(g)