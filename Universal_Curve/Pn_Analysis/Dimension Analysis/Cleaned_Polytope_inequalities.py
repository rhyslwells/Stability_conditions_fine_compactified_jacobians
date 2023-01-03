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

def load(number):
    def Load_P3():
        pickle_in = open("Load_Inputs/Dataframe_P3", "rb")
        df_P3 = pickle.load(pickle_in)
        pickle_in.close()
        return df_P3

    def Load_P4():
        pickle_in = open("Load_Inputs/Dataframe_P4", "rb")
        df_P4 = pickle.load(pickle_in)
        pickle_in.close()
        return df_P4

    def Load_P5():
        pickle_in = open("Load_Inputs/Dataframe_P5", "rb")
        df_P5 = pickle.load(pickle_in)
        pickle_in.close()
        return df_P5

    def Load_P6ExampleFunct():
        pickle_in = open(r"C:\Users\RhysL\Desktop\P6ExampleFunct\Combinatorics2021 - Copy\Clean_Hyperplane_Incon\Load_Inputs\Dataframe_P6ExampleFunct", "rb")
        df_P6ExampleFunct = pickle.load(pickle_in)
        pickle_in.close()
        return df_P6ExampleFunct

    n=number
    if n==3:
       return Load_P3()
    elif n ==4:
     return   Load_P4()
    elif n ==5:
      return  Load_P5()

    elif n==6:
        return Load_P6ExampleFunct()
    
def load_node_only(number):
    def NodeOnly_Load_P3():
        pickle_in = open("Load_Inputs/DF_NodeOnly_subset_P3", "rb")
        df_P3 = pickle.load(pickle_in)
        pickle_in.close()
        return df_P3

    def NodeOnly_Load_P4():
        pickle_in = open("Load_Inputs/DF_NodeOnly_subset_P4", "rb")
        df_P4 = pickle.load(pickle_in)
        pickle_in.close()
        return df_P4

    def NodeOnly_Load_P5():
        pickle_in = open("Load_Inputs/DF_NodeOnly_subset_P5", "rb")
        df_P5 = pickle.load(pickle_in)
        pickle_in.close()
        return df_P5

    def NodeOnly_Load_P6():
        pickle_in = open("Load_Inputs/DF_NodeOnly_subset_P6", "rb")
        df_P6 = pickle.load(pickle_in)
        pickle_in.close()
        return df_P6

    def Break100_NodeOnly_Load_P7():
        pickle_in = open("Load_Inputs/Break100_DF_NodeOnly_subset_P7", "rb")
        df_P7 = pickle.load(pickle_in)
        pickle_in.close()
        return df_P7

    def Break100_NodeOnly_Load_P8():
        pickle_in = open("Load_Inputs/Break100_DF_NodeOnly_subset_P8", "rb")
        df_P8 = pickle.load(pickle_in)
        pickle_in.close()
        return df_P8

    def Break10_NodeOnly_Load_P9():
        pickle_in = open("Load_Inputs/Break10_DF_NodeOnly_subset_P9", "rb")
        df_P9 = pickle.load(pickle_in)
        pickle_in.close()
        return df_P9

    def Break1_NodeOnly_Load_P10():
        pickle_in = open("Load_Inputs/Break_1_DF_NodeOnly_subset_P10", "rb")
        df_P10 = pickle.load(pickle_in)
        pickle_in.close()
        return df_P10

    m=number
    if m==3:
        return NodeOnly_Load_P3()
    elif m==4:
        return NodeOnly_Load_P4()
    elif m == 5:
        return NodeOnly_Load_P5()
    elif m == 6:
        return NodeOnly_Load_P6()
    elif m == 7:
        return Break100_NodeOnly_Load_P7()
    elif m == 8:
        return Break100_NodeOnly_Load_P8()
    elif m == 9:
        return Break10_NodeOnly_Load_P9()
    elif m == 10:
        return Break1_NodeOnly_Load_P10()
def get_formatted_hyperplanes_txt(dataframe): #put into format of sage b<Ax<b+1
    dataframe_list = dataframe.values.tolist()
    df_temp_col_list = dataframe.columns.tolist()
    df_col_list =[ list(x) for x in df_temp_col_list]
    empty_thing=[]#looks like get_formatted_hyperplanes[[[]...[]]...[[]...[]]] , term looks like [[]...[]]
    for i in dataframe_list: #creates row at a time
        l_i= [ [x,] for x in i]

        #Take b<x+y<2
        #looks like [-b,1,1] for x \ge b
        res_lower = [list(itertools.chain(*i))
                     for i in zip(l_i, df_col_list)] # Ax>b #todo need to insert minus for b term. for Ax-b>0
        for j in range(len(res_lower)):
            res_lower[j][0]=-int((res_lower[j][0])) # -b part.

        #look like [b+1,-1,-1] for x+y \le b+1
        res_upper = [list(itertools.chain(*i)) #Ab<b+1 need to arrange into same format as above -Ax+(b+1)>0
                     for i in zip(l_i, df_col_list)]
        for j in range(len(res_upper)):
            res_upper[j]=[ -1*x for x in res_upper[j]]#multpliy all elements by negative to change inequality direction.-Ax
            res_upper[j][0]=(-(res_upper[j][0]))+1 # Todo Possible check for negative position

        res_combined= res_lower +res_upper

        # empty_thing.append(res_combined) #comment below and run to check both inequalities in b<Ax<b+1

        #change format Dont need sage_format..
        formatted_ResCombine=[]
        for item in res_combined:#res_combined = [[]...[]], item = []
            x=[0]*(max(len(l) for l in res_combined)) #finding [0,0,0,0,0] for P_4 ie n+1
            x[0]=item[0]
            for k in range(1,len(item)):
                if item[k]<0:
                    x[-item[k]]=-1 #
                else:
                    x[item[k]]=1
            formatted_ResCombine.append(x)

        empty_thing.append(formatted_ResCombine)
    return empty_thing #a list of the functions P_n

#Standard All cases Sage data
    # n=5 #Recapture Sage data full MSA Pn
    # Loaded_Dataframe= load(n)
    # print(Loaded_Dataframe)
    # Data_all=get_formatted_hyperplanes_txt(Loaded_Dataframe)
    # print(Data_all[0],"\n")

    # sys.stdout = open("ForSageOutputs/Cleaned_Formated_hyperplanes_P5.txt", "w") #CHANGE ME
    # for index,i in enumerate(Data_all):
    #     print(i)
    # sys.stdout.close()

#Standard All cases Sge date: Specific Case for P6ExampleFunct
# n=6 #Recapture Sage data full MSA Pn
# Loaded_Dataframe= load(n)
# print(Loaded_Dataframe)
# Data_all=get_formatted_hyperplanes_txt(Loaded_Dataframe)
# print(Data_all[0],"\n")

# sys.stdout = open(r"C:\Users\RhysL\Desktop\P6ExampleFunct\Combinatorics2021 - Copy\Clean_Hyperplane_Incon\ForSageOutputs\hplanes_P6ExampleFunct.txt", "w") #CHANGE ME
# for index,i in enumerate(Data_all):
#     print(i)
# sys.stdout.close()

#Node only data for sage

    # m=10 # Node only case, and breaks for n strictly more than 6.
    # Loaded_Node_Dataframe= load_node_only(m)
    # Loaded_Node_Dataframe=Loaded_Node_Dataframe.head(100) #slicing first 100 to get output. Otherwise runs too long.
    # print(Loaded_Node_Dataframe)
    # Data_node=get_formatted_hyperplanes_txt(Loaded_Node_Dataframe)
    # print(Data_node[0],"\n")

    # sys.stdout = open("ForSageOutputs/Slice100_Break1_NodeOnlyP10.txt", "w") #break refers to creation of Pn from nodes, slice refers to slice first k terms of df.
    # for index,i in enumerate(Data_node):
    #     # if index ==1000:
    #     #     break
    #     print(i)
    # sys.stdout.close()

