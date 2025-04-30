#WAP to ask users to enter names of their 3 favorit movies & store them in list
movies = []
mv1 = input("Enter your favorit mv1: ") 
mv2 = input("Enter your favorit mv2: ") 
mv3 = input("Enter your favorit mv3: ") 
movies.append(mv1)
movies.append(mv2)
movies.append(mv3)
print(movies)

#Othe method
mv = input("Enter your favorit mv1: ") 
movies.append(mv)
mv = input("Enter your favorit mv2: ") 
movies.append(mv)
mv = input("Enter your favorit mv3: ")
movies.append(mv)
print(movies) 

#Another method
movies.append(input("Enter your favorit mv1: "))
movies.append(input("Enter your favorit mv2: "))
movies.append(input("Enter your favorit mv3: "))
print(movies)