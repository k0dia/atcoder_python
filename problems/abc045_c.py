S = input()
n = len(S)-1
ans = 0
for i in range(1 << n):
    p = 0
    for j in range(n):
        if i >> j & 1 == 0:
            continue
        else:
            ans += int(S[p:j+1])
            p = j+1
    ans += int(S[p:])

print(ans)