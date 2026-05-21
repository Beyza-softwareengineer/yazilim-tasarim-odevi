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
