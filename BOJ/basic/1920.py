# 수 찾기
n = int(input())
a_list = list(map(int, input().split()))
m = int(input())
num_list = list(map(int, input().split()))
a_list.sort()

for num in num_list:
    lt, rt = 0, n - 1
    isExist = False

    while lt <= rt:
        mid = (lt + rt) // 2
        if num == a_list[mid]:
            isExist = True
            print(1)
            break
        elif num > a_list[mid]:
            lt = mid + 1
        else:
            rt = mid - 1

    if not isExist:
        print(0)