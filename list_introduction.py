# List: Ordered, Mutable, Allows Duplicate

mylist = ["Banana", "Cherry", "Apple", "Mango"]
print(mylist)  # prints List


mylist2 = [True, 94, 83.93, "Hello", ["Hello", "Buddy"]]  # Can Have Different types of Data Types
print(mylist2)

print(mylist2[2])  # Prints from Beginning from 0 Index
print(mylist2[-2])  # Prints from End from Negative 1 Index

if "Banana" in mylist:
    print("Yes")
else:
    print("No")


mylist2.append(False)  # Add at last of list
print(mylist2)

mylist2.insert(2, "Vinayak")  # add the element at position
print(mylist2)


mylist2.pop()  # delete last element  && Returns Popped Element
print(mylist2)

mylist.remove("Banana")  # removes Mentioned Element from List
print(mylist)


mylist.reverse() # Reverse the List
print(mylist)

mylist.clear()  # Remove every element from the List
print(mylist)

numbers_list = [8, -8, 0, 14, 55, -88]
new_list = sorted(numbers_list)  # Returns New List Builtin Function not module of list
print(numbers_list)
print(new_list)

numbers_list.sort()  # Changes Original List
print(numbers_list)

mylist3 = [0] * 5
print(mylist3)

concate_list = mylist3 + mylist2
print(concate_list)

new_list2 = mylist2[1:5] # Slicing Method ..... includes starting but excluding ending means [starting : ending)
print(new_list2)

new_list3 = mylist2[::2] # Slicing with steps  ...Means take every second item
print(new_list3)
new_list3 = mylist2[::-1] # Trick to reverse the list
print(new_list3)


# Copying List

cpy_list = new_list3  # Copies but Changes in copy list will also do in original list

cpy_list1 = new_list3.copy()
cpy_list1 = new_list3[:]
cpy_list1 = list(new_list3)

print(numbers_list)
squared_number_list = [i*i for i in numbers_list]
print(squared_number_list)