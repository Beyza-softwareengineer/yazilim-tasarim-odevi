1. Factory Method (Creational)Uygulama Noktası:src/notification_manager.py içerisinde yer alan NotificationFactory sınıfı.
2.Gerekçe (Problem): Başlangıç kodunda (Faz 0), bildirim nesnelerinin yaratılması süreci ana yönetim sınıfı olan NotificationManager içerisinde katı bir if-else yapısıyla yapılıyordu.
Bu durum, sisteme yeni bir bildirim kanalı (örn: WhatsApp) eklendiğinde mevcut çalışan kodun değiştirilmesini zorunlu kılıyordu (Open/Closed Principle ihlali).
3.Sağlanan Avantaj (Çözüm): Nesne yaratma sorumluluğu "Fabrika" sınıfına devredilerek istemci kodun somut sınıflara (Email, SMS vb.) olan bağımlılığı koparılmıştır.
Artık sistem, kodun geri kalanını bozma riski olmadan yeni bildirim türleriyle genişletilebilir hale gelmiştir (Gevşek Bağlılık / Loose Coupling). 
