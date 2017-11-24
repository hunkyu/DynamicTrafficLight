import cv2
print(cv2.__version__)

cascade_src = 'cars.xml'
video_src = 'dataset/video1.avi'
#video_src = 'dataset/M6 Motorway Traffic.mp4'

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #gray = cv2.resize(gray,(0,0),fx = 0.8,fy = 0.8)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in cars:
        cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),2)      
    
    cv2.imshow('video', gray)
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
