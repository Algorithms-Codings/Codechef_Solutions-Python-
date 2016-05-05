for i in range(1,int(input())+1):
    rcolors=input()
    acount=rcolors.count('a')
    bcount=rcolors.count('b')
    if(acount>bcount):
        print(bcount)
    else:
        print(acount)

