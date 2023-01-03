# Main goal: To extend the functions in the P_3 case to the P_4 case.

import networkx as nx
import pickle

#region: Load data:

# * I say we leave fuction in original format and convert back and froth if needed using converters.

# fun2_1 = {(1,): 0, (2,): 0, (1, 2): 0}
# fun2_2 = {(1,): 0, (2,): 0, (1, 2): 1}

#endregion



#region: Functions

def pickle_input(name,object):
    # Name of file string, with object to be saved. Used for storing and appending to stored items.

    path=f"Cases\Main_files\in_sage\{name}"
    pickle_out = open(path, "wb") #Save List of Pn+1 for further induction.
    pickle.dump(object, pickle_out)
    pickle_out.close()
    return

def pickle_output(name):
    #name=path name, function return files items.
    
    path=f"Cases\Main_files\out_sage\{name}"
    pickle_in = open(path, "rb")
    p_in = pickle.load(pickle_in)
    pickle_in.close()
    return p_in


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
    n_1 = n_value+1

    global nset
    nset = list(range(1, n_value+1))

    global n_1set
    n_1set = list(range(1, n_1+1))

    # Next we fix the columns of the database and remove length 1 columns as they are unnecessary as value always 0.

    global Pn
    Pn = get_subsets(set(nset))
    Pn.sort(key=len)  # Here we sort by length
    Pn.remove([])

    global Pn_1
    Pn_1 = get_subsets(set(n_1set))
    # Here we sort by length #Todo xhanges order will xhange column order in final output hopefull avoiding Ordered.py step.
    Pn_1.sort(key=len)


def load_initial_results():
    """ def remove_len1_subsets_Pn(Pn_term):
        # We remove length 1 subsets for the database at the end
        sub = [i for i in Pn_term if len(i) < 2]
        Pn_tup_db = [tuple(item) for item in Pn_term if
                     item not in sub]  # removing length 1 subsets for the columns in final database.
        return Pn_tup_db

    global Pn_tup_db
    Pn_tup_db=remove_len1_subsets_Pn(Pn) """

    """     def remove_len1_subsets_Pn_1(Pn_1_term):
            sub_1 = [i for i in Pn_1_term if len(i) < 2]
            Pn_1_tup_db = [tuple(item) for item in Pn_1 if item not in sub_1]  # similar
            return Pn_1_tup_db
        global Pn_1_tup_db
        Pn_1_tup_db= remove_len1_subsets_Pn_1(Pn_1) """

    """     def Pn_1_tup_get_columns_df_format(list_Pn_1):
            # Our functions with be in dictionary format, I chose to put elements of the powerset into tuples as they are immutable unlike sets.
            Pn_1_tup = [tuple(j) for j in list_Pn_1]  # We did not remove the length 1 subsets here (kept for completeness we remove at end).
            Pn_1_tup.remove(())  # We remove the empty tuple.
            # print(Pn_1_tup)
            return Pn_1_tup
        global Pn_1_tup
        Pn_1_tup = Pn_1_tup_get_columns_df_format(Pn_1) """

    def Pn_tup_get_columns_df_format(list_Pn):
        list_Pn = list_Pn.copy()
        Pn_tup = [tuple(i) for i in list_Pn]
        return Pn_tup
    global Pn_tup
    Pn_tup = Pn_tup_get_columns_df_format(Pn)

    """     def get_blank_extension(term_Pn_1_tup,term_Pn_tup):
            blank = diff(term_Pn_1_tup, term_Pn_tup)
            # print(blank) #used to extnd Pn functions with {key: 0}
            return blank
            
        global blank
        blank = get_blank_extension(Pn_1_tup_get_columns_df_format(Pn_1),Pn_tup_get_columns_df_format(Pn)) """
    return


def get_funct_graph(x):  # element of Pn dependant
    g = nx.DiGraph()  # create directed graph
    g.add_nodes_from(Pn_tup)
    green_edges = []  # add the red and green edges to the graph.
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
    return g


#endregion

#region: Preamble
n = 5 #where we are pulling functions from: want n+1. #! CHANGE ME
load_starting_data(n)


#Get tild_Pn

name="P5" #!CHANGE ME
path=f"Cases\Main_files\Pn\{name}"
pickle_in = open(path, "rb")
p_in = pickle.load(pickle_in)
pickle_in.close()
Tilde_Pn = p_in

load_initial_results()
# endregion

# region: Main code:

funct_graph_lst = []
for counter, x in enumerate(Tilde_Pn, 1):
    #Want input for sagemath to get all upper sets
    fg=nx.to_dict_of_lists(get_funct_graph(x))  # output e.g {(1,): [(1, 2)], (2,): [(1, 2)], (1, 2): []}
    funct_graph_lst.append(fg)
    print(Tilde_Pn.index(x))# counter for the function which has been completely extended: to tell process

#endregion

#region: Output list file to for_sage:

pickle_input("for_P6",funct_graph_lst) #! CHANGE ME

#endregion
