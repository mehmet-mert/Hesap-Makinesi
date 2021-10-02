#import besmele
#import Mehmet Mert Altuntas

import sys
import random
import turtle
import smtplib

def goto_x_zero():
    turtle2.goto(0, y)
    turtle2.color("red")
    turtle2.goto(x, 0)

def draw_x_y ():
    turtle2.penup()
    turtle2.goto(-400, 0)
    turtle2.pendown()
    turtle2.width(3)
    turtle2.forward(800)
    turtle2.penup()
    turtle2.goto(0, -400)
    turtle2.left(90)
    turtle2.pendown()
    turtle2.forward(800)
    turtle2.goto(0, 0)

def draw_bg():
    turtle2.penup()
    turtle2.goto(-400, -400)
    turtle2.pendown()
    for i in range(8):
        turtle2.forward(800)
        turtle2.left(90)
        turtle2.forward(50)
        turtle2.left(90)
        turtle2.forward(800)
        turtle2.right(90)
        turtle2.forward(50)
        turtle2.right(90)
    for i in range(8):
        turtle2.forward(50)
        turtle2.right(90)
        turtle2.forward(800)
        turtle2.left(90)
        turtle2.forward(50)
        turtle2.left(90)
        turtle2.forward(800)
        turtle2.right(90)
    draw_x_y()



print(
"██╗░░██╗███████╗░██████╗░█████╗░██████╗░  ███╗░░░███╗░█████╗░██╗░░██╗██╗███╗░░██╗███████╗░██████╗██╗\n"
"██║░░██║██╔════╝██╔════╝██╔══██╗██╔══██╗  ████╗░████║██╔══██╗██║░██╔╝██║████╗░██║██╔════╝██╔════╝██║\n"
"███████║█████╗░░╚█████╗░███████║██████╔╝  ██╔████╔██║███████║█████═╝░██║██╔██╗██║█████╗░░╚█████╗░██║\n"
"██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔═══╝░  ██║╚██╔╝██║██╔══██║██╔═██╗░██║██║╚████║██╔══╝░░░╚═══██╗██║\n"
"██║░░██║███████╗██████╔╝██║░░██║██║░░░░░  ██║░╚═╝░██║██║░░██║██║░╚██╗██║██║░╚███║███████╗██████╔╝██║\n"
"╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░░░░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝╚═════╝░╚═╝\n")

print(
"█▀▄▀█ █▀▀ █  █ █▀▄▀█ █▀▀ ▀▀█▀▀ 　 █▀▄▀█ █▀▀ █▀▀█ ▀▀█▀▀ 　 █▀▀█ █   ▀▀█▀▀ █  █ █▀▀▄ ▀▀█▀▀ █▀▀█ █▀▀\n" 
"█ ▀ █ █▀▀ █▀▀█ █ ▀ █ █▀▀   █   　 █ ▀ █ █▀▀ █▄▄▀   █   　 █▄▄█ █     █   █  █ █  █   █   █▄▄█ ▀▀█\n" 
"▀   ▀ ▀▀▀ ▀  ▀ ▀   ▀ ▀▀▀   ▀   　 ▀   ▀ ▀▀▀ ▀ ▀▀   ▀   　 ▀  ▀ ▀▀▀   ▀    ▀▀  ▀  ▀   ▀   ▀  ▀ ▀▀▀\n")


check_function = True
while True:
    helping_num = 1
    print("Hangi işlemi yapmak istersiniz\n"
          "1 - Toplama\n"
          "2 - Çıkarma\n"
          "3 - Çarpma\n"
          "4 - Bölme\n"
          "5 - Mod Alma(Kalan bul)\n"
          "6 - Üs Alma\n"
          "7 - Kök Alma\n"
          "8 - Faktöriyel Alma\n"
          "9 - Rastgele sayı seçici\n"
          "10 - Doğrusal fonksiyon çiz(beta)\n"
          "11 - Görüş bildirin!\n"
          "Yardım için 'h' giriniz.\n"
          "Çıkış için 'e' giriniz.\n")

    operation = input("İşlem numarasını giriniz:")
    exit = False
    if operation == "1":
        print("Toplama işlemini seçtiniz.")
        while exit == False:
            try:
                first_num = float(input("Hangi sayıyı toplamak istersiniz:"))
                exit = True
            except:
                print("Lütfen bir sayı giriniz!")
        exit = False
        while exit == False:
            try:
                second_num = float(input(f"{first_num} sayısını hangi sayı ile toplamak istersiniz:"))
                exit = True
            except:
                print("Lütfen bir sayı giriniz!")
        print("Sonuç:", first_num + second_num, "\n")
        input()

    elif operation == "2":
        print("Çıkarma işlemini seçtiniz.")
        while exit == False:
            try:
                first_num = float(input("Eksilen sayı nedir:"))
                exit = True
            except:
                print("Lütfen bir sayı giriniz!")
        exit = False
        while exit == False:
            try:
                second_num = float(input(f"{first_num} sayısından kaçı çıkarmak istersiniz:"))
                exit = True
            except:
                print("Lütfen bir sayı giriniz!")
        print("Sonuç:", first_num - second_num, "\n")
        input()

    elif operation == "3":
        print("Çarpma işlemini seçtiniz.")
        while exit == False:
            try:
                first_num = float(input("Kaçı çarpmak istersiniz:"))
                exit = True
            except:
                print("Lütfen bir sayı giriniz!")
        exit = False
        while exit == False:
            try:
                second_num = float(input(f"{first_num} sayısını kaçla çarpmak istersiniz:"))
                exit = True
            except:
                print("Lütfen bir sayı giriniz!")
        print("Sonuç:", first_num * second_num, "\n")
        input()

    elif operation == "4":
        print("Bölme işlemini seçtiniz.")
        while exit == False:
            try:
                first_num = float(input("Bölünen kaç:"))
                exit = True
            except:
                print("Lütfen bir sayı giriniz!")
        exit = False
        while exit == False:
            try:
                second_num = float(input(f"{first_num} sayısını kaça bölmek istersiniz:"))
                exit = True
            except:
                print("Lütfen bir sayı giriniz!")
        try:
            print("Sonuç:", first_num / second_num, "\n")
            input()
        except ZeroDivisionError:
            print("Sıfıra bölünemez!", "\n")
            input()

    elif operation == "5":
        print("Mod Alma işlemini seçtiniz.")
        while exit == False:
            try:
                first_num = float(input("Kaçın modunu almak istersiniz:"))
                exit = True
            except:
                print("Lütfen bir sayı giriniz!")
        exit = False
        while exit == False:
            try:
                second_num = float(input(f"{first_num} sayısını kaçla modunu almak istersiniz:"))
                exit = True
            except:
                print("Lütfen bir sayı giriniz!")
        try:
            print("Sonuç:", first_num % second_num, "\n")
        except ZeroDivisionError:
            print("0 giremezsiniz")
        input()

    elif operation == "6":
        print("Üs Alma işlemini seçtiniz.")
        while exit == False:
            try:
                first_num = float(input("Taban sayısını giriniz:"))
                exit = True
            except:
                print("Lütfen bir sayı giriniz!")
        exit = False
        while exit == False:
            try:
                second_num = float(input(f"{first_num} sayısının üssünü giriniz:"))
                exit = True
            except:
                print("Lütfen bir sayı giriniz!")
        print("Sonuç:", first_num ** second_num, "\n")
        input()
    elif operation == "7":
        print("Kök Alma işlemini seçtiniz.")
        while exit == False:
            try:
                first_num = float(input("Kaçın kökünü almak istersiniz:"))
                exit = True
            except:
                print("Lütfen bir sayı giriniz!")
        exit = False
        while exit == False:
            try:
                second_num = float(input(f"{first_num} sayısının kaç kökünü almak istersiniz:"))
                exit = True
            except:
                print("Lütfen bir sayı giriniz!")
        print("Sonuç:", pow(first_num, 1/second_num), "\n")
        input()

    elif operation == "8":
        print("Faktöriyel Alma işlemini seçtiniz.")
        while exit == False:
            try:
                first_num = int(input("Kaçın faktöriyelini almak istersiniz:"))
                exit = True
            except:
                print("Tekrar deneyiniz!")
        exit = False

        for i in range(first_num):
            helping_num = helping_num * (i+1)
        print("Sonuç:", helping_num, "\n")
        input()

    elif operation == "9":
        print("Rastgele Sayı Seçme işlemini seçtiniz.")
        while exit == False:
            try:
                how_many = int(input("Kaç adet sayı istersiniz:"))
                exit = True
            except:
                pass
        exit = False
        while exit == False:
            try:
                first_num = float(input("Minimum değer nedir:"))
                exit = True
            except:
                print("Lütfen bir sayı giriniz!")
        exit = False
        while exit == False:
            try:
                second_num = float(input("Maksimum değer nedir:"))
                if second_num < first_num:
                    print("Maksimum değer minimum değerden küçük olamaz!")
                else:
                    exit = True
            except:
                print("Lütfen bir sayı giriniz!")
        for i in range (how_many):
            print("Sonuç:", random.randint(first_num, second_num), "\n")
        input()

    elif operation == "10":
        if check_function == False:
            print("Malesef bazı nedenlerden dolayı ikinci kez fonksiyon çizemiyoruz. Sadece programı kapatıp açarsanız çalışmaktadır. İlginiz ve anlayışınız için teşekkür ederiz.\n")
            input()
        else:
            print("Doğrusal fonksiyon oluşturmayı seçtiniz.")
            choice = input("Fonksiyonu oluşturduktan sonra resmini kaydetmek ister misiniz? Evet için 'e' giriniz:")
            print("Doğrusal fonksiyonların formülü 'ax+b'dir.")
            while exit == False:
                try:
                    b_num = float(input("'b' değerini giriniz:"))
                    exit = True
                except:
                    print("Lütfen bir sayı giriniz!")
            print(f"    ax+{b_num}")
            exit = False
            while exit == False:
                try:
                    coefficient_x = float(input("x, yani 'a'nın katsayısı kaçtır:"))
                    if coefficient_x == 0:
                        print("0'dan farklı bir sayı giriniz.")
                        Nasılsın
                    exit = True
                except:
                    print("Lütfen bir sayı giriniz!")
            print(f"{coefficient_x}a+{b_num} fonksiyonu çiziliyor, yeni pencereye bakınız.")
            y = b_num*100

            x = -b_num/coefficient_x*100

            if (x < 0 or y < 0):
                while x < -400 or y < -400:
                    x = x * 0.9
                    y = y * 0.9
            else:
                while y > 400 or x > 400:
                    x = x*0.9
                    y = y*0.9
            root = turtle.Screen()
            root.setup(800, 800)
            root.title("Fonksiyon Çizimi")
            turtle2 = turtle.Turtle()
            turtle2.speed(10)
            draw_bg()
            goto_x_zero()

            check_function = False
            if choice == "e":
                ts = turtle2.getscreen()
                ts.getcanvas().postscript(file="fonksiyon.eps")
            root.mainloop()
            input()

    elif operation == "11":
        print("Görüşleriniz bizim için değerlidir ve ne düşündüğünüzü bilmek isteriz!\n"
              "Adınızı yazın, düşüncelerinizi ve önerilerinizi belirtin.")
        mail_adress = "mmailg2005@gmail.com"
        password = "do not hack my acoount"
        send_to = "mhmtmrtltnts@gmail.com"
        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login(mail_adress, password)
            message = input("Mesajınız:")
            message = message.encode()
            mail.sendmail(mail_adress, send_to, message)
            print("Mesajınız alınmıştır. Teşekkürler!")
        except:
            print("Malesef bir sorun oluştu.")
        input()
    elif operation == "e":
        print("Kullandığınız için teşekkür ederiz!\n"
              "Problemlerinizi çözmek için her zaman burada olacağız")
        input()
        sys.exit()
    elif operation == "h":
        print("Bu program bir hesap makinesidir.\n"
              "İlk 8 işlem temel işlemleri yapmanıza olanak sağlar.\n"
              "9. işlem ile rastgele bir sayılar seçebilirsiniz.\n"
              "10. işlem ile de doğrusal bir fonksiyon çizebilirsiniz.\n"
              "11. işlem ile görüş ve önerilerinizi bildirebilirsiniz.")
        input()
    else:
        print("Malesef ne kastetmek istediğinizi anlayamadık. Lütfen işlem numarasını doğru girdiğinizden emin olun.")
        input()

