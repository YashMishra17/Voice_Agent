from stt import STT
from tts import TTSModule
from dialogue import DialogueManager
from utils import record

# Initialize modules
stt = STT()
tts = TTSModule()
dm = DialogueManager()

print("=== Subscription Cancellation Agent ===")

while True:
    audio_file = record(duration=5)
    user_text = stt.transcribe(audio_file)
    print("User:", user_text)

    response = dm.next_response(user_text)
    print("Agent:", response)
    tts.speak(response)

    if dm.state == "close":
        break

print("Conversation ended.")
