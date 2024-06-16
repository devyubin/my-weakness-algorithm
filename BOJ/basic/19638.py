# 센티와 마법의 뽕망치
# 시간 초과
import sys
import heapq
n, h, t = map(int, sys.stdin.readline().split())
people = []

# 모든 거인이 센티보다 키가 작도록 할 수 있는 경우 YES
# 가장 키가 큰 거인 가운데 하나 - 뿅망치에 맞은 사람의 키 / 2
for i in range(n):
    p = int(sys.stdin.readline()) * -1
    heapq.heappush(people, p)
cnt = 0

# 키가 1인 경우
if heapq.nsmallest(1, people)[0] == 1:
    print("NO")
    print(int(heapq.heappop(people) * -1))
    exit()
else:
    for i in range(t):
        person = heapq.heappop(people)
        person //= 2
        heapq.heappush(people, person)
        cnt += 1
        if (heapq.nsmallest(1, people)[0] * -1) < h:
            # 사용한 뽕망치 횟수 출력
            print("YES")
            print(cnt)
            exit()

# 여전히 거인이 더 큰 경우
print("NO")
print(int(heapq.heappop(people) * -1))