import numpy as np
from PIL import Image
from scipy.ndimage.filters import convolve

def edge_enhancement(image_path, kernel):
    # 이미지 불러오기
    image = Image.open(image_path)
    grayscale_image = image.convert("L")
    pixels = np.array(grayscale_image)

    # 엣지 강화 수행
    enhanced_pixels = convolve(pixels.astype(float), kernel)

    # 픽셀 값 클리핑 (0 ~ 255)
    enhanced_pixels = np.clip(enhanced_pixels, 0, 255)

    # 강화된 픽셀로 새로운 이미지 생성
    enhanced_image = Image.fromarray(enhanced_pixels.astype(np.uint8))

    return enhanced_image

# 엣지 강화 수행
input_image_path = "input_image.jpg"  # 입력 이미지 경로
kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])  # 엣지 강화 커널
output_image = edge_enhancement(input_image_path, kernel)

# 강화된 이미지 저장
output_image.save("output_image.jpg")
