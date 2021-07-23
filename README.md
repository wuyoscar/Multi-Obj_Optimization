# MOOP





----
# [Problems](https://en.wikipedia.org/wiki/Test_functions_for_optimization)
  



| Probelm | Function | Constarints | 
| --- | --- | ---| 
| Binh and Korn function | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/9aa4f87d1b4fc51d737a1b704b439c21524880b3" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:45.023ex; height:6.176ex;">  |   <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/dcf4d0ed143bf25faa633f16bb8b7e12b9c46456" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.671ex; width:44.813ex; height:6.509ex;">| 
| Chankong and Haimes function | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/02e80c4945529ec09f3af1a6ad50316fc3432958" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.671ex; width:49.026ex; height:6.509ex;" alt="{\displaystyle {\text{Minimize}}={\begin{cases}f_{1}\left(x,y\right)=2+\left(x-2\right)^{2}+\left(y-1\right)^{2}\\f_{2}\left(x,y\right)=9x-\left(y-1\right)^{2}\\\end{cases}}}"> |<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/b58aa032dc58ef5662d175fba627d111aed9e088" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:35.599ex; height:6.176ex;" alt="{\displaystyle {\text{s.t.}}={\begin{cases}g_{1}\left(x,y\right)=x^{2}+y^{2}\leq 225\\g_{2}\left(x,y\right)=x-3y+10\leq 0\\\end{cases}}}">|
|Test function|<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/3113203c5d455e0e1e6397d57094e80e527b34ba" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -5.505ex; width:54.238ex; height:12.176ex;" alt="{\displaystyle {\text{Minimize}}={\begin{cases}f_{1}\left({\boldsymbol {x}}\right)=1-\exp \left[-\sum _{i=1}^{n}\left(x_{i}-{\frac {1}{\sqrt {n}}}\right)^{2}\right]\\f_{2}\left({\boldsymbol {x}}\right)=1-\exp \left[-\sum _{i=1}^{n}\left(x_{i}+{\frac {1}{\sqrt {n}}}\right)^{2}\right]\\\end{cases}}}">|<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/291ff07f4dc4fd50cca9e599d67250438681663f" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -3.756ex; margin-bottom: -0.248ex; width:38.378ex; height:9.176ex;" alt="{\displaystyle {\text{s.t.}}={\begin{cases}g_{1}\left(x,y\right)=6.5-{\frac {x}{6}}-y\geq 0\\g_{2}\left(x,y\right)=7.5-0.5x-y\geq 0\\g_{3}\left(x,y\right)=30-5x-y\geq 0\\\end{cases}}}">|
|Osyczka and Kundu function|<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/1b323f84528593a2e74aedde4d0feded35ff7355" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -3.171ex; width:45.34ex; height:7.509ex;" alt="{\displaystyle {\text{Minimize}}={\begin{cases}f_{1}\left(x,y\right)=x\\f_{2}\left(x,y\right)=\left(1+y\right)\exp \left(-{\frac {x}{1+y}}\right)\end{cases}}}">|<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/3eacb31aceceeeca8d22d7d9d580ec42eea0c5c9" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -4.171ex; width:43.183ex; height:9.509ex;" alt="{\displaystyle {\text{s.t.}}={\begin{cases}g_{1}\left(x,y\right)={\frac {f_{2}\left(x,y\right)}{0.858\exp \left(-0.541f_{1}\left(x,y\right)\right)}}\geq 1\\g_{2}\left(x,y\right)={\frac {f_{2}\left(x,y\right)}{0.728\exp \left(-0.295f_{1}\left(x,y\right)\right)}}\geq 1\end{cases}}}">|
｜Problem_1｜｜
｜Problem_2｜｜
｜Problem_3｜｜
｜Problem_4｜｜
｜Problem_5｜｜

----



### Click here to use [Problems files](https://github.com/wuyoscar/MOOP/tree/master/Loop%20files/problems)
   - Can be used for random searching, and will generate result files, including:
      1. search_domain_feasible_X.txt, 
      2. search_domain_infeasible_X.txt, 
      3. search_domain_feasible_F.txt, 
      4. search_domain_infeasible_F.txt

   - **Options**: The number of data points (code line 73)and search domain can be defined by user (code line 69), default: random searching

----
### Algorithmns





```
updating........
```

## [Example.pdf](https://github.com/wuyoscar/MOOP/blob/master/examples.ipynb)
<img src="others/images/example_fig.jpg">

