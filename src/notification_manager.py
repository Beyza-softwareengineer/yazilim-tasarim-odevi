# src/notification_manager.py

class NotificationManager:
    def send(self, type, message, receiver):
        if type == "email":
            if "@" in receiver:
                print(f"E-posta sunucusuna bağlanılıyor...")
                print(f"Alıcı: {receiver} | Mesaj: {message}")
            else:
                print("Hata: Geçersiz mail!")
        
        elif type == "sms":
            if len(receiver) >= 10:
                print(f"SMS hattı açılıyor...")
                print(f"Telefon: {receiver} | Mesaj: {message}")
            else:
                print("Hata: Numara kısa!")
        
        # Yeni bir tip eklemek için bu dosyayı hep değiştirmek ZORUNDAYIZ.
        # Bu 'Open-Closed Principle' kuralına aykırıdır.
