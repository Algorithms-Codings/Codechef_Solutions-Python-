for t in range(0,int(input())):
    temp=list(map(int,input().split()))
    coins=temp[0]
    mbarking=temp[1]
    ncoins=[coins%i for i in range(1,mbarking+1)]
    ncoins.sort()
    print(ncoins[len(ncoins)-1])

    
    
