import os
import cv2

images = os.listdir('image-2')
for image in images:
  print(image)
  gray = cv2.imread(f'image-2/{image}', 0)
  print(gray)
  cv2.imwrite(f'gray-{image}', gray)