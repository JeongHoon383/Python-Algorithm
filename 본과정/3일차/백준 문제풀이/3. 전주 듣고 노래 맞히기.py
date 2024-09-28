# 문제 분석
# 정환은 첫 세음만으로 노래 제목을 맞춰야됨
# 정환은 음을 아는 노래가 N개
# 첫 세 음으로 시작하는 노래가 여러개 있어 노래를 알 수 없는 경우 ? 출력
# 첫 세 음에 맞는 저장된 노래가 없을 경우 !를 출력

# 입력
# 첫번째 줄 : N = 음을 아는 노래의 개수, M = 맞추기를 시도할 노래 개수
# 두번째 줄부터 N 개 줄에 걸쳐서 노래 제목의 길이 T , 영어 대소문자로 이루어진 문자열 노래제목 S
# 처음 등장하는 일곱개의 음이름 a1~a7 공백으로 구분 됫 ㅓ주어짐

# N+2 번째 줄부터 M 개 줄에 걸쳐서 정환이가 맞히기를 시도할 노래의 첫 세음 b1~b3 a1~a7, b1~b3 = cdefgab
# 같은 제목 두번 이상 x



#출력 : 맞힌기를 시도할 노래에 대하여 프로그램에 저장된 노래와 첫 세음이 동일한 노래가 하나만 있따면 해당 노래 제목을,
# 만약 두개 이상 있다면 ?
# 없으면 !



N, M = map(int, input().split())  # N, M

song = {}

for _ in range(N):
    T, S, a1, a2, a3, a4, a5, a6, a7 = input().split()
    first_3_A = [a1, a2, a3]
    song[S] = first_3_A
    # song = {"TwinkleStar": [C, C, G], "Marigold": [E, D, E]... }

for _ in range(M):
    first_3_B = input().split()
    count = 0
    title = ""  # 노래 제목 저장할 변수

    for s in song:
        if first_3_B == song[s]:  # 세 음이 같으면
            count += 1
            title = s

    if count >= 2:
        print("?")
    elif count == 1:
        print(title)
    else:
        print("!")
