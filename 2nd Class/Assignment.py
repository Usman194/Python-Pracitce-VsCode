#Write a programme to check if a number entered by the user is even or odd
num = int(input("Please enter your number: "))

rem = num % 2
if(rem == 0):
    print("Even")
else:
    print("Odd")

#Question 2)Write a programme to find the three greatest of 3 entered by the user
a = int(input("Please enter your number: "))
b = int(input("Please enter your number: "))
c = int(input("Please enter your number: "))

if(a > b and a > c):
    print(a)
elif(b > c):
    print(b)
else:
    print(c)