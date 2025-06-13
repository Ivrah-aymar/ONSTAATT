if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lisn=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                lis=[i,j,k]
                if i+j+k != n:
                    lisn.append(lis)
    print(lisn)
