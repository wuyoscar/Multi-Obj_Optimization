from problems_files import binh_and_korn, test, constr_ex, changkong_and_haimes,filter_input
import numpy as np


binh_and_korn = binh_and_korn()
test = test()
constr_ex = constr_ex()
changkong_and_haimes = changkong_and_haimes

#print(binh_and_korn)
#print(test)
#print(constr_ex)
#print(Changkong_and_haimes)





rng = np.random.default_rng(seed=22)
x = 11*rng.random((20000,1))-7 #[0,5]
y = 11*rng.random((20000,1))-7  #[0,3]
X = np.concatenate([x,y],axis=1)


feasible_X, infeasible_X, feasible_F,infeasible_F,feasible_G,infeasible_G = filter_input(problem = test, X=X)

from matplotlib import pyplot as plt
number_of_input = X.shape[0]
number_of_feasible = feasible_X.shape[0]
number_of_infeasible = infeasible_X.shape[0]

figure, ax = plt.subplots(1,2)
#figure for feasible input
ax[0].scatter(feasible_F[:,0],feasible_F[:,1], alpha=0.03, color = 'blue', edgecolor= 'black') #alpha change color tranparent
ax[0].set_xlabel("$minf(1)$")
ax[0].set_ylabel("$minf(2)$")
ax[0].set_title('{} feasible input out of {}'.format(number_of_feasible, number_of_input))

#figure for infeasible input
ax[1].scatter(infeasible_F[:,0], infeasible_F[:,1],alpha=0.2)
ax[1].set_xlabel("$minf(1)$")
ax[1].set_ylabel("$minf(2)$")
ax[1].set_title('{} infeasible input out of {}'.format(number_of_infeasible, number_of_input))
plt.show()


