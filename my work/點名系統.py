# coding: utf-8
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from ipywidgets import interact_manual
l=["大雄","小夫","靜香","小杉","胖虎"]    
def f(x):
    x=np.random.choice(l)
    print("今天抽到的同學是:{}".format(x))
interact_manual(f,x="以下是今天點到的同學")
from ipywidgets import interact
