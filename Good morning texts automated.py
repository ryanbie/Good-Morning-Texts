# importing modules
import random, schedule, time

# importing Twilio API
from twilio.rest import Client
from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number

# Step one : Creating Quotes to be Automated in the morning
# An Array for Good Morning Quotes
GOOD_MORNING_QUOTES = [
    "Good Morning!"
]

def send_message(quotes_list=GOOD_MORNING_QUOTES):

    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    quote = quotes_list(random.randint(0, len(quotes_list)-1))

    client.messages.create(to=cellphone, from=twilio_number, body=quote)

    # Send a message in the morning
    schedule.everyday().day.at("9:00").do(send_message, GOOD_MORNING_QUOTES)

while True:
    # Checks whether a scheduled task is pending to run or not
    schedule.run_pending()
    time.sleep(2)
