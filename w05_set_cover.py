# w05_집합 커머 문제

def set_cover(u, f):
    uncoverd = set(u)
    chosen = []
    while uncoverd:
        best = None
        best_count = -1
        for k, s in f.items():
            count = len(uncoverd & set(s)) # &연산으로 동일한, 커버 가능한 원소의 개수만 셈
            if count > best_count:
                best = k
                best_count = count

            if best is None:
                raise ValueError(f"커버 불가: {uncoverd}")

            gain = uncoverd & f[best]
        chosen.append(best)
        uncoverd -= gain

    return chosen 

# 전체 집합
u = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
f = {
    "학원1": {'a', 'b', 'd', 'f', 'g'},
    "학원2": {'c', 'f', 'h', 'i'},
    "학원3": {'a', 'g', 'h'},
    "학원4": {'b', 'c', 'e', 'g', 'h'},
    "학원5": {'c', 'd', 'i'},
    "학원6": {'e', 'j'}

}
result = set_cover(u, f)
print(f"근사해: {result}")