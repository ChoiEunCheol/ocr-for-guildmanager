from PIL import Image
import pytesseract

# Tesseract 경로 설정 (Windows의 경우)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 이미지 파일 불러오기
image = Image.open('./example_image1.png')

# 이미지에서 텍스트 추출
text = pytesseract.image_to_string(image, lang='eng+kor')

print(text)