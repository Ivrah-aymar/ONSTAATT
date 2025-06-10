if __name__ == '__main__':
    s = input()
    an=0
    al=0
    di=0
    lo=0
    up=0
    #print(len(s))
    for i in range(len(s)):
        if s[i].isalnum():
            an=an+1
        if s[i].isalpha():
            al=al+1
        if s[i].isdigit():
            di=di+1
        if s[i].islower():
            lo=lo+1
        if s[i].isupper():
            up=up+1
    res1=True if an>0 else False  
    res2=True if al>0 else False
    res3=True if di>0 else False
    res4=True if lo>0 else False
    res5=True if up>0 else False
    print(res1)
    print(res2)
    print(res3)
    print(res4)
    print(res5)           
