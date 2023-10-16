#find the target sum elements
l=list(map(int,input().split()))
target=int(input())
i=0;
currentsum=l[0]
j=0
while j<len(l):
    if currentsum==target:
        print(i,j,currentsum)
        break
    elif currentsum>target:
        currentsum-=l[i]
        i+=1
    else:
        j+=1
        currentsum+=l[j]