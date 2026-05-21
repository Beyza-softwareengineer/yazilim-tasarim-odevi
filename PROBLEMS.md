
# 🔍 PROBLEMS.md — Başlangıç Kodunun Analizi (Faz 0)
## Benim Tespit Ettiğim Sorunlar
### Sorun 1: Tek Sınıfta Çok Fazla Sorumluluk (God Class)
`NotificationManager` sınıfı hem e-posta hem SMS hem de push bildirimlerinin tüm gönderim mantığını içeriyor. Bir sınıfın tek bir değişme sebebi olmalıdır; bu sınıfın birden fazla sebebi var.
### Sorun 2: if-else Zincirleri ile Tip Kontrolü
Bildirim tipi eklendiğinde mevcut `send_notification` metodunun içine girerek yeni bir `elif` bloğu eklemek gerekiyor. Bu, mevcut çalışan kodu her seferinde bozma riski taşıyor.
### Sorun 3: Sıkı Bağlılık (Tight Coupling)
Yönetici sınıf, her bildirim tipinin (e-posta sunucusu, SMS sağlayıcısı vb.) teknik detaylarını biliyor. Bir sağlayıcı değiştiğinde bu büyük sınıfın içine girmek gerekiyor.
### Sorun 4: Yeni Tip Eklemenin Zorluğu
WhatsApp gibi yeni bir kanal eklemek için mevcut kodu değiştirmek zorundayız. Kod, gelişime açık ama değişime kapalı olmalıdır (OCP ihlali).
### Sorun 5: Okunabilirlik ve Bakım Zorluğu
Gerçek projede bu if-else blokları yüzlerce satıra ulaşır. Belirli bir mantığı bulmak ve test etmek giderek imkânsız hale gelir. Her bildirim tipinin kendi sınıfı olmalıdır.

---

## 🤖 AI'ın Tespit Ettikleri

AI'a şu prompt'u sordum:
> "Bu kodda hangi tasarım sorunlarını görüyorsun? Hangi tasarım örüntüleri bu sorunları çözebilir? Her sorun için kısa bir açıklama yaz."

AI şunları tespit etti:
- **Sıkı Bağlılık (Tight Coupling):** `NotificationManager` sınıfı her bildirim tipinin iç mantığını biliyor.
- **OCP İhlali:** Yeni bildirim yöntemi eklemek için mevcut metoda `elif` eklemek gerekiyor.
- **SRP İhlali:** Sınıf; e-posta sunucusu, SMS sağlayıcısı veya bildirim mantığı değiştiğinde güncellenmek zorunda.
- **Kodun Katılığı (Rigidity):** E-posta kısmındaki bir hata tüm sınıfı ve SMS'i de bozabilir.
- **Düşük Okunabilirlik:** if-else blokları büyüdükçe test etmek ve bakım yapmak imkânsızlaşır.

---

## 🔄 Karşılaştırma: Ben vs. AI

| Sorun | Ben Gördüm mü? | AI Gördü mü? |
| if-else zincirleri / OCP ihlali | ✅ Evet | ✅ Evet |
| Sıkı Bağlılık | ✅ Evet | ✅ Evet |
| SRP ihlali (tek sınıf çok sorumluluk) | ✅ Evet | ✅ Evet |
| Kodun Katılığı (hata yayılımı riski) | ❌ Ben özellikle fark etmedim | ✅ AI fark etti |
| Okunabilirlik ve bakım zorluğu | ✅ Evet | ✅ Evet |

**Fark:** AI, bir bildirim tipindeki hatanın diğerlerine yayılma riskini (Rigidity) benden daha net ifade etti. Ben daha çok yeni tip eklemenin zorluğuna odaklanmıştım.AI böyle deyince, kodların birbirine girmemesi için nesne yaratma sorumluluğunu ayrı bir sınıfa almanın ne kadar mantıklı olduğunu bir kez daha anladım. .
