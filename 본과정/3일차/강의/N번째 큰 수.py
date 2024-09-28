import heapq

n = int(input())
min_heap = []
cnt = n * n # ?

for _ in range(cnt):
  num = int(input())
  if len(min_heap) < n:
    heapq.heappush(min_heap, num)
  elif min_heap[0] < num:
    heapq.heappop(min_heap)
    heapq.heappush(min_heap, num)

print(min_heap[0])