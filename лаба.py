n, x, k = map(int, input().split())
s = 0
days = 1
for i in range(n):
    a = int(input())
    s+=a
    if s>k+x:
        days+=1
        s-=k+x
print(days*2)
