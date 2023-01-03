import pandas as pd 
import pickle

#region: Functions

def get_output(df):

    data_ext = df
    cols = list(data_ext.columns.values) #Put columns into the right order
    cols.sort(key=len)
    data_ext = data_ext[cols]

    return data_ext

#endregions


""" 

#region:Try with P3 new and old:

# current df with 10 elements
path = "Cases\Main_files\Pn\P3"
pickle_in = open(path, "rb")
p_in = pickle.load(pickle_in)
pickle_in.close()
df_new=pd.DataFrame.from_dict(p_in, orient="columns",dtype=object)
pd.set_option("display.max_rows", None, "display.max_columns", None)
# df_new=pd.DataFrame(p_in,dtype=object)
df_new=get_output(df_new)
# print(df_new)

path = "Cases\Storage\Data_df\Dataframe_P3"
pickle_in = open(path, "rb")
p_in = pickle.load(pickle_in)
pickle_in.close()
df_old=pd.DataFrame(p_in)
pd.set_option("display.max_rows", None, "display.max_columns", None)
# print(df_old)

#endregion: 

#region: Comparing old and new P3's

# print(df_new==df_old)

df_diff=pd.concat([df_new,df_old]).drop_duplicates(keep=False)
print(df_diff)
#endregion: 
 """

""" 
#region:Try with P4 new and old:

# current df 
path = "Cases\Main_files\Pn\P4"
pickle_in = open(path, "rb")
p_in = pickle.load(pickle_in)
pickle_in.close()
df_new=pd.DataFrame.from_dict(p_in, orient="columns",dtype=object)
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# df_new=pd.DataFrame(p_in,dtype=object)
df_new=get_output(df_new)
# print(df_new)

path = "Cases\Storage\Data_df\Dataframe_P4"
pickle_in = open(path, "rb")
p_in = pickle.load(pickle_in)
pickle_in.close()
df_old=pd.DataFrame(p_in)
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# print(df_old)

#endregion: 

#region: Comparing old and new P4's

df_diff=pd.concat([df_new,df_old]).drop_duplicates(keep=False)
print(df_diff)
#endregion: 
 """

#region:Try with P5 new and old:

# current df 
path = "Cases\Main_files\Pn\P5"
pickle_in = open(path, "rb")
p_in = pickle.load(pickle_in)
pickle_in.close()
df_new=pd.DataFrame.from_dict(p_in, orient="columns",dtype=object)
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# df_new=pd.DataFrame(p_in,dtype=object)
df_new=get_output(df_new)
# print(df_new)

""" path = "Cases\Storage\Data_df\Dataframe_P5"
pickle_in = open(path, "rb")
p_in = pickle.load(pickle_in)
pickle_in.close()
df_old=pd.DataFrame(p_in)
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# print(df_old)
 """
#endregion: 

#region: Comparing old and new P4's

""" df_diff=pd.concat([df_new,df_old]).drop_duplicates(keep=False)
print(df_diff) """
#endregion: 

#region: Issue with calculating p6 from sage.

df=df_new.iloc[51] #issue case
df=df[[(1, 2, 3, 5), (2,), (2, 3, 4, 5), (3,)]]

print(df)
#endregion: 