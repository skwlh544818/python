from collections import defaultdict
def choice():
    n=int(input())
    a=input().split()
    if n<1 or n!=len(a) or len(a)%2==0:
        return '-1'
    m=defaultdict(int)
    for i in a:
        m[i]+=1
    for i in a:
        if m[i]%2==1:
            return i
print(choice())