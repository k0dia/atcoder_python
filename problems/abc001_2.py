M = int(input())
VV = ""
m = M/1000

if m < 0.1:
    VV = "00"
elif 0.1 <= m <= 5:
    VV = int(m * 10)
    if VV < 10:
        VV = "0" + str(VV)
elif 6 <= m <= 30:
    VV = str(int(m + 50))
elif 35 <= m <= 70:
    VV = str(int((m - 30) // 5 + 80))
elif 70 < m:
    VV = "89"

print(VV)
