# MOOP

----

## *Script-main folder*


### problems_files
  1. Call the problems from **problems_files**
  
   - Available problems:
      - [binh_and_korn](https://en.wikipedia.org/wiki/File:Binh_and_Korn_function.pdf)
      - [test](https://en.wikipedia.org/wiki/File:Test_function_4_-_Binh.pdf)
      - [constr_ex](https://en.wikipedia.org/wiki/File:Constr-Ex_problem.pdf)
      - [Changkong_and_haimes](https://en.wikipedia.org/wiki/File:Chakong_and_Haimes_function.pdf)
  
   
```
from problems_files imnport binh_and_korn 
problem = binh_and_korn()
```
  2. Call the filter_input from **problems_files**

   - Filtering the feasible input and infeasible input; feasible objective value as well
```
from problem_files import filter_input
feasible_X, infeasible_X, feasible_F,infeasible_F,feasible_G,infeasible_G =  filter_input(problem, X = input)
```
---
### Algorithmns
