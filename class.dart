import 'dart:math';

class Veritabani {
  String _isim = "Eray";
  String _sifre = "12346";
  bool baglan() {
    if (_intkontrol()) {
      if (_isim == "Eray" && _sifre == "12346") {
        print("Giriş Yapıldı");
        return true;
      } else {
        return false;
      }
    } else {
      print("İnternet Bağlantınız Kontrol Edin");
      return false;
    }
  }

  bool _intkontrol() {
    if (Random().nextBool()) {
      return true;
    } else {
      return false;
    }
  }
}
