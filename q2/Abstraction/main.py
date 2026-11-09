from abc import ABC, abstractmethod


class NotificationSystem(ABC):
    
    @abstractmethod
    def send(self, user, message):
        pass


class EmailNotification(NotificationSystem):
    

    def send(self, users, message, x):
        print(f"Sending email to {users}: {message} {x}")


# my_notifier = NotificationSystem()  
email_notifier = EmailNotification()  # <-- SUCCESS: Child implemented the contract
email_notifier.send("alice@example.com", "Welcome!", 1)