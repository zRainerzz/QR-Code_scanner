import cv2
from pyzbar.pyzbar import decode
import time


cam = cv2.VideoCapture(0)
cam.set(5, 640)
cam.set(6, 480)

camera = True
while camera:
    success, frame = cam.read()
    
    if success:
        for i in decode(frame):
            print(i.type)
            print(i.data.decode('utf-8'))
            time.sleep(6)
            
            cv2.imshow("OurQR_Code_Scanner", frame)
            cv2.waitKey(3)
    else:
        print("Error reading frame from the camera")
        break

cam.release()
cv2.destroyAllWindows()