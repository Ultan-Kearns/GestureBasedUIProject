import cv2

def app():
    print("Test")
    video_capture = cv2.VideoCapture(0)
    while True:
        ret,frame = video_capture.read()
        cv2.imshow('My Video', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

app();
