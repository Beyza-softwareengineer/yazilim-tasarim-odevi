# yazilim-tasarim-odevi

# Tasarım Örüntüleri Ödevi - A) Bildirim Sistemi

Hocam , bu projede başlangıçta spagetti halde olan bir bildirim sistemini (Faz 0), her aşamada farklı tasarım örüntüleri uygulayarak adım adım daha esnek ve profesyonel bir mimariye dönüştürdüm. 


## Projede Kullandığım Örüntüler ve Mantıkları

### 1. Faz 1: Creational  Örüntü
* **Factory Method :** Projenin en başında `NotificationManager` içinde e-posta veya SMS nesnelerini doğrudan `if-else` bloklarıyla üretiyordum. Bu bağımlılığı ortadan kaldırmak için nesne üretim işini tamamen `NotificationFactory` sınıfına devrettim. Böylece istemci kod somut sınıflara bağımlı olmaktan kurtuldu.

### 2. Faz 2: Structural Örüntüler
* **Adapter Pattern :** Sisteme sonradan eklediğim üçüncü parti harici servislerin metot isimleri (örneğin `dispatch_text`), bizim projedeki standart `send()` metoduyla uyuşmuyordu. Mevcut çalışan kodları hiç kurcalamadan bu harici yapıları sisteme bağlamak için araya bir `SMSAdapter` yazdım.
* **Decorator Pattern :** Gönderilen mesajları şifrelemek veya loglamak gibi ekstra işler gerekti. Bunları sınıfların içine gömmek ya da her kombinasyon için yeni alt sınıflar açıp kod patlaması yaşamak yerine Decorator kullandım. Bu sayede çalışma zamanında (runtime) istediğim bildirime istediğim özelliği bir kılıf gibi giydirebiliyorum.

### 3. Faz 3: Behavioral  Örüntüler
* **Observer Pattern :** Sisteme kayıtlı kullanıcıların tek bir merkezden (`BildirimMerkezi`) tetiklenen toplu duyuruları ve kampanyaları otomatik olarak alabilmesini sağladım. Yeni bir kullanıcı sisteme dahil olduğunda merkezdeki kodları hiç değiştirmemiz gerekmiyor.
* **Strategy Pattern :** Bildirimlerin gönderim moduna göre (Acil/Hızlı veya Ekonomik/Toplu) farklı algoritmalarla çalıştırılabilmesini sağladım. İleride yeni bir gönderim stratejisi eklemek istersek mevcut kodlara dokunmadan sadece yeni bir strateji sınıfı açmamız yetecek.

## Mimari Diyagram Linkleri

Her faz için hazırladığım UML sınıf diyagramlarına (Mermaid kodlarına) aşağıdaki klasör yollarından grafiksel olarak bakabilirsiniz:
* [Faz 1 Diyagramı (Factory Method)](docs/diagrams/phase1_factory.md)
* [Faz 2 Diyagramı (Adapter & Decorator)](docs/diagrams/phase2_structural.md)
* [Faz 3 Diyagramı (Observer & Strategy)](docs/diagrams/phase3_behavioral.md)

