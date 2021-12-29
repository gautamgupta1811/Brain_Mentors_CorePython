import cv2
import os
# path --> video
# 0 --> default camera
# 1 --> Secondary camera

# to read and capture camera
vid = cv2.VideoCapture(0)

# to make folder if it doesn't exist
if not os.path.exists("Images"):
    os.mkdir("Images")
i = 0
while True:
    # to check availability and read frames
    ret, frame = vid.read()
    if ret:
        # to save images
        # cv2.imwrite("Images/some_file_"+str(i)+".png", frame)
        i += 1
        # to change color
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # to see the output
        frame = cv2.resize(frame, (500, 500))
        cv2.imshow("result", frame)
        print(frame.shape)
        # to add closing condition
        if cv2.waitKey(1) == 27:
            break
    else:
        print("Error in reading camera")
# to release camera
vid.release()
# to destroy all windows of cv2
cv2.destroyAllWindows()
