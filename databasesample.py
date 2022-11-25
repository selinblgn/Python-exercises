import sqlite3,os
dosya_mevcut=os.path.exists("database.sqlite")

database=sqlite3.connect("database.sqlite")

cursor=database.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS adres_defteri(isim TEXT,adres TEXT)")

if not dosya_mevcut:
    cursor.execute("INSERT INTO adres_defteri VALUES ('Tuba','Antep'),('Gizem','Osmaniye')")
    database.commit()

veriler=[('Esile','Hakkari'),('Aynur','Bitlis'),('Zehra','Mersin'),('Nazan','Van')]
for i in veriler:
    pass
  #cursor.execute("INSERT INTO adres_defteri VALUES (?,?)",i)

database.commit()

cursor.execute("SELECT isim FROM adres_defteri")
isimler=cursor.fetchall()
#print(isimler)

cursor.execute("SELECT name FROM sqlite_master")
#print(cursor.fetchall())
cursor.execute("SELECT * FROM  adres_defteri")
#print(*cursor)
for i in range(5):
    pass
    #print(cursor.fetchone())
    #print("finish")
    
#print(cursor.execute("SELECT sql FROM sqlite_master").fetchall())    

isim=input("isim girin:")
adres=input("adres girin")

#cursor.execute(""" INSERT INTO adres_defteri VALUES ( '%s','%s')"""%(isim,adres))
#database.commit()


cursor.execute("SELECT * FROM adres_defteri")
data=cursor.fetchone()
#print(data[0])

#if data[1]=="Ayşe":
#   print("buyur Ayşecim")
#else:
 #  print("giremezsiniz")  

if isim.isalnum() and adres.isalnum():   
    print(cursor.execute("SELECT * FROM adres_defteri WHERE isim=? AND adres=?",(isim,adres)).fetchone())
    print("oldu5")