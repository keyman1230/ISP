import numpy as np
from PIL import Image

def white_balance(image_path, red_gain, green_gain, blue_gain):
    # 이미지 불러오기
    image = Image.open(image_path)
    pixels = np.array(image)

    # 화이트 밸런스 조정
    adjusted_pixels = np.copy(pixels)
    adjusted_pixels[:, :, 0] *= red_gain
    adjusted_pixels[:, :, 1] *= green_gain
    adjusted_pixels[:, :, 2] *= blue_gain

    # 픽셀 값 클리핑 (0 ~ 255)
    adjusted_pixels = np.clip(adjusted_pixels, 0, 255)

    # 조정된 픽셀로 새로운 이미지 생성
    adjusted_image = Image.fromarray(adjusted_pixels.astype(np.uint8))

    return adjusted_image

# 화이트 밸런스 조정 수행
input_image_path = "input_image.jpg"  # 입력 이미지 경로
red_gain = 1.2  # 빨간색 게인
green_gain = 1.0  # 초록색 게인
blue_gain = 0.8  # 파란색 게인
output_image = white_balance(input_image_path, red_gain, green_gain, blue_gain)

# 조정된 이미지 저장
output_image.save("output_image.jpg")