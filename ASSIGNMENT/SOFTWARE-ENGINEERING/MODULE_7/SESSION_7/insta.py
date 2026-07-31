# Create a class InstaStory with a method share() that prints 'Sharing an image story'. Now create another class WhatsAppStory that overrides share() to print 'Sharing a text status'. Instantiate both and call share() to show method overriding in action.

class instastory():
    def __init__(self):
        pass
    def share(self):
        print("sharing an image story")
class whstashappstory(instastory):
    def __init__(self):
        pass
    def share(self):
        print("sharing a text status")

p1 = instastory()
p2 = whstashappstory()
p1.share()
p2.share()