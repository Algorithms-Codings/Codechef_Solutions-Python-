for t in range(0,int(input())):
    nDolls=int(input())
    misDoll=[]
    for x in range(0,nDolls):
        doll=int(input())
        if(doll in misDoll):
            misDoll.remove(doll)
        else:
            misDoll.append(doll)
    print(misDoll[0])
