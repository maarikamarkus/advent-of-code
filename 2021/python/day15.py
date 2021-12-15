import heapq
from math import inf
from collections import defaultdict

def neighbours(y, h, x, w):
  ns = []
  for diff_y, diff_x in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
    new_y, new_x = (y + diff_y, x + diff_x)
    if 0 <= new_y < h and 0 <= new_x < w:
      ns.append((new_y, new_x))
  return ns

def dijkstra():
  w, h = len(graph[0]), len(graph)
  source = (0, 0)
  destination = (h - 1, w - 1)

  heap = [(0, source)]
  min_dist = defaultdict(lambda: inf, {source: 0})
  visited = set()

  while heap:
    dist, node = heapq.heappop(heap)
    if node == destination:
      return dist
    
    if node in visited:
      continue

    visited.add(node)

    for n in (list(filter(lambda x: x not in visited, neighbours(node[0], h, node[1], w)))):
      new_dist = dist + graph[n[0]][n[1]]

      if new_dist < min_dist[n]:
        min_dist[n] = new_dist
        heapq.heappush(heap, (new_dist, n))

  return inf 



with open('../data/day15-input.txt') as f:
  graph = [list(map(int, line.strip())) for line in f.readlines()]

print("Part I:", dijkstra())

tile_w = len(graph)
tile_h = len(graph[0])

for _ in range(4):
  for row in graph:
    extension = row[-tile_w:]
    row.extend((x + 1) if x < 9 else 1 for x in extension)

for _ in range(4):
  for row in graph[-tile_h:]:
    row = [(x + 1) if x < 9 else 1 for x in row]
    graph.append(row)

print("Part II: ", dijkstra())