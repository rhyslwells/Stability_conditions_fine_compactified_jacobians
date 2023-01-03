# Objective: get data from out_sage and correct to dataframe format.
import pickle
import csv
import ast  # https://stackoverflow.com/questions/1894269/how-to-convert-string-representation-of-list-to-a-list

#region: Fucntions


def get_Up_lst():
    """ Turns Up_lst list in text format from sage to list """
    Up_lst = load_data()

    empty = []
    for i in range(len(Up_lst)):
        lst = []
        for item in Up_lst[i]:
            extend = ast.literal_eval(item)
            lst.append(extend)
        empty.append(lst)
    Up_lst = empty

    return Up_lst


def pickle_output(name):
    # name=path name, function return files items.

    path = f"Cases\Main_files\Pn\{name}"
    pickle_in = open(path, "rb")
    p_in = pickle.load(pickle_in)
    pickle_in.close()
    return p_in


def pickle_input(name, object):
    # Name of file string, with object to be saved. Used for storing and appending to stored items.

    path = f"Cases\Main_files\Pn\{name}"
    pickle_out = open(path, "wb")  # Save List of Pn+1 for further induction.
    pickle.dump(object, pickle_out)
    pickle_out.close()
    return


def load_data():
    with open('Cases\Main_files\out_sage\cvs_P5.csv', 'r') as file: #! CHANGE ME
        reader = csv.reader(file)
        data = list(reader)
        # for row in reader:
        # print(row)
        # print(data[0][1])
    return data


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

    """ def remove_len1_subsets_Pn_1(Pn_1_term):
        sub_1 = [i for i in Pn_1_term if len(i) < 2]
        Pn_1_tup_db = [tuple(item) for item in Pn_1 if item not in sub_1]  # similar
        return Pn_1_tup_db
    global Pn_1_tup_db
    Pn_1_tup_db= remove_len1_subsets_Pn_1(Pn_1) """

    def Pn_1_tup_get_columns_df_format(list_Pn_1):
        # Our functions with be in dictionary format, I chose to put elements of the powerset into tuples as they are immutable unlike sets.
        # We did not remove the length 1 subsets here (kept for completeness we remove at end).
        Pn_1_tup = [tuple(j) for j in list_Pn_1]
        Pn_1_tup.remove(())  # We remove the empty tuple.
        # print(Pn_1_tup)
        return Pn_1_tup
    global Pn_1_tup
    Pn_1_tup = Pn_1_tup_get_columns_df_format(Pn_1)

    def Pn_tup_get_columns_df_format(list_Pn):
        list_Pn = list_Pn.copy()
        Pn_tup = [tuple(i) for i in list_Pn]
        return Pn_tup
    global Pn_tup
    Pn_tup = Pn_tup_get_columns_df_format(Pn)

    def get_blank_extension(term_Pn_1_tup, term_Pn_tup):
        blank = diff(term_Pn_1_tup, term_Pn_tup)
        # print(blank) #used to extnd Pn functions with {key: 0}
        return blank
    global blank
    blank = get_blank_extension(Pn_1_tup_get_columns_df_format(
        Pn_1), Pn_tup_get_columns_df_format(Pn))


# endregion:

#region: Preamble
n = 4  # where we are pulling functions from: want n+1. #! CHANGE ME
P4 = pickle_output("P4") #Loading in 
Tilde_Pn = P4

load_starting_data(n)
load_initial_results()

# endregion

# region:Main

Up_lst = get_Up_lst() 

""" Up_lst is a list which contains lists from each function of Pn of extensions, these lists contain lists which are the extensions. """

# print(Up_lst)

extensions = [] #* Want to compute
for counter in range(len(Up_lst)):

    prev_funct = Tilde_Pn[counter]  # function from graph poset
    copy_no_extension = prev_funct.copy()  # Necessary:

    # Need black function with remaining slots to be filled ()
    for i in blank:
        prev_funct[i] = 0 # fill in 0 to positions we are calculating "those with n element".

    # add values into the blank spaces corresponding upper sets in Up_lst[counter][num_extend].
    
    for num_extend in range(len(Up_lst[counter])):

        for l_tup in [Up_lst[counter][num_extend]]:  # !change back#

            # print(l_tup,"\n")

            # may change x # Copy of current function with added keys for changing.
            copyx = prev_funct.copy()
            # We treat the empty epsilon separatly.
            if len(l_tup) == 0:  # Treating the empty extension seperately.
                for i in [j for j in copy_no_extension.keys()]:  # Does extension by 0 part #See begining for details on copy_no_extension
                    copyx[i + (n + 1,)] = copyx[i]
                # print(copyx)
                # print("We do this")
            else:
                for tup in l_tup:
                    if () in l_tup:
                        # print("We do this")
                        continue
                    else:
                        # Moving from (1,3) to (1,3,4) adding in extra element.
                        extra_element = tup + (n + 1,)
                        # print(extra_element)
                        copyx[extra_element] = copyx[tup] + 1  # Adding one to the cases where we have eplsion {(1,3):0} -> {(1,3):1}
                        
                        for i in [j for j in copy_no_extension.keys() if j not in l_tup]:  # See begining for details on copy_no_extension #Fixme: dont want to add blanks in here
                            copyx[i + (n + 1,)] = copyx[i]  # Adding zero to the case where we dont have epsilon. ie retaining the value {(1,3):0} -> {(1,3):0}
            # print(copyx,"\n \n")
            extensions.append(copyx)


print(len(extensions))


#region: Saving data Save Pn1

pickle_input("P5",extensions) #!CHANGE ME

# endregion
