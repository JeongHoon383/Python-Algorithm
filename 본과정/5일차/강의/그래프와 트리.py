# 그래프

class GraphAdjMatrix:
  def __init__(self, vertices):
    self.vertices = vertices
    self.adj_matrix = [[0] * vertices for _ in range(vertices)]

  def add_edge(self, src, dest):
    self.adj_matrix[src][dest] = 1
    self.adj_matrix[dest][src] = 1

  def remove_edge(self, src, dest):
    self.adj_matrix[src][dest] = 0
    self.adj_matrix[dest][src] = 0

  def is_edge(self, src, dest):
    return self.adj_matrix[src][dest] != 0
  
class GraphAdjList:
  def __init__(self, vertices):
    self.vertices = vertices
    self.adj_list = [[] for _ in range(vertices)]

  def add_edge(self, src, dest):
    self.adj_list[src].append(dest)
    self.adj_list[dest].append(src)

  def remove_edge(self, src, dest):
    self.adj_list[src].remove(dest)
    self.adj_list[dest].remove(dest)

  def is_edge(self, src, dest):
    return dest in self.adj_list[src]
  
  # 트리

  class BinaryTree:
    def __init__(self, size):
      self.size = size
      self.tree = [None] * size

    # 루트 노드 값 설정
    def set_root(self, value):
      self.tree[0] = value

    # 왼쪽 자식 값 설정(2 * i + 1)
    def set_left(self, parent_index, value):
      left_index = 2 * parent_index + 1
      if left_index < self.size:
        self.tree[left_index] = value
      else : 
        print("Index out of bounds for left child")

    # 오른쪽 자식 값 설정(2 * i + 2)
    def set_right(self, parent_index, value):
      right_index = 2 * parent_index + 2
      if right_index < self.size:
        self.tree[right_index] = value
      else:
        print("Index out of bounds for right child")

# 트리 인스턴스 생성
bt = BinaryTree(7) # 7의 정점 
bt.set_root(1)
bt.set_left(0, 2) 
bt.set_right(0, 3)
bt.set_left(1, 4)
bt.set_right(1, 5)
bt.set_left(2, 6)
bt.set_right(2, 7)

class Edge:
  def __init__(self, src, dest, weight):
    self.src = src
    self.dest = dest
    self.weight = weight

# 크루스칼 알고리즘
class Kruskal:
  def __init__(self, vertices, edges):
    self.V = vertices
    self.E = edges
    self.edges = []

  def find(self, parent, i):
    if parent[i] == -1:
      return i
    return self.find(parent, parent[i])
  
  def union(self, parent, x, y):
    xset = self.find(parent, x)
    yset = self.find(parent, y)
    if xset != yset:
      parent[xset] = yset

  def mst(self):
    self.edges.sort()
    parent = [-1] * self.V
    mst = []

    for edge in self.edges:
      x = self.find(parent, edge.src)
      y = self.find(parent, edge.dest)

      if x != y:
        mst.append(edge)
        self.union(parent, x, y)

    print("Following are the edges in the constructed MST")
    for edge in mst:
      print(f"{edge.src} -- {edge.dest} == {edge.weight}")

def main():
  V = 4
  E = 5
  graph = Kruskal(V, E)

  graph.edges.append(Edge(0, 1, 10))
  graph.edges.append(Edge(0, 2, 6))
  graph.edges.append(Edge(0, 3, 5))
  graph.edges.append(Edge(1, 3, 15))
  graph.edges.append(Edge(2, 3, 4))

  graph.mst()

if __name__ == "__main__":
  main()