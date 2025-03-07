for x in range(10):
    print(x)


numbers=[x**2 for x in range(10) if x%3==0] # bu şekilde yazımla bir diziyi range ile yazıp x ile gösterp x i dizi içerisine yazarabiliriz.
print(numbers)  # dizi içinde yazar    #bu şekilde işlemleri ekleyebiliriz


sayi=[]
for x in range(10):
    sayi.append(x)
print(sayi)



cumle="merhaba"
liste=[]
for letter in cumle:
    liste.append(letter)
print(liste)


liste=[letter for letter in cumle]
print(liste)



yillar=[1992,1989,2004,1970]
yaslar=[2024-yil for yil in yillar ]
print(yaslar)


cevaplar=[x if x%2==0 else "tek" for x in range(10)]
print(cevaplar)



cev1=[]
for x in range(3):
    for y in range(3):   #x döngüsünde x in ilk kısmı için döndürürken x=0 da y için 0,1,2,3 yapacak sonra x=1 e geçecek
        cev1.append((x,y))
print(cev1)

sayi2= [(x,y) for x in range(5) for y in range(4)]
print(sayi2)
