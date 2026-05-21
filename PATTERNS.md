# Tasarım Örüntüleri Raporu (Faz 2)
## 🏗️ Faz 2: Structural Örüntüler

### 1. Adapter Pattern 
* **Nerede? :** Projeye dışarıdan eklediğimiz harici SMS ve e-posta servislerinin entegrasyonunda kullandım (`src/` altındaki kodlarda).
* **Neden? :** Sisteme bağlamak istediğim üçüncü parti kütüphanelerin metot isimleri (örneğin `dispatch_text`), bizim projenin başından beri kullandığı standart `send()` metoduyla uyuşmuyordu. Sırf dışarıdan yeni bir servis geldi diye mevcut çalışan kodlarımı tek tek değiştirip bozmak istemediğim için araya bir dönüştürücü koymak mantıklı geldi ve bu örüntüyü seçtim.
* **Ne Kazandınız? :** Sistemin ana kodlarına ve işleyişine hiç dokunmadan, tamamen yabancı ve uyumsuz kütüphaneleri sanki bizim kendi kodumuzmuş gibi tıkır tıkır çalıştırabilme esnekliği kazandım. İleride başka bir SMS firmasına geçsek bile ana kodlar hiç etkilenmeyecek.

### 2. Decorator Pattern 
* **Nerede? (Where):** Gönderilen bildirimlere ekstra şifreleme ve loglama özellikleri eklerken kullandım.
* **Neden? (Why):** Gönderilen mesajları veri tabanına kaydetmek (logging) veya güvenlik için mesaj içeriğini şifrelemek (encryption) gerekiyordu. Bunları doğrudan ana bildirim sınıflarının (`EmailNotification` vb.) içine yazsaydım kodlar çorba olacaktı. Üstelik her özellik kombinasyonu için (örn: hem şifreli hem loglu, sadece şifreli vb.) ayrı ayrı alt sınıflar türetmeye kalksam sınıf patlaması (class explosion) yaşayacaktım. Kodları şişirmeden bu ek özellikleri dinamik olarak giydirmek için bu örüntüyü seçtim.
* **Ne Kazandınız? :** Mevcut bildirim sınıflarının özüne ve koduna dokunmadan, çalışma zamanında (runtime) bir bildirme istediğim an şifreleme, istediğim an loglama özelliğini bir kılıf gibi giydirip çıkarabilme esnekliği kazandım. Kodlar çok daha temiz ve modüler oldu.

  ---

##  Faz 3: Behavioral Örüntüler 

### 1. Observer Pattern (Gözlemci Örüntüsü)
* **Nerede?:** Kullanıcıların toplu bildirim listelerine veya kampanya duyurularına abone olduğu sistem yapısında kullandım (`BildirimMerkezi` ve `KullaniciGozlemci` sınıfları).
* **Neden?:** Bir sistemde durum değiştiğinde (örneğin sisteme yeni bir duyuru girildiğinde), bu duyuruyu bekleyen birden fazla kullanıcı nesnesini tek tek manuel haberdar etmek yerine, tek bir tetiklemeyle hepsine otomatik gitmesini istedim.
* **Ne Kazandınız?:** Bildirim merkezi ile kullanıcıları birbirinden tamamen bağımsız hale getirdim (Loose Coupling). Sisteme yeni kullanıcılar eklense bile merkez kodum bundan hiç etkilenmiyor.

### 2. Strategy Pattern
* **Nerede?:** Bildirimlerin gönderim önceliği ve maliyet senaryolarına göre değişen gönderim algoritmalarında kullandım (`GonderimStratejisi` ve alt sınıfları).
* **Neden?:** Bazı bildirimlerin acil (anlık), bazılarının ise ekonomik (toplu ve yavaş) gitmesi gerekiyordu. Bunları karmaşık `if-else` yapılarıyla çözmeye çalışmak yerine her bir gönderim modunu bağımsız birer sınıf olarak tasarladım.
* **Ne Kazandınız? :** Tam olarak Açık/Kapalı Prensibini (OCP) sağladım. İleride sisteme "Yapay Zeka Destekli Akıllı Gönderim Stratejisi" gibi yeni bir mod eklemek istersem, mevcut hiçbir kodu değiştirmeden sadece yeni bir strateji sınıfı eklemem yeterli olacak.
