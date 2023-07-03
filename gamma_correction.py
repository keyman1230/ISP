import numpy as np
from PIL import Image

def gamma_correction(image_path, gamma):
    # 이미지 불러오기
    image = Image.open(image_path)
    pixels = np.array(image)

    # 감마 보정 수행
    corrected_pixels = np.power(pixels / 255.0, gamma) * 255.0
    corrected_pixels = np.clip(corrected_pixels, 0, 255)

    # 보정된 픽셀로 새로운 이미지 생성
    corrected_image = Image.fromarray(corrected_pixels.astype(np.uint8))

    return corrected_image

# 감마 보정 수행
input_image_path = "input_image.jpg"  # 입력 이미지 경로
gamma = 2.2  # 감마 값
output_image = gamma_correction(input_image_path, gamma)

# 보정된 이미지 저장
output_image.save("output_image.jpg")
