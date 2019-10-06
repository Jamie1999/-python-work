# coding: utf-8
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy.random import randint
#以後就不用打np.random.randint
words='''
我
我的
妳
妳的
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
吹過
思念
靈魂
停止'''
#三個引號是可以使這些字分行
from numpy.random import choice
n=randint(3,6)#行數

for i in range(n):
    k=randint(5,8)#字數
    egg=choice(phrase,k)#從phrase中篩選
    ham=' '.join(egg)#用空白隔開
    print(ham)
