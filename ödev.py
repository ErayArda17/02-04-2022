class Çalışan():
    def __init__(self,ad,soyad,tc,maaş):
        self.ad=ad
        self.soyad=soyad
        self.tc=tc
        self.maaş=maaş
    def zam(self,yenizamn):
        if self.maaş/2<=yenizamn:
            print("Emin misin bu zam miktarı çok")
            x=input("Eminsen E'ye Değilsen H'ye Tıkla:")
            if x=="E": 
                self.maaş+=yenizamn
                print(self.maaş)
            else:
                print("İşleminiz Sonlanmıştır")
        else:
            self.maaş+=yenizamn
            print(self.maaş)
    def bilgileri_göster(self):
        print("Ad: {}\nSoyad: {}\nTc: {}\nMaaş: {}".format(self.ad,self.soyad,self.tc,self.maaş))

class Al_At():
    çalışanlar=[]

    def __init__(self,ad,soyad,tc,maaş):
        self.ad=ad
        self.soyad=soyad
        self.tc=tc
        self.maaş=maaş
    def alimyap(self,ad):
        print("Alınan Kişinin Adı:{} Soyadı:{} Tcsi:{} Maaşı:{}".format(self.ad,self.soyad,self.tc,self.maaş))
        self.çalışanlar.append(ad)
    
    def at(self,ad):
        print("Atılan Kişinin Adı:{} Soyadı:{} Tcsi:{} Maaşı:{}".format(self.ad,self.soyad,self.tc,self.maaş))
        self.çalışanlar.remove(ad)
çalışan=Çalışan("Eray","Dahan",121498014,120000)
çalışan.zam(200000)
eray=Al_At("Arda","Dahan",1241545345,20000)
eray.alimyap("Arda")