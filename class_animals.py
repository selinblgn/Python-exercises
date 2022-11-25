class Animals:
    cins="no information"
    def __init__(self,name,yas,tür):
         self.name=name
         self.yas=yas
         self.tür=tür
         
         print("hayvan eklendi")
   
class Köpek(Animals):

    def __init__(self,name,yas,tür,cins):
        Animals.__init__(self,name,yas,tür)
        self.cins=cins
    def konus(self):
        print("HAVHAV")   

class Kus(Animals):

    def __init__(self,name,yas,tür,cins):
        Animals.__init__(self,name,yas,tür)
        self.cins=cins
    def konus(self):
        print("ÇİKÇİK")   


class At(Animals):

    def __init__(self,name,yas,tür,cins):
        Animals.__init__(self,name,yas,tür)
        self.cins=cins
    def konus(self):
        print("HIHHH")                   

    
animal1=Animals(input("Hayvanın ismini giriniz"),input("Hayvanın yaşını giriniz"),input("Hayvanın türünü giriniz") )
animal2=Köpek(input("Hayvanın ismini giriniz"),input("Hayvanın yaşını giriniz"),input("Hayvanın türünü giriniz"),input("Hayvanın cinsini giriniz"))
animal3=Kus(input("Hayvanın ismini giriniz"),input("Hayvanın yaşını giriniz"),input("Hayvanın türünü giriniz"),input("Hayvanın cinsini giriniz"))
animal4=At(input("Hayvanın ismini giriniz"),input("Hayvanın yaşını giriniz"),input("Hayvanın türünü giriniz"),input("Hayvanın cinsini giriniz"))
animal2.konus()
animal3.konus()
animal4.konus()
print(f'Hayvanın ismi :{animal1.name} yaşı:{animal1.yas} türü:{animal1.tür} cinsi:{animal1.cins}')
print(f'Hayvanın ismi :{animal2.name} yaşı:{animal2.yas} türü:{animal2.tür} cinsi:{animal2.cins}')
print(f'Hayvanın ismi :{animal3.name} yaşı:{animal3.yas} türü:{animal3.tür} cinsi:{animal3.cins}')
print(f'Hayvanın ismi :{animal4.name} yaşı:{animal4.yas} türü:{animal4.tür} cinsi:{animal4.cins}')
