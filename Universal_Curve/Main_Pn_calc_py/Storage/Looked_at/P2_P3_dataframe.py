import scipy
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import csv
import time
import sys
import pickle
import itertools


fun2_1={(1,):0,(2,):0,(1,2):0}
fun2_2={(1,):0,(2,):0,(1,2):1}

l_df_P2= [fun2_1,fun2_2]
df_P2=pd.DataFrame(l_df_P2)
print(df_P2)

pickle_out = open("../Hyperplane_inconsistency/Ordered_P_2", "wb")
pickle.dump(df_P2, pickle_out)
pickle_out.close()

fun3_1= {(1,):0,(2,):0,(3,):0, (1,2):0, (1,3):0, (2,3):0, (1,2,3):0}
fun3_2= {(1,):0,(2,):0,(3,):0,(1,2):0, (1,3):0, (2,3):0, (1,2,3):1}
fun3_3= {(1,):0,(2,):0,(3,):0,(1,2):1, (1,3):0, (2,3):0, (1,2,3):1}
fun3_4= {(1,):0,(2,):0,(3,):0,(1,2):0, (1,3):1, (2,3):0, (1,2,3):1}
fun3_5= {(1,):0,(2,):0,(3,):0,(1,2):0, (1,3):0, (2,3):1, (1,2,3):1}
fun3_6= {(1,):0,(2,):0,(3,):0,(1,2):1, (1,3):1, (2,3):0, (1,2,3):1}
fun3_7= {(1,):0,(2,):0,(3,):0,(1,2):0, (1,3):1, (2,3):1, (1,2,3):1}
fun3_8= {(1,):0,(2,):0,(3,):0,(1,2):1, (1,3):0, (2,3):1, (1,2,3):1}
fun3_9= {(1,):0,(2,):0,(3,):0,(1,2):1, (1,3):1, (2,3):1, (1,2,3):1}
fun3_10= {(1,):0,(2,):0,(3,):0,(1,2):1, (1,3):1, (2,3):1, (1,2,3):2}

l_df_P3=[fun3_1,fun3_2,fun3_3,fun3_4,fun3_5,fun3_6,fun3_7,fun3_8,fun3_9,fun3_10]
df_P3=pd.DataFrame(l_df_P3)
# print(df_P3)
pickle_out = open("../Hyperplane_inconsistency/Ordered_P_3", "wb")
pickle.dump(df_P3, pickle_out)
pickle_out.close()
