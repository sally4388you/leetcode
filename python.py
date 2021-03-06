# 1. list comprehesion
l = [x for x in nums if True]

# 2. extended slices
[start:stop:step]

# 3. lambda function: lambda x : expression
k = sorted(k lambda x: k[0])

# 4. stack extend
stack.extend()

# 5. queue
from collections import deque
queue = deque([src])
queue.popleft()
queue.append()

# 6. priority queue
# https://docs.python.org/3/library/heapq.html
import heapq
heap = []
heapq.heappush(heap, (-dist(pt), pt))
heapq.heappop(heap)