
# [Coded Problems](https://en.wikipedia.org/wiki/Test_functions_for_optimization)
  



<!-- $
\text{s.t.=}
\begin{cases}
g_{1}\left(x,y,z\right)={x-3+y^2+z}\leq0\\
g_{2}\left(x,y,z\right)={y^2+z-x^4}\leq5\\
g_{3}\left(x,y,z\right)={z^3+\frac{y^2}{2}}\leq0\\
\end{cases}
$ --> 



| Probelm | Function | Constarints | 
| --- | --- | ---| 
|p1| <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/9aa4f87d1b4fc51d737a1b704b439c21524880b3" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:45.023ex; height:6.176ex;">  |   <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/dcf4d0ed143bf25faa633f16bb8b7e12b9c46456" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.671ex; width:44.813ex; height:6.509ex;">| 
|p2 | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/02e80c4945529ec09f3af1a6ad50316fc3432958" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.671ex; width:49.026ex; height:6.509ex;" alt="{\displaystyle {\text{Minimize}}={\begin{cases}f_{1}\left(x,y\right)=2+\left(x-2\right)^{2}+\left(y-1\right)^{2}\\f_{2}\left(x,y\right)=9x-\left(y-1\right)^{2}\\\end{cases}}}"> |<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/b58aa032dc58ef5662d175fba627d111aed9e088" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:35.599ex; height:6.176ex;" alt="{\displaystyle {\text{s.t.}}={\begin{cases}g_{1}\left(x,y\right)=x^{2}+y^{2}\leq 225\\g_{2}\left(x,y\right)=x-3y+10\leq 0\\\end{cases}}}">|
|p3|<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/9c96e6f33f22f37f529ffe93914807349fa3b282" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:40.073ex; height:6.176ex;" alt="{\displaystyle {\text{Minimize}}={\begin{cases}f_{1}\left(x,y\right)=x^{2}-y\\f_{2}\left(x,y\right)=-0.5x-y-1\\\end{cases}}}">|<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/291ff07f4dc4fd50cca9e599d67250438681663f" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -3.756ex; margin-bottom: -0.248ex; width:38.378ex; height:9.176ex;" alt="{\displaystyle {\text{s.t.}}={\begin{cases}g_{1}\left(x,y\right)=6.5-{\frac {x}{6}}-y\geq 0\\g_{2}\left(x,y\right)=7.5-0.5x-y\geq 0\\g_{3}\left(x,y\right)=30-5x-y\geq 0\\\end{cases}}}">|
|p4|<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/1b323f84528593a2e74aedde4d0feded35ff7355" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -3.171ex; width:45.34ex; height:7.509ex;" alt="{\displaystyle {\text{Minimize}}={\begin{cases}f_{1}\left(x,y\right)=x\\f_{2}\left(x,y\right)=\left(1+y\right)\exp \left(-{\frac {x}{1+y}}\right)\end{cases}}}">|<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/3eacb31aceceeeca8d22d7d9d580ec42eea0c5c9" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -4.171ex; width:43.183ex; height:9.509ex;" alt="{\displaystyle {\text{s.t.}}={\begin{cases}g_{1}\left(x,y\right)={\frac {f_{2}\left(x,y\right)}{0.858\exp \left(-0.541f_{1}\left(x,y\right)\right)}}\geq 1\\g_{2}\left(x,y\right)={\frac {f_{2}\left(x,y\right)}{0.728\exp \left(-0.295f_{1}\left(x,y\right)\right)}}\geq 1\end{cases}}}">|
|p5|<img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Ctext%7BMinimize%3D%7D%0A%5Cbegin%7Bcases%7D%0Af_%7B1%7D%5Cleft(x%2Cy%2Cz%5Cright)%3D%7Bx%5E3%2By%2Bz%7D%5C%5C%0Af_%7B2%7D%5Cleft(x%2Cy%2Cz%5Cright)%3D%7B%5Cfrac%7Bx%5E2-y%7D%7B4%7D%2B5z%7D%5C%5C%0Af_%7B3%7D%5Cleft(x%2Cy%2Cz%5Cright)%3D%7B9%2B%5Cleft(x%2By%5Cright)%5E2%2B%5Cleft(y-z%5Cright)%5E2%7D%5C%5C%0A%5Cend%7Bcases%7D">|<img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Ctext%7Bs.t.%3D%7D%0A%5Cbegin%7Bcases%7D%0Ag_%7B1%7D%5Cleft(x%2Cy%2Cz%5Cright)%3D%7Bx-3%2By%5E2%2Bz%7D%5Cleq0%5C%5C%0Ag_%7B2%7D%5Cleft(x%2Cy%2Cz%5Cright)%3D%7By%5E2%2Bz-x%5E4%7D%5Cleq5%5C%5C%0Ag_%7B3%7D%5Cleft(x%2Cy%2Cz%5Cright)%3D%7Bz%5E3%2B%5Cfrac%7By%5E2%7D%7B2%7D%7D%5Cleq0%5C%5C%0A%5Cend%7Bcases%7D">|
|p6|<img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Ctext%7BMinimize%3D%7D%0A%5Cbegin%7Bcases%7D%0Af_%7B1%7D%5Cleft(x%2Cy%5Cright)%3D%7B%5Cleft(x-2%5Cright)%5E2%2B%5Cleft(y-1%5Cright)%5E2%2B2%7D%5C%5C%0Af_%7B2%7D%5Cleft(x%2Cy%5Cright)%20%3D%209x-%5Cleft(y-1%5Cright)%5E2%20%5C%5C%0A%5Cend%7Bcases%7D">|<img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Ctext%7Bs.t.%3D%7D%0A%5Cbegin%7Bcases%7D%0Ag_%7B1%7D%5Cleft(x%2Cy%2Cz%5Cright)%3D%7Bx%5E2%2By%5E2-255%7D%5Cleq0%5C%5C%0Ag_%7B2%7D%5Cleft(x%2Cy%2Cz%5Cright)%3D%7Bx-3y%2B10%7D%5Cleq0%5C%5C%0A%5Cend%7Bcases%7D">|


---
# Problem from Pacages 
| Probelm | Function  | Variables | Objectives | Description|
| --- | --- | ---|---|--- |
|   BNH   |<img style="transform: translateY(0.1em); background: white;" src="Problems/images/bnh.jpg"  width="400" height="130"/> |   2  |  2  | 2 | 
|   OSY   |  <img src="Problems/images/osy.png"  width="400" height="130"/> |   6  | 2   |6 |
|   TNK    | <img src="Problems/images/tnk.png"  width="400" height="130"/> |  2   | 2   |2 |
|   ZDT1   | <img src="Problems/images/zdt1.png"  width="400" height="130"/> | 30    |  2  | |
|   ZDT2   | <img src="Problems/images/zdt2.png"  width="400" height="130"/> | 30    |  2 | |
|   ZDT3   | <img src="Problems/images/zdt3.png"  width="400" height="130"/> | 30    |  2| |
|   ZDT4   | <img src="Problems/images/zdt4.png"  width="400" height="130"/> | 10    |  2  | |
|   ZDT5   | <img src="Problems/images/zdt5.png"  width="400" height="130"/> | 80    |  2  | |
|   ZDT6   | <img src="Problems/images/zdt6.png"  width="400" height="130"/> | 10    |  2  | |



----



<!-- $
\text{s.t.=}
\begin{cases}
g_{1}\left(x,y,z\right)={x^2+y^2-255}\leq0\\
g_{2}\left(x,y,z\right)={x-3y+10}\leq0\\
\end{cases}
$ -->



<!-- $
\text{s.t.=}
\begin{cases}
g_{1}\left(x,y\right)={x^2+y^2-225} \le0\\
g_{2}\left(x,y\right) = x-3y+10\le0\\
-20\le x \le20\\
-20\le y \le20
\end{cases}

$ --> 

## Testing problem


```bash

$ python NSGA-II.py -p p4 -lb 1 2 -ub  6 6 -s 600 -f NSGA-II_p3_lb_1_2_ub_6_6_s_400 -eval 800


output>>>
***********
probelm is :
# name: p4
# n_var: 2
# n_obj: 2
# n_constr: 2



********************
According input, design variable bound is as below
[[1. 6.]
 [2. 6.]]


from bound give above, generating  data points (600, 2) successfully

********************

------problem evaluation-----
600 is feasible and 0 is infeasible among 600 data points


---------
feasible_X path is:  /Users/wuyoscar/Desktop/MOOP/Result/NSGA-II_p3_lb_1_2_ub_6_6_s_400feasible_X.txt
------------
infeasible_X path is:  /Users/wuyoscar/Desktop/MOOP/Result/NSGA-II_p3_lb_1_2_ub_6_6_s_400infeasible_X.txt
------------
feasible_F path is:  /Users/wuyoscar/Desktop/MOOP/Result/NSGA-II_p3_lb_1_2_ub_6_6_s_400feasible_F.txt
------------
infeasible_F path is:  /Users/wuyoscar/Desktop/MOOP/Result/NSGA-II_p3_lb_1_2_ub_6_6_s_400infeasible_F.txt
=====================================================================================
n_gen |  n_eval |   cv (min)   |   cv (avg)   |  n_nds  |     eps      |  indicator  
=====================================================================================
    1 |     100 |  0.00000E+00 |  0.00000E+00 |      10 |            - |            -
    2 |     200 |  0.00000E+00 |  0.00000E+00 |      14 |  0.062171519 |        ideal
    3 |     300 |  0.00000E+00 |  0.00000E+00 |      21 |  0.069999124 |        ideal
    4 |     400 |  0.00000E+00 |  0.00000E+00 |      33 |  0.014889819 |            f
    5 |     500 |  0.00000E+00 |  0.00000E+00 |      44 |  0.169329240 |        nadir
    6 |     600 |  0.00000E+00 |  0.00000E+00 |      59 |  0.009545153 |            f
    7 |     700 |  0.00000E+00 |  0.00000E+00 |      77 |  0.498303345 |        nadir
    8 |     800 |  0.00000E+00 |  0.00000E+00 |      99 |  0.006696543 |        ideal

Time elapsed for solving problem:  0.05109810829162598  seconds
```

