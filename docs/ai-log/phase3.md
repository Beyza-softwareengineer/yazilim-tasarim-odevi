# AI Günlüğü (Phase 3)

###  Soru: AI olmadan bu faz ne kadar sürerdi? AI sizi nerede yanılttı?
**Benim Analizim ve Yanıtım:**
* **AI Olmadan Ne Kadar Sürerdi?:** Davranışsal örüntülerin (özellikle Observer ve Strategy arasındaki veri akışı bağının) mantıksal olarak kurulması, unit testlerin hazırlanması ve GitHub Actions konfigürasyonunun hatasız yapılması yapay zeka desteği olmadan muhtemelen 4-5 günümü alırdı. AI sayesinde tasarım kararlarını hızla doğrulayarak süreyi birkaç saate indirdim.
* **AI Beni Nerede Yanılttı?:** İlk başta yapay zeka, bizim bildirim sistemine davranışsal örüntü olarak **Chain of Responsibility** (Sorumluluk Zinciri) eklememi önerdi. Ancak projenin yapısını incelediğimde bildirimlerin bir onay zincirinden geçmesi gerekmediğini, daha ziyade toplu kitlelere duyurulması (Observer) ve hız/maliyet yönetimi (Strategy) gerektiğini fark ettim. AI'ın ilk önerisi projenin ölçeğine göre gereksiz derecede karmaşıktı . Bu noktada projeyi boşuna şişirmemek adına AI'ın o yönlendirmesini reddedip, sisteme daha çok uyan bu iki örüntüyü kendim seçtim.
