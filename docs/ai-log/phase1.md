Al'a ne sordunuz (prompt): > "Python ile yazdığım, if-else bloklarından arındırılmış NotificationFactory kodumu, PROBLEMS.md ve PATTERNS.md dosyalarımı paylaştım ve kod incelemesi istedim."

Al ne yanıtladı : > "AI, kodun genel mimarisini (ABC ve Factory örüntüsü kullanımını) doğru buldu. Ancak kodda yer alan printf (Python'da bulunmayan fonksiyon) ve abstracthmethod (yazım hatası) gibi kritik çalışma zamanı hatalarını tespit etti.
Ayrıca Factory içerisindeki if-else yapısını Python sözlükleri (dictionary mapping) ile değiştirerek Açık/Kapalı Prensibini (OCP) daha katı ve temiz bir şekilde uygulayabileceğimi önerdi."

Siz ne uyguladınız ve neden farklı/aynı: "AI'ın tespit ettiği yazım hatalarını düzelttim. Fabrika içindeki if-else yapısını daha modüler ve 
genişletilebilir olduğu için AI'ın önerdiği gibi sözlük yapısına dönüştürerek uyguladım."
