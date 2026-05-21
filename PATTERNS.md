1. Factory Method (Creational)Uygulama Noktası:src/notification_manager.py içerisinde yer alan NotificationFactory sınıfı.
2.Gerekçe (Problem): Başlangıç kodunda (Faz 0), bildirim nesnelerinin yaratılması süreci ana yönetim sınıfı olan NotificationManager içerisinde katı bir if-else yapısıyla yapılıyordu.
Bu durum, sisteme yeni bir bildirim kanalı (örn: WhatsApp) eklendiğinde mevcut çalışan kodun değiştirilmesini zorunlu kılıyordu (Open/Closed Principle ihlali).
3.Sağlanan Avantaj (Çözüm): Nesne yaratma sorumluluğu "Fabrika" sınıfına devredilerek istemci kodun somut sınıflara (Email, SMS vb.) olan bağımlılığı koparılmıştır.
Artık sistem, kodun geri kalanını bozma riski olmadan yeni bildirim türleriyle genişletilebilir hale gelmiştir (Gevşek Bağlılık / Loose Coupling). 





## Faz 1: Creational Design Patterns 
### 1. Factory Method

* **Nerede Kullanıldı?**
    `src/notification_manager.py` dosyası içerisinde, istemci kodun doğrudan e-posta, SMS veya Push bildirim sınıflarını ürettiği kısımda kullanıldı. Nesne üretimi, yeni oluşturulan `NotificationFactory` sınıfının `create_notification` metoduna devredildi.

* **Neden Kullanıldı?**
    Başlangıç kodunda (Faz 0), bildirim nesnelerinin yaratılması ana yönetim sınıfı içerisinde katı if-else zincirleriyle yapılıyordu. Bu durum, sisteme yeni bir bildirim kanalı (örneğin WhatsApp) eklenmek istendiğinde mevcut çalışan kodun değiştirilmesini zorunlu kılıyor ve Açık/Kapalı Prensibini (Open/Closed Principle - OCP) ihlal ediyordu. Ayrıca tek bir sınıf, tüm bildirim tiplerinin detaylarını bilerek Sıkı Bağlılık (Tight Coupling) oluşturuyordu.

* **Ne Kazandınız?**
    * **Gevşek Bağlılık (Loose Coupling):** İstemci kod, somut bildirim sınıflarına (EmailNotification, SMSNotification vb.) bağımlı olmaktan kurtuldu, sadece soyut `Notification` arayüzünü tanır hale geldi.
    * **Genişletilebilirlik (OCP Uyumu):** Gelecekte yeni bir bildirim türü eklemek istediğimizde mevcut çalışan gönderme mantığına dokunmadan, sadece fabrikaya yeni bir sınıf tanıtmamız yeterli olacaktır.
    * **Tek Sorumluluk Prensibi (SRP):** Bildirim gönderme mantığı ile o bildirimin nesnesini yaratma sorumluluğu birbirinden tamamen ayrıldı.
 


Bu faza ait UML Sınıf Diyagramına projenin `docs/diagrams/phase1_factory.md` konumundan grafiksel olarak ulaşabilirsiniz.
