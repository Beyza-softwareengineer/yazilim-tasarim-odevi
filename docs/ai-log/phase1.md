# 🤖 AI Log — Faz 1: Creational Pattern (Factory Method)

## Kullandığım Prompt

> "Elimde bir bildirim sistemi var. NotificationManager içinde
> if-else bloklarıyla e-posta ve SMS nesneleri üretiliyor.
> Bu nesne yaratma sorununu çözmek için hangi Creational
> örüntüyü önerirsin ve neden?"

## AI'ın Yanıtı

AI, Factory Method örüntüsünü önerdi. İstemci kodun somut sınıflara
bağımlı olmaması gerektiğini, nesne üretim sorumluluğunun ayrı bir
fabrika sınıfına devredilmesi gerektiğini söyledi. Yeni bir bildirim
tipi eklendiğinde sadece fabrikaya yeni sınıf tanıtmak yeterli olur,
mevcut kod değişmez dedi. Abstract Factory'yi de alternatif olarak
sundu ama birden fazla ürün ailesi olduğunda uygun olduğunu belirtti.

## Ben Ne Uyguladım?

Factory Method'u uyguladım. `NotificationFactory` adında ayrı bir
sınıf oluşturdum. İstemci kod artık sadece bu fabrikaya tip ismini
veriyor, somut sınıfları hiç tanımıyor.

## AI'dan Farklı Yaptığım Noktalar

- **Aynı:** Factory Method seçiminde AI ile hemfikirim.
- **Farklı:** AI Abstract Factory'yi de önerdi ama sistemde tek
  bir bildirim ailesi olduğu için bunu aşırı mühendislik olarak
  değerlendirip reddettim. Tek aile varken gereksiz karmaşıklık ekler.
- Kod iskeletini AI'dan almak yerine mantığı anladıktan sonra
  kendim yazdım, sınıf isimlerini projemin terminolojisine göre
  uyarladım.
