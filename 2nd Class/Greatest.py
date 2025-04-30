#Question 2)Write a programme to find the three greatest of 3 entered by the user
a = int(input("Please enter your number: "))
b = int(input("Please enter your number: "))
c = int(input("Please enter your number: "))
d = int(input("Please enter your number: "))

if(a >= b and a >= c and a >= d):
    print("First number is largest: ",a)
elif(b >= c and b >= d):
    print("Second number is largest: ",b)
elif(c >= d):
    print("Third number is largest: ",c)
else:
    print("Fourth number is largest: ",d)