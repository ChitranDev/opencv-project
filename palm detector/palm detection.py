import cv2
# you can also take like images using your web camera 
image = cv2.imread("ME.jpg")

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
   


    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    edges = cv2.bitwise_not(edges)
    cv2.imwrite("line.jpg",edges)
    palmlines = cv2.imread("line.jpg")
    img = cv2.addWeighted(palmlines, 0.3, image, 0.7,0)
    cv2.imshow("final output", img)
    cv2.imwrite("final Me.jpg",img)


