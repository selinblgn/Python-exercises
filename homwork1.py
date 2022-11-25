#dik kenar alan hesap

"""a=int(input("ilk dik kenarı yazın"))
b=int(input("ikinci dik kenarı yazın"))
print((a*b)/2)"""

#kullanıcıdan iki tane girdi alıp değer değiştirme 


"""a=input("ilk değer")
b=input("ikinci değer")
print(a,b)
c=a
a=b
b=c
print(a,b)"""

#vize final notu hesaplama 


vize=int(input("vize notunu giriniz"))
proje=int(input("proje notunu giriniz"))
final=int(input("final notunu giriniz"))

sonuc=int((vize*30+proje*20+final*50)/100)

if  (sonuc >=80):
    harf_notu="AA"
elif (sonuc <80 and sonuc>=75):
    harf_notu="BA" 
elif sonuc<75 and sonuc>=70:
    harf_notu="BB" 
elif sonuc<70 and sonuc>=60:
    harf_notu="BC" 
elif sonuc<60 and sonuc>=50:
    harf_notu="CC" 
elif sonuc<50 and sonuc>=45:
    harf_notu="DC" 
elif sonuc<45 and sonuc>=40:
    harf_notu="DD" 
elif sonuc<40 and sonuc>=35:
    harf_notu="FD"                          
else:
    harf_notu="FF"

print(harf_notu)