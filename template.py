import cv2
import numpy as np

# 입력 이미지 불러오기
input_image = cv2.imread('cutting3.jpg',0 )  # 입력 이미지 경로

# 템플릿 이미지들의 리스트 생성
templates = [cv2.imread(f'./template/template{i}.jpg', 0) for i in range(10)]

# 임계값 설정
threshold = 0.95

# 매칭 결과를 저장할 리스트
matches = []

# 각 템플릿에 대해 매칭 수행
for idx, template in enumerate(templates):
    res = cv2.matchTemplate(input_image, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    
    # 매칭된 위치에 대한 정보 저장
    for pt in zip(*loc[::-1]):
        matches.append((idx, pt))  # (매칭된 숫자, 위치 좌표)

# y좌표에 따라 매칭 결과를 정렬
matches.sort(key=lambda x: x[1][1])

# 각 줄의 숫자를 추출하기 위해 리스트 생성
lines = []
current_line = []
last_y = 0
line_height = 15  # 숫자 간의 예상 높이를 설정합니다. 이 값은 조정이 필요할 수 있습니다.

for match in matches:
    _, (x, y) = match
    if y - last_y > line_height or not current_line:  # 새로운 줄이 시작됨
        lines.append(current_line)
        current_line = []
    current_line.append(match)
    last_y = y
lines.append(current_line)  # 마지막 줄 추가

# 줄의 시작을 감지하지 못하는 경우를 처리하기 위해 첫 번째 빈 줄을 제거
if lines[0] == []:
    lines = lines[1:]

# 각 줄의 숫자를 x 좌표에 따라 정렬하고 배열로 출력
number_lines = []
for line in lines:
    line.sort(key=lambda x: x[1][0])  # x 좌표에 따라 정렬
    number_line = ''.join(str(num) for num, _ in line)
    number_lines.append(number_line)

# 결과 배열 출력
print(number_lines)