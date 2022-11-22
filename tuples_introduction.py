import sys
import timeit
# Tuples: Ordered, immutable, Allows Duplicate
my_tuple = ("Vinayak")
print(my_tuple, type(my_tuple))  # Recognized as String

my_tuple = ("Vinayak",)
print(my_tuple, type(my_tuple))  # Now Recognized as Tuples

my_tuple = ("Vinayak", 19, "Vispute")
print(my_tuple)

my_list = ["Hello", "Buddy", "Hello"]
my_tuple2 = tuple(my_list)  # List is converted into tuples
print(my_tuple2, type(my_tuple2))

item = tuple[1] # Index from Zero and Same for Negative element like list

# Length and iteration over tuples and check element is present or not
# Are Same as List

print(my_tuple2.count("Hello"))  # Count Specified Element
print(my_tuple.index(19))  # Returns index of element

# Slicing and Step SLicing are Same as List

name, age, surname = my_tuple

print("==>", name, age, surname)

my_tuple3 = (1, 2, 3, 4, 5, 6, 7)

i1, *i2, i3 = my_tuple3

print(i1)
print(i3)
print(i2, type(i2))


# Tuples is More Efficient then List
mylist = [0, 1, 2, "Hello", True]
mytuple = (0, 1, 2, "Hello", True)


print(sys.getsizeof(mylist), "Bytes")
print(sys.getsizeof(mytuple), "Bytes")


# Also More efficient to Iterate and also to create tuples

# Here we are going to calculate time for creating 1 million list and 1 million tuples
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))

