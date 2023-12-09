from pathlib import Path

import sys

import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file_info = sys.argv[1].split('.')

print(file_info)
file_name = file_info[0].split('/')[-1]
file_type = "." + file_info[1]

img = cv2.imread(file_info[0] + file_type)
print(type(img))

dictionary = {}

before_data = []
after_data = []

before_name = "before_image_format.csv"
after_name = "after_image_format.csv"

before_data = pd.read_csv(before_name,sep='\t',header=None).values.tolist()
#print(before_data)
after_data = pd.read_csv(after_name,sep='\t',header=None).values.tolist()

size = (16, 16)  # 分割後の大きさ
rows = int(np.ceil(img.shape[0] / size[0]))  # 行数
cols = int(np.ceil(img.shape[1] / size[1]))  # 列数

# print(np.array_split(img,rows,axis=0))
for i,row_img in enumerate(np.array_split(img, rows, axis=0)):
    for j,chunk in enumerate(np.array_split(row_img, cols, axis=1)):
        #print(before_data[i][j])
        dictionary[before_data[i][j]] = chunk
#print(dictionary)



img_list = []

for row in after_data:
    img_row = []
    for number in row:
        if not number == 0:
            img_row.append([dictionary[number]])
            #print(dictionary[number])
        else:
            img_row.append([np.zeros(shape=(size[0],size[1],3),dtype='uint8')])
            
    img_list.append(img_row)


img = np.block(img_list)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()

# 保存する。
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)


save_path = output_dir / f"{file_name}_remake.png"
cv2.imwrite(str(save_path), img)