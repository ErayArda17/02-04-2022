class Sporcu():
    sporcu=[]
    def __init__(self,ad,soyad,yas,boy,kilo):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.boy=boy
        self.kilo=kilo
    def sporcuekle(self):
        self.sporcu.append(self.ad)
    def bilgigöster(self):
        print("Ad:{} Soyad:{} Yas:{} Boy:{} Kilo:{}".format(self.ad,self.soyad,self.yas,self.boy,self.kilo))
    

class Futbolcu(Sporcu):
    def __init__(self,ad,soyad,yas,boy,kilo,hız):
        super().__init__(ad,soyad,yas,boy,kilo)
        self.hız=hız
        self.güç=50
    def oyna(self):
        self.güç-=1
        if self.güç<=20:
            print("Oyuncu Yoruldu Oyundan Alsanız İyi Olur")
        else:
            print("Oyuncu Koşuyor")
kaan=Futbolcu("Eray","Dahan",24,199,80,100)
eray=Futbolcu("Eray","Dahan",22,199,90,120)
eray.bilgigöster()
mami=Futbolcu("Mami","Blmm",33,150,120,110)
mami.sporcuekle()
eray.oyna()
print(eray.sporcu)

