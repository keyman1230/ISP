import numpy as np
from PIL import Image

def color_correction(image_path, adjustment_matrix):
    # 이미지 불러오기
    image = Image.open(image_path)
    pixels = np.array(image)

    # 컬러 보정 수행
    corrected_pixels = np.dot(pixels.astype(np.float32), adjustment_matrix.T)
    corrected_pixels = np.clip(corrected_pixels, 0, 255)

    # 보정된 픽셀로 새로운 이미지 생성
    corrected_image = Image.fromarray(corrected_pixels.astype(np.uint8))

    return corrected_image

# 컬러 보정 수행
input_image_path = "input_image.jpg"  # 입력 이미지 경로
adjustment_matrix = np.array([[1.2, 0, 0], [0, 1, 0], [0, 0, 0.8]])  # 보정 행렬
output_image = color_correction(input_image_path, adjustment_matrix)

# 보정된 이미지 저장
output_image.save("output_image.jpg")
