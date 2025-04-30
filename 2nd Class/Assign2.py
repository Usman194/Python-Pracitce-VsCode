#Write a programme to check if a number is a multiple of 7
x = int(input("Please enter your number: "))

rem = x % 7 
if(rem == 0):
    print("Muliple of 7")
else:
    print("The number is not multiple of 7")