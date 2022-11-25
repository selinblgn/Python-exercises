# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 21:36:52 2022

@author: elif
"""

from kütüphane_ayse import Kütüphane 

print("""
      Kütüphaneye hoşgeldin
      
      İşlemler:
          1-kitapları Göster
          2-Kitap Sorgula
          3-Kitap Ekle
          4-Kitap Sil
          5-Baskı Yükselet
      çıkmak İçin q ya basın      
      """)


while True:
    işlem=input("Yapmak istediğiniz işlemi giriniz")
    if(işlem=="q"):
        print("Programdan çıkıyorsunuz")
        break
    elif(işlem=="1"):
        Kütüphane.kitap_göster()
    elif(işlem=="2"):
        isim=input("Aradığınız kitabın adını giriniz")
        Kütüphane.sorgu_kitap(isim)
    elif(işlem=="3"):
        isim=input("İsmi: ")
        yazar=input("yazarı: ")
        yayınevi=input("yayınevi: ")
        tür=input("tür: ")
        baskı=int(input("baskı: "))
        sayfasay=int(input("sayfa sayısı: "))
        Kütüphane.ekle(isim,yazar,yayınevi,tür,baskı,sayfasay)
        print("kitap eklendi")
    elif(işlem=="4"):
        isim=input("Silmek istediğiniz kitabın adını giriniz")
        Kütüphane.sil(isim)
        print("{} kitabı silindi".format(isim))
    elif(işlem=="5"):
        isim=input("Baskı sayısını güncellemek istediğiniz kitabın adını giriniz ")
        baski=int(input("Baskı yılını giriniz "))
        Kütüphane.baski(isim,baski)
        print("{} baskı yılı güncellendi".format(isim))
    else:
        print("geçersiz işlem")


