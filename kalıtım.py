class Çalışan():
    def __init__(self,isim,maaş,departman):
        self.isim=isim
        self.maaş=maaş
        self.departman=departman
    def bilgileri_göster(self):
        print("Çalışan Sınıfının Bilgileri")
        print("İsim: {}\nMaaş: {}\nDepartman: {}".format(self.isim,self.maaş,self.departman))
    def departman_deiştir(self,yenidepartman):
        self.departman=yenidepartman

class Yönetici(Çalışan):
    def __init__(self,isim,maaş,departman,kişi):
        super().__init__(isim,maaş,departman)
        self.kişi=kişi
    def zam(self,yenizamn):
        self.maaş+=yenizamn
yönetici=Yönetici("Eray",200000,"Bilişim",2000)
yönetici.bilgileri_göster()