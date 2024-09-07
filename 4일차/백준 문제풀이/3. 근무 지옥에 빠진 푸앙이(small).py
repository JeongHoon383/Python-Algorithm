n = int(input())  # 주의 개수

work_time = {}  # 각 사람의 근무 시간을 저장할 딕셔너리

# 각 근무 시간대에 해당하는 시간
shift_hours = [4, 6, 4, 10]

for _ in range(n):  # 주의 개수만큼 반복
    for shift in range(4):  # 4개의 근무 시간대
        shifts = input().split()  # 근무자 목록 입력받기
        for person in shifts:
            if person != "-":  # 근무자가 있을 경우
                if person not in work_time:
                    work_time[person] = 0  # 처음 등장하는 근무자는 근무시간을 0으로 초기화
                work_time[person] += shift_hours[shift]  # 해당 시간대의 근무시간을 추가
print(work_time)
# 근무 시간이 기록된 딕셔너리의 길이가 0이면 아무도 근무하지 않은 경우
if not work_time:  # work_time이 빈 딕셔너리일 경우
    print("YES")
else:
    # 최대와 최소 근무시간 차이를 계산
    max_time = max(work_time.values())
    min_time = min(work_time.values())
    # 근무시간 차이가 12시간 이하인지 확인
    if max_time - min_time <= 12:
        print("YES")
    else:
        print("NO")




