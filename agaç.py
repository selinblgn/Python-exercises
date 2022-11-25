
"""from asyncio.proactor_events import _ProactorBasePipeTransport
from traceback import print_tb


class Person:
#attribute class
 address="no information"
#methods
#constructur(yapıcı method)
 def __init__(self,name,year):
    #object attribute
    self.name=name
    self.year=year
    print("init metodu çalıştı")
#instance method
 def intro(self,parametre):
    print("hello there ", parametre    + self.name)

 def calculateAge(self):
      return 2022-self.year

p1=Person("ayşe",1995)
p2=Person("selin",2000)
  
print(p1)
print(p2)
print(type(p1))
print(type(p2))
#updating
p1.intro('ayşe')
p2.intro("selin")
p1.name="bilgin"
#accessing object attributes
print(f'p1 name :{p1.name} year:{p1.year} address:{p1.address}')
print(f"yaşım:{p1.calculateAge()}")"""

"""class Circle:
    pi=3.14

    def __init__(self,yaricap=1):
        self.yaricap=yaricap

    def cevre_hesapla(self):
        return 2* self.pi*self.yaricap

    def alan_hesapla(self):
        return self.pi*(self.yaricap**2) 


c1=Circle()
c2=Circle(5)

print(f"c1:alan ={c1.alan_hesapla()} çevre={c1.cevre_hesapla()}")
print(f"c1:alan ={c2.alan_hesapla()} çevre={c2.cevre_hesapla()}")"""


"""class Person():

    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        print("person created")

    def who_am_i(self):
        print("ı am a person")

    def eat(self):
        print("ı am eating")

class Student(Person):
     def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.student_number=number
        print("student created")
     #override(ezme)   
     def who_am_i(self):
        print("ı am a student")

     def sayHello(self):
        print("hellooo")


class Teacher(Person):
      def __init__(self,fname,lname,branch):
         Person.__init__(self,fname,lname)
       # super().__int__(fname,lname)     
         self.branch=branch
      def who_am_i(self):
           print(f"a am a teacher{self.branch} ")

p1=Person("ayşe","bilgin")
s1=Student("selin","bilgin",1234)
t1=Teacher("ayse","bilgin","ingilizce")
print(p1.fname+' '+p1.lname)
print(s1.fname+' '+s1.lname+' '+str(s1.student_number))
print(t1.fname+' '+t1.lname+' '+t1.branch)
p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()
print(t1.branch)"""

"""mylist=[1,2,3]

class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("movie obj olusturuldu")
    def  __str__(self):
        return f"{self.title}by{self.director}"

    def __len__(self):
        return self.duration 

    def __del__(self):
        print("film obj silindi")      
m=Movie("film adı","yönetmen adı",120)

print(len(mylist))
print(len(m))"""
"""

class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkanswer(self,answer):
        return self.answer==answer
  

class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0
    def getQuestion(self):
          return self.questions[self.questionIndex]
    def displayQuestion(self):
        question=self.getQuestion()
        print(f'soru{self.questionIndex+1}:{question.text}')
        for q in question.choices:
            print("-"+q)

        answer=input("cevap")
        self.quess(answer)
        self.loadQuestion()
        question.checkanswer == answer
    def quess(self,answer):
        question=self.getQuestion()

        if question.checkanswer(answer):
            self.score +=1
        self.questionIndex +=1


    def  loadQuestion(self):
        if len(self.questions) == self.questionIndex:
               self.showScore()

        else:
            self.displayQuestion()


    def showScore(self):
      print("score",self.score)         

q1=Question('en iyi prog dili?',['c','java','python','javascript'],'python')
q2=Question('en popüler prog dili?',['c','java','python','javascript'],'python')
q3=Question('en çok kazandıran prog dili?',['hiçbiri','java','python','javascript'],'python')
questions=[q1,q2,q3]
quiz=Quiz(questions)
question=quiz.getQuestion()
quiz.displayQuestion()
print(question.text)
"""

#error  handling

"""try:
  x=int(input("x:"))
  y=int(input("y:"))
  print(x/y)
except (ZeroDivisionError,ValueError) as e:
    print("sayıları kontrol ediniz ")  
    print(e)"""

"""try:
  x=int(input("x:"))
  y=int(input("y:"))
  print(x/y)
except:
    print("sayıları kontrol ediniz ")"""

"""while True:
  try:
    x=int(input("x:"))
    y=int(input("y:"))
    print(x/y)
  except Exception as ex:
     print("sayıları kontrol ediniz ",ex)  
  else:
    break
  finally:
    print("try except sonlandı")"""

"""x=10

if  x>5:
    raise Exception("x beşten büyük olamaz")"""

"""def check_password(psw):
    import re
    if len(psw)<8:
        raise Exception("parola en az 7 karakter olmalıdır ")
   
    elif not re.search("[a-z]",psw):
        raise Exception("parola küçük harf içermeli")
    elif not re.search("[A-Z]",psw):
        raise Exception("parola büyük harf içermeli")
    elif not re.search("[0-9]",psw):
        raise Exception("parola rakam harf içermeli")
    elif not re.search("[_@$]",psw):
        raise Exception("parola aplha numeric karakter içermeli")    
    elif  re.search("\s",psw):
        raise Exception("parola boşluk içermemeli")
    else:
        print("geçerli parola")
password="12345678aS@"

try:
    check_password(password)
except Exception as a:
    print(a)
else:
        print("geçerli parola:else")    
finally:
   print("validation tamamlandı")"""    


"""class Person:
    def __init__(self,name,year):
        if len(name)> 10:
            raise Exception("name alanı fazla karakter içeriyor")
        else:
            self.name=name    
p=Person("Aliiiiiiiiiii",1989)"""

from typing import Type


liste=["1","2","5a","10b","abc","10","50"]
  
#liste elemanı içinde sayısal değerleri bulma 

"""for x in liste:
    try:
      result=int(x)
      print(result)
    except ValueError:
        continue"""
#kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı olup olmadığından emin olunuz aksi halde hata msj yazın
"""while True:
  sayi=input("sayı")
  if sayi=='q':
    break

  try:
    result=float(sayi)
    print("girdiğiniz sayı",result)
  except ValueError:
     print("geçersiz sayı") 
     continue"""
#kullanıcının girdiği sayı için türkçe karakter hatası
"""def checkPassword(parola):
   turkce_karakterler='şçğüöıİ'

   for i in parola:
        if i in turkce_karakterler:
         raise TypeError('Parola türkçe karakter içermez')
        else:
          pass
   print('geçerli parola')    


parola=input("parola:")

checkPassword(parola)"""
#faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata msjları üret
"""def faktoriyel(x):
    x=int(x)
    if x<0:
        raise ValueError("Negatif değer")
    result=1
    for i in range(1,x+1):
        result*=i
    return result  
for x in[5,10,20,-3,'10a']:
    try:
        y=faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y) """

#File işlemleri
""""file=open("newfile.txt","w",encoding='utf-8')
file.write("Ayşe Selin Bilgin\n")
file.close()

file=open("newfile.txt","a",encoding='utf-8')
file.write("Ayşe Selin Bilgin\n")
file.close()
newfile2=open("newfile2.txt","x",encoding='utf-8')"""
"""try:
   file=open("newfile.txt","r")
except FileNotFoundError:
      print("dosya okuma hatası")
finally:
    file.close()
    print("dosya kapandı")"""

"""file=open("newfile.txt","r", encoding="utf-8")
#for döngüsü

# for i in file:
#     print(i,end="")
#read fonk
content1=file.read()
print("içerik 1")
print(content1)

file=open("newfile.txt","r", encoding="utf-8")
content2=file.read()
print("içerik 2")
print(content2)
file.close()

file=open("newfile.txt","r", encoding="utf-8")
content3=file.read(5)
print(content3)
content3=file.read(8)
print(content3)
file.close()

file=open("newfile.txt","r", encoding="utf-8")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")

liste=file.readlines()
print(liste[2])
file.close()"""

"""with open("newfile.txt","r",encoding="utf-8") as file:
   content=file.read()
   print(content)
   print(file.tell())
   file.seek(10)
   content2=file.read()
   print(content2)"""

"""with open("newfile.txt","r+",encoding="utf-8") as file:
    file.seek(20)
    file.write("deneme")
with open("newfile.txt","r+",encoding="utf-8") as file:
    print(file.read())  """

"""with open("newfile.txt","a",encoding="utf-8") as file:
    file.write("\nZehranur Çalış")"""     

"""with open("newfile.txt","r+",encoding="utf-8") as file:
    content=file.read()
    content="Bengi Çalış\n"+ content
    file.seek(20)
    file.write(content)"""

"""with open("newfile.txt","r+",encoding="utf-8") as file:
      pasta=file.readlines()
    
      pasta.insert(1,"Yılmaz Aygün\n")
      file.seek(0)
      #for i in pasta:
       # file.write(i)
      file.writelines(pasta) 

with open("newfile.txt","r",encoding="utf-8") as file:
     print(file.read()) """ 
"""def not_hesapla(satir):
    satir=satir[:-1]
    liste=satir.split(":")
    ogrenci_adı=liste[0]
    notlar=liste[1].split(",")

    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])

    ortalama=int((not1+not2+not3)/3)

    if ortalama>=90:
        harf="AA"
    elif ortalama>=85 and ortalama<=89:
        harf="BB"
    else:
        harf="FF" 
    return ogrenci_adı+":"+harf+"\n"       
def ortamalari_oku():
     with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
          print(not_hesapla(satir))


def not_gir():
    ad=input("öğrenci adı")
    soyad=input("öğrenci soyadı")
    not1=input("öğrenci not1")
    not2=input("öğrenci not2")
    not3=input("öğrenci not3")
   
    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
      file.write(ad+" "+soyad+":"+not1+","+not2+","+not3+"\n" )

def notlari_kayitet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
       liste=[]

       for i in file:
          liste.append(not_hesapla(i))
    with open("sonuçlar.txt","w",encoding="utf-8") as file2:
        for i in liste:
            file2.write(i)



while True:
    islem=input("1-Notları Oku\n2-Not Gir\n3-Notları Kayıt Et\n4-Çıkış\n")
    if islem=="1":
        ortamalari_oku()
    elif islem=="2":
        not_gir()
    elif islem=="3":
        notlari_kayitet()
    else:
        break 
a='canımistedi'
b=".txt"
file=open(a+b,"w",encoding="utf-8") 
file.write("Ayşe Selin Bilgin")
file.close       
 """

"""liste=[1,2,3,4,5]
a=iter(liste)
while True:
    try:
        print(next(a))
    except: 
        break """

"""def cube():
   
    for i in range(5):
        yield i**3
for i in cube():
    print(i)  
liste=[i**3 for i in range ] 
print(liste) """


"""from datetime import datetime

simdi=datetime.now()
result=datetime.now()
result=simdi.year
result=simdi.month
result=simdi.day
result=simdi.hour
result=datetime.ctime(simdi)
print(result)"""


#import re 
#result=dir(re)
#str="Python Kursu"
#result=re.findall("Python",str)
#result=len(result)
#result=re.split(" ",str)
#result=re.sub(" ","-",str)
#result=re.search("Python",str)

#result=result.span()
#result=result.start()
#result=result.group()
#result=result.string

#result=re.findall("[^a-n]", str)
#result=re.findall("...",str)
#result=re.findall("P",str)
#result=re.findall("u$",str)
#result=re.findall("sa*t",str)
#result=re.findall("y{1}",str)


"""import json

person_string='{"name":"Ayse","languages":["python","c#"]}'
#JSON string to Dic
#result=json.loads(person_string)
#result=result["name"]
#print(type(result))
# with open("person.json") as f:
#      data=json.load(f)
#      print(data)
person_dict={
    "name":"Ali",
    "languages":["Python","C#"]
}

# result=json.dumps(person_dict)
# print(type(result))
with open("person.json","w") as file:
  json.dump(person_dict,file)

person_dict=json.loads(person_string) 
result=json .dumps(person_dict,indent=4,sort_keys=True) 
print(person_dict)
print(result)"""
###JSON İLE KULLANICI GİRİŞİ ÇIKIŞI
"""import json
import os
class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email

class UserRepository:
    def __init__(self) -> None:
        self.user=[]
        self.isLoggedIn=False
        self.currentUser={}

      #load ussers from .json file
        self.loadUsers()


    def loadUsers(self):
          if os.path.exists("user.json"):
            with open("user.json","r",encoding="utf-8") as file:
                users=json.load(file)
                for user in users:
                    user=json.loads(user)
                    newUser=User(username=user["username"],password=user["password"],email=user["email"])
                    self.user.append(newUser)
                    print(self.user)
                print(user)
    def register(self,user:User):
        self.user.append(user)
        self.savetoFile()
        print("kullanıcı oluşturuldu")
    def login(self,username,pasword):
        
                
             for user in self.user:
               if user.username==username and user.password==password:
                  self.isLoggedIn=True
                  self.currentUser=user
                  print("login yapıldı")
                  break
    def logOut(self):
        self.isLoggedIn=False
        self.currentUser={} 
        print("çıkış yapıldı")
    def identity(self): 
        if self.isLoggedIn:
            print(f"username:{self.currentUser.username}")
        else:
            print("giriş yapılmadı")    

    def savetoFile(self):
        list=[]
        for user in self.user:
            list.append(json.dumps(user.__dict__))
        with open("user.json","w") as file:
            json.dump(list,file)


repository=UserRepository()

while True:
    print("Menü".center(50,"*"))
    secim=input("1-REgister\n2-Login\n3-Logout\n4-Identify\n5-Exit\nseçiminiz: ")
    if secim=="5":
        break    
    else:
        if secim=="1":
            username=input("username:")
            password=input("password:")
            email=input("email:")
            
            user=User(username=username,password=password,email=email)
            repository.register(user)
            print(repository.user)
        elif  secim=="2":
            if repository.isLoggedIn:
                print("zaten login oldunuz")
            else:
              username=input("username:")
              password=input("password:")
              repository.login(username,password)
        elif  secim=="3":
             repository.logOut()
        elif  secim=="4":
              repository.identity()
        else:
            print("yanlış seçim")"""


"""import requests
import json

result=requests.get("https://jsonplaceholder.typicode.com/todos")
result=json.loads(result.text)
for i in result:
    if i["userId"]==1:
      print(i["title"])
print(type(result))"""

#reguest
"""import requests
class Github:
    pass

while True:
    secim=input("1-Find User\n2-Get Repositories\n3-Create Repository\n4-Exit\nSEçim:")
    if secim=="4":
        break
    else:
        if secim=="1":
            pass"""

#numpy kütüphanesi
# 
import numpy as np

"""py_list=[1,2,3,4,5,6,7,8,9]
 #numpuy array

np_array=np.array([1,2,3,4,5,6,7,8,9])
print(type(py_list))
print(type(py_list))

py_multi=[[1,2,3],[4,5,6],[7,8,9,]]
np_multi=np_array.reshape(3,3)

print(py_multi)
print(np_multi)


print(np_array.ndim)
print(np_multi.ndim)
print(np_array.shape)
print(np_multi.shape)"""

#result=np.arange(10,100,3)
#result=np.zeros(10)
#result=np.ones(10)
#result=np.linspace(0,100,5)
#result=np.linspace(0,5,5)
#result=np.random.randint(100)
#result=np.random.randint(1,10,3)
#result=np.random.rand(5)
#result=np.arange(50)
#np_array=np.arange(50)
#result=np_array.reshape(5,10)

#print(result.sum(axis=0))

"""numberss=np.array([0,5,10,15,20,25,50,75])

result=numberss[::-2]

numberss2=np.array([[0,5,10],[15,20,25],[50,75,85]])
#result=numberss2[2,2]
result=numberss2[:2,:2]

arr1=np.arange(0,10)
#arr2=arr1#referans
arr2=arr1.copy()
#print(arr1)
#print(arr2)

arr2[0]=20

print(arr1)
print(arr2)"""

import numpy as np

number1=np.random.randint(1,100,6)
number2=np.random.randint(1,100,6)
#print(number1)
#number1=number1+10
# print(number1)
# print(number2)
# result=number1-number2
# result=number1*number2
# result=np.sin(number1)

mnumber1=number1.reshape(2,3)
mnumber2=number2.reshape(2,3)
#result=np.hstack((mnumber1,mnumber2))
#result=number1>50
result=number1%2==0
print(number1[result])
#print("mn1",mnumber1)
#print("mn2",mnumber2)
print(result)
