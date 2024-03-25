import pyfirmata

comport='COM3'

board=pyfirmata.Arduino(comport)


led_1=board.get_pin('d:8:o')
led_2=board.get_pin('d:9:o')
led_3=board.get_pin('d:10:o')
led_4=board.get_pin('d:11:o')
led_5=board.get_pin('d:12:o')

def led(fingerUp):
    if fingerUp==[0,0,0,0,0]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)

    elif fingerUp==[0,1,0,0,0]:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp==[0,1,1,0,0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)    
    elif fingerUp==[0,1,1,1,0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp==[0,1,1,1,1]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    elif fingerUp==[1,1,1,1,1]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)


""" 
Bu kodlar, Arduino ve Python aracılığıyla LED'leri kontrol etmeye yarar. Kodun genel işlevi şu şekildedir:

İlk olarak pyfirmata modülü import edilir ve Arduino'nun bağlı olduğu seri port belirlenir (comport='COM3').

board değişkeni oluşturularak Arduino ile bağlantı sağlanır.

Ardından LED'lerin bağlı olduğu pinler belirlenir (led_1, led_2, vb.).

led adında bir fonksiyon tanımlanır. Bu fonksiyon, aldığı fingerUp parametresine göre LED'leri kontrol eder. fingerUp parametresi, parmakların yukarıda olup olmadığını temsil eden bir listedir. Her bir parmak için 0 (aşağıda) veya 1 (yukarıda) değeri bulunur.

fingerUp parametresine göre belirli bir kombinasyona karşılık gelen LED'ler açılır veya kapanır. Örneğin, [0,1,1,1,0] kombinasyonu LED_1'i açarken diğerlerini kapatır.

Bu kodlar, Arduino üzerindeki LED'leri farklı parmak hareketleriyle kontrol etmek için kullanılabilir. Örneğin, bir el hareket sensörü kullanarak belirli bir parmak pozisyonu algılandığında belirli LED'leri açabilirsiniz.

"""