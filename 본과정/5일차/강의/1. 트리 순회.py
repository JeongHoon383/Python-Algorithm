# 백준 1991번

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    # TreeNode 클래스: value(값), left(왼쪽 자식), right(오른쪽 자식) 노드를 가지는 트리의 기본 구조를 정의합니다.
    # 생성자는 노드의 값(value)을 초기화하고, 왼쪽과 오른쪽 자식 노드는 초기값으로 None으로 설정합니다.

def pre_order_traversal(node):
  if node is None:
    return
  # 전위 순회(pre-order): 루트 → 왼쪽 자식 → 오른쪽 자식 순서로 탐색
  print(node.value, end='') 
  # 현재 노드의 값을 출력
  pre_order_traversal(node.left)
  # 왼쪽 자식을 재귀적으로 탐색
  pre_order_traversal(node.right)
  # 오른쪽 자식을 재귀적으로 탐색

def in_order_traversal(node):
  if node is None:
    return
  # 중위 순회(in-order): 왼쪽 자식 → 루트 → 오른쪽 자식 순서로 탐색
  in_order_traversal(node.left)
  # 왼쪽 자식을 먼저 재귀적으로 탐색
  print(node.value, end='')
  # 그 다음 현재 노드의 값을 출력
  in_order_traversal(node.right)
  # 마지막으로 오른쪽 자식을 재귀적으로 탐색

def post_order_traversal(node):
  if node is None:
    return
  # 후위 순회(post-order): 왼쪽 자식 → 오른쪽 자식 → 루트 순서로 탐색
  post_order_traversal(node.left)
  # 왼쪽 자식을 먼저 재귀적으로 탐색
  post_order_traversal(node.right)
  # 오른쪽 자식 재쉬적으로 탐색
  print(node.value, end='')
  # 마지막으로 현재 노드의 값 출력

def main():
  import sys
  input = sys.stdin.read
  # sys.stdin.read: 전체 입력을 한 번에 받기 위한 함수 (여러 줄 입력을 받을 때 사용)
  data = input().splitlines()
  # 입력 데이터를 줄 단위로 분리하여 리스트 형태로 저장

  N = int(data[0])
  # 첫 번째 줄에는 트리의 노드 개수(N)를 저장

  nodes = {}
  # 각 노드를 저장할 딕셔너리. key는 노드 값, value는 TreeNode 객체로 저장

  for i in range(1, N + 1):
    # 두 번째 줄부터 N개의 줄까지 각 노드의 정보가 주어짐
    node_info = data[i].split()
    # 여기에 A B C 를 받아줌
    # 현재 줄의 정보를 공백 기준으로 분리 (root, left, right)

    root = node_info[0]
    left = node_info[1]
    right = node_info[2]
    # 현재 노드(root)와 그 왼쪽 자식(left), 오른쪽 자식(right) 정보를 변수에 저장

    if root not in nodes:
      nodes[root] = TreeNode(root)
    # root가 딕셔너리에 없으면 새로운 TreeNode 객체를 만들어 저장
    # 키를 저장하는것 까지 이해, 값이 왜 이런식으로 담기는지 이해 안감
    rootNode = nodes[root]
    # rootNode에 root에 해당하는 노드 객체를 저장

    if left != '.':
      if left not in nodes:
        nodes[left] = TreeNode(left)
      rootNode.left = nodes[left]
    # left가 '.'이 아닌 경우, 즉 왼쪽 자식 노드가 존재할 때,
    # 딕셔너리에 left가 없으면 새로운 TreeNode 객체를 만들어 저장하고,
    # rootNode의 left 속성에 해당 노드를 연결

    if right != '.':
      if right not in nodes:
        nodes[right] = TreeNode(right)
      rootNode.right = nodes[right]
    # right도 마찬가지로 '.'이 아닌 경우, 오른쪽 자식 노드를 생성 또는 연결

    root = nodes['A']
    # 'A'는 루트 노드이므로 루트 노드를 지정

    pre_order_traversal(root)
    # 전위 순회 출력
    print()
    # 한 줄 출력 후 줄바꿈

    in_order_traversal(root)
    # 중위 순회 출력
    print()
    # 한 줄 출력 후 줄바꿈

    post_order_traversal(root)
    # 후위 순회 출력
    print()
    # 한 줄 출력 후 줄바꿈

if __name__ == "__main__":
  main()
  # 스크립트가 직접 실행될 때 main 함수를 실행
