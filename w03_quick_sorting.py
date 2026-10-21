# w03_분할정복 퀵정렬 구현
# pivot < low / pivot > high -> low <-> high 교환

# partition
def partition(arr, left, right): 
    pivot = arr[left]
    i = left + 1 # low의 인덱스    
    j = right # high의 인덱스

    # 예) 5(pivot), 3, 9(low), 2(high), 7(high)
    while i <= j :
        while i <= j and arr[i] <= pivot: # l < p , p < l 이면 탈출
            i += 1 
        while i <= j and arr[j] > pivot: # h > p , p > h 면 탈출
            j -= 1

        if(i < j): 
            arr[i], arr[j] = arr[j], arr[i] # low <-> high 위치 변경


    arr[left], arr[j] = arr[j], arr[left] 

    return j

# quick_sort
def quick_sort(arr, left, right):

    if(left >= right): return 
    p = partition(arr, left, right)
    quick_sort(arr, left, p - 1) # low
    quick_sort(arr, p + 1, right) # high

    return arr, p

    

# array
# 1회 -> [17, 9, 13, 25, 5, 4, 35, 71, 53, 42]
# [17, 9, 13, 25, 5, 4] / [71, 53, 42]
# 
array = [35, 53, 25, 5, 4, 71, 17, 13, 9, 42]
test = [5, 3, 9, 2, 7]
p = quick_sort(test, 0, len(test) - 1) # 인덱스 값을 넘겨야함
print(f"결과: {p[0]}, 회전횟수: {p[1]}")


