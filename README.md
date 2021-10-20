
# [Coded Problems](https://en.wikipedia.org/wiki/Test_functions_for_optimization)
  







| Problem | Formula| Constraints|Search Domain|
|---      |----    |----         |----|
|Kursawe| $\text{Minimize=}\begin{cases}f_{1}\left(x\right)={\sum_{i=1}^{2}[-10exp(-0.2\sqrt{x_{i}^{2}+x^2_{i+1}})]} \\f_{2}(x)=\sum_{i=1}^{3}[\|x_i\|^{0.8}+5sin(x_{i}^{3})]\end{cases}$ |None |$-5\leq{}x_{1}\leq{5}$| 
|Binh and Korn function|$\text{Minimize=}\begin{cases}f_{1}\left(x,y\right)=4x^{2}+4y^{2}\\f_{2}\left(x,y\right)=\left(x-5\right)^{2}+\left(y-5\right)^{2}\end{cases}$| $\text{s.t.}=\begin{cases}g_{1}\left(x,y\right)=\left(x-5\right)^{2}+y^{2}\leq 25\\g_{2}\left(x,y\right)=\left(x-8\right)^{2}+\left(y+3\right)^{2}\geq 7.7\end{cases}$|$0\leq{x}\leq5\\0\leq{y}\leq3$|
|OSY|${\text{Minimize}}={\begin{cases}f_{1}\left({\boldsymbol {x}}\right)=-25\left(x_{1}-2\right)^{2}-\left(x_{2}-2\right)^{2}-\left(x_{3}-1\right)^{2}-\left(x_{4}-4\right)^{2}-\left(x_{5}-1\right)^{2}\\f_{2}\left({\boldsymbol {x}}\right)=\sum _{i=1}^{6}x_{i}^{2}\\\end{cases}}$|${\text{s.t.}}={\begin{cases}g_{1}\left({\boldsymbol {x}}\right)=x_{1}+x_{2}-2\geq 0\\g_{2}\left({\boldsymbol {x}}\right)=6-x_{1}-x_{2}\geq 0\\g_{3}\left({\boldsymbol {x}}\right)=2-x_{2}+x_{1}\geq 0\\g_{4}\left({\boldsymbol {x}}\right)=2-x_{1}+3x_{2}\geq 0\\g_{5}\left({\boldsymbol {x}}\right)=4-\left(x_{3}-3\right)^{2}-x_{4}\geq 0\\g_{6}\left({\boldsymbol {x}}\right)=\left(x_{5}-3\right)^{2}+x_{6}-4\geq 0\end{cases}}$|$0\leq{x_1, x_2,x_6}\leq10\\1\leq{x_5,x_3}\leq5\\0\leq{x_4}\leq{6}$|
|Chankong and Haimes function| ${\text{Minimize}}={\begin{cases}f_{1}\left(x,y\right)=2+\left(x-2\right)^{2}+\left(y-1\right)^{2}\\f_{2}\left(x,y\right)=9x-\left(y-1\right)^{2}\\\end{cases}}$| ${\text{s.t.}}={\begin{cases}g_{1}\left(x,y\right)=x^{2}+y^{2}\leq 225\\g_{2}\left(x,y\right)=x-3y+10\leq 0\\\end{cases}}$|$-20\leq{x,y}\leq20$ |
|Kur1|${\text{Minimize}}={\begin{cases}f_{1}\left(x_1,x_2,....,x_n\right)=\sum_{i=1}^{n-1}-10exp^{-0.2}\sqrt{x^2_{i}+x^2_{i+1}}\\f_{2}\left(x_1,x_2,....,x_n\right)=\sum^{n}_{i=1}\|x_i\|^{0.8}+5sin^3x_i\\\end{cases}}$|None|None|
|ZDT1|${\text{Minimize}}={\begin{cases}f_{1}\left(x\right)=x_1\\h(f_1, g)= 1-\sqrt{f1/g} \\\end{cases}} \text{where}, g(x) = 1+ \frac{9}{n-1}\sum_{i=2}^{n}x_i$|None|$0\leq{x_i}\leq{1}, i=2, ...n$|
|ZDT2|${\text{Minimize}}={\begin{cases}f_{1}\left(x\right)=x_1\\h(f_1, g)= 1-\sqrt{f1/g} \\\end{cases}} \text{where}, g(x) = 1+ \frac{9}{n-1}\sum_{i=2}^{n}x_i$|None|$0\leq{x_i}\leq{1}, i=2, ...n$|
|ZDT3|${\text{Minimize}}={\begin{cases}f_{1}\left(x\right)=x_1\\h(f_1, g)= 1-\sqrt{f1/g} \\\end{cases}} \text{where}, g(x) = 1+ \frac{9}{n-1}\sum_{i=2}^{n}x_i$|None|$0\leq{x_i}\leq{1}, i=2, ...n$|
|ZDT4|${\text{Minimize}}={\begin{cases}f_{1}\left(x\right)=x_1\\h(f_1, g)= 1-\sqrt{f1/g} \\\end{cases}} \text{where}, g(x) = 1+ \frac{9}{n-1}\sum_{i=2}^{n}x_i$|None|$0\leq{x_i}\leq{1}, i=2, ...n$|
|ZDT5|${\text{Minimize}}={\begin{cases}f_{1}\left(x\right)=x_1\\h(f_1, g)= 1-\sqrt{f1/g} \\\end{cases}} \text{where}, g(x) = 1+ \frac{9}{n-1}\sum_{i=2}^{n}x_i$|None|$0\leq{x_i}\leq{1}, i=2, ...n$|


