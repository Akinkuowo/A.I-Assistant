import pyttsx3  # A speech to text liabery
import datetime  # A current date and time liabery

engine = pyttsx3.init()


# i create a function that speak what ever a user put in the function agrument
def speech(audio):
    engine.say(audio)
    engine.runAndWait()


def getTime():
    # get the current date and convert to a string
    time = datetime.datetime.now().strftime('%I:%M:%S')
    speech(time)


def getDate():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speech(day)
    speech(month)
    speech(year)


def welcome():
    speech("Welcome Master Elijah")
    speech("The current time is")
    getTime()
    speech("And today's date is")
    getDate()


welcome()
