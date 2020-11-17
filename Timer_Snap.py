import cv2

video = cv2.VideoCapture(0)
img_counter = 0
lock = True
i = 0

while True:
    _, frame = video.read()
    frame = cv2.flip(frame,1)
    (h,w) = frame.shape[:2]

    if lock:
        i+=1
        if 10 - int(i/30) == 0:
            lock = False
            temp = frame[(h//2-100):(h//2+100),(w//2-100):(w//2+100)]
            cv2.imwrite("capture.png", temp)
            print("ROI cropped n saved as capture.png in pwd")
            break
        cv2.putText(frame, "Capturing ROI in "+str(10 - int(i/30)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 4)
        cv2.rectangle(frame, (w//2-100,h//2-100), (w//2+100,h//2+100), (0,0,0), 4)
    #else: use temp for template matching

    cv2.imshow("frame",frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()