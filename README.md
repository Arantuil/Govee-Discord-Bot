# Govee-Discord-Bot-Ledstrip
## A discord bot to control your Govee wifi-enabled rgb ledstrip

## The main.py file uses information from a file called 'personaldata.py'
This file should contain the follow constants:
- API_KEY
> 'your_govee_api_key'
- DEVICEMAC
> 'your_govee_device_macaddress'
- DEVICEMODEL
> 'your_devicemodel' e.g 'H619E'
- BANNEDUSERS
> By default everyone can use the bot, only the users in this list with userids are not permitted to use the bot.

To-do list:
- Rate limit on the bot side (not on the side of the discord channel, which server owners could bypass).
