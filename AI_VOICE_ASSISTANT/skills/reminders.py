import schedule, time
from core.tts import speak

def set_reminder(msg, minutes):
    def task():
        speak(msg)
    schedule.every(minutes).minutes.do(task)

def run_pending():
    schedule.run_pending()
