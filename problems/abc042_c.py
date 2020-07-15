N , K = map(int, input().split())
Dk = input().split()

for i in range(N,10*N+1):
    if set(str(i))&set(Dk) == set():
        print(i)
        break
