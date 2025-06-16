import textwrap

def wrap(string, max_width):
    r=textwrap.fill(string,width=max_width)
    return r
    #n=len(string)
    #m=int(max_width)
    #h=n-m+1
    #print(h)
    #for i in range(0,h,m):
    #while(len(string != 0)):
     #   print(string[i:m])
        #print(string[i])
        #return (string[i:n+1:4])
        
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

"""
Input (stdin)
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Expected Output
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""
