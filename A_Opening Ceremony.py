import sys
#10 B6 D3

n, ini, dest= sys.stdin.readline().split()
n= int(n)
r1,r2=ord(ini[0]), ord(dest[0])
c1,c2=int(ini[1]), int(dest[1])

print(n,r1,c1,r2,c2)
if(c1==c2 and r1==r2):
    print(0)
else:
    df1=(n+1)-c1
    df2=(n+1)-c2

    drow= r2-r1
    d=drow+c1+c2
    df=drow+df1+df2

    if(d<df):
        print(d)
    else:
        print(df)