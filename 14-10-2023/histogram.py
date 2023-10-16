'''l=list(map(int,input().split(" ")))
n=len(l)
for i in range(max(l),0,-1):
    for j in range(n):
        if l[j]>=i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

l=list(map(int,input().split(" ")))
maxele=max(l)
for i in range(maxele,-1,-1):
    print(f"{i:2d} |",end="")
    for j in l:
        if j>=i:
            print(" * ",end="")
        else:
            print("   ",end="")
    print()