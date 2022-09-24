# Unix-time-discord-bot
Converts local time to unix timestamp format for discord

# Discord
Discord added unix formatting a little while ago that lets users enter a timestamp that would get displayed in every users local time. ie if someone wanted to start an event at 7:30est; People in any other time zone regions would get the time formatted for them automatically. Issue is, it was complicated to use, it often times required the user to use outside sources and websites to get the right formatting. 

# Bot
The bot uses regex to determine what time users are referring to and responds with a auto formatted unix timestamp in the same channel. Example below:

![imgur](https://i.imgur.com/lTtPuB5.png "Unix Bot Example")


# few things to note
1st, if not provided the bot assumes the user is referring to PM.

2nd, The bot only responds to messages that have a specific timezone attached. So 730pm will not work, but 730pm est will work. This is done to have an accurate representation of what time the user is referring to.
