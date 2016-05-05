# for each testcase
for i in range(1,int(input())+1):
    temp=list(map(int,input().split()))
    nFLang=temp[0]
    N=temp[1]
    FLang=list(input().split())
    bFLang=["NO"] * nFLang
    allwords=[]
    #for each lang phrases
    for j in range(0, N):
        allwords=allwords + input().split()
        res=''
    for k in range(nFLang):
        if(FLang[k] in allwords):
            res=res + 'YES '
        else:
            res=res+ 'NO '

    print(res.strip())

        
