import cv2

color = cv2.imread('image-1/download.jpeg', 0)
cv2.imwrite('image-1/galaxy-gray.jpeg', color)
