S = input()

ans = ""

for s in S:
    if s == "0":
        ans += s
    elif s == "1":
        ans += s
    elif s == "B":
        ans = ans[:-1]

print(ans)