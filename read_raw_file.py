import numpy as np
from PIL import Image
from file_control import untitled


def read_raw_file(file_path, width, height):
    # raw 파일 불러오기
    with open(file_path, 'rb') as file:
        raw_data = file.read()

    # raw 데이터를 numpy 배열로 변환
    image_array = np.frombuffer(raw_data, dtype=np.uint8)

    # 배열을 이미지로 변환
    image = Image.fromarray(image_array.reshape(height, width), 'L')

    return image

file_path = untitled.select_file(init_dir='./') # raw 파일 경로

# raw 파일 읽기
# file_path = "input_image.raw"  # raw 파일 경로

width = 4224 # 640  # 이미지 너비
height = 3024 # 480  # 이미지 높이
output_image = read_raw_file(file_path, width, height)

# 이미지 저장
output_image.save("output_image.jpg")