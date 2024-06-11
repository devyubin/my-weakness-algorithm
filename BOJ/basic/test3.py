# heap basic
import heapq

list = [32, 16, 54, 94, 81, 31]
heapq.heapify(list)

heapq.heappush(list, 7)
print(heapq.heappop(list))

print(heapq.heappushpop(list, 100))

small_elements = heapq.nsmallest(4, list)
print(small_elements)

large_elements = heapq.nlargest(4, list)
print(large_elements)