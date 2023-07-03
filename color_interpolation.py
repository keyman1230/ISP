import numpy as np
from PIL import Image

def color_interpolation(image_path):
    # 이미지 불러오기
    image = Image.open(image_path)
    pixels = np.array(image)

    # 컬러 보간 수행
    interpolated_pixels = np.copy(pixels)
    for i in range(1, pixels.shape[0] - 1):
        for j in range(1, pixels.shape[1] - 1):
            r, g, b = pixels[i, j]

            # 주변 픽셀 값으로 컬러 보간
            interpolated_r = (pixels[i-1, j-1, 0] + pixels[i-1, j, 0] + pixels[i-1, j+1, 0] +
                              pixels[i, j-1, 0] + pixels[i, j, 0] + pixels[i, j+1, 0] +
                              pixels[i+1, j-1, 0] + pixels[i+1, j, 0] + pixels[i+1, j+1, 0]) // 9
            interpolated_g = (pixels[i-1, j-1, 1] + pixels[i-1, j, 1] + pixels[i-1, j+1, 1] +
                              pixels[i, j-1, 1] + pixels[i, j, 1] + pixels[i, j+1, 1] +
                              pixels[i+1, j-1, 1] + pixels[i+1, j, 1] + pixels[i+1, j+1, 1]) // 9
            interpolated_b = (pixels[i-1, j-1, 2] + pixels[i-1, j, 2] + pixels[i-1, j+1, 2] +
                              pixels[i, j-1, 2] + pixels[i, j, 2] + pixels[i, j+1, 2] +
                              pixels[i+1, j-1, 2] + pixels[i+1, j, 2] + pixels[i+1, j+1, 2]) // 9

            interpolated_pixels[i, j] = [interpolated_r, interpolated_g, interpolated_b]

    # 보간된 픽셀로 새로운 이미지 생성
    interpolated_image = Image.fromarray(interpolated_pixels.astype(np.uint8))

    return interpolated_image

# 컬러 보간 수행
input_image_path = "input_image.jpg"  # 입력 이미지 경로
output_image = color_interpolation(input_image_path)

# 보간된 이미지 저장
output_image.save("output_image.jpg")
