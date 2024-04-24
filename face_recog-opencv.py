import cv2

img = cv2.imread("C:\\Users\nikhi\Desktop\faces\original\1.jpg")
cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

rects = cascade.detectMultiScale(img,1.3,5,cv2.CASCADE_SCALE_IMAGE)
if len(rects) == 0: 
    print("No face detected.")
rects[:, 2:] += rects[:, :2]
for x1,y1,x2,y2 in rects: 
    cv2.rectangle(img,(x1,y1),(x2,y2),(127,255,0),2)
cv2.imwrite("%s" % img)