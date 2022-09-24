import discord
import re
from datetime import datetime
from dateutil import parser
import os
from dotenv import load_dotenv

def convert_to_unix(time):
    """
    Discord uses a unix timestamp (unix time is just the amount of seconds passed from 1970) for the dynamic timing within the app, 
    this function converts the matches found by the bot into that format and returns them as a unix timestamp
    """
    hours, minutes, am_pm, timezone = int(time.group(2)), time.group(3), time.group(4), time.group(5)

    # if the user doesnt add a minute amount to their message, ex: 8pm instead of 8:00pm
    # default minutes to 00
    if minutes:
        pass
    else:
        minutes = 00

    # if user doesnt enter am pm value, assume pm
    if am_pm:
        pass
    else:
        am_pm = 'pm'


    # use dict to deal with timezone differences
    # local timezone is est for this pc
    # so we change hours accordingly
    timezones = {
        'e': 0, # easter
        'c': 1, # central
        'm': 2, # mountain
        'p': 3, # pacific
    }
    hours += timezones[timezone[0].lower()] # check first letter of timezone to see if we need to adjust the hours for timezones

    if (hours >= 12 and int(minutes) > 0) or (hours > 12): # check to make sure we dont take a 11 pst time and make it a 14 est when it should be 2 est
        
        if hours > 15:
            # check for 24 hour clock before changing am pm
            hours -= 12
        else:
            hours -= 12

            if am_pm.lower() == 'pm':
                print('changing to am')
                am_pm = 'am'
            else:
                print('changing to pm')
                am_pm = 'pm'

    # print('adjusted hours:', hours, am_pm)
    user_time = parser.parse(f'{hours}:{minutes} {am_pm}')
    # print(user_time)
    epoch = datetime(1971, 1, 1, 0, 0, 0).timestamp() # the start of unix time
    converted = datetime(user_time.year, user_time.month, user_time.day, user_time.hour, user_time.minute, user_time.second).timestamp()
    unix_time = f'<t:{int(converted)}:t>'
    return unix_time


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    pattern = '((\d?\d):?(\d\d)?) ?([ap]m)? ?([ecmp][sd]+t)'
    matches = re.search(pattern, message.content, flags=re.IGNORECASE)
    if matches:
        print(matches)
        unix_timestamp = convert_to_unix(matches)
        await message.channel.send(unix_timestamp)
    

load_dotenv()
TOKEN = os.getenv('UNIXBOTTOKEN')
client.run(TOKEN)
