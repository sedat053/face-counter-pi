from picamera2 import Picamera2
import cv2
from gpiozero import LED
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

led1= LED(17)
led2= LED(27)
led3= LED(22)

reader = SimpleMFRC522()
izinli_kart= [151821882918]

picam2= Picamera2()
picam2.preview_configuration.main.size =(1280,720)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

led2.on()

try:
    print("Cipi okutunuz")
    id,text = reader.read()

    if id in izinli_kart:
        print("kilit acildi")
        print("kamera devreye giriyor")
        led2.off()
        led1.on()

        picam2.start()
        while True:
            frame = picam2.capture_array()
            gray= cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors=3)

            for(x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y), (x+w, y+h),(0, 255,0),2)

            if len(faces) >0:
                led3.on()
            else:
                led3.off()

            cv2.putText(frame, f"Faces: {len(faces)}", (20,40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
            cv2.imshow("proje",frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    else:
        print("yanliss cip bir daha dene")
        print("cipi okutunuz")
finally:
    GPIO.cleanup()
    picam2.stop()
    cv2.destroyAllWindows()