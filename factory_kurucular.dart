void main(List<String> args) {
  Ogrenci eray = Ogrenci.faktor(-9, "Eray");
  eray.bilgi();
}

class Ogrenci {
  int id = 0;
  String isim = "Eray";
  Ogrenci(this.id, this.isim) {}
  Ogrenci.idsiz(this.isim) {}
  void bilgi() {
    print("İsim $isim,id $id");
  }

  factory Ogrenci.faktor(int id, String isim) {
    if (id < 0) {
      return Ogrenci(5, isim);
    } else {
      return Ogrenci(id, isim);
    }
  }
}
