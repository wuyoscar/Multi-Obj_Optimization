from pymoo.indicators.hv import Hypervolume
import os, sys,argparse,time,csv,uuid
import numpy as np 
import pandas as pd 
from datetime import datetime
currentdir = os.getcwd()
file_path = os.path.join(currentdir, 'Jobs_record')

parser = argparse.ArgumentParser(description='''This programming is to calculate hypervolumn, default input file is Jobs_record''')
parser.add_argument('-f', '--fpath', default= file_path,type = str, required=True)
parser.add_argument('-ref_p','--reference_point', type=float, help= "this is reference point values")
args = parser.parse_args()


ref_value = args.reference_point
file_path = args.fpath
result = pd.read_csv(file_path)

def calculate_hv(result =result ):
    path = result['path']
    F = np.loadtxt(path)

    ref_dir = np.ones(F.shape[1])*ref_value
    metric = Hypervolume(nds=True,ref_point = ref_dir,norm_ref_point=False)
    start_time = time.time()
    hv = metric.do(F)
    exc_time = time.time() - start_time
    return [hv,exc_time,ref_dir]

get = result.apply(calculate_hv, axis=1)

df = pd.DataFrame(get.tolist(), columns = ['hv','hv_exc_time','hv_ref'])

final_result = pd.concat([result, df],axis=1)

output_result = final_result[['Problem', 'Alg_name', 'Iteration', 'Objectives', 'n_variables',
    'exec_time', 'solutions', 'hv',
    'hv_exc_time', 'hv_ref', 
    'lower_bound', 'upper_bound','path']]

date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")

output_result.to_csv(f'result_{date}')







