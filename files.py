#Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
#Kullanım= open(dosy_adi,dosya_erisme_modu)
#dosya_erişme_modu=> dosyayı hangi amaçla açtığımızı belirtir

# "w": (write) dosyadaki verinin üzerine yazma modu. dosya konumda oluşşturur
# "a":(append) dosyaya veri ekleme. dosya konumda yoksa oluşturur
# "x":(create) oluşturma. Dosya zaten varsa hata verir
# "r":(read) okuma. varsayılan. dosya konumda yoksa hata verir


# "w
#result= open("yenidosya.txt","w") #buu dosya yok. bu konumda dosya oluşturalım. bu dosya files.py içinde oluşturulur
#print(result) #encoding=windows işletim sistemindeki karakter kodlama tipidir. biz  bunu utf ile değiştireceğiz


#
#file.close() # uygulama sonlanınca dosyayı kapatırız. sistemi yormaması için

#file=open("C:/users/aaa/desktop/yenidosya.txt","w") # bu şekil yazımında c klasöründe bri dosya oluşturmuş ollur. aynı zamanda file.py nin bulunduğu dizin içersinde de bu dosya oluşmuş olur. Adres gösterimiyle yazdığımız bir dosya masaüstünde de gözükür"C:/users/aaa/desktop/dosya_adi.uzantisi" şeklşinde yazmalıyızb


# file= open("yenidosya.txt","w",encoding="utf-8")  # "w" modunda dosya açınca ve dosyaya bir bilgi eklemek istediğimizde dosyadaki eski bilgileri siler. örneğin beran deniz akar yazılı kısmı değiştirirsek beran deniz akar yazan kısım yerine başka şey yazmış oluruz."w" tipinde oldğumuz için bu şekide silme yapmı olur
# file.write("beran deniz akar  ")  # mesela şu anda bizim dosyamızın karakter dizini(encoding=1254) miş biz bunu çevirip, türkçe karakterleri tanımlamak için
# file.write("pırt") # .write() dosyaya bir şey eklemeizi sağlar
# file.close() # iş bitti. dosyayı kapatalım


# file= open("yenidosya.txt","w",encoding="utf-8")
# file.close()  # bütün ifadeleri sildik





#2 "a" modu

# file= open("yenidosya.txt","a",encoding="utf-8")
# file.write("\n erzincanspor") # "a" mod dosya kısmını tekrar tekrar çalıştırınca aynı veriyi tekrar tekrar yazar. biz erzincnansporluyum ifadesini değiştirp aynı .write() içerisinde yazılsa dahi eskii bilgiyi silmez ve yeni bilgiyi sonuna eklemeye devam eder
# file.close()  # bu dosya modunda eski bilgileri silmez UNUTMA****




# # 3 :"x" tip dosyalar: içerisine veri eklenmesine izin vermez.
# file= open("yenidosya2.txt","x",encoding="utf-8") # aynı dosyayı tekrardan çalıştırırsak dosyanın var olduğu hatasını verir.


# print(file)

file=open("C:/users/aaa/desktop/denemedosya1.txt","w")