"""a=3;
x=6;
b=9;
c=8;

f_x=int(a*(x**2)+2*b*x+c)
print(f_x)

a="merhaba dünya"
b="python bootcamp"
print(b[3])
print(b[5:9])
print(b[2:9:3])
print(b[:9])

a="çiçek"

a="güzel" + a

print(a)

a="Güzel"
b="Gören"
c="Güzel"
d="Düşünür"

e=a + b+ c+ d

print(e)
a=15
b=2
c=int(a/b)
print(c)

a="3.890"
b=float(a)
print(type(b))
print(b)

print(*"python")


liste2.append("yenidünya")
liste2.sort()
liste2.sort(reverse=True)

iciceliste=[liste11,liste12,liste13]"""

"""
demet=()
type(demet)

demet=(1,2,3,4,5,6)
print(type(demet))
print(demet[4])
print(demet.index(5))
demet3=(3,5,6,1,3,7,3,4,1,8,7)
print(demet3.count(7))

sözlük={}
sözlük2=dict()

sözlük={"elma":15,"kiraz":20,"incir":30}
print(sözlük)
print(sözlük.items())
print(sözlük.values())
print(sözlük.keys())

sözlük["şeftali"]=30
print(sözlük)
icsözlük={"ingilizce":{"a":1,"b":2}, "almanca":{"d":3,"g":7},"italyanca":{"t":"tea","a":"aya"}}
print(icsözlük)
print(icsözlük["ingilizce"]["a"])

icsözlük.values()
print(icsözlük["ingilizce"].values())

print(icsözlük.keys())
print(icsözlük.items())

a=int(input("bir sayı girin "))
b=5
print(a+b)
c=int(input("birinci sayıyı giriniz"))
d=int(input("ikinci sayıyı giriniz"))
e=int(input("üçüncü sayıyı giriniz"))
print("Toplam:", c+d+e)"""


"""a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
x=int(input("x:"))
print(f(x))
delta=b**2-4*a*c
print(delta)"""


"""print("oyuna kaydolun lütfen")
ad=input("adınızı giriniz")
soyad=input("soyadınızı giriniz")
takım=input("takım adınız ")
print("bilgilerinizi kontrol ediniz")
print("adınız={}\nSoyadınız={}\nTakımınız={}".format(ad,soyad,takım))"""


"""a=True
b=False
a=bool(12)
b=bool(7)
c=bool(0)
d=bool(0.0)
print(a,b,c,d)

a=None
print(a)"""

"""a=1>3 or 1<3
print(a)

print("Araba"<"Zula"and("Bebek"<"Çocuk" or (not 14)))
print(14+6==20 and 50-27==23 or not 14)

a=5
if a==5:
    print(a)
print("kontrol sağlandı")   
adı=input("adınızı girin ")
soyadı=input("soyadınızı giriniz")
if (adı=="Aslıhan" and soyadı=="Ayvaz"):
    print("adınızı doğru girdiniz ")
else:
    print("böyle bir kişi yok ") """

"""sayı=int(input("sayı giriniz"))
if(sayı>0):
    print("sayı pozitif")
elif(sayı<0):
    print("negatif sayı")
else:
    print("sayı sıfırdır") """    



"""kullanıcı_adı=input("kullanıcı adını giriniz")
parola=input("parola giriniz")

if(kullanıcı_adı !="ayşe" and parola=="123" ):
    print("kullanıcı adı hatalı")
elif(kullanıcı_adı=="ayşe" and parola!="123"):
    print("parola hatalı")
elif(kullanıcı_adı!="ayşe" and parola!="123"):       
     print("ikiside hatalı")
else:
    print("başarılı giriş yaptınız")"""      


"""a=int(input("ilk sayı="))
b=int(input("ikinci sayı="))
islem=input("yapmak istediğiniz işlemi giriniz")

if(islem=="1"):
    print("{} ve {}toplam {} ".format(a,b,a+b))
elif(islem=="2"):
    print("{} ve {}fark {} ".format(a,b,a-b)) 
elif(islem=="3"):
    print("{} ve {}çarpm {} ".format(a,b,a*b))
elif(islem=="4" and b!=0):
    print("{} ve {}bölme {} ".format(a,b,a/b))
elif(islem=="4" and b==0):
    print("{} eşit sıfır olduğundan bölme yapılamaz  ".format(b))    
else:
    print("geçerli bir işlem numarası giriniz") """              

"""boy=float(input("Boyunuzu giriniz"))
kilo=int(input("Kilonuzu giriniz"))

bki=kilo/(boy**2)
if(bki<18.5):
    print("Zayıf")
elif(18.5>=18.5 and bki<25):
    print("Normal")
elif(bki>=25 and bki<30):
     print("Fazla kilolu")
else:
    print("Obez")"""



"""liste=[1,2,3,4,5]

for eleman in liste:
    print(eleman)
toplam=0
carpım=1
for eleman in liste:
    toplam+=eleman
    print("listenin elemanları toplamı", toplam)

for eleman in liste:
    carpım*=eleman
    print("çarpım sonucu ", carpım)
           

a="Python"

for i in a:
    print(i)

demet=(1,2,3,4,5)
for i in demet:
    print(i)    

liste=[(1,2,"a"),(3,4,"b"),(5,6,"c")]

for i in liste:
    print(i)
for (i,j,k) in liste: 
     print(i,j,k)  
for (i,j,k) in liste: 
     print(i*j*k)   

sözlük={"çilek":25,"şeftali":23,"incir":40}
#for i in sözlük:
 #   print(i)
for i in sözlük.keys():
    print(type(i))
    print(i)
for i in sözlük.items():
    print(type(i))
    print(i)"""

#for i in sözlük.values():
   # print(i)    

"""i=0

while(i<10):
    print(i)
    i+=2

while(i<5):
    print("python",1)
    i+=1

print(*range(0,20,2)) 
print(*range(20,0,-1))"""


#or i in range(0,10):
  #  print(i)
   # i+=1

#while(i<20):
    #print(i)
    #if(i==3):
     #  print("hedefe ulaştın") 
     
      # break 


"""while True:
    isim=input("isminizi girini.Çıkmak için q'ya basınız ")
    if(isim=="q"):
        break
    print(isim) """

"""liste=[1,2,3,4,5,6,7,8,]
for i in liste:
        print("i=",i)

for i in liste:
        if(i==3 or i==5):
            continue
        print("i:",i)

i=0
while(i<10):
    print(i)
    if(i==2):
        i+=1
        continue
    i+=1
     
liste=[1,2,3,4]
liste.append(5)
liste2=list()

for i in liste:
    liste2.append(i)

print(liste2)   
liste3=[i for i in liste2]
print(liste3)

liste4=[i**2 for i in liste]
print(liste4)
a="Python"
liste5=[i for i in a ]
print(liste5)

liste6=[[1,2,3,4,5],[6,7,8,9],[10,11,12,13]]
liste7=[]

for i in liste6:
    for k in i:
        print(k)
        liste7.append(k)
print(liste7)

liste8=[k for i in liste6 for k in i]
print(liste8)"""


"""kayıt_kul_adı="Aslıhan"
kayıt_kul_par="Parola12345"
giris_hakkı=3
while True:
    kullanıcı_adı=input("kullanıcı adını giriniz")
    kullanıcı_par=input("parolanızı giriniz")
    if(kayıt_kul_adı==kullanıcı_adı and kayıt_kul_par!=kullanı_par):
        print("yanlış parola")
        giris_hakkı-=1

    elif(kayıt_kul_adı!=kullanıcı_adı and kayıt_kul_par==kullanı_par):
        print("yanlış adı")
        giris_hakkı-=1  
    elif(kayıt_kul_adı==kullanıcı_adı and kayıt_kul_par!=kullanı_par):
        print("yanlış parola")
        giris_hakkı-=1 
      
    elif(kayıt_kul_adı==kullanıcı_adı and kayıt_kul_par==kullanı_par):
        print("başarılı giriş")
        giris_hakkı-=1
    else:
        print("başarılı giriş yaptınız")
        break
    if(giris_hakkı==0):
        print("giriş hakkınız doldu")     
        break"""

"""print("1-bakiye sorgulama 2-para yatırma 3 para çekme ")
bakiye=15000
while True:
    islem=input("yapmak istediğiniz işlemş giriniz") 
    if(islem=="q"):
        print("kartınızı unutmayın")
        break
    elif(islem=="1"):
        print("{} bakiyeniz bulunmakta".format(bakiye))
        print("devam etmek istiyorsanız d ye basın ", input())
      
        continue
    elif(islem=="2"):
        miktar=int(input("yatırmak istediğiniz parayı girin"))
        bakiye+=miktar
        islem=input("devam etmek istiyorsanız d ye basın")
        if(islem=="d"):        
         continue
        else:
            break
    elif(islem=="3"):
        miktar=int(input("çekmek istediğiniz miktarı girin"))
        if(bakiye-miktar<0):
            print("bakiyeniz yetersiz")
            print("{} bakiyeniz var".format(bakiye))
            islem=input("devam etmekl için d ye basınız ")
            if(islem=="d"):        
               continue
            
        bakiye-=miktar
        islem=input("devam etmek istiyorsanız d ye basın")
        if(islem=="d"):        
          continue 
    else:
        print("gecerli bir işlem giriniz")"""
#print("çıkış için q ya basın")

"""while True:
    sayı=input("sayınızı veya çıkış kodunu giriniz")
    if (sayı=="q"):
        print("programdan çıkıyoruz")
        break
    sayı=int(sayı)
    faktoriyel=1
    for i in range(2, sayı+1):
        faktoriyel*=i
    print ("{} faktoriyel sonucu{}".format(sayı,faktoriyel)) """ 
    

"""ilk_sayı=1
ikinci_sayı=1
fibonacci=[ilk_sayı,ikinci_sayı]
for i in range(50):
      ilk_sayı,ikinci_sayı=ikinci_sayı,ikinci_sayı+ilk_sayı
      fibonacci.append(ikinci_sayı)
print(fibonacci)"""

"""for i in range(1,6):
    print("**********")
    for j in range (1,11):
        print("{} x {}={}".format(i,j,i*j))"""




"""def topla(a,b):
    return a+b
print(type(topla)) 

class  telefon():
    model="samsung s22"
    renk="yeşil"
    ram:8
    kamera_sayısı=4

telefon1=telefon()
print(type(telefon1))
print(telefon1.model)
dir(telefon1)

telefon2=telefon()

class telefon():
    def __init__(self):
        print("init çalıştı")


telefon1=telefon()

class telefon():
    def __init__(self,model,renk,ram,kamera_sayısı):
        self.model=model
        self.renk=renk
        self.ram=ram
        self.kamera_sayısı=kamera_sayısı

telefon1=telefon("ıphone 13 ","beyaz",6,5)
telefon2=telefon("samsung s22","kırmızı",8,4)
print(telefon1.model)
print(telefon2.model)"""        

"""try:
    a=int(input("birinci sayıyı giriniz"))
    b=int(input("ikinci sayıyı giriniz"))
    print(a/b)

except (ValueError):
    print("lütfen girdiğiniz değerin bir sayı olduğundan emin olun")
except ZeroDivisionError:
     print("sayı sıfıra bölünemez")
finally:
      print("beni çağırmadann gidemezsin") 
print("bu blokla işimiz bitti")          

def terscevir(kelime):
    if(type(kelime)!=str):
        raise ValueError("lütfen kelime girin")
    else:
        return kelime[::-1]
print(terscevir("python"))

open("deneme.txt","w")
file=open("deneme.txt","w",encoding="utf-8")
file.write("osman Aga\n")
file.close()

file=open("deneme.txt","a",encoding="utf-8")
file.write("Arzu Karadağ\n")
file.close
file=open("deneme.txt","r",encoding="utf-8")
print(file)
try:
    file=open("deneme1.txt","r",encoding="utf-8")
except FileNotFoundError:
    print("böyle bir dosya yok")
for i in file:
    print(i,end="")


file=open("deneme.txt","r",encoding="utf-8")
icerik=file.read()
print("dosya içeriği\n",icerik,sep="")
icerik2=file.read()
print("dosya 2. içeriği\n",icerik2,sep="")
file.close()

file=open("deneme.txt","r",encoding="utf-8")
icerik=file.readline()
print("dosya içeriği\n",icerik,sep="")
print(file.readline())

with open("deneme.txt","r",encoding="utf-8") as file:
   file.seek(23)
   file.write("Burcu Sevinç")
   file.seek(0) 
  #arzu=file.read(17)
   #print(arzu)
   print(file.tell())
   file.close()
file.close
with open("deneme.txt","r+",encoding="utf-8") as file:
     icerik=file.read()
     icerik="Arzu Kardoğan"+icerik
     file.seek(0)
     file.write(icerik)
     print(icerik)
     liste=file.readlines()
     liste.insert(2,"Büşra Oran")
     file.seek(0)
     for i in liste:
        file.write(i)
        file.close


     file.write(icerik)
     print(icerik)"""

"""def double(x):
    return x*2

double(4)
liste=[1,2,34,5,67,8]
for i in liste:
    print(double(i))

list(map(double,[1,2,34,5,67,8])) 
list(map(lambda x:x*2,[1,2,34,5,67,8])) 

liste2=[3,4,5,9,11,12]

list(map(lambda x,y:x+y,liste,liste2))

print(bin(4))

print(pow(2,4))


print("python".upper())

liste="güzel gören güzel düşünür".split(" ")
print(liste)

x=set()
x=set(liste)
print(x)"""

"""import sqlite3

con=sqlite3.connect("kütüphane.db")
cursor=con.cursor()


def tablo_ol():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (isim TEXT, yazar TEXT,yayınevi TEXT,sayfasay INT)")
    con.commit()
def veri_ekle(isim,yazar,yayınevi,sayfasay):
     cursor.execute("Insert Into kitaplik values(?,?,?,?) " ),(isim,yazar,yayınevi,sayfasay)
def veri_al(yayınevi):
    cursor.execute("Select isim,yazar from kitaplik Where yayınevi=? ", (yayınevi,))
    data=cursor.fetchall()
    print("elimizdeki  veriler")
    for i in data:
        print(i)
def güncelleme(yayınevi):
    cursor.execute("Update kitaplik set yayınevi = ? where yayınevi = ? ",("indigo" ,yayınevi,))
    con.commit()

tablo_ol()

güncelleme("iş bankası")
#cursor.execute("Insert Into kitaplik values ('insan ne ile yasar','tolsoy','iş bankası','100')")
#con.commit()
#veri_ekle("savas ve barış","tolstoy","yapıkredi",2000)
#veri_ekle(input("kitap ismi"),input("yazar ismi"),input("yayınevi"),int(input("sayfasayısı")))
con.close() """


