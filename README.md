# Tasarım Örüntüleri Ödevi — A) Bildirim Sistemi

**Konu Seçimi: A — Bildirim Sistemi**
Bu konuyu seçmemin sebebi: tüm bildirim tiplerinin tek bir sınıfta
if-else zincirleriyle yönetilmesi, gerçek projelerde sık karşılaşılan
ve Creational + Structural + Behavioral örüntülerin üçünü de doğal
olarak tetikleyen bir senaryo sunuyor. 

---

## Projenin Ne Yaptığı

Başlangıçta spagetti halde olan bir bildirim sistemini (Faz 0),
her aşamada farklı tasarım örüntüleri uygulayarak adım adım daha
esnek ve profesyonel bir mimariye dönüştürdüm.

Sistem; e-posta, SMS ve push bildirimi gönderebiliyor. Üçüncü parti
servislerle uyumlu çalışabiliyor, mesajlara şifreleme ve loglama
eklenebiliyor, toplu veya acil gönderim stratejisi seçilebiliyor.

---

## Kullanılan Tasarım Örüntüleri

| Faz | Örüntü | Kategori | Kısa Açıklama |
|-----|--------|----------|---------------|
| Faz 1 | Factory Method | Creational | Nesne üretim sorumluluğunu fabrika sınıfına devreder; istemci kod somut sınıfları tanımaz |
| Faz 2 | Adapter | Structural | Uyumsuz üçüncü parti arayüzleri mevcut sisteme bağlar |
| Faz 2 | Decorator | Structural | Runtime'da nesnelere şifreleme/loglama gibi özellikler ekler |
| Faz 3 | Observer | Behavioral | Abone kullanıcılar merkez tetiklenince otomatik bildirim alır |
| Faz 3 | Strategy | Behavioral | Acil veya ekonomik gönderim algoritması runtime'da seçilir |

---

## Mimari Diyagramlar

Her faz için UML sınıf diyagramları:

- [Faz 1 Diyagramı — Factory Method](docs/diagrams/phase1_factory.md)
- [Faz 2 Diyagramı — Adapter & Decorator](docs/diagrams/phase2_structural.md)
- [Faz 3 Diyagramı — Observer & Strategy](docs/diagrams/phase3_behavioral.md)

---


## Proje Yapısı

```
├── README.md
├── PATTERNS.md
├── PROBLEMS.md
├── src/
├── docs/
│   ├── diagrams/
│   └── ai-log/
│       ├── phase1.md
│       ├── phase2.md
│       └── phase3.md
└── .github/workflows/ci.yml
```
