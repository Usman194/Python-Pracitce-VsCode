#Palindrome mean the vale of list is same when we reverse this list
list = [1, 2, 1]
list1 = [1, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("Not palindrome")