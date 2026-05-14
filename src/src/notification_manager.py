# src/notification_manager.py
# BU KOD BİLEREK TASARIM ÖRÜNTÜSÜ OLMADAN YAZILMIŞTIR (FAZ 0)

class NotificationManager:
    def send_notification(self, type, message, receiver):
        # Her şey tek bir metodun içinde, if-else zinciriyle yönetiliyor 
        if type == "email":
            print(f"E-posta sunucusuna bağlanılıyor: {receiver}")
            print(f"İçerik: {message}")
            print("E-posta başarıyla gönderildi.")
        
        elif type == "sms":
            print(f"SMS Gateway'e bağlanılıyor: {receiver}")
            print(f"Mesaj: {message}")
            print("SMS başarıyla gönderildi.")
        
        elif type == "push":
            print(f"Mobil cihaz ID'si aranıyor: {receiver}")
            print(f"Bildirim: {message}")
            print("Push bildirimi gönderildi.")
        
        else:
            print("Hata: Geçersiz bildirim tipi!")

# Kullanım
notifier = NotificationManager()
notifier.send_notification("email", "Merhaba!", "test@mail.com")
