# 🤖 AI Log — Faz 2: Structural Patterns (Adapter & Decorator)

## Kullandığım Prompt

> "Sistemime üçüncü parti bir SMS kütüphanesi entegre etmem gerekiyor
> ama bu kütüphanenin metot ismi dispatch_text(), bizim standart
> send() metodumuzla uyuşmuyor. Mevcut kodu bozmadan bunu sisteme
> bağlamak için Adapter mi kullanmalıyım yoksa Facade mi?
> Farkını ve hangisinin daha uygun olduğunu açıkla."

---

## AI'ın Yanıtı (Özet)

AI ikisinin farkını şöyle açıkladı:
- **Adapter:** Uyumsuz iki arayüzü birbirine bağlar. Mevcut bir
  sınıfı değiştirmeden sisteme entegre etmek için kullanılır.
  Birebir dönüşüm ilişkisi vardır.
- **Facade:** Karmaşık bir alt sistemi basitleştirilmiş tek bir
  arayüzle sunar. Birden fazla sınıfı arkasında gizler.

AI, benim durumum için **Adapter**'ın daha doğru olduğunu söyledi
çünkü tek bir uyumsuz sınıfı mevcut arayüze uydurmaya çalışıyorum,
karmaşık bir sistemi gizlemeye değil.

---

## AI'ın Yanlış veya Eksik Önerdiği Nokta ⚠️

AI başlangıçta Facade'ı da geçerli bir seçenek olarak sundu ve
"ikisi de işe yarar" dedi. Bu bence eksik bir yaklaşım. Facade
burada anlamsız olurdu çünkü gizlemem gereken karmaşık bir alt
sistem yok, sadece metot ismi uyumsuzluğu var. AI'ın "ikisi de
olur" demesi beni yanıltabilirdi; kendi analizimle Adapter'ın
tek doğru seçim olduğuna karar verdim.

---

## Decorator İçin Kullandığım Prompt

> "Bildirim nesnelerime runtime'da şifreleme ve loglama özelliği
> eklemek istiyorum. Alt sınıf açmak yerine daha esnek bir yol
> var mı?"

---

## AI'ın Yanıtı (Özet)

AI Decorator örüntüsünü önerdi. Her ek özelliği ayrı bir
Decorator sınıfı olarak sarmalayabileceğimi, istediğim kombinasyonu
runtime'da oluşturabileceğimi açıkladı.

---

## Ben Ne Uyguladım?

Her iki örüntüyü de uyguladım:
- `SMSAdapter` sınıfı: üçüncü parti kütüphanenin `dispatch_text()`
  metodunu bizim `send()` arayüzüne bağladı.
- `EncryptionDecorator` ve `LoggingDecorator` sınıfları: bildirimlere
  runtime'da şifreleme ve loglama özelliği giydirdi.

---

## AI'dan Farklı Yaptığım Noktalar

- Facade önerisini reddettim, Adapter'ı bilinçli seçtim.
- AI'ın Decorator kod iskeletinde her decorator kendi içinde
  `super().send()` çağırıyordu; ben buna ek olarak hata durumunda
  orijinal mesajın bozulmaması için try-except bloğu ekledim.
  Bu AI'ın önerisinde yoktu.
