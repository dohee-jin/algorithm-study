# w04_부분배낭 문제 구현
# 단위 무게당 가장 가치있는 물건을 배낭에 넣음


def fractional_knapsack(W, items):

    # 단위 무게당 가치 구하기
    ratio = []
    for w, v, id in items:
        ratio.append((v / w, w, v, id))

    # 단위 무게당 가치 순으로 정렬
    # ratio= [(6.0, 10, 60) ...]
    for i in range(len(ratio)):
        for j in range(len(ratio) - i - 1):
            if ratio[j][0] < ratio[j + 1][0]:
                ratio[j], ratio[j+1] = ratio[j+1], ratio[j]

    # 배낭 담기
    total = 0.0
    selected_items = []
    i = 0
    while i < len(ratio) and W > 0:
        vw, w, v, id = ratio[i]
        if W >= w:
            W -= w
            total += v
            selected_items.append({"물건": id, "담은무게": w, "비율": "100%"})
        else:
            fraction = W / w
            total = total + v * fraction
            selected_items.append({"물건": id, "담은무게": W, "비율": f"{fraction * 100:.0f}%"})
            W = 0
        i += 1

    return total, selected_items

        
# 아이템(무게, 가치)
items = [(10, 60, "A"), (40, 40, "B"), (20, 100, "C"), (30, 120, "D")]
result, selected = fractional_knapsack(50, items)
print(f"배낭에 담은 가치: {result}")
print("-- 선택된 물건 리스트 --")
for item in selected:
    print(f"- {item['물건']}: {item['담은무게']}만큼 담음 ({item['비율']})")