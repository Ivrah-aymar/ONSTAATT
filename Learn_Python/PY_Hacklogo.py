m=int(input())
lm=int((m-2)/2)
lm1=int((m+1)/2)
#print(lm)
for i in range(1,m*2,2):
    h1=i*'H'
    print(h1.center(m*2," "))
for j in range(m+1):
    h2=m*'H'
    print(" "*lm,(h2.ljust(m," "))," "*(m*3-2),(h2.rjust(m," ")))
for k in range(1,lm1+1):
    print(" "*lm,m*5*'H')
for j in range(m+1):
    h3=m*'H'
    print(" "*lm,(h3.ljust(m," "))," "*(m*3-2),(h3.rjust(m," ")))
for l in range(m*2,1,-2):
    h4=(l-1)*'H'
    #print(" "*(l+4),h4.center(m*2," "))
    print(" "*(m*4-1),h4.center(m*2," "))  
