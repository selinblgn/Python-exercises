# -*- coding: utf-8  -*-

#print("selam")

#myvar=input('gir:')

#print("Godora")
#print("Godoro","Yazılım","Eğitim")
#line=input("Dize gir:")
#print("Girilen dize:"+line)
#print("Bir" ,  end ='')
#print("İki", end=' ')
#print("Üç", end=' \t ')
#print("Dört", end='\n')#

#myint= int("3")
#myint=int(input("Bütün sayı gir:"))
#mystring=str(myint)
#print("Bütün sayı:"+ str(myint))

#print("Ondalık sayı:"+hex(myint))
#print("Sekizlik sayı" +oct(myint))
#print("İkilik sayı" +bin(myint))

#myfloat=float("3")
#myint=float(int("Kayan sayı gir:"))
#mystring=str(myint)
#print("Kayan sayı:"+str(myint))

#positive_infinity=float('inf')
#print(positive_infinity)

"""mystring='Godoro Python'
print(mystring)
mystring="Godoro Python"
print(mystring)
mystring="Godoro'nun Pyton'u"
print(mystring)"""
"""mystring='Godoro\'nun Python'
print(mystring)

print("Metin:"+mystring)
mystring=mystring.replace("Python","piton")
print(mystring)
mysub=mystring[7:10]
print(mysub)"""

"""yas=int(input("sayı  gir :"))

if yas<18:
    print("küçük")

else:
    print("büyük")"""


""""cases={1:'A', 2:'B', 3:'C'}
result1=cases[2]
print("Sonuç 1:" +result1)

result2=cases.get(3,'x')
print("Sonuç 2:"+result2)

assert result1=='D'"""

"""index=0
while index<5 :
    print("Sürece"+str(index+1))
    index+=1"""



"""index=0    
for index in list(range(30)):
    print("İçin:"+str(index+1))
    if index==1:
        print("Sürdür:"+str(index+1)+"\n")

    if index==2:
        print("Geç:"+str(index+1))
        pass
    if index==3:
        print("Kır:"+str(index+1))
        break

    print("Bitir"+str(index+1)+"\n") """

#mylist=[4,8,12] 

#for  myelement in mylist:
   # print(myelement)   

"""myiterator=iter(mylist)
print(myiterator)"""

"""mylist=[4,6,12]
print("İçin Döngüsünde")

for myelement in mylist:
    print("$",myelement)

myiterator=iter(mylist)
print("Yinelendirici & Sıradaki")
print("Öğe 1:",next(myiterator))
print("Öğe 2:",next(myiterator))
print("Öğe3:", next(myiterator)) 

print("Sürece Döngüsünde")
mylooper=iter(mylist)
while True:
 myitem=next(mylooper, None)
 if(myitem==None):
     break
print("*",myitem)"""

"""def mygenerator():
    yield  3
    yield  6
    yield  9 

print(type(mygenerator()))

for element in mygenerator():
 print(element)

generator=mygenerator()
print(next(generator))
print(next(generator))
print(next(generator))

def myproducer():
    for i in range(30):
        yield i

for y in myproducer():
    print(y)"""


"""mylist = ["Value1" , "Value2" , "Value3" , "Value4"]
print(mylist)
if "Value1" in mylist:
  print("öge var")
else:
  print("öge yok ")
for myelement in mylist:
    print(myelement)
for myindex in range(0,4):
    print(str(myindex)+" : "+mylist[myindex])  
     
print(mylist[1:3])
del mylist[3]
print(mylist)"""

"""#parolam 5-8 karakter uzunluğunda olsun.
#range kullanarak yapalım

parola=input("parolayı giriniz")
if len(parola) in range(5,8): 
    print("Parola kabul edildi")
else:
    print("parola kabul edilmedi")"""


"""mylist=("a", "b", "c", "d")
print(mylist)

myset={"x","y","z","x"}
print(myset)
myset.add("w")
print(myset)"""

#mydictionary={"a":2, "b":4,"c":1,"d":5,"e":1}
"""print(mydictionary["a"]) 
for mykey in mydictionary:
    print(str(mykey)+". öğe :" +str(mydictionary[mykey]))"""

#for x, y in mydictionary.items():
 #   print("açar :"+ str(x)+". öğe "+str(y))    

#number=[3]*10
#print(number)    

"""digits=[aa for aa in range(0,10)]
print(digits)

values=[1,2,3,4]
lengths=[my_function(value) for value in values ]
print(lengths)"""

"""numbers=[3]*10
print("üçler",numbers)
digits=[4 for value in range (10)]
print("dörtler", digits)
digits= [ value for value in  range (10)]
print("sayma sayıları", digits)
hourse=[value for value in range (9,18)]
print("saatler", hourse)
values=["Python","Java","C#","PHP"]
lengths=[len(i)for i in values]
print("uzunluklar", lengths)"""

"""list_right=[1,2,3,4,5]
list_left=[6,7,8,9,10]
list_all=list_right+list_left
print(list_all)
list_left.extend(list_right)
print(list_left)
list_right.reverse()
print(list_right)
myresult=list_all.copy()
print(myresult)
list_all.append(11)
print(list_all)"""

#point=(3,4,5)
#(x,y,z)=point
"""x,y,z=point
print("x:",x,"y:",y,"z",z)
_,_,z2=point
print("z:",z2,x,y,z)
_,y2,_=point
print("y:",y2)
print("son değişken")
print(_)
_=8
print("adsız değişken:" ,_)

_={'a':1,'b':2,'c':3}
print("adsız sözlük")
print(_)
print("adsız giriş")
print(_["b"])
print("kullanılmayan dizin")
for _ in range(3):
   print("sınama")

dictionary={"x":3,"y":4,"z":5}
print("kullanılmayan açar")
for _ , i in dictionary.items():
    print(i)"""

"""def my_function(*args):
     print("------")

     if(len(args)>=1):
        value_0=args[0]
        print("değer 0:", value_0)
     if(len(args)>=2):
        value_1=args[1]
        print("value 1 :", value_1) 
     print("tartışımlar:")
     for arg in args:
        print("\tdeğer:", arg)

my_function()
my_function('zero a')
my_function('zero b', 'one b ')
my_function('zero c ','one c', 'two c ') 

def my_function(**kwargs):
    print("------")

    if('name_x' in kwargs):
        value_x=kwargs['name_x']
        print("değer x:", value_x)

    if('name_y'in kwargs):
        value_y=kwargs['name_y']
        print("değer y :", value_y)

    print("açasöz tartışımları")
    for keyword, value in kwargs.items():
        print("\t", keyword,":",value)

my_function()
my_function(name_x=123)
my_function(name_x=123,name_y="godoro")"""


"""my_list=[91,92,93]
print("dizelge önce ", my_list)

my_list[1]=99
print("değiştir", my_list)
my_list.append(94)
print("ekle(append)", my_list)
my_list.insert(1,98)
print("ekle(insert) ", my_list)
my_list.remove(91)
print("sil(remove)", my_list)
my_list.pop(2)
print("sil(pop)", my_list)"""

"""positive=[True,True,True]
print("olumlula herhangi biri ", any(positive))
print("olumlular tümü", all(positive))

neutrals=[True,False,True]
print("ılınlar herhangi biri", any(neutrals))
print("ılınlar tümü", all(neutrals))

negatives=[False,False,False]
print("olumsuzlar herhangi biri", any(negatives))
print("olumsuzlar tümü", all(negatives))

values=["Python", "Java","C#","PHP"]
results_any=any(len(values)>=5 for values in values)
print("herhangi biri ?", results_any)

results_all=all(len(values)>=5 for values in values )
print("Tümü?", results_all)"""
"""
listeSayı=[1,2,3,4]
listeHarf=["a","b","c","d","e"]
zip(listeSayı,listeHarf)
print(*zip(listeSayı,listeHarf))"""
#newList=list()

#item=0

"""while(item<len(listeHarf)  and item<len(listeSayı)):
    newList.append((listeSayı[item],listeHarf[item]))
    item+=1

print(newList)"""



"""codes=['tr','az','tm','uz','ky','kk']
countries=['Türkiye','Azerbaycan','Türkmenistan','Özbekistan','Kazakistan','Kırgızistan']
zipped=zip(codes,countries)
print("Zipli yinelendirici", zipped)
print("Ülkeler")
for code,countries in zip (codes,countries):
    print("\t",code,":",countries)

ids=[301,302,303] 
names=['Telefon','Bilgisayar','Kamera'] 
prices=[1300,4355,1690]

def print_product(product):
    print("\t",product[0],product[1],product[2])
print("ürünler")
for product in zip (ids,names,prices):
    print_product(product) """

"""def get_length(name):
    return len(name)


names=["C","C++","Java","C#","PHP","Python"]

lengths=[]
for name in names:
    length=get_length(name)
    lengths.append(length)
print("Uzunluklar:")
for length in lengths:
    print("\t", length)

lengths=map(get_length,names)
print("uzunluk")
for length in lengths:
    print("\t",length)"""


class Apple:
     pass

apple=Apple()

print("calss name", Apple.__name__)
print("instance class", type(apple))
print("instance class name ", type(apple).__name__)
print("instance id",id(apple))

class Production:

  def __init__(self,parameter):
   print("yapılanıyor"+parameter)
   
product=Production("   elma")


print("class name ", Production.__name__)
print("instance class", type(product))
print("instance class mame", type(product).__name__)    