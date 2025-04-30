#str.endswith("er.") Returns true if string ends with er
str = "I am a programmer"
print(str.endswith("er"))   
print(str.endswith("ar"))
# 2)str.capitalize() It means capitalize 1st character
str1 = "muhammad Usman"
print(str1.capitalize())   
str2 = str1.capitalize()
print(str2)

# 3)str.replace(old, new) Replace alloccurance old value with new value
str4 = "My name is Muhammad Usman"
print(str4.replace("Muhammad", "Mian"))

# 4)str.find(word) Returns 1st index of 1st occurer
str5 = "Faran model college jhang"
print(str5.find("m"))
print(str5.find("model"))

# 5)str.count() Returns the occurence of substr

str6 = "I am study in govt school"
print(str6.count("study"))
str7 = "My name is muhammad usman and My father name is muhammad yousaf"
print(str7.count("My"))
print(str7.count("y"))