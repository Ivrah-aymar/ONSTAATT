#print decimal oct hex binary format of the given number
def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        d=str(i)
        #print(d)
        #print(oct(i))
        o=oct(i)[2:]
        #print(o)
        h=hex(i)[2:].upper()
        b=bin(i)[2:]
        bl=len(bin(number)[2:])
        s=" "
        print(d.rjust(bl,s),o.rjust(bl,s),h.rjust(bl,s),b.rjust(bl,s))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
