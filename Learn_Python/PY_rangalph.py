#rangoli with alphabets
import string
def print_rangoli(size):
    # your code goes here
    width=4 * size - 3
    lines=[]
    for row in range(size):
        pr="-".join(string.ascii_lowercase[row:size])
        line=(pr[::-1]+pr[1:]).center(width,'-')
        lines.append(line)
    #print(lines)
    for line in lines[::-1]:
        print(line)
    for line in lines[1:]:
        print(line)
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
