# FAZ 3: BEHAVIORAL  ÖRÜNTÜLER

class KullaniciGozlemci:
    def __init__(self, isim: str):
        self.isim = isim

    def guncelleme_al(self, mesaj: str):
        print(f" [Kullanıcı Bildirimi] {self.isim} kişisine mesaj ulaştı: {mesaj}")

class BildirimMerkezi:
    def __init__(self):
        self._aboneler = []

    def abone_ekle(self, abone: KullaniciGozlemci):
        if abone not in self._aboneler:
            self._aboneler.append(abone)

    def abone_cikar(self, abone: KullaniciGozlemci):
        self._aboneler.remove(abone)

    def herkese_duyur(self, mesaj: str):
        for abone in self._aboneler:
            abone.guncelleme_al(mesaj)


class GonderimStratejisi:
    def gonder(self, mesaj: str):
        pass

class AcilGonderimStratejisi(GonderimStratejisi):
    def gonder(self, mesaj: str):
        print(f" [ACİL STRATEJİ] En yüksek öncelikli hat kullanılarak hemen gönderildi: {mesaj}")

class EkonomikGonderimStratejisi(GonderimStratejisi):
    def gonder(self, mesaj: str):
        print(f" [EKONOMİK STRATEJİ] Sunucu yoğunluğu beklenerek toplu şekilde gönderildi: {mesaj}")

class BildirimGondericiContext:
    def __init__(self, strateji: GonderimStratejisi):
        self._strateji = strateji

    def strateji_degistir(self, yeni_strateji: GonderimStratejisi):
        self._strateji = yeni_strateji

    def islemi_tetikle(self, mesaj: str):
        self._strateji.gonder(mesaj)
