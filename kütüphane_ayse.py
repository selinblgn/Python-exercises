#Ayşe Selin Bilgin
import sqlite3

data=sqlite3.Connection("kütüphane.sqlite")
cursor=data.cursor()


class Kütüphane():
 
    def __init__(self,isim,yazar,yayınevi,tür,baski,sayfasay):
        self.isim=isim
        self.yazar=yazar
        self.yayınevi=yayınevi
        self.tür=tür
        self.baski=baski
        self.sayfasay=sayfasay

          

    def kitap_göster():
        print(cursor.execute("SELECT * FROM kitaplar").fetchall())


    def sorgu_kitap(isim):
        cursor.execute("SELECT * FROM kitaplar WHERE isim= ?",(isim,))
        
        if len(cursor.fetchall())==0:
            print("Aradığınız kitap bulunamadı")
        else:
            print(cursor.fetchall())

        

    def ekle(isim,yazar,yayınevi,tür,baskı,sayfasay):
        cursor.execute("CREATE TABLE IF NOT EXISTS kitaplar(isim TEXT,yazar TEXT,yayınevi TEXT,tür TEXT,baskı INT, sayfasay INT) ")
        cursor.execute("INSERT INTO kitaplar VALUES(?,?,?,?,?,?)",(isim,yazar,yayınevi,tür,baskı,sayfasay,))
        data.commit()

        
    def sil(isim):
        cursor.execute("DELETE FROM kitaplar WHERE isim=?",(isim,))
        data.commit()

    def baski(isim,baski):
        cursor.execute("UPDATE kitaplar SET baskı=? WHERE isim= ?",(baski,isim,))
        data.commit() 