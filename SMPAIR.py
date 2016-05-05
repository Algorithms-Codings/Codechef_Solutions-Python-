for t in range(0,int(input())):
    N=int(input())
    L=list(map(int,input().split()))
    L.sort()
    print(L[0]+L[1])

