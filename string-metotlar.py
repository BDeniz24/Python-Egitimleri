mesaj=" Merhabalar ismim . Instagramda 5 takipcim var"

mesaj= mesaj.upper() # bütün karakterleri büyük harf yapar
print(mesaj)

mesaj=mesaj.lower()
print(mesaj)

mesaj=mesaj.title() # cümlede her kelimeni başı büyük harf olur
print(mesaj)

mesaj=mesaj.capitalize() # sadece cümlenin ilk kelimesinin ilk harfi büyük oldu
print(mesaj)

mesaj=mesaj.strip() # metin ifadesindeki baş ve sonda olan boşlukları siler. "lstrip" sol boşluğu siler. "rstrip" sağ boşluğu siler bulunan boşluk karakterleri silinir
print(mesaj)



mesaj= mesaj.split() #bir metin ifadesindeki bütün kelime gruplarını boşlukları bulup ayırır. Kelime grubu bir liste gibi olur
print(mesaj) #bu şekilde de ikinci[2] ifadeyi yazdırırız.******* EĞER SPLİT İÇİNE BİR İŞARET GİRERSEK AYIRMA REFERANSINI O KARAKTER OLARAK ALIR



#split ile ayrılan kelimeyi nasıl birleştiririz.
mesaj= " ".join(mesaj)# ilk eklediğimiz tırnak bize birleştirirken araya ne koyayım diyor
print(mesaj)


# bir cümle içinde aradığımız kelimeyi nasıl bulabiliriz
index= mesaj.find("14 m") # rfind,lfind da var
print(index)
# find yerine kullanabileceğimiz " .index" metodu var.

isFound= mesaj.startswith("m") #işlenilen cümlenin ilk karakteri bu mu diye sorar. DİKKAT biz bu dosyada daha önceden program çalıştırdığımız için sistem bize programda en son ne çalıştırdıysak son çalıştırma halindeki şekli verir. 
print(isFound)   # .endwith zaten adından anlaşılyor :)


mesaj=mesaj.replace("i̇brahim","Baris") # cümle içindeki karakterleri değiştirir
print(mesaj)
# ".isalpha" metodu ise ilgili karakter bloğu alfabetik mi ona bakar. ".isdigit" ise bu bir sayısal ifade mi diye sordurur.


mesaj=mesaj.center(150,"/") # bu fonksiyon bize parantez içinde girdiğimiz değer kadar karakter oluşturur. ve bu karakter içinde "mesaj" metnini ortalar. ikinci yer ise boşluğa neyin konulacağını belirtir
print(mesaj)# buna benzer olarak "ljust"(kelimeyi sola yaslar ve boşlukları istenilen ifadeye göre doldurur). rjust ise aynı işlemi sağa yaslayıp yapar     
mesaj = print("ali veli mehmet".center(100,"*"))



#### Birçok metod ekinde örneğin aradğımız karakteri bulurken vs. Bu karakterleri metod parantezi içinde belli bir karakter alanında sınırlayabiliriz
# ya da metodları sağdan ya da soldan başlayıp arayacak şekilde ayarlayabiliriz