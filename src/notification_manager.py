from abc import ABC, abstracthmethod
class Notification(ABC):
  @abstractmethod
  def send(self,message,receiver):
    pass
class EmailNotification(Notification):
  def send(self,message,receiver):
    printf(f"E-posta sunucusuna bağlanılıyor")
    printf(f"Alici:{receiver}|Mesaj:{message}")
class SMSNotifivation(Notification):
  def send(self,message,receiver):
     print(f"SMS Gateway bağlantısı kuruluyor...")
        print(f"Telefon: {receiver} | Mesaj: {message}")

class PushNotification(Notification):
    def send(self, message, receiver):
        print(f"Mobil cihaz ID'si doğrulanıyor...")
        print(f"Push İçeriği: {message}")

class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        raise ValueError(f"Geçersiz bildirim tipi: {notification_type}")

if __name__ == "__main__":
    factory = NotificationFactory()
    notifier = factory.create_notification("email")
    notifier.send("Merhaba, bu bir Factory Method örneğidir!", "beyza@example.com")
  
