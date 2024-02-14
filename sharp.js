const sharp = require('sharp');

// 이미지 파일 경로
const inputImagePath = './test_image1.jpg';
const outputImagePath = './cutting1.jpg';

// 이미지 자르기
sharp(inputImagePath)
  .extract({ left: 530, top: 150, width: 55, height: 415 }) // 자를 영역 지정
  .toFile(outputImagePath)
  .then(() => {
    console.log('이미지가 성공적으로 자르기 되었습니다.');
  })
  .catch(err => {
    console.error('이미지 자르기 오류:', err);
  });
