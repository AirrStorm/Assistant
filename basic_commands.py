import datetime
import requests
from speechrecognitionfunc import listen
from speech import convert

def get_time(command):
    if "what is the time" in command:
        now = datetime.datetime.now()  # Get the current date and time
        print(now.strftime("%I:%M %p"))
        return now.strftime("%I:%M %p")  # Format it as hours:minutes:seconds
    # return "Command not recognized."  # Return a default message if the command isn't matched

def joke(command):
    if "joke" in command:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        prejoke = response.json()
        joke = f"{prejoke['setup']} - {prejoke['punchline']}"
        print(joke)
        return joke

def get_date(command):
    if "what is the date" in command:
        today = datetime.datetime.now()  # Get the current date and time
        print(today.strftime("%B %d, %Y"))
        return today.strftime("%B %d, %Y")
    

# convert(get_time(listen()))
convert(joke(listen()))

# convert(get_date(listen()))

