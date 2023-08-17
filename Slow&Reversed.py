import cv2

cap = cv2.VideoCapture("D:/Python/OpenCV/videoplayback.mp4")

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = cap.get(cv2.CAP_PROP_FPS)
nframes= cap.get(cv2.CAP_PROP_FRAME_COUNT)

path = "D:Python/OpenCV/videoplayback.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter(path, fourcc, 2,
						(width, height))
index = nframes -1

while True:
	cap.set(cv2.CAP_PROP_POS_FRAMES,index)
	ret, frame = cap.read()
	cv2.imshow("frame", frame)
	output.write(frame)
	k = cv2.waitKey(50)
	index = index-1
	if k == ord("q"):
		break

cap.release()
output.release()
cv2.destroyAllWindows()