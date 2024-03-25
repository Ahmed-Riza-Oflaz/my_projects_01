import cv2
import controller as cnt
from cvzone.HandTrackingModule import HandDetector

detector=HandDetector(detectionCon=0.8,maxHands=1)


video=cv2.VideoCapture(0)

while True:
    ret,frame=video.read()
    frame=cv2.flip(frame,1)
    hands,img=detector.findHands(frame)
    if hands:
        lmList=hands[0]
        fingerUp=detector.fingersUp(lmList)

        print(fingerUp)
        cnt.led(fingerUp)
        if fingerUp==[0,0,0,0,0]:
            cv2.putText(frame,'Finger count:0',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[0,1,0,0,0]:
            cv2.putText(frame,'Finger count:1',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)    
        elif fingerUp==[0,1,1,0,0]:
            cv2.putText(frame,'Finger count:2',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[0,1,1,1,0]:
            cv2.putText(frame,'Finger count:3',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[0,1,1,1,1]:
            cv2.putText(frame,'Finger count:4',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[1,1,1,1,1]:
            cv2.putText(frame,'Finger count:5',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA) 

    cv2.imshow("frame",frame)
    k=cv2.waitKey(1)
    if k==ord("k"):
        break

video.release()
cv2.destroyAllWindows()

""" 
Bu kodlar bir el izleme ve hareket algılama uygulaması için kullanılır. İşlevlerini adım adım açıklayalım:

İlk olarak, gerekli kütüphaneler ve modüller içe aktarılır:

cv2: OpenCV kütüphanesi için kullanılır.
controller as cnt: controller modülü içinden cnt adı altında fonksiyonları içe aktarır.
HandDetector sınıfı: cvzone modülü içinden el tespiti yapmak için kullanılır.

HandDetector sınıfı detectionCon=0.8 ve maxHands=1 parametreleriyle oluşturulur. Bu parametreler, el tespiti hassasiyetini ve maksimum el sayısını belirler.

Kameradan görüntü almak için cv2.VideoCapture(0) kullanılır.

Sonsuz bir döngü başlatılır (while True), bu döngü içinde:

video.read() ile kameradan görüntü okunur ve frame değişkenine atanır.
Görüntü yatay olarak (cv2.flip(frame,1)) çevrilir.
detector.findHands(frame) ile el tespiti yapılır ve el pozisyonları hands değişkenine atanır.
Eğer el tespit edilmişse, elin parmak pozisyonları lmList değişkenine atanır ve detector.fingersUp(lmList) ile parmak pozisyonları belirlenir.
Belirlenen parmak pozisyonlarına göre cnt.led(fingerUp) fonksiyonu çağrılır. Bu fonksiyon, parmak pozisyonlarına göre LED'leri kontrol eder.
Ayrıca, ekrana parmak sayısını gösteren metinler yazılır (cv2.putText).

cv2.imshow("frame",frame) ile işlenen görüntü ekranda gösterilir.

Klavyeden "k" tuşuna basıldığında döngü sonlandırılır (if k==ord("k")).

video.release() ve cv2.destroyAllWindows() ile kamera kaynağı serbest bırakılır ve pencereler kapatılır.

Bu kodlar, kameradan alınan görüntü üzerinde el izleme ve parmak hareketlerini algılayarak belirli işlevleri gerçekleştirmek için kullanılır. Örneğin, belirlenen parmak pozisyonlarına göre LED'leri kontrol edebilir veya ekrana parmak sayısını yazdırabilirsiniz.

"""