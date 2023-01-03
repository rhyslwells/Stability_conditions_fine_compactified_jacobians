#Remember to change the output file! & Preamble.
import scipy
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import csv
import time
import sys
import pickle

start_time = time.time() #checks run time.

#Main goal:
#To extend the functions in the P_n case to the P_n+1 case and output an dataframe.Construct a list of dictionaries for Pn+1.
#To move from \tildeP_n function to a \tildeP_n+1 we need to add new single {key:value} pairs for each element in Pn_1 not in P_n.

#Todo: Need to load in \tilde P_n, P_4,P_5,P_6...
def get_tilde_P2():
    fun2_1 = {(1,): 0, (2,): 0, (1, 2): 0}
    fun2_2 = {(1,): 0, (2,): 0, (1, 2): 1}
    P_2 = [fun2_1, fun2_2]
    return P_2
def get_tilde_P3():
    pickle_in = open("List_P3", "rb")
    P_3 = pickle.load(pickle_in)
    pickle_in.close()
    return P_3

def get_tilde_P4():
    pickle_in = open("List_P4", "rb")
    P_4 = pickle.load(pickle_in)
    pickle_in.close()
    return P_4
def get_tilde_P5():
    pickle_in = open("List_P5", "rb")
    P_5 = pickle.load(pickle_in)
    pickle_in.close()
    return P_5
def get_tilde_P6():
    pickle_in = open("List_P5", "rb")
    P_6 = pickle.load(pickle_in)
    pickle_in.close()
    return P_6

def diff(first, second):  # This outputs the set difference.
    second = set(second)
    return [item for item in first if item not in second]
def get_subsets(fullset):  # this is used to output the powerset.
    listrep = list(fullset)
    subsets = []
    for i in range(2 ** len(listrep)):
        subset = []
        for k in range(len(listrep)):
            if i & 1 << k:
                subset.append(listrep[k])
        subsets.append(subset)
    return subsets
def load_starting_data(n_value):

    global n_1
    n_1=n_value+1

    global nset
    nset=list(range(1,n_value+1))

    global n_1set
    n_1set=list(range(1,n_1+1))

    # Next we fix the columns of the database and remove length 1 columns as they are unnecessary as value always 0.

    global Pn
    Pn= get_subsets(set(nset))
    Pn.sort(key=len) # Here we sort by length
    Pn.remove([])

    global Pn_1
    Pn_1 =get_subsets(set(n_1set))
    Pn_1.sort(key=len)  # Here we sort by length #Todo changes order will change column order in final output hopefull avoiding Ordered.py step.

def load_initial_results():

    def remove_len1_subsets_Pn(Pn_term):
        # We remove length 1 subsets for the database at the end
        sub = [i for i in Pn_term if len(i) < 2]
        Pn_tup_db = [tuple(item) for item in Pn_term if
                     item not in sub]  # removing length 1 subsets for the columns in final database.
        return Pn_tup_db
    global Pn_tup_db
    Pn_tup_db=remove_len1_subsets_Pn(Pn)

    def remove_len1_subsets_Pn_1(Pn_1_term):
        sub_1 = [i for i in Pn_1_term if len(i) < 2]
        Pn_1_tup_db = [tuple(item) for item in Pn_1 if item not in sub_1]  # similar
        return Pn_1_tup_db
    global Pn_1_tup_db
    Pn_1_tup_db= remove_len1_subsets_Pn_1(Pn_1)

    def Pn_1_tup_get_columns_df_format(list_Pn_1):
        # Our functions with be in dictionary format, I chose to put elements of the powerset into tuples as they are immutable unlike sets.
        Pn_1_tup = [tuple(j) for j in list_Pn_1]  # We did not remove the length 1 subsets here (kept for completeness we remove at end).
        Pn_1_tup.remove(())  # We remove the empty tuple.
        # print(Pn_1_tup)
        return Pn_1_tup
    global Pn_1_tup
    Pn_1_tup = Pn_1_tup_get_columns_df_format(Pn_1)

    def Pn_tup_get_columns_df_format(list_Pn):
        list_Pn=list_Pn.copy()
        Pn_tup = [tuple(i) for i in list_Pn]
        return Pn_tup
    global Pn_tup
    Pn_tup = Pn_tup_get_columns_df_format(Pn)

    def get_blank_extension(term_Pn_1_tup,term_Pn_tup):
        blank = diff(term_Pn_1_tup, term_Pn_tup)
        # print(blank) #used to extnd Pn functions with {key: 0}
        return blank
    global blank
    blank = get_blank_extension(Pn_1_tup_get_columns_df_format(Pn_1),Pn_tup_get_columns_df_format(Pn))
def get_epsilon_from_one_node(x): #element of Pn dependant
    g = nx.DiGraph() #create directed graph
    g.add_nodes_from(Pn_tup)
    green_edges = []# add the red and green edges to the graph.
    red_edges = []
    for i in Pn:
        for j in Pn:
            complement = diff(j, i)  # may be empty
            if complement == []:
                continue
            elif set(i) == set(i).issubset(set(j)):
                continue
            elif set(i).issubset(set(j)):
                # add green  list
                if x[tuple(j)] == x[tuple(i)] + x[tuple(complement)]:
                    green_edges.append((tuple(i), tuple(j)))
                # add red list.
                elif x[tuple(j)] == x[tuple(i)] + x[tuple(complement)] + 1:
                    red_edges.append(
                        (tuple(j), tuple(i)))  # I swapped the order here to account for downward closed.
                    # given this swapped order wecan use a graph traversal to determine epsilon^-1 as mentioned in MSA Musings.
    g.add_edges_from(green_edges)
    g.add_edges_from(red_edges)
    # We now create the epsilon list
    epsilon = []  # this will look like [[(1,2)],[(1,),(1,2),(1,2,3)]]
    for i in Pn_tup:  # For each node we see where we can walk to along edges.
        tree = nx.depth_first_search.dfs_tree(g, i)
        epsilon.append(list(tree.nodes))
    return epsilon
def get_epsilon_combin(epsilon):#Todo: Find all combinations in less time to find P_6 case.
    set_epsilon = set([frozenset(i) for i in epsilon])  # remove duplicates.
    Back_to_list_epsilon = [list(i) for i in set_epsilon]

    # If these paths from distinct nodes are different we wish to take the union and add them to epsilon which changes Back_to_list_epsilon above effecting the for loop below.
    # We limit this to total length of the node set.
    # We are working with var=epsilon here and aim to remove duplicates.

    for j in Back_to_list_epsilon:
        epsilon_minus = Back_to_list_epsilon.copy()
        epsilon_minus.remove(j)  # We dont want combinations with itself.
        # print("This is epsilion minus j",epsilon_minus)
        if j in epsilon_minus:  # incase there are multiple.
            continue
        if len(j) == len(Pn) - 1:  # if full length of nodes we want to skip.
            continue
        elif len(j) != len(Pn) - 1:
            # print(j)
            T = j
            T = [list(i) for i in T]  # change tuples to lists.
            for S in epsilon:  # Want to compare two terms in Back_to_list_epsilon and epsilon.
                S = [list(i) for i in S]
                if S == T:  # if the combination already lives in epsilon want to skip.
                    continue
                elif len(S) == len(Pn) - 1:  # there wont be anything larger than pn-1
                    continue
                elif S != T and len(S) < len(Pn) - 1:
                    unionST = T + S
                    res_unionST_0 = [i for n, i in enumerate(unionST) if
                                     i not in unionST[:n]]  # removes duplicates.
                    res_unionST = [tuple(i) for i in res_unionST_0]
                    if res_unionST not in epsilon:  # If the term is new to epsilon we add it into  epsilon.
                        # print("The term being appended to epsilon is:",res_unionST)
                        epsilon.append(res_unionST)
                        # print("The set of epsilon with new term added is:",Back_to_list_epsilon) #with new added term.
    # We now have our extentions of P_n+1:

    # We remove any duplicates again and add the Empty and Everything epsilon extensions (see MSA-Musings).
    epsilon_set = [set(i) for n, i in enumerate(epsilon) if i not in epsilon[:n]]  # Remove duplicates
    epsilon_set.append([tuple([])])  # Adding the empyty epsilon extension condition.
    epsilon_set.append(x.keys())  # Adding in length EVERYTHING extension.
    epsilon_no_rep = [list(i) for n, i in enumerate(epsilon_set) if i not in epsilon_set[:n]]  # Remove duplicates

    # Using these epsilon extensions we create the elements of P_n+1 for each element of P_n.
    # take Pn_1 and add in key :value pairs where key has been extended to n+1.
    # Use the blank to get a blank extension e.g fun3_4= {(1,):0,(2,):0,(3,):0,(1,2):0, (1,3):1, (2,3):0, (1,2,3):1}
    # to get fun3_4= {(1,):0,(2,):0,(3,):0,(1,2):0, (1,3):1, (2,3):0, (1,2,3):1, (4,):0, (1,4):0,(2,4):0...(124):0,...(1234):0}}
    for i in blank:
        x[i] = 0

    # We now add the values into the blank extentions corresponding to the extentions in epsilon_no_rep.
    # Given epsilon list we extend current function x.
    extensions_epsilon = []  # After add the contents of this list to P_4.#Done: is [x] neccesary?: No see P_4 t P_3 sheet.
    for l_tup in epsilon_no_rep:
        copyx = x.copy()  # may change x # Copy of current function with added keys for changing.
        # We treat the empty epsilon separatly.
        if l_tup == [()]:  # Treating the empty extension seperately.
            for i in [j for j in
                      copy_no_extension.keys()]:  # Does extension by 0 part #See begining for details on copy_no_extension
                copyx[i + (n + 1,)] = copyx[i]
            # print(copyx)
        else:
            for tup in l_tup:
                if () in l_tup:
                    continue
                else:
                    extra_element = tup + (n + 1,)  # Moving from (1,3) to (1,3,4) adding in extra element.
                    # print(extra_element)
                    copyx[extra_element] = copyx[
                                               tup] + 1  # Adding one to the cases where we have eplsion {(1,3):0} -> {(1,3):1}
                    for i in [j for j in copy_no_extension.keys() if
                              j not in l_tup]:  # See begining for details on copy_no_extension #Fixme: dont want to add blanks in here
                        copyx[i + (n + 1,)] = copyx[
                            i]  # Adding zero to the case where we dont have epsilon. ie retaining the value {(1,3):0} -> {(1,3):0}
        extensions_epsilon.append(copyx)

    return (extensions_epsilon)
def get_output():
    # pickle_out = open("List_P6", "wb") #Save List of Pn+1 for further induction.
    # pickle.dump(extensions, pickle_out)
    # pickle_out.close()

    data_ext = pd.DataFrame.from_dict(extensions, orient="columns")
    cols = list(data_ext.columns.values) #Put columns into the right order
    cols.sort(key=len)
    data_ext = data_ext[cols]

    # pickle_out = open("Dataframe_P6", "wb") #Save database_Pn+1. For Poltope calculations.
    # pickle.dump(data_ext, pickle_out)
    # pickle_out.close()
    data_ext_minus = pd.DataFrame(data_ext,columns=Pn_1_tup_db)  # power set minus empty and length 1 sets, tunred to tuples
    return data_ext_minus

def ExtendedFromFunctionLabelled(extensions_epsilon,counter):
    extensions_epsilon_extra_col = []
    counter=counter
    for extension in extensions_epsilon:
        lower_funct = {"Extended from function labelled": int(counter)}
        extension = extension | lower_funct
        extensions_epsilon_extra_col.append(extension)
    return extensions_epsilon_extra_col
def get_output_labelled():
    data_ext = pd.DataFrame.from_dict(extensions_ExtendedFromFunctionLabelled, orient="columns")
    cols = list(data_ext.columns.values)
    cols.sort(key=len)  # Here we sort by length
    data_ext = data_ext[cols]

    for i in range(1, len(extensions_ExtendedFromFunctionLabelled) + 1):
        sliced = data_ext.loc[data_ext['Extended from function labelled'] == i]
        pd.set_option("display.max_rows", None, "display.max_columns", None, 'display.width', None)
        # print(sliced) #Done:to be checked with sheets P4 to P3

    len2cols = [x for x in cols if len(x) == 2]
    len3cols = [x for x in cols if len(x) == 3]
    len4cols = [x for x in cols if len(x) == 4]
    len5cols = [x for x in cols if len(x) == 5]
    len6cols = [x for x in cols if len(x) == 6]

    # groupby cols of length 2 take sum and add to far right. sim for rest.
    data_ext["2-set sum"] = data_ext[len2cols].sum(axis=1)  # but for specific cols, can do select only those cols by groupby.
    data_ext["3-set sum"] = data_ext[len3cols].sum(axis=1)  # but for specific cols, can do select only those cols by groupby.
    data_ext["4-set sum"] = data_ext[len4cols].sum(axis=1)  # but for specific cols, can do select only those cols by groupby.
    data_ext["5-set sum"] = data_ext[len5cols].sum(axis=1)  # but for specific cols, can do select only those cols by groupby.
    data_ext["6-set sum"] = data_ext[len6cols].sum(axis=1)  # but for specific cols, can do select only those cols by groupby.
    data_ext["Characteristic"] = pd.concat((data_ext["2-set sum"], data_ext["3-set sum"], data_ext["4-set sum"]),
                                        axis=1).values.tolist()
    # df_P4["Characteristic"] = df_P4[["2-set sum","3-set sum",(1,2,3,4)]].join(axis=1) #but for specific cols, can do select only those cols by groupby.
    return data_ext

#Preamble
n=4
Tilde_Pn= get_tilde_P4()# Change for load \tildeP_n
load_starting_data(n)
load_initial_results()

# Main code:
extensions = []
extensions_ExtendedFromFunctionLabelled=[] #remembers which function it has been extended from

for counter,x in enumerate(Tilde_Pn,1):

    copy_no_extension = x.copy()  # to get the complement of the extension from keys
    # i) starting with paths from a specific node
    epsilon=get_epsilon_from_one_node(x)
    # ii) Then taking combinations of paths from a specific node in i).
    extensions_epsilon= get_epsilon_combin(epsilon)
    extensions.extend(extensions_epsilon)
    #Decorations.
    extensions_ExtendedFromFunctionLabelled.extend(ExtendedFromFunctionLabelled(extensions_epsilon,counter))

    print(Tilde_Pn.index(x))  # counter for the function which has been completely extended.

#After finished:
print("--- %s seconds ---" % (time.time() - start_time)) #prints timer.
print(get_output()) #Pickles list and dataframe of Pn+1, prints dataframe at end.
# print(get_output_labelled())#Remembers extention from function from database+descipters files.
