if __name__ == '__main__':
    newd={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        newd[name]=score
    valu=newd.values()
    vall=list(set(valu))
    vald=sorted(vall)
    keys=[]
    for key,val in newd.items():
        if val == vald[1]:
           keys.append(key)
           
    for i in sorted(keys):
         print(i)      
