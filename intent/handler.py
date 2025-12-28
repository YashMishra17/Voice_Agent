import re

class IntentHandler:
    def detect_intent(self, text):
        text = text.lower()
        if re.search(r"(cancel|unsubscribe|stop)", text):
            return "cancellation_request"
        elif re.search(r"(keep|continue|no)", text):
            return "objection"
        elif re.search(r"(bye|thanks|goodbye)", text):
            return "close"
        else:
            return "unknown"
