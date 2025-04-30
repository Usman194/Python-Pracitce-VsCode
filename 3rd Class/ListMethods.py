list = [2, 5, 6, 7, 4, 8]

#Append method => Adds one element at the end
list.append(9)
print(list) #This is called mutating the list (Mutate mean change)

#Sort =. Sort in accending order
list1 = [3, 2, 8, 5, 9, 4]
print(list1.append(6))
list1.sort()
print(list1)
list1.sort(reverse=True) #This method change the list in decending order
print(list1)
list1.insert(3, 77)
print(list1)

list2 = ["Banana", "Litchi", "Mango", "Apple"]
list2.sort()
print(list2)
list2.sort(reverse=True) #This method change the list in decending order
print(list2)
#Reverse method => This method is used to reverse all values
list2.reverse()
print(list2)

#Insert method => this method is used to insert element at index
list3 = [1, 2, 3, 4, 5, 6, 8]
list3.insert(4, 55)
print(list3)

#Remove method => Remove first occurance of element
list4 = [23, 22, 44, 34, 54]
list4.remove(44)
list4.pop(0) #POP =>Pop method removes the values at index
print(list4)