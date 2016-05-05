for t in range(0,int(input())):
    N=list(map(int,input().split()))
    N.sort()
    a=N[1]
    b=N[0]
    c=0
    while(b!=0):
        a,b=b,a%b
    gcd=a
    lcm=(N[0]*N[1])/gcd
    print(gcd,int(lcm))
