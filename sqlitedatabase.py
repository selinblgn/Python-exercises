import sqlite3
import random
import datetime
import time

con=sqlite3.connect("dersler.db")

cursor=con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS  ogrenciler(ad TEXT ,soyad TEXT ,numara INT,ogrencinotu INT) ")
    con.commit()
    
    
def degerekle():
    cursor.execute("INSERT INTO ogrenciler VALUES ('Hira Nur','Bilgin',5678,60)")
    con.commit()
    
  
#tabloolustur() 
#degerekle()  
def tabloekle():
    cursor.execute("CREATE TABLE IF NOT EXISTS Table1(zaman REAL,tarih TEXT, anahtarkelime TEXT,deger REAL)")
    con.commit()
def rasgeledegerekle():
    zaman=time.time()
    tarih=str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    anahtarkelime= "Python Sqlite3"
    deger=random.randrange(0,10)
    cursor.execute("INSERT INTO Table1(zaman,tarih, anahtarkelime ,deger ) VALUES (? ,? ,? ,? )",(zaman, tarih, anahtarkelime ,deger))
    con.commit()
def degerlerial():
    cursor.execute("SELECT * FROM Table1 WHERE deger=2.0") 
    data=cursor.fetchall()
    for i in data:
        print(i)
def silvegüncel():
    cursor.execute("SELECT * FROM Table1 ") 
    data=cursor.fetchall()
    print("ilk degerler----------------")
    for i in data:
        print(i)
    """cursor.execute("UPDATE Table1 SET deger=56 WHERE deger=2")  
    cursor.execute("SELECT * FROM Table1")
    data=cursor.fetchall()
    print("güncellendikten sonra")  
    for i in data:
        print(i) """ 
    cursor.execute("DELETE FROM Table1 WHERE deger=2")
    cursor.execute("SELECT * FROM Table1")
    data=cursor.fetchall()
    print("güncellendikten sonra")  
    for i in data:
        print(i)  
    con.commit()      
silvegüncel()
#degerlerial()   
#tabloekle()
i=0
while(i<10):
    #rasgeledegerekle()
    time.sleep(1)
    i+=1 
con.close()
print("done")      