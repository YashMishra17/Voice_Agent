from faster_whisper import WhisperModel

class STT:
    def __init__(self, model_size="small"):
        self.model = WhisperModel(model_size)

    def transcribe(self, audio_path):
        segments, _ = self.model.transcribe(audio_path)
        return " ".join([seg.text for seg in segments])
