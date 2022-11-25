# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 21:36:32 2022

@author: elif
"""
import sqlite3

class Kitap():
    def __init__(self,isim,yazar,yayınevi,tür,baskı,sayfasay):
        self.isim=isim
        self.yazar=yazar
        self.yayınevi=yayınevi
        self.tür=tür
        self.baskı=baskı
        self.sayfasay=sayfasay
    def __str__(self):
        return "kitap ismi: {}\nyazar: {}\nyayınevi: {}\ntür: {}\nbaskı: {}\nsayfasay: {}\n".format(
            self.isim,self.yazar,self.yayınevi,self.tür,self.baskı,self.sayfasay)
    
class Kütüphane():
    def __init__(self):
        self.baglantı_olustur()
    def baglantı_olustur(self):
        self.bag=sqlite3.connect("kütüphane1.db")
        self.cursor = self.bag.cursor()
        sorgu="Create Table If Not Exists kitaplar (isim TEXT, yazar TEXT,yayınevi TEXT,tür TEXT,baskı INT,sayfasay INT)"
        self.cursor.execute(sorgu)
        self.bag.commit()
    def bag_kapat(self):
        self.bag.close()
    def kitap_göster(self):
        sorgu="Select * from kitaplar"
        self.cursor.execute(sorgu)
        kitaplar=self.cursor.fetchall()
        if(len(kitaplar) == 0):
            print("Kütüphanede kitap yok")
            
        else:
            for i in kitaplar:
                print("kitap ismi: {}\nyazar: {}\nyayınevi: {}\ntür: {}\nbaskı: {}\nsayfasay: {}\n".format(
                    i[0],i[1],i[2],i[3],i[4],i[5]))
    def sorgu_kitap(self,isim):
        sorgu="select * from kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()
        if(len(kitaplar) == 0):
            print("Kütüphanede aradığınız kitap yok")
        else:
            for i in kitaplar:
                print("kitap ismi: {}\nyazar: {}\nyayınevi: {}\ntür: {}\nbaskı: {}\nsayfasay: {}\n".format(
                    i[0],i[1],i[2],i[3],i[4],i[5]))
        
    def ekle(self,isim,yazar,yayınevi,tür,baskı,sayfasay):
        sorgu="Insert into kitaplar values(?,?,?,?,?,?)"
        self.cursor.execute(sorgu,(isim,yazar,yayınevi,tür,baskı,sayfasay))
        self.bag.commit()
    def sil(self,isim):
        sorgu="Delete from kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.bag.commit()
    def baskı(self,isim):
        sorgu="Select * from kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()
        if(len(kitaplar) == 0):
            print("Kütüphanede aradığınız kitap yok")
        else:
            baskı=kitaplar[0][4]
            baskı +=1
            sorgu2 ="Update kitaplar set baskı = ? where isim = ? "
            self.cursor.execute(sorgu2,(baskı,isim))
            self.bag.commit()