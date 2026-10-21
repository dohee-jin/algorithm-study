# w03_분할정복_합병정렬
def merge_sort(arr, left, right):
    # 배열의 크기가 0 또는 1인 경우 이미 정렬된 것으로 본다
    if left >= right:
        return arr
    
    # 배열의 크기가 1보다 큰 경우
    mid = (left + right) // 2
    # ~ mid
    merge_sort(arr, left, mid)
    # mid + 1 ~ 
    merge_sort(arr, mid + 1, right)

    # 합치기(merge)


            


array = [37, 10, 22, 30, 35, 13, 25, 24]
merge_sort(array, 0, len(array) - 1)