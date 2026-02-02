import sounddevice as sd
import numpy as np
import speech_recognition as sr

def listen(duration=5, fs=16000):
    r = sr.Recognizer()
    print("Listening...")

    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    audio_data = sr.AudioData(recording.tobytes(), fs, 2)

    try:
        text = r.recognize_google(audio_data)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None
