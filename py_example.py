# x = 2
# y = 3

# text = "This is a text"
# #This is a comment

# print(text)

# sum = x + y

# print("The result is: ", sum)

# print("Hello World!")

# list_x = [1,2,3,4,5,6,7]

# for i in list_x:
#     if i % 2 == 0:
#         print(i)


# # print(7 is None)
# # print(7 == 4)
# # print(7 == 7)

# # x = 7.5
# # print(x, type(x))

# # print(2**2)

# var1 = 7
# var2 = 3
# # print(var1 != var2)

# # print(var1 < var2 or var1 == var2)

# # print(var1 is not var2)
# # print(1 not in [1, 2, 3])

# # print(bin(6))
# print(bin(6 & 7))
# print(bin(60))
# print(bin(32))
# print(bin(60 & 32))
# print(bin(60|32))
# print(60|32)

# x = 5
# print(type(x))

# x = "string"

# print(type(x))

# my_age = 18

# print(id(my_age))
# print("-------")
# my_name = "Sonia"
# my_number = 23

# print(id(my_name))
# print(id(my_number))

# my_number = my_number + 5
# my_number += 5
# print(my_number)

# print("-------")
# print(ord("a"), ord("z"))

# print(chr(97), chr(65))

# print("Numele meu este \"Sonia\"!")

# print("This is the first line\nThis is the second line")

# print("""This is the first line
# This is the second line""")


# name = "Sonia"
# age = 28
# print("Numele meu este {} si am {} ani". format(name, age))

# print("Numele meu este {name} si am {age} ani". format(name=name, age=27))

# print(f"Numele meu este {name} si am {age} ani.")

# print(f"Numele meu este %s si am %d ani." % ("Sonia", 28))

# my_list = []

# my_list = list()

# my_list = [1, 2, 3.5, 3+6j, "Sonia", False, True, None, [1,2,3]]

# print(type(my_list))
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[6])
# print(my_list[8][0])
# print(my_list[-1])
# print(my_list[-9])
# print(len(my_list), type(len(my_list)))
# print(my_list[len(my_list)//2])
# index = 8
# print(my_list[index])
# print(my_list[1:])
# print(my_list[1:5])
# print(my_list[5:1:-1])
# print(my_list[::-1])

# my_name = "Sonia"
# print(len(my_name))
# print(my_name[1])
# print(my_name[1:4])
# print(my_name[::-1])

# my_second_list =  ["a", "b"]
# print(my_second_list * 6)
# print(my_name * 6)

# another_list = [1, 2, 3, -1, 4, 6, 10, [1, 2, 3]]
# # print(min(another_list))

# print(another_list.index(1))
# # another_list.append(11)
# # another_list.insert(1, "a")
# # another_list.remove(2)
# # another_list.pop()
# # another_list.clear()
# # new_list = another_list.copy()

# # print(another_list)
# # print(new_list)

# import copy
# from typing import MutableMapping

# new_list = copy.deepcopy(another_list)
# print(another_list)
# another_list[-1][1] = "a"
# print(new_list)
# print(another_list)

# another_list.reverse()

# print(another_list)

# my_name = "Sonia"

# print(my_name[::-1])

# my_list1 = [1,2]
# my_list2 = [3,4]

# print(id(my_list1))
# print(my_list1 + my_list2)

# # my_list1.extend(my_list2)
# # print(my_list1)
# # print(id(my_list1))

# # my_list1 += my_list2
# # print(id(my_list1))

# # another_list.sort()
# # print(another_list)

# # my_tuple = (1, 2 , "Sonia", [1,2])

# # my_tuple1 = (1, 2)
# # my_tuple2 = (3, 4)

# # print(my_tuple1 + my_tuple2)

# # my_list = list(my_tuple)

# # print(my_list, type(my_tuple), type(my_list))
# # my_list.append("a")
# # my_tuple = tuple(my_list)
# # print(my_tuple)


# my_tuple = (1,2, "Sonia")

# var1, var2, name = my_tuple

# print(var1)


# my_dict = {
#     "a":1,
#     "b":2,
#     "c":3
# }

# print(my_dict, type(my_dict))
# print(my_dict['a'])
# print(my_dict.keys())

# print(1 in my_list)


# print("a" in my_dict)

# print(my_dict.get("l", "nu exista"))

# # my_dict.clear()
# print(my_dict)

# dict_keys = my_dict.keys()
# print(dict_keys, type(dict_keys))
# key_list = list(dict_keys)

# print(key_list, type(key_list))

# dict_values = my_dict.values()
# print(dict_values, type(dict_values))

# values_list = list(dict_values)
# print("a" in values_list)

# dict_items = my_dict()
# print(dict_items, type(dict_items))

# my_dict.pop("a")

# print(my_dict)

# my_dict["a"] = 0
# my_dict["d"] = 'd'
# print(my_dict)

my_set = {1, 2, 3, 4, 5, 6}

print(my_set, type(my_set))
# my_set.remove(8)
my_set.discard(8)
my_set.clear()
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = _set = {4, 5, 6, 7, 8}

print(set1.intersection(set2))
print(set1.union(set2))

print(set1.issuperset(set2))

print(set2.issubset(set1))
print(set1.difference(set2))