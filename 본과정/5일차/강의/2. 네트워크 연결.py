# 백준 1922번

class Edge:
    def __init__(self, src, dest, weight):
      self.src = src
      self.dest = dest
      self.weight = weight

    def __it__(self, other):
      return self.weight < other.weight
  

def find(parent, i):
  if parent[i] == i:
      return i
  else : 
      parent[i] = find(parent, parent[i])
      return parent[i]
  
def union(parent, x, y):
  rootX = find(parent, x)
  rootY = find(parent, y)
  if rootX != rootY:
    parent[rootY] = rootX

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    N = int(data[0])
    M = int(data[1])

    edges = []

    for i in range(2, 2 + M):
      A, B, C = map(int, data[i].split())
      edges.append(Edge(A - 1, B - 1, C))

    edges.sort()

    parent = [i for i in range(N)]

    mst_weight = 0
    for edge in edges:
        x = find(parent, edge.src)
        y = find(parent, edge.dest)

        if x != y :
            union(parent, x, y)
            mst_weight += edge.weight

    print(mst_weight)

if __name__ == "__main__":
    main()