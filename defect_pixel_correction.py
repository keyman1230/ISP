import numpy as np
from PIL import Image

### From Chat GPT

def defect_pixel_correction(image_path, threshold):
    # 이미지 불러오기
    image = Image.open(image_path)
    pixels = np.array(image)

    # 각 픽셀의 RGB 값과 임계값을 비교하여 불량 픽셀 교정
    corrected_pixels = np.copy(pixels)
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            r, g, b = pixels[i, j]

            # RGB 값이 임계값보다 작은 경우에만 교정
            if r < threshold and g < threshold and b < threshold:
                # 주변 픽셀의 평균값으로 현재 픽셀 교정
                neighbors = []
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if x >= 0 and x < pixels.shape[0] and y >= 0 and y < pixels.shape[1]:
                            neighbors.append(pixels[x, y])
                neighbors = np.array(neighbors)
                mean_r = np.mean(neighbors[:, 0])
                mean_g = np.mean(neighbors[:, 1])
                mean_b = np.mean(neighbors[:, 2])

                corrected_pixels[i, j] = [mean_r, mean_g, mean_b]

    # 교정된 픽셀로 새로운 이미지 생성
    corrected_image = Image.fromarray(corrected_pixels.astype(np.uint8))

    return corrected_image

# 불량 픽셀 교정 수행
input_image_path = "input_image.jpg"  # 입력 이미지 경로
threshold_value = 50  # 불량 픽셀 판단을 위한 임계값
output_image = defect_pixel_correction(input_image_path, threshold_value)

# 교정된 이미지 저장
output_image.save("output_image.jpg")