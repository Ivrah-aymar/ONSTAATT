if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sarr=sorted(list(set(arr)))
    print(sarr[len(sarr)-2])
