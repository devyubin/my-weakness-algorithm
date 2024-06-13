# 카드 2
from collections import deque
n = int(input())
cards = deque([i+1 for i in range(n)])

while len(cards) > 1:
    # 한개는 버림
    cards.popleft()
    # 한개는 제일 아래로
    cards.rotate(-1)

print(cards[0])