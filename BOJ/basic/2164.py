# 카드 2
from collections import deque

n = int(input())

cards = deque()

for i in range(n):
    cards.append(i+1)
# TODO: 간단하게
# cards = deque(range(1, n + 1))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])