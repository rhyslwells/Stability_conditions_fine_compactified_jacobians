import csv 

with open('cvs_P3.csv', 'r') as file:
    reader = csv.reader(file)
    data=list(reader)
    # for row in reader:
        # print(row)
    print(data[0][1])

""" 
# my_file = open("cvsP3.txt", "r")
  
# # reading the file
# data = my_file.read()
# # data_into_list = data.replace('\n', ' ').split(".")
  
# # printing the data
# # print(list(data))

# # c = StringIO(data)
# # print(np.loadtxt(c))
# my_file.close()

# # print(list(data))

# # lis = []

# # with open("P3.txt" , "r+") as f:    
# #     for data in f.read().split():
# #             lis.append(data)
# # print(lis)

# # def stringToList(string):
# #     listRes = list(string.split(" "))
# #     return listRes

# # # print(stringToList(data))

# # def Convert(string):
# #     list1=[]
# #     list1[:0]=string
# #     return list1
# # # # Driver code
# # # print(Convert(str1))

# # print(Convert(data)) """