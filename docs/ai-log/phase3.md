# 🤖 AI Log — Faz 3: Behavioral Patterns (Observer & Strategy)

## Pair Programming Oturumu — ~35 Dakika

---

## Bölüm 1: Observer Pattern

### Kullandığım Prompt

> "Sistemde bir BildirimMerkezi var. Kayıtlı kullanıcıların yeni
> bir duyuru geldiğinde otomatik haberdar olmasını istiyorum.
> Observer pattern burada nasıl uygulanır? Kullanıcı sayısı
> artsa bile merkez kodunu değiştirmek istemiyorum."

### AI'ın Yanıtı (Özet)

AI Observer örüntüsünün tam olarak bu senaryo için tasarlandığını
açıkladı:
- `Subject` (BildirimMerkezi): gözlemci listesini tutar,
  `subscribe()`, `unsubscribe()`, `notify()` metodları.
- `Observer` (KullaniciGozlemci): `update()` metodunu implement eder.
- Yeni kullanıcı eklendiğinde merkez kodu hiç değişmez.

### Ben Ne Uyguladım?

AI'ın önerdiği yapıyla büyük ölçüde aynı gittim.
`BildirimMerkezi` sınıfına `abone_ekle()`, `abone_cikar()` ve
`bildir()` metodları ekledim. Her kullanıcı `KullaniciGozlemci`
sınıfından türüyor ve `guncelle()` metodunu kendine göre implement
ediyor.

---

## Bölüm 2: Strategy Pattern

### Kullandığım Prompt

> "Bazı bildirimler acil gitmeli (anlık), bazıları ekonomik
> (toplu, yavaş). Bunu if-else ile çözmek yerine daha temiz
> bir yol istiyorum. Strategy pattern uygun mu?"

### AI'ın Yanıtı (Özet)

AI Strategy'nin bu senaryo için biçilmiş kaftan olduğunu söyledi.
Her gönderim modunu bağımsız bir strateji sınıfı olarak tasarlamayı
ve bağlamın (context) stratejiyi runtime'da almasını önerdi.
Ayrıca State pattern'i alternatif olarak sundu.

### AI'ın Yanlış Önerdiği Nokta ⚠️

AI, State pattern'i de geçerli alternatif olarak sundu. Ancak
State, nesnenin iç durumuna göre davranışın otomatik değişmesi
içindir. Benim durumumda kullanıcı bilinçli olarak gönderim modunu
seçiyor — bu bir durum geçişi değil, açık bir algoritma seçimi.
Bu farkı AI tam netleştirmedi, ben kendim analiz ederek Strategy'nin
doğru seçim olduğuna karar verdim.

### Ben Ne Uyguladım?

`GonderimStratejisi` adında soyut bir sınıf oluşturdum.
`AcilGonderim` ve `EkonomikGonderim` alt sınıfları kendi
`gonder()` metodlarını implement etti. Bağlam sınıfı stratejiyi
dışarıdan alıyor, hiçbir if-else yok.

---

## Genel Değerlendirme

### AI olmadan bu faz ne kadar sürerdi?
Observer ve Strategy'nin teorisini bilsem de doğru sınıf
hiyerarşisini kurmak muhtemelen 2-3 kat daha uzun sürerdi.
AI, hangi metodun nerede olması gerektiğini hızla gösterdi
ve iterasyon süresini kısalttı. Tahminen 35 dakika yerine
2 - 3 gün sürerdi.

### AI beni nerede yanılttı?
State ve Strategy arasındaki farkı net çizmedi. "İkisi de
işe yarar" demesi beni neredeyse yanlış örüntüye yönlendiriyordu.
Kendi analizimle ikisi arasındaki temel farkı (iç durum geçişi
vs. dışarıdan algoritma seçimi) kavrayarak doğru kararı verdim.
Bu deneyim bana gösterdi ki AI iyi bir başlangıç noktası sunuyor
ama son kararı her zaman kendim vermem gerekiyor.
