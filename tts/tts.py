import pyttsx3

class TTSModule:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # default speed
        self.engine.setProperty('volume', 1.0)  # max volume

    def speak(self, text, speed=1.0, pitch=1.0):
        """
        Speak text aloud.
        - speed: multiplier for speaking rate (default 1.0)
        - pitch: Not supported in pyttsx3 Windows
        """
        # Adjust rate
        self.engine.setProperty('rate', int(150 * speed))
        # pyttsx3 doesn't support pitch adjustment reliably on Windows
        self.engine.say(text)
        self.engine.runAndWait()
