from pathlib import Path

import sys

import cv2
import numpy as np

file_info = sys.argv[1].split('.')

print(file_info)
file_name = file_info[0]
file_type = "." + file_info[1]

img = cv2.imread(file_name + file_type)

size = (96, 64)  # 分割後の大きさ
rows = int(np.ceil(img.shape[0] / size[0]))  # 行数
cols = int(np.ceil(img.shape[1] / size[1]))  # 列数

chunks = []
for row_img in np.array_split(img, rows, axis=0):
    for chunk in np.array_split(row_img, cols, axis=1):
        chunks.append(chunk)
print(len(chunks))

# 保存する。
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)
for i, chunk in enumerate(chunks):
    save_path = output_dir / f"{file_name}_{i:02d}.png"
    cv2.imwrite(str(save_path), chunk)