#Variables
age1=30
print(age1)
name="Urewa Monkey D Luffy"
print(name)
Luffy,Sabo,Ace = 17,19,19
print(Luffy)
print(Sabo)
print(Ace)
Luffy=Sanji=Zoro=2
print(Luffy)
print(Sanji)
print(Zoro)

age2=4
print(age1+age2)
print(age1-age2)
print(age1*age2)
print(age1/age2)
print(age1%age2)

#strings
str1="Nami"
str2="Swan"
print(str1+" "+str2)
#print(str1-str2)
#TypeError: unsupported operand type(s) for -: 'str' and 'str'
print(str2*4)
#index
print(str1[0:3])
#prints Nam
# Placeholders in Strings

#He="Luffy"
#age=7
sent1="%s was just %d years old"
print(sent1 % ("Luffy",7))
print("%s was just %d years old"  % ("Luffy",7) )
He="Luffy"
age=7
print(f"{He} was {age} years old")
#fstrings
x=5
y=6
print(f"sum of x and y = {x + y}")
#result
'''Luffy was just 7 years old
Luffy was just 7 years old
Luffy was 7 years old
sum of x and y = 11
'''
