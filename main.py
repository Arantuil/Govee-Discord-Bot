import discord
from discord.ext import commands

from personaldata import *

import requests

headers = {'Govee-API-Key': API_KEY, 'content-type': 'application/json'}
apicontrolurl = 'https://developer-api.govee.com/v1/devices/control'

client = discord.Client()

client.state = ''

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    devicestateurl = f'https://developer-api.govee.com/v1/devices/state?device={DEVICEMAC[0:2]}%3A{DEVICEMAC[3:5]}%3A{DEVICEMAC[6:8]}%3A{DEVICEMAC[9:11]}%3A{DEVICEMAC[12:14]}%3A{DEVICEMAC[15:17]}%3A{DEVICEMAC[18:20]}%3A{DEVICEMAC[21:23]}&model={DEVICEMODEL}'
    devicestate = requests.get(devicestateurl, headers=headers)
    onoroff = (devicestate.json()['data']['properties'][1]['powerState'])
    if onoroff == 'on':
        await client.change_presence(status=discord.Status.online, activity=discord.Game(f'🟢 Ledstrip is now turned ON'))
    else:
        await client.change_presence(status=discord.Status.online, activity=discord.Game(f'🔴 Ledstrip is now turned OFF'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        await message.channel.send('''A list of all the current available commands:
- $on - To turn the ledstrip on
- $off - To turn the ledstrip off
- $state - To get the current state of the ledstrip (on/orr)
- $brightness N - Change the brightness of the ledstrip to N procent brightness
- $color R,G,B - To change the color of the ledstrip input requires 3 numbers (max. 255) separated by a comma (R= Red, G= Green, B= Blue), a list of a few example colors:
    - 🔴Red: 255,0,0
    - 🟠Orange: 255,165,0
    - 🟡yellow: 255,255,0
    - 🟢Green: 0,255,0
    - 🔵Cyan: 173,216,230
    - 🧿Blue: 0,0,255
    - 🟣Purple: 128,0,128
    - 🌸Pink: 255,20,147
''')
    
    if message.content.startswith('$off'):
        if message.author.id not in BANNEDUSERS:
            await message.channel.send('Ledstrip is now turned OFF 🟥')
            putrequest = requests.put(apicontrolurl, json={"device": DEVICEMAC,"model": DEVICEMODEL,"cmd": {"name": "turn","value": 'off'}}, headers=headers)
            print(putrequest)
            await client.change_presence(status=discord.Status.online, activity=discord.Game(f'🔴 Ledstrip is now turned OFF'))
            client.state = 'off'
        else:
            await message.channel.send('You are not permitted to control the ledstrip')
    
    if message.content.startswith('$on'):
        if message.author.id not in BANNEDUSERS:
            await message.channel.send('Ledstrip is now turned ON 🟩')
            putrequest = requests.put(apicontrolurl, json={"device": DEVICEMAC,"model": DEVICEMODEL ,"cmd": {"name": "turn","value": 'on'}}, headers=headers)
            print(putrequest)
            await client.change_presence(status=discord.Status.online, activity=discord.Game(f'🟢 Ledstrip is now turned ON'))
            client.state = 'on'
        else:
            await message.channel.send('You are not permitted to control the ledstrip')

    if message.content.startswith('$state'):
        if client.state == 'on':
            await message.channel.send('Ledstrip is currently turned ON 🟢')
        elif client.state == 'off':
            await message.channel.send('Ledstrip is currently turned OFF 🔴')
        elif client.state == '':
            await message.channel.send('Ledstrip is currently turned ❔')
        
    if message.content.startswith('$brightness'):
        if message.author.id not in BANNEDUSERS:
            devicestateurl = f'https://developer-api.govee.com/v1/devices/state?device={DEVICEMAC[0:2]}%3A{DEVICEMAC[3:5]}%3A{DEVICEMAC[6:8]}%3A{DEVICEMAC[9:11]}%3A{DEVICEMAC[12:14]}%3A{DEVICEMAC[15:17]}%3A{DEVICEMAC[18:20]}%3A{DEVICEMAC[21:23]}&model={DEVICEMODEL}'
            devicestate = requests.get(devicestateurl, headers=headers)
            onoroff = (devicestate.json()['data']['properties'][1]['powerState'])
            if onoroff == 'on':
                if (len(message.content) == 13):
                    try:
                        num = int(message.content[-1])
                        await message.channel.send(f"The ledstrip's brightness will be set to {num}%")
                        client.brightness = num
                        brightnesslevel = {"device": DEVICEMAC,"model": DEVICEMODEL ,"cmd": {"name": "brightness","value": client.brightness}}
                        putrequest = requests.put(apicontrolurl, json=brightnesslevel, headers=headers)
                    except:
                        await message.channel.send('Beep Boop Error!🤖 (Enter a number under 100 after $brightness)')

                if (len(message.content) == 14):
                    try:
                        num = int(message.content[-2:])
                        await message.channel.send(f"The ledstrip's brightness will be set to {num}%")
                        client.brightness = num
                        brightnesslevel = {"device": DEVICEMAC,"model": DEVICEMODEL ,"cmd": {"name": "brightness","value": client.brightness}}
                        putrequest = requests.put(apicontrolurl, json=brightnesslevel, headers=headers)
                    except:
                        await message.channel.send('Beep Boop Error!🤖 (Enter a number under 100 after $brightness)')

                if (len(message.content) == 15):
                    try:
                        num = int(message.content[-3:])
                        await message.channel.send(f"The ledstrip's brightness will be set to {num}%")
                        client.brightness = num
                        brightnesslevel = {"device": DEVICEMAC,"model": DEVICEMODEL ,"cmd": {"name": "brightness","value": client.brightness}}
                        putrequest = requests.put(apicontrolurl, json=brightnesslevel, headers=headers)
                    except:
                        await message.channel.send('Beep Boop Error!🤖 (Enter a number under 100 after $brightness)')
            else:
                await message.channel.send('The ledstrip is currently turned off, use $on')
        else:
            await message.channel.send('You are not permitted to control the ledstrip')
    
    if message.content.startswith('$color'):
        if message.author.id not in BANNEDUSERS:
            devicestateurl = f'https://developer-api.govee.com/v1/devices/state?device={DEVICEMAC[0:2]}%3A{DEVICEMAC[3:5]}%3A{DEVICEMAC[6:8]}%3A{DEVICEMAC[9:11]}%3A{DEVICEMAC[12:14]}%3A{DEVICEMAC[15:17]}%3A{DEVICEMAC[18:20]}%3A{DEVICEMAC[21:23]}&model={DEVICEMODEL}'
            devicestate = requests.get(devicestateurl, headers=headers)
            onoroff = (devicestate.json()['data']['properties'][1]['powerState'])
            if onoroff == 'on':
                colorlevel = message.content[7:]
                x = colorlevel.split(",")
                colorlevelcmd = {"device": DEVICEMAC,"model": DEVICEMODEL ,"cmd": {"name": "color","value": {'r': int(x[0]),'g': int(x[1]),'b': int(x[2])}}}
                putrequest = requests.put(apicontrolurl, json=colorlevelcmd, headers=headers)
                await message.channel.send('The color of the ledstrip has now changed 🔴🟠🟡🟢🔵🟣')
            else:
                await message.channel.send('The ledstrip is currently turned off, use $on')
    
        else:
            await message.channel.send('You are not permitted to control the ledstrip')

@client.event
async def on_application_command_error(message, error):
    if isinstance(error, commands.CommandOnCooldown):
        await message.channel.send(error)
    else:
        raise error

client.run(DISCORDBOTTOKEN)
