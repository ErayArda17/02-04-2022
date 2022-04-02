void main(List<String> args) {
  Araba araba = Araba("BMW", 1999, "V8");
  araba.bilgiver();
  araba.yashesap();
  Araba yeni = Araba.modelsiz(1999, "V8");
  yeni.bilgiver();
  Araba bmw = Araba.yilsiz("V8", "BMW");
  bmw.yashesap();
}

class Araba {
  String? model;
  int? yil;
  String? motor;
  Araba(this.model, this.yil, this.motor) {
    print("Kurucu metad tetiklendi");
  }
  Araba.motorsuz(this.model, this.yil) {}
  Araba.yilsiz(this.motor, this.model) {}
  Araba.modelsiz(this.yil, this.motor) {}
  void bilgiver() {
    print(
        "Arabanın modeli: $model, arabanın yaşı: $yil, arabanın motoru: $motor");
  }

  void yashesap() {
    if (yil != null) {
      print("${2021 - yil!}");
    } else {
      print("Yıl Bilgisi Bilinmemektedir");
    }
  }
}
