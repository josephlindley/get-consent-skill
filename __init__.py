from mycroft import MycroftSkill, intent_file_handler


class GetConsent(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('consent.get.intent')
    def handle_consent_get(self, message):
        self.speak_dialog('consent.get')


def create_skill():
    return GetConsent()

