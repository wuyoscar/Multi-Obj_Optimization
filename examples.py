from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination
from pymoo.factory import get_problem
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
from pymoo.util.termination.default import MultiObjectiveDefaultTermination
from pymoo.factory import get_performance_indicator
from matplotlib import pyplot as plt 
import numpy as np
import time
import sys
from tqdm import tqdm
import os 



#get problem
p = get_problem('ZDT1')


#pareto front
pf = p.pareto_front()

loss = []

#a set of generations
n= np.linspace(100,2000,15)

for i in tqdm(n):
    
    #NSGA algorithms
    algorithm = NSGA2(
        n_offspring = 20,
        crossover=get_crossover("real_sbx", prob=0.9, eta=15),
        mutation=get_mutation("real_pm", eta=20),
        eliminate_duplicates=True    
    )


    termination = get_termination("n_eval", i) #! change #generation each time
    start = time.time()
    res = minimize(p,
                algorithm,
                termination = termination,
                seed=1,
                save_history=True,
                verbose=False)
                
    # The result found by an algorithm
    A = res.F
    #
    gd = get_performance_indicator("igd",pf )

    #performace indicator 
    print('IGD+ is',gd.calc(res.F))
    print('# generation is',i)
    print('\n')
    loss.append(gd.calc(res.F))

    end_time = time.time() - start


label = str(n[-1])

plt.subplot(1,2,1)

plt.plot(n, loss)
plt.ylabel('loss')
plt.xlabel('#generations')
plt.title('#_gens $vs$ loss')

plt.subplot(1,2,2)
plt.scatter(pf[:,0],pf[:,1],label='pareto_front')
plt.scatter(A[:,0],A[:,1],label='algorithms')
plt.title('When #gens is equal ' + str(n[-1]))

plt.legend()
plt.show()


print('Time elapsed for solving problem: ', end_time,' seconds\n')
#print('Solution',np.array(res.X), 'Obj_value',np.array(res.F), 'CV',np.array(res.CV))
#print("GD", loss)


# plot the result
#Scatter(legend=True,title = '#generation '+str(n[-1])).add(pf, label="Pareto-front").add(A, label="Result").show()