![fewfweg](https://user-images.githubusercontent.com/67122764/170590841-ed7a957e-9651-4227-b1e8-c0014e6f770d.png)
# Govee-Discord-Bot
## This Discord bot lets you control your wifi-enabled Govee RGB device
This discord bot uses Govee's public http api to control a wifi-enabled Govee rgb device

## A list of all the current available bot commands:
- $on - To turn the device on
- $off - To turn the device off
- $state - To get the current state of the device (on/orr)
- $brightness N - Change the brightness of the device to N procent brightness
- $color R,G,B - To change the color of the device input requires 3 numbers (max. 255) separated by a comma (R= Red, G= Green, B= Blue), a list of a few example colors:
    - 🔴Red: 255,0,0
    - 🟠Orange: 255,165,0
    - 🟡yellow: 255,255,0
    - 🟢Green: 0,255,0
    - 🔵Cyan: 173,216,230
    - 🧿Blue: 0,0,255
    - 🟣Purple: 128,0,128
    - 🌸Pink: 255,20,147

## The main.py file uses information from a file called 'personaldata.py'
This file should contain the follow constants:
- DISCORDBOTTOKEN = 'your_discord_bot_token'
- API_KEY = 'your_govee_api_key'
- DEVICEMAC = 'your_govee_device_macaddress'
- DEVICEMODEL = 'your_devicemodel' 
> e.g 'H619E'
- BANNEDUSERS = [12345678987654321]
> By default everyone can use the bot, only the users in this list with userids (separated by commas) are not permitted to use the bot.

## To-do list:
- Rate limit on the bot side (not on the side of the discord channel, which server owners could bypass).
