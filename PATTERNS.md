# 🗺️ Tasarım Örüntüleri Genel Gelişim Raporu

Hocam selamlar, projenin başından (Faz 0'dan) son aşamasına kadar sisteme dahil ettiğim tüm tasarım örüntülerini, bunları tam olarak projenin neresinde, hangi mantıkla uyguladığımı ve bana ne kazandırdıklarını kronolojik olarak aşağıda özetledim.

---

##  Faz 1: Creational Design Patterns (Yaratımsal Örüntüler)

### 1. Factory Method (Fabrika Örüntüsü)
* **Nerede Kullanıldı?:** `src/` altındaki kodlarımızda, istemci kodun doğrudan e-posta veya SMS sınıflarını ürettiği kısımda kullandım. Nesne üretme işini tamamen araya yazdığım `NotificationFactory` sınıfına devrettim.
* **Neden Kullanıldı?:** Projenin en başındaki halinde (Faz 0), bildirim nesnelerinin yaratılması ana yönetim sınıfı içerisinde katı `if-else` zincirleriyle yapılıyordu. Bu durum, sisteme yarın bir gün WhatsApp gibi yeni bir kanal eklemek istediğimizde mevcut çalışan kodun değiştirilmesini zorunlu kılıyor ve Açık/Kapalı Prensibini (OCP) baltalıyordu. Ayrıca tek bir sınıf, tüm bildirim tiplerinin detaylarını bilerek Sıkı Bağlılık (Tight Coupling) oluşturuyordu.
* **Ne Kazandınız?:** * **Gevşek Bağlılık (Loose Coupling):** İstemci kod, somut bildirim sınıflarına bağımlı olmaktan kurtuldu, sadece soyut arayüzü tanır hale geldi.
    * **Genişletilebilirlik (OCP Uyumu):** Gelecekte yeni bir bildirim türü eklemek istediğimizde mevcut çalışan gönderme mantığına dokunmadan, sadece fabrikaya yeni bir sınıf tanıtmamız yeterli hale geldi.
    * **Tek Sorumluluk Prensibi (SRP):** Bildirim gönderme mantığı ile o bildirimin nesnesini yaratma sorumluluğu birbirinden tamamen ayrıldı.

*Bu faza ait UML Sınıf Diyagramına projenin `docs/diagrams/phase1_factory.md` konumundan grafiksel olarak ulaşabilirsiniz.*

---

##  Faz 2: Structural Design Patterns (Yapısal Örüntüler)

### 1. Adapter Pattern (Adaptör Örüntüsü)
* **Nerede Kullanıldı?:** Projeye dışarıdan entegre ettiğimiz harici SMS ve e-posta servislerinin bağlandığı kısımlarda kullandım.
* **Neden Kullanıldı?:** Sisteme bağlamak istediğim üçüncü parti kütüphanelerin metot isimleri (örneğin `dispatch_text`), bizim projenin başından beri kullandığı standart `send()` metoduyla uyuşmuyordu. Sırf dışarıdan yeni bir servis geldi diye mevcut çalışan kodlarımı tek tek değiştirip bozmak istemediğim için araya bir dönüştürücü koymak mantıklı geldi ve bu örüntüyü seçtim.
* **Ne Kazandınız?:** Sistemin ana kodlarına ve işleyişine hiç dokunmadan, tamamen yabancı ve uyumsuz kütüphaneleri sanki bizim kendi kodumuzmuş gibi tıkır tıkır çalıştırabilme esnekliği kazandım. İleride başka bir SMS firmasına geçsek bile ana kodlar hiç etkilenmeyecek.

### 2. Decorator Pattern (Süsleyici Örüntüsü)
* **Nerede Kullanıldı?:** Gönderilen bildirimlere ekstra şifreleme ve loglama özellikleri eklerken kullandım.
* **Neden Kullanıldı?:** Gönderilen mesajları veri tabanına kaydetmek (logging) veya güvenlik için mesaj içeriğini şifrelemek (encryption) gerekiyordu. Bunları doğrudan ana bildirim sınıflarının içine yazsaydım kodlar çorba olacaktı. Üstelik her özellik kombinasyonu için (örn: hem şifreli hem loglu, sadece şifreli vb.) ayrı ayrı alt sınıflar türetmeye kalksam sınıf patlaması (class explosion) yaşayacaktım. Kodları şişirmeden bu ek özellikleri dinamik olarak giydirmek için bu örüntüyü seçtim.
* **Ne Kazandınız?:** Mevcut bildirim sınıflarının özüne ve koduna dokunmadan, çalışma zamanında (runtime) bir bildirme istediğim an şifreleme, istediğim an loglama özelliğini bir kılıf gibi giydirip çıkarabilme esnekliği kazandım. Kodlar çok daha temiz ve modüler oldu.

*Bu faza ait UML Sınıf Diyagramına projenin `docs/diagrams/phase2_structural.md` konumundan grafiksel olarak ulaşabilirsiniz.*

---

##  Faz 3: Behavioral Design Patterns (Davranışsal Örüntüler)

### 1. Observer Pattern (Gözlemci Örüntüsü)
* **Nerede Kullanıldı?:** Kullanıcıların toplu bildirim listelerine veya kampanya duyurularına abone olduğu sistem yapısında kullandım (`BildirimMerkezi` ve `KullaniciGozlemci` sınıfları).
* **Neden Kullanıldı?:** Bir sistemde durum değiştiğinde (örneğin sisteme yeni bir duyuru girildiğinde), bu duyuruyu bekleyen birden fazla kullanıcı nesnesini tek tek manuel haberdar etmek yerine, tek bir tetiklemeyle hepsine otomatik gitmesini istedim.
* **Ne Kazandınız?:** Bildirim merkezi ile kullanıcıları birbirinden tamamen bağımsız hale getirdim (Loose Coupling). Sisteme yeni kullanıcılar eklense bile merkez kodum bundan hiç etkilenmiyor.

### 2. Strategy Pattern (Strateji Örüntüsü)
* **Nerede Kullanıldı?:** Bildirimlerin gönderim önceliği ve maliyet senaryolarına göre değişen gönderim algoritmalarında kullandım (`GonderimStratejisi` ve alt sınıfları).
* **Neden Kullanıldı?:** Bazı bildirimlerin acil (anlık), bazılarının ise ekonomik (toplu ve yavaş) gitmesi gerekiyordu. Bunları karmaşık `if-else` yapılarıyla çözmeye çalışmak yerine her bir gönderim modunu bağımsız birer sınıf olarak tasarladım.
* **Ne Kazandınız?:** Tam olarak Açık/Kapalı Prensibini (OCP) sağladım. İleride sisteme "Yapay Zeka Destekli Akıllı Gönderim Stratejisi" gibi yeni bir mod eklemek istersem, mevcut hiçbir kodu değiştirmeden sadece yeni bir strateji sınıfı eklemem yeterli olacak.

*Bu faza ait UML Sınıf Diyagramına projenin `docs/diagrams/phase3_behavioral.md` konumundan grafiksel olarak ulaşabilirsiniz.*