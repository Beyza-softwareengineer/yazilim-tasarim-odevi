# 🤖 AI Log — Faz 1: Creational Pattern (Factory Method)

## Kullandığım Prompt

> "Elimde bir bildirim sistemi var. NotificationManager sınıfı içinde
> if-else bloklarıyla EmailNotification ve SMSNotification nesneleri
> üretiliyor. Bu nesne yaratma sorununu çözmek için hangi Creational
> tasarım örüntüsünü önerirsin ve neden?"

---

## AI'ın Yanıtı (Özet)

AI, Factory Method örüntüsünü önerdi. Gerekçesi şuydu:
- İstemci kodun somut sınıflara (EmailNotification, SMSNotification)
  doğrudan bağımlı olmaması gerekir.
- Nesne üretim sorumluluğu ayrı bir fabrika sınıfına devredilmeli.
- Böylece yeni bir bildirim tipi eklendiğinde sadece fabrikaya yeni
  bir sınıf tanıtmak yeterli olur, mevcut kod değişmez (OCP).

AI ayrıca Abstract Factory'yi de alternatif olarak sundu; birden fazla
ürün ailesi olduğunda (örn. hem masaüstü hem mobil bildirimler) daha
uygun olduğunu belirtti.

---

## Ben Ne Uyguladım?

Factory Method'u uyguladım. `NotificationFactory` adında ayrı bir
sınıf oluşturdum. İstemci kod artık sadece bu fabrikaya tip ismini
veriyor, somut sınıfları hiç tanımıyor.

---

## AI'dan Farklı Yaptığım / Aynı Kaldığım Noktalar

- **Aynı:** Factory Method seçimi konusunda AI ile hemfikirim,
  gerekçeler örtüşüyor.
- **Farklı:** AI Abstract Factory'yi de önerdi ama sistemde şu an
  tek bir bildirim ailesi olduğu için bunu aşırı mühendislik (over-
  engineering) olarak değerlendirip reddettim. Tek aile varken
  Abstract Factory gereksiz karmaşıklık ekler.
- Kod iskeletini AI'dan almak yerine mantığı anladıktan sonra
  kendim yazdım. AI'ın önerdiği yapıyı referans aldım ama
  sınıf isimlerini ve metot imzalarını projemin terminolojisine
  göre uyarladım.
