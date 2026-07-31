class Notification:
    def send(self):
        print("Sending a notification")

class EmailNotification(Notification):
    def send(self):
        print("Sending notification via Email")

class SMSNotification(Notification):
    def send(self):
        print("Sending notification via SMS")

n1 = Notification()
n2 = EmailNotification()
n3 = SMSNotification()

n1.send()
n2.send()
n3.send()