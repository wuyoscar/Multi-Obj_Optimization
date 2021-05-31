# MOOP

----

## *Script-main folder*

----
### [problems](https://en.wikipedia.org/wiki/Test_functions_for_optimization)
  1. Call the problems from **problems**
  
   - Available problems:
      - [binh_and_korn](https://en.wikipedia.org/wiki/File:Binh_and_Korn_function.pdf)
      - [test](https://en.wikipedia.org/wiki/File:Test_function_4_-_Binh.pdf)
      - [constr_ex](https://en.wikipedia.org/wiki/File:Constr-Ex_problem.pdf)
      - [changkong_and_haimes](https://en.wikipedia.org/wiki/File:Chakong_and_Haimes_function.pdf)
  
   
```
from problems imnport binh_and_korn 
problem = binh_and_korn()
```
  2. Call the filter_input from **problems**

   - Filtering the feasible input and infeasible input; feasible objective value as well
```
from problem import sp
feasible_X, infeasible_X, feasible_F,infeasible_F,feasible_G,infeasible_G =  filter_input(problem, X = input)
```

  3. call visaul_algorithmns from **problems**
```
#feasible_F produced after applying algorithmns
#feasible_F_old produced by random picked
from problems import visaul_algorithmns
visaul_algorithmns(feasible_F,feasible_F_old,'algorithms_name')

```
----
### Algorithmns
