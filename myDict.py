# my_dict={"name":"Binpe", "age":25}

# my_dict["age"]=27
# my_dict["name"]= "Kenne"

# #print(my_dict)

# for key,value in my_dict.items():
#     print(key,value)

my_list = []
my_dict={}


my_list.extend(["Bimpe", 35, "Dart"])
my_dict["name"]=my_list[0]
my_dict["age"]=my_list[1]
my_dict["course"]=my_list[2]

for key,value in my_dict.items():
    print(key,value)

