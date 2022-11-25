import sqlite3

marketdata=sqlite3.Connection("marketdata.sqlite")
cursor=marketdata.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS ürünler(ürün_adı TEXT,stok_sayısı INT,fiyat INT)")

def satınal(ürün_adı,miktar):
    cursor.execute("SELECT stok_sayısı  FROM ürünler WHERE ürün_adı=? ",(ürün_adı,))
    stok=cursor.fetchone()[0]
    stok=stok-miktar
    
    if stok<0:
        print("Üründen sadece {} tane var  ".format(stok+miktar)) 

    else:  
     cursor.execute("UPDATE ürünler SET stok_sayısı='%s' WHERE ürün_adı=? "%(stok),(ürün_adı,))
     marketdata.commit()    
     
     
def tutar(ürün_adı,miktar):
    cursor.execute("SELECT fiyat  FROM ürünler WHERE ürün_adı=? ",(ürün_adı,))
    tutar=cursor.fetchone()[0]
    tutar=tutar*miktar
    print("Tutar:",tutar)

def delete():
    cursor.execute("DELETE FROM ürünler WHERE stok_sayısı=0 ") 
    marketdata.commit()   
 
ürün_adı=input("Satın almak istediğiniz ürünün adı:")
miktar=int(input("Almak istediğiniz miktarı girin:")) 
   
satınal(ürün_adı,miktar)
tutar(ürün_adı,miktar)
delete()
marketdata.close()