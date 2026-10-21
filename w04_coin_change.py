# w04_동전 거스름돈 구현

def coin_change(w):
    n25 = n10 = n5 = n1 = 0
    
    while w >= 25:
        w -= 25
        n25 += 1

    while w >= 10:
        w -= 10
        n10 += 1

    while w >= 5:
        w -= 5
        n5 += 1

    while w >= 1:
        w -= 1
        n1 += 1

    return n25, n10, n5, n1

change = 68
r25, r10, r5, r1 = coin_change(change)
print(f"거스름돈: 25센트-{r25}개 / 10센트-{r10}개 / 5센트-{r5}개 / 1센트-{r1}개")