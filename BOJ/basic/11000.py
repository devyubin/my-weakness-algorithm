# 강의실 배정
# (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.
import sys
import heapq
heap_class = []
arr = []
cnt = 0

n = int(sys.stdin.readline())
for _ in range(n):
    s, t = map(int, sys.stdin.readline().split())
    arr.append([s,t])

# arr 정렬
arr.sort(key=lambda x: x[0])
# 첫번째 강의가 끝나는 시간
heapq.heappush(heap_class, arr[0][1])
for i in range(1, n):
    # 현재 가장 작은 시작 시간이 리스트의 시작 시간보다 크다면
    if heap_class[0] > arr[i][0]:
        # 새로운 수업 생성
        heapq.heappush(heap_class, arr[i][1])
    # 하나의 클래스로 만들기
    else:
        heapq.heappop(heap_class)
        heapq.heappush(heap_class, arr[i][1])
print(len(heap_class))