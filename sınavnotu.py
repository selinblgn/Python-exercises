with open("ornek_metin.txt",encoding="utf-8") as f:
    with open("gecenler.txt","w",encoding="utf-8") as g:
        with open("kalanlar.txt","w",encoding="utf-8") as k:
            icerik=f.readlines()
            m=0
            for satir in icerik:
                if m==0:
                    m+=1
                    continue
                satir=satir.replace("\n","")
                bosluk_sayisi=0
                bosluk_indexleri=[]
                index=0
                for karakter in satir:
                    if karakter==" ":
                        bosluk_sayisi+=1
                        bosluk_indexleri.append(index)
                    index+=1
                ad_soyad=satir[:bosluk_indexleri[0]]
                print(ad_soyad)
                soyad=ad_soyad.split("-")[-1]
                print(soyad)
                ad=ad_soyad[:ad_soyad.index(soyad)-1].replace('-',' ')
                print(ad)
                notlar=satir.split()[-1].split("/")
                print(notlar)
                birinci_vize=int(notlar[0])
                ikinci_vize=int(notlar[1])
                final=int(notlar[2])
                ortalama=birinci_vize * 0.3 + ikinci_vize * 0.3 +final * 0.4
                print(ortalama)
                bolum=satir[bosluk_indexleri[0]+1 :bosluk_indexleri[len(bosluk_indexleri)-1]]
                if ortalama>=70 and final>=70:
                    g.write(ad)
                    g.write(" "*(25-len(ad)))
                    g.write(soyad)
                    g.write(" "*(25-len(soyad)))
                    g.write(bolum)
                    g.write(" "*(25-len(bolum)))
                    g.write(str(round(ortalama,1)))
                    g.write(" "*21)
                    g.write("Geçti\n")
                else:
                    k.write(ad)
                    k.write(" "*(25-len(ad)))
                    k.write(soyad)
                    k.write(" "*(25-len(soyad)))
                    k.write(bolum)
                    k.write(" "*(25-len(bolum)))
                    k.write(str(round(ortalama,1)))
                    k.write(" "*21)
                    k.write("Geçti\n")

"""with open("ornek_metin.txt") as ornek:
    with open("kalanlar.txt", "w") as kalan:
        with open("gecenler.txt", "w") as gecen: 
            ornekicerik = ornek.readlines()
            for satir in ornekicerik:
                soyad = satir.split()[0].split("-")[-1]
                ad = satir.split()[0].split("-")
                del ad[-1]
                ad = str(ad)
                ad = ad.strip("[]").replace("'","").replace(",", "")
                bolum = satir.split()[1:-1]
                bolum = str(bolum)
                bolum = bolum.strip("[]").replace("'", "").replace(",", "")
                notlar = satir.split()[-1].split("/")
                birinci =int(notlar[0])
                #print(birinciVize)
                ikinciVize =int(float(notlar[1]))
                #print(ikinciVize)
                final =int(float(notlar[-1]))
                #print(final)
                ortalama =int(float(int(birinciVize) * 0.3 +int(ikinciVize) * 0.3 + int(final) * 0.4))
                if final < 70 or ortalama < 70:
                    kalan.write("{:<30}{:<30}{:<30}{:.1f}{:>30}\n".format(ad,soyad,bolum,ortalama,"KALDI"))
                else:
                    gecen.write("{:<30}{:<30}{:<30}{:.1f}{:>30}\n".format(ad,soyad,bolum,ortalama,"GEÇTİ"))
print("Kalanlar, kalanlar.txt dosyasına, Geçenler, gecenler.txt dosyasına yazdırıldı...")"""