for i in range(1,int(input())+1):
    rooms=int(input())
    rcolors=raw_input()
    rcount=rcolors.count('R')
    bcount=rcolors.count('B')
    gcount=rcolors.count('G')
    l=[rcount,bcount,gcount]
    l.sort()
    print(l[0]+l[1])
