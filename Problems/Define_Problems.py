from pymoo.model.problem import Problem
import numpy as np
import autograd.numpy as anp


def lsp(objective_function):
    num_weight = len(objective_function)
    w = np.random.rand(num_weight)
    w=w/w.sum()
    fp = np.array(objective_function)
    lsp = np.dot(w, fp)
    print('weight is: ',w)
    return lsp


def random_pick_X(sd, size = 100):
    # you have data size and a set of bound
    # based on this generating random data points(
    #sd is np.columnstack([lb,ub])
    lst = []
    for each_variable_domain in sd:
        aryl = np.random.uniform(low=each_variable_domain[0], high=each_variable_domain[1], size =size).reshape(-1,1)
        lst.append(aryl) 
    return np.column_stack(lst) #stack all variables search domain

def split_X(X,problem_F,problem_CV):
    
    #filter infeasible and feasible index
    infeasible_index = np.where(problem_CV > 0)[0]
    feasible_index = [i for i in range(X.shape[0]) if i not in infeasible_index ]
    #get feasible and infeasible input
    feasible_X = X[feasible_index]         

    infeasible_X = X[infeasible_index]
    feasible_F = problem_F[feasible_index]
    infeasible_F = problem_F[infeasible_index]

    print('------problem evaluation-----')
    print('{} is feasible and {} is infeasible among {} data points'.format(len(feasible_index), len(infeasible_index), len(X)))

    return feasible_X,infeasible_X, feasible_F,infeasible_F




## multi problems 
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

###Carside
class Carside(Problem):
    def __init__(self):
        self.xl = anp.array([0.5, 0.45, 0.5, 0.5, 0.875, 0.4, 0.4])
        self.xu = anp.array([1.5, 1.35, 1.5, 1.5, 2.625, 1.2, 1.2])
        super().__init__(n_var=7, n_obj=3,n_constr=10, type_var=np.double)
        

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

        out["F"] = np.column_stack([f1, f2, f3])
        out["G"] = np.column_stack([g1, g2, g3, g4, g5, g6, g7, g8, g9, g10])
        


class Clutch(Problem):
    def __init__(self):
        
        super().__init__(n_var=5, n_obj=2, n_constr=19, type_var=np.int32)
        # ri, ro, t, F, Z
        # self.xl = anp.array([60, 90, 1, 600, 2]
        self.xl = anp.array([0, 0, 0, 0, 0])
        self.xu = anp.array([20, 20, 4, 400, 7])
        self.x1 = anp.arange(60, 81)
        self.x2 = anp.arange(90, 111)
        self.x3 = anp.arange(1, 3.5, 0.5)
        self.x4 = anp.arange(600, 1001)
        self.x5 = anp.arange(2, 11)

    def _evaluate(self, x, out, *args, **kwargs):

        x1, x2, x3, x4, x5 = anp.split(x, 5, axis=1)

        x1 = self.x1[x1]
        x2 = self.x2[x2]
        x3 = self.x3[x3]
        x4 = self.x4[x4]
        x5 = self.x5[x5]

        pi = anp.pi
        mu = 0.5
        s = 1.5
        M_f = 3  # Nm
        ri_max = 80  # mm
        t_max = 3  # mm
        n = 250  # rpm
        w = pi * n/30  # rad/s
        R_sr = (2/3) * ((x2**3 - x1**3)/(x2**2 - x1**2))  # mm
        p_max = 1  # MPa
        T_max = 15  # s
        I_z = 55  # kg*m^2
        ro_min = 90  # mm
        F_max = 1000  # N
        A = pi * (x2**2 - x1**2)  # mm^2
        deltaR = 20  # mm
        rho = 0.0000078  # kg/mm^2
        delta = 0.5  # mm
        ro_max = 110  # mm

        Z_max = 9
        p_rz = x4/A  # N/mm^2
        L_max = 30  # mm
        Vsr_max = 10  #m/s
        M_s = 40  # Nm
        ri_min = 60  # mm
        t_min = 1.5  # mm

        M_h = (2/3) * mu * x4 * x5 * ((x2**3 - x1**3)/(x2**2 - x1**2))  # N*mm
        Vsr = (pi * R_sr * n)/30  # mm/s

        T = (I_z * w)/(M_h/1000 + M_f)

        g1 = (x2 - x1 - deltaR) * -1
        g2 = (L_max - (x5 + 1) * (x3 + delta)) * -1
        g3 = (p_max - p_rz) * -1
        g4 = (p_max * Vsr_max*1000 - p_rz * Vsr) * -1
        g5 = (Vsr_max*1000 - Vsr) * -1
        g6 = (M_h/1000 - (s * M_s)) * -1
        g7 = T * -1
        g8 = (T_max - T) * -1

        _g9 = -x1 + ri_min
        _g10 = x1 - ri_max

        _g11 = -x2 + ro_min
        _g12 = x2 - ro_max

        _g13 = -x3 + t_min
        _g14 = x3 - t_max

        _g15 = -x4
        _g16 = x4 - F_max

        _g17 = -x5 + 2
        _g18 = x5 - Z_max

        f1 = pi * (x2**2 - x1**2) * x3 * (x5 + 1) * rho
        f2 = T

        out["F"] = anp.column_stack([f1, f2])
        out["G"] = anp.column_stack([g1, g2, g3, g4, g5, g6, g7, g8])



class Kursawe(Problem):
    def __init__(self):
        super().__init__(n_var=3, n_obj=2, xl=-5,xu=5,n_constr=0, type_var=anp.double)

    def _evaluate(self, x, out, *args, **kwargs):
        l = []
        for i in range(2):
            l.append(-10 * anp.exp(-0.2 * anp.sqrt(anp.square(x[:, i]) + anp.square(x[:, i + 1]))))
        f1 = anp.sum(anp.column_stack(l), axis=1)

        f2 = anp.sum(anp.power(anp.abs(x), 0.8) + 5 * anp.sin(anp.power(x, 3)), axis=1)

        out["F"] = anp.column_stack([f1, f2])



class WeldedBeam(Problem):
    def __init__(self):
        super().__init__(n_var=4, n_obj=2, n_constr=4, type_var=anp.double)
        self.xl = anp.array([0.125, 0.1, 0.1, 0.125])
        self.xu = anp.array([5.0, 10.0, 10.0, 5.0])
        
    def _evaluate(self, x, out, *args, **kwargs):
        f1 = 1.10471 * x[:, 0] ** 2 * x[:, 1] + 0.04811 * x[:, 2] * x[:, 3] * (14.0 + x[:, 1])
        f2 = 2.1952 / (x[:, 3] * x[:, 2] ** 3)

        P = 6000
        L = 14
        t_max = 13600
        s_max = 30000

        R = anp.sqrt(0.25 * (x[:, 1] ** 2 + (x[:, 0] + x[:, 2]) ** 2))
        M = P * (L + x[:, 1] / 2)
        J = 2 * anp.sqrt(0.5) * x[:, 0] * x[:, 1] * (x[:, 1] ** 2 / 12 + 0.25 * (x[:, 0] + x[:, 2]) ** 2)
        t1 = P / (anp.sqrt(2) * x[:, 0] * x[:, 1])
        t2 = M * R / J
        t = anp.sqrt(t1 ** 2 + t2 ** 2 + t1 * t2 * x[:, 1] / R)
        s = 6 * P * L / (x[:, 3] * x[:, 2] ** 2)
        P_c = 64746.022 * (1 - 0.0282346 * x[:, 2]) * x[:, 2] * x[:, 3] ** 3

        g1 = (1 / t_max) * (t - t_max)
        g2 = (1 / s_max) * (s - s_max)
        g3 = (1 / (5 - 0.125)) * (x[:, 0] - x[:, 3])
        g4 = (1 / P) * (P - P_c)

        out["F"] = anp.column_stack([f1, f2])
        out["G"] = anp.column_stack([g1, g2, g3, g4])


class Truss2D(Problem):

    def __init__(self):
        super().__init__(n_var=3, n_obj=2, n_constr=1,type_var=anp.double)
        self.Amax = 0.01
        self.Smax = 1e5

        self.xl = anp.array([0.0, 0.0, 1.0])
        self.xu = anp.array([self.Amax, self.Amax, 3.0])

    def _evaluate(self, x, out, *args, **kwargs):

        # variable names for convenient access
        x1 = x[:, 0]
        x2 = x[:, 1]
        y = x[:, 2]

        # first objectives
        f1 = x1 * anp.sqrt(16 + anp.square(y)) + x2 * anp.sqrt((1 + anp.square(y)))

        # measure which are needed for the second objective
        sigma_ac = 20 * anp.sqrt(16 + anp.square(y)) / (y * x1)
        sigma_bc = 80 * anp.sqrt(1 + anp.square(y)) / (y * x2)

        # take the max
        f2 = anp.max(anp.column_stack((sigma_ac, sigma_bc)), axis=1)

        # define a constraint
        g1 = f2 - xu

        out["F"] = anp.column_stack([f1, f2])
        out["G"] = g1


class TNK(Problem):
    def __init__(self):
        super().__init__(n_var=2, n_obj=2, n_constr=2, type_var=anp.double)
        self.xl = anp.array([0, 1e-30])
        self.xu = anp.array([anp.pi, anp.pi])

    def _evaluate(self, x, out, *args, **kwargs):
        f1 = x[:, 0]
        f2 = x[:, 1]
        g1 = -(anp.square(x[:, 0]) + anp.square(x[:, 1]) - 1.0 - 0.1 * anp.cos(16.0 * anp.arctan(x[:, 0] / x[:, 1])))
        g2 = 2 * (anp.square(x[:, 0] - 0.5) + anp.square(x[:, 1] - 0.5)) - 1

        out["F"] = anp.column_stack([f1, f2])
        out["G"] = anp.column_stack([g1, g2])



class OSY(Problem):
    def __init__(self):
        super().__init__(n_var=6, n_obj=2,n_constr=6, type_var=anp.double)
        self.xl = anp.array([0.0, 0.0, 1.0, 0.0, 1.0, 0.0])
        self.xu = anp.array([10.0, 10.0, 5.0, 6.0, 5.0, 10.0])

    def _evaluate(self, x, out, *args, **kwargs):
        f1 = - (25 * (x[:, 0] - 2) ** 2 + (x[:, 1] - 2) ** 2 + (x[:, 2] - 1) ** 2 + (x[:, 3] - 4) ** 2 + (
                    x[:, 4] - 1) ** 2)
        f2 = anp.sum(anp.square(x), axis=1)

        g1 = (x[:, 0] + x[:, 1] - 2.0) / 2.0
        g2 = (6.0 - x[:, 0] - x[:, 1]) / 6.0
        g3 = (2.0 - x[:, 1] + x[:, 0]) / 2.0
        g4 = (2.0 - x[:, 0] + 3.0 * x[:, 1]) / 2.0
        g5 = (4.0 - (x[:, 2] - 3.0) ** 2 - x[:, 3]) / 4.0
        g6 = ((x[:, 4] - 3.0) ** 2 + x[:, 5] - 4.0) / 4.0

        out["F"] = anp.column_stack([f1, f2])

        out["G"] = anp.column_stack([g1, g2, g3, g4, g5, g6])
        out["G"] = - out["G"]




#################################################################
#################problem_2#######################################
class Chankong(Problem):

#clarify the problem
    def __init__(self):

        super().__init__(n_var=2, n_obj=2,n_constr=2)
        self.xl = anp.array([-20,-20])
        self.xu = anp.array([20,20])
    def _evaluate(self, X, out,*args, **kwargs):
        f1 = 2 + (X[:,0]-2)**2 + (X[:,1]-1)**2
        f2 = 9*X[:,0] - (X[:,1]-1)**2


    #constraints need to be formulated as g(xi)<=0
        g1 =  1/225*(X[:,0]**2 + X[:,1]**2 -225)
        g2 =  X[:,0] - 3*X[:,1] + 10

        out["F"] = np.column_stack([f1, f2]) 
        out["G"] = np.column_stack([g1, g2]) 

#################################################################
#################problem_3#######################################
class Test(Problem):

#clarify the problem
    def __init__(self):

        super().__init__(n_var=2,
                        n_obj=2,
                        n_constr=3)
        self.xl = anp.array([-7,-7])
        self.xu = anp.array([4,4])

    def _evaluate(self, X, out,*args, **kwargs):
        f1 = X[:,0]**2 - X[:,1]
        f2 = -0.5*X[:,0] - X[:,1] -1
        g1 =  -(6.5 - X[:,0]/6 - X[:,1])
        g2 =  -(7.5 - 0.5*X[:,0] - X[:,1])
        g3 = -(30 - 5*X[:,0] - X[:,1])

        out["F"] = np.column_stack([f1, f2]) 
        out["G"] = np.column_stack([g1, g2, g3]) 


class CTP(Problem):

    def __init__(self, n_var=2, n_constr=1, option="linear"):
        super().__init__(n_var=n_var, n_obj=2, n_constr=n_constr, xl=0, xu=1, type_var=anp.double)

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

#################################################################
#################problem_5###########
class PRO1(Problem):
    def __init__(self):
        self.xl = np.array([0,0,0])
        self.xu = np.array([4,4,4])

        super().__init__(n_var=3,
                        n_constr=3,
                        n_obj=3
                        )

    def _evaluate(self, X,out, *args, **kwargs):
        f1 = X[:,0]**3 + X[:,1] + X[:,2] 
        f2 =  (X[:,0]**2 - X[:,1])/4 + 5*X[:,2]
        f3 =  9 + (X[:,0]+X[:,1])**2 + (X[:,1]-X[:,2])**2


        g1 = X[:,0] - 3 + X[:,1]**2 +  X[:,2]
        g2 =1/5*( X[:,1]**2 + X[:,2] -X[:,0]**4-5)
        g3 =  -X[:,2]**3 -(X[:,1]**2)/2

        out["F"] = np.column_stack([f1, f2,f3]) 
        out["G"] = np.column_stack([g1, g2, g3]) 



##### zdt
class ZDT(Problem):

    def __init__(self, n_var=30, **kwargs):
        super().__init__(n_var=n_var, n_obj=2, n_constr=0, xl=0, xu=1, type_var=anp.double, **kwargs)


class ZDT1(ZDT):
    def __init__(self, n_var=30):
        super().__init__(n_var=n_var)

    def _calc_pareto_front(self, n_pareto_points=100):
        x = anp.linspace(0, 1, n_pareto_points)
        return anp.array([x, 1 - anp.sqrt(x)]).T

    def _evaluate(self, x, out, *args, **kwargs):
        f1 = x[:, 0]
        g = 1 + 9.0 / (self.n_var - 1) * anp.sum(x[:, 1:], axis=1)
        f2 = g * (1 - anp.power((f1 / g), 0.5))

        out["F"] = anp.column_stack([f1, f2])


class ZDT2(ZDT):
    def __init__(self, n_var=30):
        super().__init__(n_var=n_var)

    def _calc_pareto_front(self, n_pareto_points=100):
        x = anp.linspace(0, 1, n_pareto_points)
        return anp.array([x, 1 - anp.power(x, 2)]).T

    def _evaluate(self, x, out, *args, **kwargs):
        f1 = x[:, 0]
        c = anp.sum(x[:, 1:], axis=1)
        g = 1.0 + 9.0 * c / (self.n_var - 1)
        f2 = g * (1 - anp.power((f1 * 1.0 / g), 2))

        out["F"] = anp.column_stack([f1, f2])


class ZDT3(ZDT):
    def __init__(self, n_var=30):
        super().__init__(n_var=n_var)

    def _calc_pareto_front(self, n_points=100, flatten=True):
        regions = [[0, 0.0830015349],
                   [0.182228780, 0.2577623634],
                   [0.4093136748, 0.4538821041],
                   [0.6183967944, 0.6525117038],
                   [0.8233317983, 0.8518328654]]

        pf = []

        for r in regions:
            x1 = anp.linspace(r[0], r[1], int(n_points / len(regions)))
            x2 = 1 - anp.sqrt(x1) - x1 * anp.sin(10 * anp.pi * x1)
            pf.append(anp.array([x1, x2]).T)

        if not flatten:
            pf = anp.concatenate([pf[None,...] for pf in pf])
        else:
            pf = anp.row_stack(pf)

        return pf

    def _evaluate(self, x, out, *args, **kwargs):
        f1 = x[:, 0]
        c = anp.sum(x[:, 1:], axis=1)
        g = 1.0 + 9.0 * c / (self.n_var - 1)
        f2 = g * (1 - anp.power(f1 * 1.0 / g, 0.5) - (f1 * 1.0 / g) * anp.sin(10 * anp.pi * f1))

        out["F"] = anp.column_stack([f1, f2])


class ZDT4(ZDT):
    def __init__(self, n_var=10):
        super().__init__(n_var)
        self.xl = -5 * anp.ones(self.n_var)
        self.xl[0] = 0.0
        self.xu = 5 * anp.ones(self.n_var)
        self.xu[0] = 1.0
        self.func = self._evaluate

    def _calc_pareto_front(self, n_pareto_points=100):
        x = anp.linspace(0, 1, n_pareto_points)
        return anp.array([x, 1 - anp.sqrt(x)]).T

    def _evaluate(self, x, out, *args, **kwargs):
        f1 = x[:, 0]
        g = 1.0
        g += 10 * (self.n_var - 1)
        for i in range(1, self.n_var):
            g += x[:, i] * x[:, i] - 10.0 * anp.cos(4.0 * anp.pi * x[:, i])
        h = 1.0 - anp.sqrt(f1 / g)
        f2 = g * h

        out["F"] = anp.column_stack([f1, f2])


class ZDT5(ZDT):

    def __init__(self, m=11, n=5, normalize=True, **kwargs):
        self.m = m
        self.n = n
        self.normalize = normalize
        super().__init__(n_var=(30 + n * (m - 1)), **kwargs)

    def _calc_pareto_front(self, n_pareto_points=100):
        x = 1 + anp.linspace(0, 1, n_pareto_points) * 30
        pf = anp.column_stack([x, (self.m-1) / x])
        if self.normalize:
            pf = normalize(pf)
        return pf

    def _evaluate(self, x, out, *args, **kwargs):

        _x = [x[:, :30]]
        for i in range(self.m - 1):
            _x.append(x[:, 30 + i * self.n: 30 + (i + 1) * self.n])

        u = anp.column_stack([x_i.sum(axis=1) for x_i in _x])
        v = (2 + u) * (u < self.n) + 1 * (u == self.n)
        g = v[:, 1:].sum(axis=1)

        f1 = 1 + u[:, 0]
        f2 = g * (1 / f1)

        if self.normalize:
            f1 = normalize(f1, 1, 31)
            f2 = normalize(f2, (self.m-1) * 1/31, (self.m-1))

        out["F"] = anp.column_stack([f1, f2])


class ZDT6(ZDT):

    def __init__(self, n_var=10, **kwargs):
        super().__init__(n_var=n_var, **kwargs)

    def _calc_pareto_front(self, n_pareto_points=100):
        x = anp.linspace(0.2807753191, 1, n_pareto_points)
        return anp.array([x, 1 - anp.power(x, 2)]).T

    def _evaluate(self, x, out, *args, **kwargs):
        f1 = 1 - anp.exp(-4 * x[:, 0]) * anp.power(anp.sin(6 * anp.pi * x[:, 0]), 6)
        g = 1 + 9.0 * anp.power(anp.sum(x[:, 1:], axis=1) / (self.n_var - 1.0), 0.25)
        f2 = g * (1 - anp.power(f1 / g, 2))

        out["F"] = anp.column_stack([f1, f2])