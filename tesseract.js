const Tesseract = require('tesseract.js');
const path = require('path');

const imagePath = path.join(__dirname, './test_image1.jpg'); // 이미지 파일 경로

Tesseract.recognize(
    imagePath,
    'kor', // 또는 다른 언어 코드
    {
        logger: m => console.log(m), // 진행 상황 로그
        rectangle: { left: 520, top: 150, width: 70, height: 450 },// 인식할 영역 지정
        tessedit_char_whitelist: '0123456789', // 숫자만 인식하도록 설정
    }
).then(({ data: { text } }) => {
    console.log(text); // 추출된 텍스트 출력
});
