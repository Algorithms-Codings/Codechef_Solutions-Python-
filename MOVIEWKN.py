for i in range(1,int(input())+1):
    N=int(input())
    L=list(map(int,input().split()))
    R=list(map(int,input().split()))
    val=[]
    maxval=0
    maxindex=-1
    for j in range(0,N):
        temp=L[j]*R[j]
        if(temp>maxval):
            maxval=temp
            maxindex=j
        elif(temp==maxval):
            if(R[j]>R[maxindex]):
                maxval=temp
                maxindex=j
    print(maxindex+1)
    
