 Farklı bildirim mantıkları tek bir sınıfın içinde.  
 Yeni bir tip (örneğin WhatsApp) eklemek için bu kodu değiştirmek zorundayız.
 Sınıf hem e-posta hem SMS süreçlerini biliyor.
 Her if bloğu benzer bağlantı mantıklarını içeriyor.
 Kod uzadıkça bu if-else yapısı okunamaz hale gelecek.


yapay zeka ne dedi?
❌ Mevcut Koddaki Tasarım Sorunları
Sıkı Bağlılık (Tight Coupling): NotificationManager sınıfı; e-posta, SMS ve Push bildirimlerinin her birinin iç mantığını (bağlantı kurma, gönderim formatı vb.) bilmek zorunda. Bu, sınıflar arası bağımlılığı aşırı artırır. 
Açık/Kapalı Prensibi (OCP) İhlali: Yeni bir bildirim yöntemi (örneğin WhatsApp) eklemek istediğinde, mevcut send_notification metodunun içine girip yeni bir elif bloğu eklemen gerekir. Kod, gelişime açık ama değişime kapalı olmalıdır; oysa burada her yeni özellikte eski kodu değiştiriyoruz.  
Tek Sorumluluk Prensibi (SRP) İhlali: Bir sınıfın değişmek için tek bir nedeni olmalıdır. Ancak bu sınıf; e-posta sunucusu değiştiğinde de, SMS sağlayıcısı değiştiğinde de, bildirim mantığı değiştiğinde de güncellenmek zorunda kalıyor.
Kodun Katılığı (Rigidity): Bir bildirim türündeki hata (örneğin e-posta kısmındaki bir parantez hatası), tüm NotificationManager sınıfını etkileyebilir ve SMS gönderimini de bozabilir.
Düşük Okunabilirlik ve Bakım Zorluğu: Gerçek bir projede bu if-else blokları yüzlerce satıra ulaşır. Kodun içinde aradığın bir mantığı bulmak ve test etmek imkansız hale gelir.  
