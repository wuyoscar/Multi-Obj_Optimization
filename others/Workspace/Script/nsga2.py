import time

from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_problem
from pymoo.model.result import Result
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter

class NSGA2MultiTask(NSGA2):
    def solve(self):
        # the result object to be finally returned
        res = Result()
        # set the timer in the beginning of the call
        res.start_time = time.time()
        # call the algorithm to solve the problem
        self.iterator = self._solve(self.problem)
        next(self.iterator)
        # create the result object based on the current iteration
        res = self.result()
        return res

    def _solve(self, problem):
        # the termination criteria should be set
        if self.termination is None:
            raise Exception("No termination criterion defined and algorithm has no default termination implemented!")
        # when the termination criterion is not fulfilled
        while self.has_next():
            self.next()
            yield
        yield "Terminate"
        
if __name__ == '__main__':
    # define problems
    algorithms = []
    problems = []
    problem_names = ['zdt1', 'zdt2']
    for p in problem_names:
        problem = get_problem(p)
        problems.append(problem)
        algorithm = NSGA2MultiTask(pop_size=500)
        algorithms.append(algorithm)

    # obtain iterators
    iterators = []
    for problem, algorithm in zip(problems, algorithms):
        minimize(problem, algorithm, termination=('n_gen', 50), copy_algorithm=False)
        iterator = algorithm.iterator
        iterators.append(iterator)

    # perform evolutionary operations iteratively
    while len(iterators) > 0:
        iterator = iterators.pop(0)
        r = next(iterator)
        if r != 'Terminate':
            iterators.append(iterator)

    for i, problem, algorithm in zip(range(0, len(problems)), problems, algorithms):
        res = algorithm.result()
        plot = Scatter(title=problem_names[i])
        plot.add(problem.pareto_front(), plot_type="line", color="black", alpha=0.7)
        plot.add(res.F, color="red")
        plot.show()
