#function
def favanime(namay):
    print("Its " + namay)
    
print("Its the beginning")
favanime("One Piece and Haikyu")

def all_oper(a,b):
    print(a * b)
    print(a-b)
    print(a/b)
    print(a+b)
    print(a%b)
    
print("Its the beginning")
all_oper(32,5)

def fact(n):
    i=1
    factr=1
    while (i<=n):
        factr=factr*i
        i=i+1
    return factr
    
print("Its the beginning")
print(fact(5))
'''
Its the beginning
Its One Piece and Haikyu
Its the beginning
160
27
6.4
37
2
Its the beginning
120
'''
    
def apb(a,b):
    return a+b
def amb(a,b):
    return a-b
def a2mb2(x,y):
    res=x * y
    return res
print("Its the a2mb2")
print(a2mb2(apb(4,2),amb(4,2)))
'''
Its the a2mb2
12
'''
