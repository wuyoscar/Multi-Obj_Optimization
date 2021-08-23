from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination
from pymoo.optimize import minimize
from pymoo.util.termination.default import MultiObjectiveDefaultTermination
from pymoo.factory import get_performance_indicator
import numpy as np
import time
import sys
import os 
import argparse

module_path = os.getcwd()+'/Problems/'
sys.path.append(module_path)
from Problems.Define_Problems import *  

p = Carside()
print(p)