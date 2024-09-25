from collections import deque  # 덱을 사용하기 위해 collections 모듈에서 deque를 불러옴

testCases = int(input())  # 테스트 케이스 개수를 입력받음

for _ in range(testCases):
    n, m = map(int, input().split())  # n: 문서의 개수, m: 우리가 찾고 싶은 문서의 index

    queue = deque()  # 문서의 인덱스와 우선순위를 저장할 큐
    priorities = [0] * 9  # 우선순위가 1부터 9까지이므로, 우선순위 카운트를 저장하는 리스트 (0 ~ 8까지 사용)

    documents = list(map(int, input().strip().split()))  # 각 문서의 우선순위를 리스트로 입력받음
    for i in range(n):
        priority = documents[i]  # i번째 문서의 우선순위
        queue.append((i, priority))  # (문서의 인덱스, 우선순위)를 큐에 저장
        priorities[priority - 1] += 1  # 해당 우선순위의 문서 개수를 증가

    printOrder = 0  # 출력 순서를 기록하는 변수

    while queue:  # 큐가 빌 때까지 반복
        current = queue.popleft()  # 큐의 맨 앞에 있는 문서를 꺼냄
        hasHigherPriority = False  # 더 높은 우선순위의 문서가 있는지 체크하는 변수

        for i in range(current[1], 9):  # 현재 문서의 우선순위보다 높은 우선순위를 확인 (current[1]은 우선순위)
            if priorities[i] > 0:  # 더 높은 우선순위의 문서가 남아있으면
                hasHigherPriority = True  # 더 높은 우선순위의 문서가 존재함을 표시
                break  # 반복문 종료

        if hasHigherPriority:  # 더 높은 우선순위의 문서가 있다면
            queue.append(current)  # 현재 문서를 다시 큐의 맨 뒤에 넣음
        else:  # 더 높은 우선순위의 문서가 없다면
            printOrder += 1  # 출력 순서를 증가
            priorities[current[1] - 1] -= 1  # 현재 문서의 우선순위 개수를 감소
            if current[0] == m:  # 현재 문서가 우리가 찾던 m번째 문서라면
                print(printOrder)  # 출력 순서를 출력
                break  # 반복 종료
