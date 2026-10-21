# w04_선택 정렬 구현

# partition
def partition(arr, left, right): 
    pivot = arr[left]
    i = left + 1 # low의 인덱스    
    j = right # high의 인덱스

    while i <= j :
        while i <= j and arr[i] <= pivot: # l < p , p < l 이면 탈출
            i += 1 
        while i <= j and arr[j] > pivot: # h > p , p > h 면 탈출
            j -= 1

        if(i < j): 
            arr[i], arr[j] = arr[j], arr[i] # low <-> high 위치 변경


    arr[left], arr[j] = arr[j], arr[left] 

    return j

# selection
# 피봇보다 작은 값을 찾은 수 1회전 후(파티션)
# 찾아야 할 수의 위치값 확인 후 해당하는 부분만 추가 정렬
# 배열, 왼쪽 인덱스, 오른쪽 인덱스, 찾을 위치)
def selection(arr, left, right, k):
    r = partition(arr, left, right)

    if r == k:
        return arr[k]
    elif r < k:
        return selection(arr, r + 1, right, k) # 오른쪽 탐색
    else:
        return selection(arr, left, r - 1, k) # 왼쪽 탐색




array = [8, 1, 15, 11, 4, 3, 14, 6, 16, 9]
result = selection(array, 0, len(array) - 1, 8)
print(f"8번째로 작은 수: {result}")






