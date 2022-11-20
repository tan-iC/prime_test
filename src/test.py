
ans = [2]
MAX = 10
tgt = 3

while (len(ans) < MAX):

    tmp = 0
    idx = len(ans)
    for i in range(idx):
        num = ans[i]
        if ((tgt % num) == 0):
            tmp = 1
            break
    if (tmp == 0):
        ans.append(tgt)

    tgt += 2

print(ans)
