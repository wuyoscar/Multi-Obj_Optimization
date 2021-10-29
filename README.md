
# [Coded Problems](https://en.wikipedia.org/wiki/Test_functions_for_optimization)
  


![Problem_list](Workspace/images/problem_list.png?raw=true "Title")




| Problem | Formula| Constraints|Search Domain|
|---      |----    |----         |----|
|Kursawe| $\text{Minimize=}\begin{cases}f_{1}\left(x\right)={\sum_{i=1}^{2}[-10exp(-0.2\sqrt{x_{i}^{2}+x^2_{i+1}})]} \\f_{2}(x)=\sum_{i=1}^{3}[\|x_i\|^{0.8}+5sin(x_{i}^{3})]\end{cases}$ |None |$-5\leq{}x_{1}\leq{5}$| 
|Binh and Korn function|$\text{Minimize=}\begin{cases}f_{1}\left(x,y\right)=4x^{2}+4y^{2}\\f_{2}\left(x,y\right)=\left(x-5\right)^{2}+\left(y-5\right)^{2}\end{cases}$| $\text{s.t.}=\begin{cases}g_{1}\left(x,y\right)=\left(x-5\right)^{2}+y^{2}\leq 25\\g_{2}\left(x,y\right)=\left(x-8\right)^{2}+\left(y+3\right)^{2}\geq 7.7\end{cases}$|$0\leq{x}\leq5\\0\leq{y}\leq3$|
|OSY|${\text{Minimize}}={\begin{cases}f_{1}\left({\boldsymbol {x}}\right)=-25\left(x_{1}-2\right)^{2}-\left(x_{2}-2\right)^{2}-\left(x_{3}-1\right)^{2}-\left(x_{4}-4\right)^{2}-\left(x_{5}-1\right)^{2}\\f_{2}\left({\boldsymbol {x}}\right)=\sum _{i=1}^{6}x_{i}^{2}\\\end{cases}}$|${\text{s.t.}}={\begin{cases}g_{1}\left({\boldsymbol {x}}\right)=x_{1}+x_{2}-2\geq 0\\g_{2}\left({\boldsymbol {x}}\right)=6-x_{1}-x_{2}\geq 0\\g_{3}\left({\boldsymbol {x}}\right)=2-x_{2}+x_{1}\geq 0\\g_{4}\left({\boldsymbol {x}}\right)=2-x_{1}+3x_{2}\geq 0\\g_{5}\left({\boldsymbol {x}}\right)=4-\left(x_{3}-3\right)^{2}-x_{4}\geq 0\\g_{6}\left({\boldsymbol {x}}\right)=\left(x_{5}-3\right)^{2}+x_{6}-4\geq 0\end{cases}}$|$0\leq{x_1, x_2,x_6}\leq10\\1\leq{x_5,x_3}\leq5\\0\leq{x_4}\leq{6}$|
|Chankong and Haimes function| ${\text{Minimize}}={\begin{cases}f_{1}\left(x,y\right)=2+\left(x-2\right)^{2}+\left(y-1\right)^{2}\\f_{2}\left(x,y\right)=9x-\left(y-1\right)^{2}\\\end{cases}}$| ${\text{s.t.}}={\begin{cases}g_{1}\left(x,y\right)=x^{2}+y^{2}\leq 225\\g_{2}\left(x,y\right)=x-3y+10\leq 0\\\end{cases}}$|$-20\leq{x,y}\leq20$ |
|ZDT1|${\text{Minimize}}={\begin{cases}f_{1}\left(x\right)=x_1\\h(f_1, g)= 1-\sqrt{f1/g} \\\end{cases}} \text{   where}, g(x) = 1+ \frac{9}{n-1}\sum_{i=2}^{n}x_i$|None|$0\leq{x_i}\leq{1}, i=2, ...n$|
|ZDT2|${\text{Minimize}}={\begin{cases}f_{1}\left(x\right)=x_1\\h(f_1, g)= 1-(f1/g)^2 \\\end{cases}} \text{  where}, g(x) = 1+ \frac{9}{n-1}\sum_{i=2}^{n}x_i$|None|$0\leq{x_i}\leq{1}, i=2, ...n$|
|ZDT3|${\text{Minimize}}={\begin{cases}f_{1}\left(x\right)=x_1\\h(f_1, g)= 1-\sqrt{f1/g}-(f_1/g)sin(10\pi f_1) \\\end{cases}} \text{   where}, g(x) = 1+ \frac{9}{n-1}\sum_{i=2}^{n}x_i$|None|$0\leq{x_i}\leq{1}, i=2, ...n$|
|ZDT4|${\text{Minimize}}={\begin{cases}f_{1}\left(x\right)=x_1\\h(f_1, g)= 1-\sqrt{f1/g} \\\end{cases}} \text{   where,} g(x) = 1+ 10(n-1)\sum_{i=2}^{n}(x_i^2-10cos(4\pi x_i))$|None|$0\leq{x_i}\leq{1}, i=2, ...n$|
|ZDT5|${\text{Minimize}}={\begin{cases}f_{1}\left(x\right)=x_1\\h(f_1, g)= 1-\sqrt{f1/g} \\\end{cases}} \text{   where}, g(x) = 1+ \frac{9}{n-1}\sum_{i=2}^{n}x_i$|None|$0\leq{x_i}\leq{1}, i=2, ...n$|
|VU1|${\text{Minimize}}={\begin{cases}f_{1}\left(x_1, x_2\right)=\frac{1}{x^2_1+x^2_2+1}\\f_{2}\left(x_1, x_2\right)={x^2_1+3x^2_2+1}\end{cases}}$|None|$-3\leq{x_1,x_2}\leq3$ |
|VU2|${\text{Minimize}}={\begin{cases}f_{1}\left(x_1, x_2\right)=x_1+x_2+1\\f_{2}\left(x_1, x_2\right)={x^2_1+2x^2_2-1}\end{cases}}$|None|$-3\leq{x_1,x_2}\leq3$  |
|SK1 |${\text{Maximum}}={\begin{cases}f_{1}\left(x\right)=-x^4-3x^3+10x^2+10x+10\\f_{2}\left(x\right)={-0.5x^4+2x^3+10x^2-10x+5}\end{cases}}$|None|$?$|
|SK2 |${\text{Maximum}}={\begin{cases}f_{1}\left(x\right)=-(x_1-2)^2-(x_2+3)^2-(x_3-5)^2-(x_4-4)^2+5\\f_{2}\left(x\right)={\frac{sinx_1+sinx_2+sinx_3+sinx_4}{1+(x_1^2+x_2^2+x_3^2+x_4^2)/100}}\end{cases}}$|None|$?$|
|Kur1|${\text{Minimize}}={\begin{cases}f_{1}\left(x_1,x_2,....,x_n\right)=\sum_{i=1}^{n-1}-10exp^{-0.2}\sqrt{x^2_{i}+x^2_{i+1}}\\f_{2}\left(x_1,x_2,....,x_n\right)=\sum^{n}_{i=1}\|x_i\|^{0.8}+5sin^3x_i\\\end{cases}}$|None|$?$|
|TKLY1|${\text{Minimum}}={\begin{cases}f_{1}\left(x_1\right)=x_1\\f_{2}\left(x_1,x_2,x_3,x_4\right)={\frac{1}{x_i}\Pi_{i=2}^{4}[2.0-exp(-(\frac{x_i-0.1}{0.004})^2)-0.8exp(-(\frac{x_i-0.9}{0.4})^2)]}\end{cases}}$|None|$0.1\leq{x_1}\leq1\\0\leq{x_2,x_3,x_4}\leq1$ |
|LTDZ1 |${\text{Maximum}}={\begin{cases}f_{1}\left(x_1,x_2,x_3\right)=3-(1+x_3)cos(x_1\pi/2)cos(x_2\pi/2)\\f_{2}\left(x_1,x_2,x_3\right)=3-(1+x_3)cos(x_1\pi/2)sin(x_2\pi/2)\\f_{3}\left(x_1,x_3\right)=3-(1+x_3)sin(x_1\pi/2)\end{cases}}$||$0\leq{x_1,x_2,x_3}\leq1$|


