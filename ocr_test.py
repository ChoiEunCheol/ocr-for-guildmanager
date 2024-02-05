from PIL import Image
import pytesseract
import cv2
import numpy as np

# Tesseract 경로 설정 (Windows의 경우)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 이미지 파일 불러오기 및 크롭하기
image = Image.open('./test_image2.jpg')
# cropped_image = image.crop((455, 150, 525, 565)) #주간점수
cropped_image = image.crop((535, 150, 600, 565)) # 수로
# cropped_image = image.crop((580, 150, 670, 565)) # 플래그


# Pillow 이미지를 OpenCV 이미지로 변환
cropped_image_np = np.array(cropped_image)
cropped_image_cv = cv2.cvtColor(cropped_image_np, cv2.COLOR_RGB2BGR)

# 전처리 시작
# 그레이스케일 변환
gray_image = cv2.cvtColor(cropped_image_cv, cv2.COLOR_BGR2GRAY)

# 이진화
_, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 노이즈 제거를 위한 가우시안 블러 (선택적)
# blur_image = cv2.GaussianBlur(binary_image, (5, 5), 0)

# 이미지에서 텍스트 추출
text = pytesseract.image_to_string(binary_image, lang='eng', config='--psm 6 --oem 3 outputbase digits --dpi 96 --user-patterns my_custom_patterns.txt')

print(text)