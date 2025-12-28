from intent import IntentHandler

class DialogueManager:
    def __init__(self):
        self.state = "greeting"
        self.intent_handler = IntentHandler()
        self.memory = []

    def next_response(self, user_text):
        self.memory.append({"state": self.state, "user": user_text})
        intent = self.intent_handler.detect_intent(user_text)

        if self.state == "greeting":
            self.state = "cancellation_request"
            return "Hello! How can I assist you today?"
        elif self.state == "cancellation_request":
            if intent == "cancellation_request":
                self.state = "objection"
                return "I understand you want to cancel. May I ask why?"
            else:
                return "I'm here to help with cancellations. Could you clarify?"
        elif self.state == "objection":
            if intent == "objection":
                self.state = "close"
                return "I see. We'll proceed with the cancellation. Thank you for your time."
            else:
                return "Thanks for the info. I will note that."
        elif self.state == "close":
            return "Goodbye!"
        else:
            return "Sorry, I didn't understand that."
