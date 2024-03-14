import cv2
import numpy as np 
from datetime import datetime 
import sys
import os
import locale
import time


#############--Merhaba, bu benim python ile yaptığım 583 satırlık ilk düzenli kod örneğidir.--############

#############--Hello, this is the first regular code example of 583 lines that I made with Python.--######

locale.setlocale(locale.LC_ALL)

while True:
    print(""" *****************
        1-giriş yap
        2-saati öğren
        3-sonlandır """)

    sys_kullanici_Adi = "ahmet rıza oflaz"
    sys_sifre = "123456"

    while True:
        
        istek1 = input("işlem giriniz :")

        if istek1 == "3":
            print("program sonlandırılıyor")
            sys.exit()

        elif istek1 == "2":
            su_an = datetime.now()
            print(datetime.ctime(su_an))

            input("devam etmek için enter tuşuna basınız...")
            continue
            
        elif istek1 == "1":

            while True:

                deneme_hakki = 3

                kullanici_Adi = input("kullanıcı adını giriniz :")
                sifre = input("sifre giriniz :")

                if deneme_hakki == 0:
                    print("çok fazla deneme yapıldı program sonlandırılıyor...")
                    sys.exit

                elif kullanici_Adi != sys_kullanici_Adi and sifre != sys_sifre:
                    print("kullanıcı adı ve şifre hatalı tekrar deneyiniz")
                    deneme_hakki = deneme_hakki - 1
                    continue

                elif kullanici_Adi != sys_kullanici_Adi or sifre != sys_sifre:
                    print("kullanıcı adı veya şifre hatalı lütfen tekrar deneyiniz")
                    deneme_hakki = deneme_hakki - 1
                    continue

                else:
                    print("HOŞGELDİN",sys_kullanici_Adi )
                    while True:
                        print("""devam etmek için işlem seçiniz 
                            0 - programı bitir
                            1 - tarih ve saati öğren
                            2 - görev listesini göster
                            3 - görev ekle
                            4 - görev listesini sıfırla
                            5 - kamerayı aç 
                            6 - çizim yap
                            7 - matamatiksel işlemler
                            8 - kullanıcı adı değiştir
                            9 - şifre değiştir
                            10- programı yeniden başlat
                            """)
                        
                        istek2 = int(input("işlem seçiniz :"))

                        try:

                            if istek2 == 0:
                                emin1 = input("programı sonlandırmak istiyormusunuz(evet/hayır) :")

                                if emin1 == "evet":
                                    print("program sonlandırılıyor...")
                                    time.sleep(1)
                                    sys.exit()
                                elif emin1 == "hayır":
                                    continue
                                else:
                                    print("lütfen evet hayır olarak cevap veriniz")

                            elif istek2 == 1:
                                    time.sleep(1)
                                    su_an = datetime.now()
                                    print(datetime.ctime(su_an))

                                    input("devam etmek için bir tuşa basınız...")
                                
                            elif istek2 == 2:
                                print("görev listesi okunuyor...")
                                time.sleep(1)

                                print("görev listesi :")

                                with open("proje_denemesi_görev_listesi.txt","r",encoding="utf-8")as file:
                                    for i in file:
                                        print(i)
                                
                                input("devam etmek için enter tuşuna basınız...")

                            elif istek2 == 3:
                                with open("proje_denemesi_görev_listesi.txt", "a", encoding="utf-8")as file:
                                        gorev = input("dosyaya eklenecek görevi giriniz :")
                                        ekleme = []
                                        ekleme.append(gorev)

                                        for i in ekleme:
                                            file.write(i)
                                        
                                        time.sleep(1)
                                        print("dosyaya kaydedildi...")
                                        input("devam etmek için enter tuşuna basınız...")
                            
                            elif istek2 == 4:
                                while True:
                                    emin2 = input("dosyayı sıfırlamak için eminmisiniz (evet/hayır) :")

                                    if emin2 == "evet":
                                        os.rmdir("proje_denemesi_görev_listesi.txt")

                                        input("devam etmek için enter tuşuna basınız")
                                        break

                                    elif emin2 == "hayır":
                                        time.sleep(1)
                                        break

                                    else:
                                        print("lütfen evet / hayır şeklinde cevap veriniz")
                                        continue

                            elif istek2 == 5:
                                print("çıkış yapmak için 'q' basınız...")
                                cap = cv2.VideoCapture(0)

                                while True:
                                    ret, frame = cap.read()

                                    frame = cv2.flip(frame, 1)

                                    cv2.imshow("Webcam", frame)
                                    cv2.waitKey(1)

                                    if cv2.waitKey(1) & 0xFF == ord("q"):
                                        break

                                cap.release()
                                cv2.destroyAllWindows()

                            elif istek2 == 6:

                                while True:
                                    print(""" *******************
                                        0 - bu programı sonlandır
                                        1 - özel boyut ver 
                                        2 - kare çiz
                                        3 - daire çiz
                                        """)
                                    
                                    try:
                                    
                                        islem4 = int(input("işlem giriniz :"))

                                        if islem4 == 0:
                                            print("bu programdan çıkılıyor...")
                                            time.sleep(1)
                                            break

                                        elif islem4 == 1:
                                            print(""" *********************
                                                  özel boyut vermek için çizmek istediğiniz şeklin kaç köşeli olacağını giriniz...""")
                                            
                                            while True:
                                                istek3 = input("kaç köşeli (min : 3 max : 5) :")

                                                if istek3 == "0":
                                                    print("program sonlandırılıyor...")
                                                    time.sleep(0.5)
                                                    break

                                                elif istek3 == "3":
                                                    print("üç köşeli şekil çizebilmek için köşelerin kordinatlarını giriniz :")

                                                    while True:

                                                        try:

                                                            a1 = int(input("birinci köşe x :"))
                                                            a2 = int(input("birinci köşe y :"))

                                                            b1 = int(input("ikinci köşe x :"))
                                                            b2 = int(input("ikinci köşe y :"))

                                                            c1 = int(input("üçüncü köşe x :"))                 
                                                            c2 = int(input("üçüncü köşe y :"))


                                                            canvas2 = np.zeros((512,512,3), dtype=np.uint8 )

                                                            points1 = np.array([[[a1,a2], [b1,b2], [c1,c2]]], np.int32)

                                                            cv2.polylines(canvas2, [points1], isClosed=False , color=(0,255,0), thickness=3)

                                                            cv2.imshow("özel boyutlu çizim", canvas2 )
                                                            cv2.waitKey(0)
                                                            cv2.destroyAllWindows()

                                                            break


                                                        except ValueError:
                                                            print("kordinatları sayısal değer olarak giriniz...")
                                                            continue

                                                elif istek3 == "4":
                                                    print("dört köşeli özel şekil çizebilmek için öncelikle kordinatları giriniz...")

                                                    while True:

                                                        try:

                                                            a1 = int(input("birinci köşe x :"))
                                                            a2 = int(input("birinci köşe y :"))

                                                            b1 = int(input("ikinci köşe x :"))
                                                            b2 = int(input("ikinci köşe y :"))

                                                            c1 = int(input("üçüncü köşe x :"))                 
                                                            c2 = int(input("üçüncü köşe y :"))

                                                            d1 = int(input("dördüncü köşe x :"))
                                                            d2 = int(input("dördüncü köşe y :"))



                                                            canvas2 = np.zeros((512,512,3), dtype=np.uint8 )

                                                            points1 = np.array([[[a1,a2], [b1,b2], [c1,c2], [d1,d2]  ]], np.int32)

                                                            cv2.polylines(canvas2, [points1], isClosed=False , color=(0,255,0), thickness=3)

                                                            cv2.imshow("özel boyutlu çizim", canvas2 )
                                                            cv2.waitKey(0)
                                                            cv2.destroyAllWindows()

                                                            break


                                                        except ValueError:
                                                            print("kordinatları sayısal değer olarak giriniz...")
                                                            continue

                                                elif istek3 == "5":
                                                    print("beş köşeli çizim yapabilmek için öncelikle kordinatları giriniz...")

                                                    while True:

                                                        try:

                                                            a1 = int(input("birinci köşe x :"))
                                                            a2 = int(input("birinci köşe y :"))

                                                            b1 = int(input("ikinci köşe x :"))
                                                            b2 = int(input("ikinci köşe y :"))

                                                            c1 = int(input("üçüncü köşe x :"))                 
                                                            c2 = int(input("üçüncü köşe y :"))

                                                            d1 = int(input("dördüncü köşe x :"))
                                                            d2 = int(input("dördüncü köşe y :"))

                                                            e1 = int(input("beşinci köşe x"))
                                                            e2 = int(input("beşinci köşe y"))


                                                            canvas2 = np.zeros((512,512,3), dtype=np.uint8 )

                                                            points1 = np.array([[[a1,a2], [b1,b2], [c1,c2], [d1,d2], [e1,e2] ]], np.int32)

                                                            cv2.polylines(canvas2, [points1], isClosed=False , color=(0,255,0), thickness=3)

                                                            cv2.imshow("özel boyutlu çizim", canvas2 )
                                                            cv2.waitKey(0)
                                                            cv2.destroyAllWindows()

                                                            break


                                                        except ValueError:
                                                            print("kordinatları sayısal değer olarak giriniz...")
                                                            continue

                                                else:
                                                    print("lütfen çizmek istediğiniz şeklin köşe sayısını doğru giriniz")
                                                    continue

                                        elif islem4 == 2:
                                            print("kare")

                                            canvas = np.zeros((512,512,3), dtype=np.uint8)

                                            x1, y1 = 100, 100
                                            x2, y2 = 200, 200

                                            cv2.rectangle(canvas, (x1,y1), (x2,y2), (0,255,0), thickness=2)

                                            cv2.imshow('Square', canvas)
                                            cv2.waitKey(0)
                                            cv2.destroyAllWindows()

                                        elif islem4 == 3:
                                            print("daire")

                                            # Boş bir siyah görüntü oluştur
                                            canvas = np.zeros((512,512,3), dtype=np.uint8)

                                            center = (250, 250)
                                            radius = 100

                                            cv2.circle(canvas, center, radius, (0,0,255), thickness=2)

                                            cv2.imshow('Circle', canvas)
                                            cv2.waitKey(0)
                                            cv2.destroyAllWindows()


                                    except ValueError:
                                        print("lütfen işlem giriniz...")
                                        continue

                            elif istek2 == 7:
                                while True:
                                    print(""" işlem yapmak için işlem seçiniz
                                          0 - bu programı sonlandır
                                          1 - sayıları topla
                                          2 - sayıların çarpımı
                                          3 - bu sayı asal mı 
                                          4 - iki sayı arasındaki asal sayılar
                                          5 - aralarında asal olup olmadığını sorgula
                                          6 - faktöriyel bul """)
                                    
                                    time.sleep(1)
                                    
                                    islem3 = input("lütfen işlem seçiniz :")

                                    if islem3 == "0":
                                        print("bu program sonlandırılıyor...")
                                        time.sleep(0.5)
                                        break

                                    elif islem3 == "1":

                                        total = 0

                                        while True:
                                            try:
                                                num = float(input("Bir sayı girin (Çıkmak için 0'a basın): "))
                                                
                                                if num == 0:
                                                    break 
                                                
                                                total += num 
                                            except ValueError:
                                                print("Geçersiz giriş. Lütfen bir sayı girin.")

                                        print("Girilen sayıların toplamı:", total)



                                    elif islem3 == "2":

                                        result = 1

                                        while True:
                                            try:
                                                num = float(input("Bir sayı girin (Çıkmak için 0'a basın): "))
                                                
                                                if num == 0:
                                                    break
                                                
                                                result *= num 
                                            except ValueError:
                                                print("Geçersiz giriş. Lütfen bir sayı girin.")

                                        print("Girilen sayıların çarpımı:", result)



                                    elif islem3 == "3":
                                        print("bu programdan çıkabilmek için '0' basınız... ")
                                        while True:
                                            try:
                                                sayı2 = int(input("Hangi sayıyının asal olup olmadığını öğrenmek istiyorsun? : "))

                                                if sayı2 == 0:
                                                    print("sonlandırılıyor...")
                                                    time.sleep(1)
                                                    break

                                                for i in range(2,sayı2):
                                                    if sayı2 % i == 0:
                                                        print(sayı2,"bir asal sayı değildir.")
                                                        input("\nDevam etmek için ENTER tuşuna bas\n")
                                                        break
                                                    elif i == sayı2-1:
                                                        print(sayı2,"bir asal sayıdır.")
                                                        input("\nDevam etmek için ENTER tuşuna bas\n")

                                            except ValueError:
                                                print("lütfen sayı giriniz...")
                                                continue

                                    elif islem3 == "4":

                                        while True:
                                            sayi1 = int(input("Aralığın ilk sayısını gir:"))
                                            sayi2 = int(input("Aralığın son sayısın gir:"))
                                            asallar = ""

                                            if sayi1 == 0 and sayi2 == 0:
                                                print("program sonlanıyor...")
                                                break                       
                                            else:
                                                for i in range(sayi1+1,sayi2):
                                                    for j in range(2,i):
                                                        if i % j == 0:
                                                            break
                                                        elif j == i-1:
                                                            asallar += str(i) + ", "
                                                            if asallar == "":
                                                                print("Bu aralıkta hiçbir asal sayı bulunmuyor.")
                                                                input("\nDevam etmek için ENTER tuşuna bas\n")
                                                            else:
                                                                print("Bu aralıktakı asal sayılar: ",asallar)
                                                                continue

                                    elif islem3 == "5":
                                        while True:
                                            try:
                                                sayii1 = int(input("ilk sayıyı giriniz :"))
                                                sayii2 = int(input("ikinci sayıyı giriniz :"))

                                                kontrol = 1
                                                while kontrol == 1:
                                                    kontrol -= 1
                                                    sayii1 = int(input("Sayı 1: "))
                                                    sayii2 = int(input("Sayı 2: "))
                                                    if sayii1 > sayi2:
                                                        for i in range(2,sayi2+1):
                                                            if sayii1 % i == 0 and sayii2 % i == 0:
                                                                print(sayi1,sayi2,"aralarında asal değildir.")
                                                                input("\nDevam etmek için ENTER tuşuna bas\n")
                                                                break
                                                    elif i == sayii2:
                                                        print(sayii1,sayii2,"aralarında asaldır.")
                                                        input("\nDevam etmek için ENTER tuşuna bas\n")

                                                    elif sayii1 < sayii2:
                                                        for i in range(2,sayi1+1):
                                                            if sayii1 % i == 0 and sayii2 % i == 0:
                                                                print(sayi1,sayi2,"aralarında asal değildir..")
                                                                input("\nDevam etmek için ENTER tuşuna bas\n")
                                                                break
                                                            elif i == sayii1:
                                                                print(sayii1,sayii2,"aralarında asaldır.")
                                                                input("\nDevam etmek için ENTER tuşuna bas\n")

                                                    else:
                                                        print("Sayılar aynı olamaz.")
                                                        input("Devam etmek için ENTER tuşuna bas.")
                                                        kontrol += 1


                                            except ValueError:
                                                print("lütfen sayı giriniz...")
                                                continue

                                    elif islem3 == "6":
                                        print("bu programı sonlandırabilmek için '0' basınız... ")
                                        while True:

                                            faktor = int(input("faktöriyelini bulmak istediğiniz sayıyı giriniz :"))

                                            def factorial(n):
                                                if n == 0:
                                                    return 1
                                                else:
                                                    return n * factorial(n-1)

                                            num = faktor

                                            print("Faktöriyel of", num, ":", factorial(num))

                                    else:
                                        print("lütfen 1-6 arasında bir işlem seçiniz...")
                                        continue
                            
                            elif istek2 == 8:
                                print("kullanıcı adının değiştirmek için giriş yapınız")
                                time.sleep(1)

                                giris_k_ad = input("kullanıcı adı :")
                                giris_sifre = input("şifre giriniz :")

                                if giris_k_ad != sys_kullanici_Adi and giris_sifre != sys_sifre:
                                    print("hatalı giriş.")
                                    sys.exit()

                                elif giris_k_ad != sys_kullanici_Adi or giris_sifre != sys_sifre:
                                    print("hatalı giriş")
                                    sys.exit()
                                
                                else:
                                    yeni_kullanici_adi = input("yeni kullanıcı adını giriniz :")

                                    sys_kullanici_Adi = yeni_kullanici_adi

                                    print("kullanıcı adı değiştiriliyor...")
                                    time.sleep(1)
                                    print("kullanıcı adı başarıyla değiştirildi.")
                                    time.sleep(1)
                                    continue

                            elif istek2 == 9:
                                print("şifreyi değiştirmek için giriş yapınız")

                                giris2_k_a = input("kullanıcı adını giriniz :")
                                giris_s = input("şifreyi giriniz :")

                                if giris2_k_a != sys_kullanici_Adi and giris_s != sys_sifre:
                                    print("hatalı giriş")
                                    sys.exit()
                                
                                elif giris2_k_a != sys_kullanici_Adi or giris_s != sys_sifre:
                                    print("hatalı giriş")
                                    sys.exit()

                                else:
                                    yeni_sifre = input("yeni şifreyi giriniz :")

                                    sys_sifre = yeni_sifre 

                                    print("şifre değiştiriliyor")
                                    time.sleep(1)

                                    print("şifre başarıyla değiştirildi")
                                    time.sleep(1)

                                    continue

                            elif istek2 == 10:
                                print("program yeniden başlatılıyor...")
                                time.sleep(1)
                                break

                            else:
                                print("hatalı işlem seçtiniz lütfen tekrar işlem seçiniz")
                                time.sleep(1)
                                continue

                        except ValueError:
                            print("lütfen sayı giriniz")
                            time.sleep(1)
                            continue

        else:
            print("saf dışı işlem seçtiniz lütfen tekrar deneyiniz...")
            time.sleep(1)
            continue