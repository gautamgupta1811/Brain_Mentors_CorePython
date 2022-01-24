import cv2

img = cv2.imread(r"C:\Users\Gautam\Desktop\img_1.jpg")
print("size of image:", img.shape)
img = cv2.resize(img, (500, 500))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# img = cv2.putText(img, text, position, font, fontsize, color, thickness)
img = cv2.putText(img, "Dog", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 255), 4)
while True:
    cv2.imshow("result", img)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
