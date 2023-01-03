import pickle
import numpy as np
from prettytable import PrettyTable

with open(r'sigma_data', 'rb') as fp:
    data=pickle.load(fp)

# Specify the Column Names while initializing the Table

# Add rows
for index,item in enumerate(data):

    myTable = PrettyTable(["Function", "{1,}","{2,}","{3,}","{4,}","{1,2}","{2,3}","{3,4}","{1,2,3}","{2,3,4}","{1,2,3,4}"])
    ass=item[1]
    sig=item[2]
    funct=f"Function {index+1}"
    lst=[funct,]
    x=np.array(sig)

    #Singletons:

    v1=x[:,0]
    v2=x[:,1]
    v3=x[:,2]
    v4=x[:,3]

    #Consecuative cases:

    #length 2:

    v12=v1+v2
    v23=v2+v3
    v34=v3+v4

    #Length 3:

    v123=v1+v2+v3
    v234=v2+v3+v4

    #Length 4:

    v1234=v1+v2+v3+v4

    #Constructing function:
    check_lst=[v1,v2,v3,v4,v12,v23,v34,v123,v234,v1234]

    for i in check_lst:
        lst.append(i.min(axis=0))

    myTable.add_row(lst)

    # Output
    print(f"Assignment: \n {ass}")
    print(f"Sigma: \n {np.array(sig)}")

    print("\n")
    print(myTable)
    print("\n")

""" with open(r'CMSA\sigma_data', 'rb') as fp:
    data=pickle.load(fp)

stabcon_lst=[i[2] for i in data]

# print(stabcon_lst)

tester=stabcon_lst[0]

arr_tester=np.array(tester)
print(arr_tester)

min_col=arr_tester.min(axis=0)
# print(min_col)

x=arr_tester

#Singletons:

v1=x[:,0]
v2=x[:,1]
v3=x[:,2]
v4=x[:,3]

#Consecuative cases:

#length 2:

v12=v1+v2
v23=v2+v3
v34=v3+v4

#Length 3:

v123=v1+v2+v3
v234=v2+v3+v4

#Length 4:

v1234=v1+v2+v3+v4

#Constructing function:
check_lst=[v1,v2,v3,v4,v12,v23,v34,v123,v234,v1234]

for i in check_lst[4:]:
    print(i)
    print(i.min(axis=0))
    print("------------------","\n") """