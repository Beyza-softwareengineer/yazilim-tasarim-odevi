
class ExternalSMSService:
    def dispatch_text(self, phone_number: str, text_content: str):
        print(f"[Harici API] {phone_number} numarasına SMS gönderildi: {text_content}")

class SMSAdapter:
    def __init__(self, external_service: ExternalSMSService):
        self.external_service = external_service

    def send(self, message: str, receiver: str):
      
        self.external_service.dispatch_text(phone_number=receiver, text_content=message)


class NotificationDecorator:
    def __init__(self, decorated_notification):
        self._decorated_notification = decorated_notification

    def send(self, message: str, receiver: str):
        self._decorated_notification.send(message, receiver)

class EncryptedNotificationDecorator(NotificationDecorator):
    def send(self, message: str, receiver: str):
        encrypted_message = f"🔒[ŞİFRELENDİ] {message}"
        super().send(encrypted_message, receiver)

class LoggingNotificationDecorator(NotificationDecorator):
    def send(self, message: str, receiver: str):
        print(f"📝 [LOG]: {receiver} adresine bildirim tetiklendi.")
        super().send(message, receiver)
