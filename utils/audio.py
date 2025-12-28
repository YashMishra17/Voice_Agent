import sounddevice as sd
import soundfile as sf

def record(duration=5, filename="input.wav", fs=16000):
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    sf.write(filename, recording, fs)
    return filename
