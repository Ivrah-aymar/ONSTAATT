def swap_case(s):
    #new=[]
    lis=list(s)
    for i in range(len(lis)):
        if lis[i].isalpha():
            if lis[i].islower():
                lis[i]=lis[i].upper()
               # print(u)
                #new[i].append(u)
               # print(new)
            else:
                #print(lis[i])
                lis[i]=lis[i].lower()
                #new[i].append(l)
            #new[i].append(lis[i])
            
    return "".join(lis)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
