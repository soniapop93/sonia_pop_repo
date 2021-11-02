x = 2
y = 3

text = "This is a text"
#This is a comment

print(text)

sum = x + y

print("The result is: ", sum)

print("Hello World!")

list_x = [1,2,3,4,5,6,7]

for i in list_x:
    if i % 2 == 0:
        print(i)


# print(7 is None)
# print(7 == 4)
# print(7 == 7)

# x = 7.5
# print(x, type(x))

# print(2**2)

var1 = 7
var2 = 3
# print(var1 != var2)

# print(var1 < var2 or var1 == var2)

# print(var1 is not var2)
# print(1 not in [1, 2, 3])

# print(bin(6))
print(bin(6 & 7))
print(bin(60))
print(bin(32))
print(bin(60 & 32))
print(bin(60|32))
print(60|32)

x = 5
print(type(x))

x = "string"

print(type(x))

my_age = 18

print(id(my_age))
print("-------")
my_name = "Sonia"
my_number = 23

print(id(my_name))
print(id(my_number))

my_number = my_number + 5
my_number += 5
print(my_number)

print("-------")
print(ord("a"), ord("z"))

print(chr(97), chr(65))

print("Numele meu este \"Sonia\"!")

print("This is the first line\nThis is the second line")

print("""This is the first line
This is the second line""")


name = "Sonia"
age = 28
print("Numele meu este {} si am {} ani". format(name, age))

print("Numele meu este {name} si am {age} ani". format(name=name, age=27))

print(f"Numele meu este {name} si am {age} ani.")

print(f"Numele meu este %s si am %d ani." % ("Sonia", 28))