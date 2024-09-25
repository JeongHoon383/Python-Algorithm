# 문제 분석
# 1. 정수를 저장하는 덱을 구현
# 2. 첫번째 줄은 명령의 수, 두번째 줄은 명령 과 정수가 주어진다.
# 3. 명령에 맞춰서 값을 출력한다. 

# 입력
# 첫번째 줄 : 명령의 수
# 두번째 줄 : 명령 하나씩 주어짐

# 의사결정
# 정수를 저장하는 데크를 구현
# 명령어에 맞춰서 조건문으로 출력


from sys import stdin
from collections import deque;

N = int(stdin.readline())
deck = deque() # 명령어의 값 저장소

for _ in range(N):
  my_list = list(map(str, stdin.readline().split()))
  if(my_list[0] == "push_front"):
    deck.appendleft(my_list[1])
  elif(my_list[0] == "push_back") : 
    deck.append(my_list[1])
  elif(my_list[0] == "pop_front"):
    # 덱의 가장 앞에있는 수를 뺌
    if(len(deck) == 0):
      print(-1)
    else:
      print(deck.popleft())
  elif(my_list[0] == "pop_back"):
    if(len(deck) == 0):
      print(-1)
    else:
      print(deck.pop())
  elif(my_list[0] == "size"):
    print(len(deck))
  elif(my_list[0] == "empty"):
    if(len(deck) == 0):
      print(1)
    else : print(0)
  elif(my_list[0] == "front"):
    # 덱의 가장 앞에 있는 정수 출력
    if(len(deck) == 0):
      print(-1)
    else:
      print(deck[0])
  elif(my_list[0] == "back"):
    if(len(deck) == 0):
      print(-1)
    else:  
      print(deck[len(deck) - 1])
    