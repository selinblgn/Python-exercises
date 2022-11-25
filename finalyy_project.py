#parola, mail  sorgu
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
   print("validation tamamlandı")    

#kullanıcının girdiği sayı için türkçe karakter hatası
   def checkPassword(parola):
   turkce_karakterler='şçğüöıİ'

   for i in parola:
        if i in turkce_karakterler:
         raise TypeError('Parola türkçe karakter içermez')
        else:
          pass
   print('geçerli parola')    


parola=input("parola:")

checkPassword(parola)"""   

#regulary expression ile e mail kontrolü

import re

"""def valid_email(email):
  a=bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))
  print(a)

valid_email("a.selinbilgingmail.com")"""  



def turkce_karakter(karakterler):
  a=bool(re.search(r"(?<=\s)|^)#(\w*[A-Za-z_ğüşıöçĞÜŞİÖÇ]+\w*)", karakterler))
  print(a)

turkce_karakter("selİn çeğö") 