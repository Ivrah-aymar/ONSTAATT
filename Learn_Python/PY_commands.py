if __name__ == '__main__':
    N = int(input())
    lst1=[]
    for i in range(1,N+1):
        l1=input()
        sps=l1.split(" ")
       # print(sps)
        sp1=list(map(int,sps[1:]))
       # print(sp1)
        if sps[0] == 'insert':
            lst1.insert(int(sp1[0]),int(sp1[1]))
        if sps[0] == 'append':
            lst1.append(sp1[0])
        if sps[0] == 'sort':
            #print(type(lst1))
            #print("sort",lst1)
            lst1=sorted(lst1)
            #print("af srt",lst1)
        if sps[0] == 'pop':
            lst1.pop()
        if sps[0] == 'reverse':
            lst1.reverse()
        if sps[0] == 'remove':
            try:
                lst1.remove(sp1[0])
            except:
                pass
        if sps[0] == 'print':
            print(lst1)                
