# 유클리드 최대공약수 알고리즘
# 재귀함수로 구현

# 유클리드 최대 공약수
# 2개의 자연수의 최대공약수는 큰 수에서 작은 수를 뺀 수와 작은 수의 최대공약수와 같다.
# a > b 라고 가정
def euclidean (a, b):
    if (a == b): return a
    if (a > b):
        return euclidean(a-b, b)
    else:
        return euclidean(b-a, a)


print(euclidean(20, 12))