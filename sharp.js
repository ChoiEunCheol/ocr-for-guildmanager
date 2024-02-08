const sharp = require('sharp');

sharp('./test_image1.jpg')
//   .resize(800) // 너비를 800px로 조정
  .greyscale() // 흑백 이미지로 변환
  .modulate({
    brightness: 1.2,
    saturation: 1.5,
  })
  .linear(2, -190) 
  .toFile('sharp_image1.jpg', (err, info) => { 
    if (err) throw err;
    console.log(info);
  });