import numpy as np
from PIL import Image

def digital_clamp(image_path, lower_threshold, upper_threshold):
    # 이미지 불러오기
    image = Image.open(image_path)
    pixels = np.array(image)

    # 디지털 클램프 수행
    clamped_pixels = np.copy(pixels)
    clamped_pixels = np.clip(clamped_pixels, lower_threshold, upper_threshold)

    # 클램프된 픽셀로 새로운 이미지 생성
    clamped_image = Image.fromarray(clamped_pixels.astype(np.uint8))

    return clamped_image

# 디지털 클램프 수행
input_image_path = "input_image.jpg"  # 입력 이미지 경로
lower_threshold = 50  # 최소 임계값
upper_threshold = 200  # 최대 임계값
output_image = digital_clamp(input_image_path, lower_threshold, upper_threshold)

# 클램프된 이미지 저장
output_image.save("output_image.jpg")