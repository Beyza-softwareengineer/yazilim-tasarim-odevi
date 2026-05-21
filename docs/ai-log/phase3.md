
#  AI ile pair programming Faz 3

* **Tarih / Süre:** 21 Mayıs 2026 / ~47 Dakika sürdü


##  Adım Adım Neler Yaşandı?

### Tasarım Kavgası ve Örüntü Seçimi
Hocam bu faza başlarken amacım, Faz 2'deki o hazır bildirim yapısını hiç bozmadan sisteme "kullanıcı grupları/abonelik mantığı" ve "gönderim öncelikleri (acil/ekonomik)" gibi dinamik davranışlar eklemekti. 
* AI'a sistemi nasıl büyütebileceğimi sorduğumda bana ilk başta onay mekanizmaları için **Chain of Responsibility** (Sorumluluk Zinciri) örüntüsünü kullanmamı dayattı. 
* Ancak yapıyı düşündüğümde bizim sistemde sırayla onay veren müdürler veya katmanlar yoktu. AI'a *"Burada bir hiyerarşi yok, bana sadece kullanıcıları dinamik olarak haberdar edecek ve duruma göre farklı algoritmayla (hızlı/yavaş) çalışacak esnek bir şey lazım"* diyerek itiraz ettim.
* Tartışma sonunda kampanya listelerine kullanıcı kaydetmek için **Observer**, gönderim bütçesi ve hız modlarını ayırmak için de **Strategy** örüntüsünün en mantıklı iki seçenek olduğuna karar verdik. AI da hatasını kabul edip bu iki örüntüye yöneldi.

### Kodlama Aşaması ve Yaşadığımız Hatalar
Örüntüleri netleştirince kodlamaya geçtik. AI bana soyut arayüzleri ve sınıfların iskeletini verdi, somut implementasyonları ve `BildirimMerkezi` ile `BildirimGondericiContext` sınıflarının birbirine bağlanma mantığını ben klavyenin başına geçerek yazdım.
* **Yaşadığımız Kritik Hata:** Kodları test ederken `KullaniciGozlemci` sınıfı tetiklendiğinde listenin içindeki nesne referansları yüzünden `AttributeError` almaya başladım. Meğer kullanıcıyı listeye eklerken aynı nesneyi iki kere ekleyebiliyormuşuz ve listeden silerken de bellek referansları çakışıyormuş.
* **Nasıl Çözdük?:** AI ile hemen kod başında refactoring yaptık. `abone_ekle` ve `abone_cikar` metotlarının içine liste kontrol mekanizmaları (`if abone not in self._aboneler:`) ekledik. Bu sayede listenin çoklu ve hatalı kayıtlardan dolayı runtime'da patlamasını tamamen engelledik.

###  Otomasyon Kurulumu
Kodların tıkır tıkır çalıştığını görünce hocanın ödevde istediği GitHub Actions kısmına geçtik. Python projesi olduğu için gidip ağır test kütüphaneleri kurmak yerine, kodlarda en ufak bir syntax (yazım/parantez) hatası olduğunda PR'ı kilitleyecek temiz bir derleme pipeline'ı kurmak istedim. AI ile birlikte `.github/workflows/ci.yml` dosyasını kurguladık ve `python -m compileall` komutunu entegre ederek otomasyonu tamamladık.


### 1. AI olmadan bu faz ne kadar sürerdi?
Açık konuşmak gerekirse hocam, AI desteği olmasaydı özellikle **Strategy** ve **Observer** gibi iki farklı davranışsal örüntüyü, Faz 2'deki yapısal kodları (Adapter ve Decorator) kırmadan aynı sisteme yedirmek (veri akışını ve Context yapısını entegre etmek) ciddi bir mimari kafa yorma gerektirirdi. Sıfırdan arayüzleri kurgulamak, UML standartlarına uydurmak ve o GitHub Actions'ın en ufak parantez hatasında çöken YAML dosyasıyla uğraşmak benim kesinlikle **1.5 - 2 günümü** alırdı. AI ile canlı pair programming yapmak bu süreyi nokta atışıyla **45 dakikaya** indirdi.

### 2. AI sizi nerede yanılttı? (Over-engineering Tuzağı)
AI oturumun başında projenin gerçek ölçeğini ve amacını doğru tartamadı. Bana sırf "davranışsal örüntü uygulamış olmak için" **Chain of Responsibility** ve **Mediator** örüntülerini de zorla koda ekletmeye çalıştı. Eğer yapay zekayı hiç sorgulamadan, körü körüne dinleseydim; topu topu 3-4 sınıfla tertemiz çözülecek bir bildirim motoru için en az 12-13 tane bomboş, işlevsiz sınıf oluşturacaktım. Projeyi gereksiz yere şişirip **Over-engineering (aşırı karmaşıklaştırma)** tuzağına düşecektim. AI'ın bu yapısal karmaşıklık önerisini erkenden fark edip reddettim, dizginleri elime alarak sistemi olması gerektiği gibi sade ve modüler tuttum.
###  Soru: AI olmadan bu faz ne kadar sürerdi? AI sizi nerede yanılttı?
**Benim Analizim ve Yanıtım:**
* **AI Olmadan Ne Kadar Sürerdi?:** Davranışsal örüntülerin (özellikle Observer ve Strategy arasındaki veri akışı bağının) mantıksal olarak kurulması, unit testlerin hazırlanması ve GitHub Actions konfigürasyonunun hatasız yapılması yapay zeka desteği olmadan muhtemelen 4-5 günümü alırdı. AI sayesinde tasarım kararlarını hızla doğrulayarak süreyi birkaç saate indirdim.
* **AI Beni Nerede Yanılttı?:** İlk başta yapay zeka, bizim bildirim sistemine davranışsal örüntü olarak **Chain of Responsibility** (Sorumluluk Zinciri) eklememi önerdi. Ancak projenin yapısını incelediğimde bildirimlerin bir onay zincirinden geçmesi gerekmediğini, daha ziyade toplu kitlelere duyurulması (Observer) ve hız/maliyet yönetimi (Strategy) gerektiğini fark ettim. AI'ın ilk önerisi projenin ölçeğine göre gereksiz derecede karmaşıktı . Bu noktada projeyi boşuna şişirmemek adına AI'ın o yönlendirmesini reddedip, sisteme daha çok uyan bu iki örüntüyü kendim seçtim.
