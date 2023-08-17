import cv2

image_path = "D:\Python\OpenCV\edge_detection.jpeg" 
image_gray = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)  
image = cv2.imread(image_path)  

edges = cv2.Canny(image_gray, threshold1=50, threshold2=200) 

cv2.imshow('Original Image', image)
cv2.imshow('Edge Detection', edges)
cv2.imshow('Gray Scale Image', image_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
