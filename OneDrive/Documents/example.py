# myList  = ["apple","banana","apple","fruit"]
# myList[3] = "pineapple"
# myList[2] = "grape"
# myList.insert(4,"mango")

# myList.insert(5,"dragan fruit")
# myList.insert(6,"dragan fruit")
# # print(myList)

# tropical = ["cherry", "pineapple", "papaya"]
# # print(tropical)
# myList.extend(tropical)

# myList = list(dict.fromkeys(myList))
# # myList.pop()
# # myList.clear()
# print(myList)




# if "dry" in myList:
#     print("yes it exists")
# else:
#     print("It does not exist")    

# print(myList[0:3])


# mylist = []
# mylist.insert(0,5)
# mylist.insert(1,10)
# mylist.insert(0,6)
# print(mylist)
# mylist.remove(6)
# mylist.append(9)
# mylist.append(1)
# mylist.sort()
# print(mylist)
# mylist.pop()
# mylist.reverse()
# print(mylist)

# import csv
# with open("addresses.csv",'r') as file:
#     csvreader = csv.reader(file)
#     for row in csvreader:
#         print(row)


# "C:\Users\kisho\csv\SalesJan2009.csv"

# import os
# cwd = os.getcwd()
# files = os.listdir(cwd)
# print("Files in %r: %s" % (cwd, files))

my_list1 = [1121, "Jackie Grainger", 22.22,1121, "Jackie Grainger", 22.22, 1121, "Jackie Grainger", 22.22,1121, "Jackie Grainger", 22.22,
1122, "Jignesh Thrakkar", 25.25,
1127, "Dion Green", 28.75, False,
24.32, 1132, "Jacob Gerber",
"Sarah Sanderson", 23.45, 1137, True,
"Brandon Heck", 1138, 25.84, True,
1152, "David Toma", 22.65,
23.75, 1157, "Charles King", False,
"Jackie Grainger", 1121, 22.22, False,
22.65, 1152, "David Toma"]
# print(my_list1)
list1 = []
for i in my_list1:
    if i not in list1:
        list1.append(i)
print(list1)   
# l = [1,"kishore",2,"reddy",3,"sai",1,"kishore"]
# print(l)



