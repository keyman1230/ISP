import numpy as np
from PIL import Image

def lens_shading_compensation(image_path, gain_map_path):
    # 이미지 불러오기
    image = Image.open(image_path)
    pixels = np.array(image)

    # 게인 맵 불러오기
    gain_map = np.load(gain_map_path)

    # 렌즈 섀딩 보정
    corrected_pixels = np.copy(pixels)
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            r, g, b = pixels[i, j]

            # 게인 맵 적용
            corrected_r = r / gain_map[i, j, 0]
            corrected_g = g / gain_map[i, j, 1]
            corrected_b = b / gain_map[i, j, 2]

            # 픽셀 값 클리핑 (0 ~ 255)
            corrected_r = np.clip(corrected_r, 0, 255)
            corrected_g = np.clip(corrected_g, 0, 255)
            corrected_b = np.clip(corrected_b, 0, 255)

            corrected_pixels[i, j] = [corrected_r, corrected_g, corrected_b]

    # 보정된 픽셀로 새로운 이미지 생성
    corrected_image = Image.fromarray(corrected_pixels.astype(np.uint8))

    return corrected_image

# 렌즈 섀딩 보정 수행
input_image_path = "input_image.jpg"  # 입력 이미지 경로
gain_map_path = "gain_map.npy"  # 게인 맵 경로
output_image = lens_shading_compensation(input_image_path, gain_map_path)

# 보정된 이미지 저장
output_image.save("output_image.jpg")