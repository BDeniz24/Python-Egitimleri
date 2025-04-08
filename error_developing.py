# x=10

# if x>5:
#     raise Exception("x 5 ten büyük değer alamaz")   # bir hata komut ifadesi oluşturmak için kullaılır "raise"


def checkpassword(psw):
    import re # regular expression modülü oluşturulup kullanılmak istenen fonksiyonun içiine atanmalı   
    if len(psw) <8 :
        raise Exception("parola en a 7 karakter olmalı")
    elif not re.search("[a-z]",psw):  # regular expression modülüyle biz parola üzerindeki harf modülnü kontrol edebiliriz.bunu i.in yyandaki gibi modülü girer ve sırasıyla 1) harf-karakter aralığını, 2) denetlenecek metin. gireriz

        raise Exception("parola küçük harf içermeli")
    elif not re.search("[A-Z]",psw):  # regular expression modülüyle biz parola üzerindeki harf modülnü kontrol edebiliriz.bunu i.in yyandaki gibi modülü girer ve sırasıyla 1) harf-karakter aralığını, 2) denetlenecek metin. gireriz

        raise Exception("parola büyük harf içermeli") # elif not bir ifade yoksa/doğru değilse oluşur

    elif not re.search("[4-7][0-9]",psw):  # regular expression modülüyle biz parola üzerindeki rakam aralığı modülnü kontrol edebiliriz.bunu i.in yyandaki gibi modülü girer ve sırasıyla 1) harf-karakter aralığını, 2) denetlenecek metin. gireriz
                                        # reg exp için br sayı aralığı girmek için ifadeler böyle yazılmalı. Bunun sebebi;her bir basamağın alt değeri ve üst değeri yan yana yazılması
        raise Exception("parola rakam içermeli")
    elif not re.search("[_/@½]",psw):  # regular expression modülüyle biz parola üzerindeki alpha numeric modülnü kontrol edebiliriz.bunu i.in yyandaki gibi modülü girer ve sırasıyla 1) harf-karakter aralığını, 2) denetlenecek metin. gireriz
                                        # alpha numeric ifadeler ya da herhangi bir ifadeni aralığını arar. yani istediğin ifadelerin kullanılmasına izin verebiliriz
        raise Exception("parola alpha numeric içermeli") 
    elif re.search("\s",psw) :                           
        raise Exception("parola boşluk içermemeli" )  # "\s" ifadesi boşluk karakteri kontrol eder
    else:
        print("geçerli parola")
# hata kontrolünde bir hata ifadesi mutlaka "try-except-else" içerisinde olur

sifre="AbCy49//////////"

try:
    checkpassword(sifre)  # try da ifade denenir
except Exception as ex:
    print(ex) # except kısmında eğer bir hata varsa hatanın sonucu çıkar
else:  #else ise hata yoksa bildirm verir
    print("parola uyumlu ")
finally: # bu mesaj mutlaka çıkar (finally)
    print("sifre analiz tamamlandı")


# hata mesajnıı bir class içinde de verebiliriz
class kisi:
    def __init__(self,ad,yil):
        if len(ad) > 10:
            raise Exception("10 karakteri aşma")
        else:
            self.ad=ad
            print(ad)


b=kisi("deniz",2004)