#def maxarray(arr):
#    return max(arr)
#arr = [2,5]
#print(maxarray(arr))
print(len(arr))
def maxarray(arr):
    res=arr[0]
    for i in range(len(arr)):
        cursum=0
#        print("i",i)
        for j in range(i,len(arr)):
#            if i==len(arr):
#                break;
#            print("j",j)
#            print("arr[j]=",arr[j])
            cursum=cursum+arr[j]
            res=max(res,cursum)
#            print("res=",res)
    return res
#arr=[-2,-4]
#-2
#arr=[5, 4, 1, 7, 8]
#25
arr=[2, 3, -8, 7, -1, 2, 3]
#11
print(arr)
print(maxarray(arr))
