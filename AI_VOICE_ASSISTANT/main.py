from core.speech import listen
from core.tts import speak
from core.intent import detect_intent
from skills.weather import get_weather
from skills.emailer import send_email
from skills.reminders import set_reminder, run_pending
from skills.smarthome import control_device
import datetime

speak("Hello Ankur, your assistant is ready.")

while True:
    # run scheduled reminders
    run_pending()

    # listen from microphone
    command = listen()

    if not command:
        continue

    print("Command:", command)

    intent = detect_intent(command)

    if intent == "greet":
        speak("Hello Ankur. How can I help you?")

    elif intent == "time":
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + now)

    elif intent == "weather":
        speak(get_weather("Delhi"))

    elif intent == "email":
        # change email id here
        send_email(
            "friend@gmail.com",
            "Message from AI Assistant",
            "Hello! This email was sent by my voice assistant."
        )
        speak("Email sent successfully.")

    elif intent == "reminder":
        set_reminder("Drink water", 30)
        speak("Reminder set for 30 minutes.")

    elif intent == "smarthome":
        control_device("light", "ON")
        speak("Light turned on.")

    else:
        speak("Sorry, I did not understand that.")
