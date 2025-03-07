def toplam(a,b):
    return a+b

def cikar(a,b):
    return a-b

def carp(a,b):
    return a*b

def bol(a,b):
    return a/b

def islem(f1,f2,f3,f4,islem_adi):
    if islem_adi=="toplama":
        print(f1(2,3))
    elif islem_adi=="cikarma":
        print(f2(5,2))
    elif islem_adi=="carp":
        print(f3(4,3))
    elif islem_adi=="bol":
        print(f4(6,3))
    else:
        print("gcersiz")

islem(toplam,cikar,carp,bol,"toplama")    # biz bu şekil ifade yazımlarıyla f1,f2,f3,f4 ü ayrı fonksiyon ifadesinde göstermiş oluyoruz yani bir fonksiyonu bir diğer fonksiyona atamış oluyoruz

