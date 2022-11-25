#AYŞE SELİN BİLGİN
with open("oyuncular.txt","r+",encoding="utf-8") as file:
  with open("besiktas.txt","w",encoding="utf-8") as bjkfile:
     with open("galatasaray.txt","w",encoding="utf-8") as gsfile:
        with open("fenerbahce.txt","w",encoding="utf-8")as fbfile:
           with open("trabzonspor.txt","w",encoding="utf-8")as tsfile:    
               icerik=file.readlines()
         
               for satir in icerik:
                 satir=satir.replace("\n","")
                 isimler=satir.split(",")
                 print(isimler)
            
                 if isimler[-1]=="Galatasaray":
                   gsfile.write(str(isimler))
                   gsfile.write("\n")
                 elif isimler[-1]=="Beşiktaş":
                   bjkfile.write(str(isimler))
                   bjkfile.write("\n")
                 elif isimler[-1]=="Fenerbahçe":
                   fbfile.write(str(isimler))     
                   fbfile.write("\n")
                 else:
                   tsfile.write(str(isimler))     
                   tsfile.write("\n") 
         

  




    