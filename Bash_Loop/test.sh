#! /bin/bash
for p in $(cat problem_txt/two_var_problems.txt)
do for s in 50 
do for n_eval in  3000 5000 
do for lb in {-3..1}
do for ub in {1..4}
do
echo "jobs/$p-2-[$lb-$ub]-$s-$n_eval".sh


echo -f "$p_2_$lb_$ub_$n_eval_$s" 


done
done
done
done 
done


