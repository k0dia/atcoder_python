N, M = map(int, input().split())
A = map(int, input().split())

NS = {key:0 for key in range(1,N+1)}
sushi_result = [-1]*M

i = 0
for ai in A:
    for n, s in NS.items():
        if s < ai:
            sushi_result[i] = n
            NS[n] = ai
            break
    i += 1

print(sushi_result)

