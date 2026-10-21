# w03_분할정복_최댓값_최솟값 찾기
# 값이 아닌 인덱스로 찾기

def find_min_max(arr, left, right):
    # 인덱스가 같은 위치인지 확인
    # 원소 1개라 비교 필요x
    if left == right:
        min_val = arr[left]
        max_val = arr[left]
        return min_val, max_val
    # 인덱스가 두개 인지 확인 
    # 비교 후 min, max 반환
    elif right - left == 1:
        # 비교
        if arr[left] < arr[right]:
            min_val = arr[left]
            max_val = arr[right]
            return min_val, max_val
        else:
            min_val = arr[right]
            max_val = arr[left]
            return min_val, max_val
    # 배열이 2개 보다 큰 경우 다시 쪼개기
    # 중간값 구하기
    mid = (left + right) // 2

    # ~ mid
    l_min, l_max = find_min_max(arr, left, mid) 
    # mid + 1 ~ 
    r_min, r_max = find_min_max(arr, mid + 1, right)

    # 최종 min, max 구하기
    if l_min < r_min:
        min_val = l_min
    else:
        min_val = r_min

    if l_max < r_max:
        max_val = r_max
    else:
        max_val = l_max

    return min_val, max_val
    

# array
array = [24, 75, 92, 83, 61, 48, 97, 50]
min_arr, max_arr = find_min_max(array, 0, len(array) - 1)
print(f"결과: 최솟값: {min_arr}, 최댓값: {max_arr}")