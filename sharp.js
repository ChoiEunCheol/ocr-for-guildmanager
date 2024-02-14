const sharp = require('sharp');

// 이미지 파일 경로
const inputImagePath = './test_image2.jpg';
const outputImagePath = './cutting3.jpg';

// 이미지 자르기
sharp(inputImagePath)
  .extract({ left: 528, top: 151, width: 60, height: 415 }) // 자를 영역 지정
  .threshold(120) // 임계값 설정 (0-255 사이의 값, 기본값은 128)
  .blur(0.5) // 블러 정도 설정 (0은 블러 없음, 숫자가 클수록 더 많은 블러 적용)
  .toFile(outputImagePath)
  .then(() => {
    console.log('완료');
  })
  .catch(err => {
    console.error('이미지 자르기 오류:', err);
  });
