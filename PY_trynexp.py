#try and except
try:
    a=4
    if a>3:
        print("a is greater than 3")
except:
    print("an error occured")
'''
a is greater than 3
'''
try:
    a=nosense
    if a>3:
        print("a is greater than 3")
except:
    print("an error occured")
'''
an error occured
'''
