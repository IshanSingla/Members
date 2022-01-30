from datetime import datetime
import json, firebase_admin, sys,telethon,asyncio,requests
from tokenize import Token
from telethon import *

from telethon import functions, types
from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession
from telethon.errors.rpcerrorlist import ChatAdminRequiredError
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest

from telethon.errors.rpcerrorlist import ChatAdminRequiredError
from firebase_admin import credentials,db
cred = credentials.Certificate('1.json')
default_app = firebase_admin.initialize_app( cred,{'databaseURL':"https://induced-scraping-bot-30ee0-default-rtdb.asia-southeast1.firebasedatabase.app/"})


APP_ID = 12468937
API_HASH = "84355e09d8775921504c93016e1e9438"
BOT_TOKEN = "5170782972:AAFba1KKvu7DzcX_4utjQqzRVidmurFMCbE"
OWNERS=[1854668908, 1303790979, 1322941082, 5217968098]
client = telethon.TelegramClient("cli", api_id=APP_ID , api_hash=API_HASH).start(bot_token=BOT_TOKEN)



@client.on(events.NewMessage(incoming=True, pattern=r"\.adding"))
async def _(e):
    if e.sender_id in OWNERS:
        TOK=(db.reference(f"/Members/Tok/")).get()
        LINK=(db.reference(f"/Members/Link/")).get()
        await e.reply(f"Adding Start")
        while True:
            for x in TOK:
                for i in LINK:
                    get_ip= requests.get(f"https://telesubs.com/api/v2?key={x}&action=add&service=56&link={i}&quantity=50")
                    red = json.loads(get_ip.text)
                    if 'error' in red:
                        if red['error']=="You have active order with this link. Please wait until order being completed.":
                            pass
                        else:
                            await e.reply(f"Error:  `{red['error']}`\n\nToken: {x}\n\nMade with ❤️ By @InducedBots")
                            return
                    else:
                        await e.reply(f"Order ID:  `{red['order']}`\nOrder Link: {i}\nOrder Token: `{x}`\n\nMade with ❤️ By @InducedBots")
            await asyncio.sleep(5)
    else:
        await e.reply("You can not use me\nContact: @IshanSingle_xD\n\nMade with ❤️ By @InducedBots")

@client.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
async def ping(e):
    if e.sender_id in OWNERS:
        start = datetime.now()
        text = "Pong! \nBy Induced"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"(●'◡'●) 𝗣𝗼𝗻𝗴!\n`{ms}` 𝗺𝘀 \n\nMade with ❤️ By @InducedBots")
    else:
        await e.reply("You can not use me\nContact: @IshanSingle_xD\n\nMade with ❤️ By @InducedBots")

@client.on(events.NewMessage(incoming=True, pattern=r"\.restart"))    
async def restart(e):
    await e.reply("**Bot Is Restarting...\n\nMade with ❤️ By @InducedBots**")
    os.execl(sys.executable, sys.executable, "-m", "main")

    
    
    
async def get_waiting(chat_id):
    try:
        users = await client(
            functions.messages.GetChatInviteImportersRequest(
                requested=True,
                peer=chat_id,
                limit=0,
                offset_date=0,
                offset_user=types.InputPeerEmpty(),
            )
        )
    except ChatAdminRequiredError:
        me = await client.get_me()
        return (
            "Chat Admin required [{}](tg://user?id={}).".format(
                me.first_name, me.id
            ),
            [],
        )
    if users.count == 0:
        return "Nothing here to approve !", []
    userids = [i.user_id for i in users.importers]
    return "**Total no of user who requesting to join**: {}\n\n".format(users.count), userids

@client.on(events.NewMessage(incoming=True,pattern=r"\.approveall",))
async def approvealll(event):
    mid = chat = None
    event.reply("Start")
    if event.is_private:
        try:
            mid = event.text.split(" ")[1]
        except IndexError:
            await event.reply(
                "Please provide a chat ID or username, or use this command in that chat/channel."
            )
            return
    else:
        mid = event.chat_id
    try:
        mid = int(mid)
        chat = (await client.get_entity(mid)).id
    except ValueError:
        chat = (await client.get_entity(mid)).id
    msg, users = await get_waiting(chat)
    if msg.startswith("Please") or msg.startswith("No"):
        await event.reply(msg)
        return
    else:
        dn = fail = 0
        err = None
        for i in users:
            try:
                await client(
                    functions.messages.HideChatJoinRequestRequest(
                        chat, user_id=int(i), approved=False
                    )
                )
                dn += 1
            except Exception as e:
                fail += 1
                err = e
        msg = "Disapproved {} user(s).".format(dn)
        if fail != 0:
            msg += "\nFailed to disapprove {} user(s).".format(fail)
            msg += "\n\nLogs Forward this to @Vexana_Support: {}".format(err)
    await event.reply(msg)

  

print("""
┏━━┓      ┏┓              ┏┓    ┏━━┓        ┏━━━┓    ┏┓           
┗┫┣┛      ┃┃              ┃┃    ┗┫┣┛        ┃┏━┓┃    ┃┃           
 ┃┃ ┏━┓ ┏━┛┃┏┓┏┓┏━━┓┏━━┓┏━┛┃     ┃┃ ┏━━┓    ┃┃ ┃┃┏━┓ ┃┃ ┏┓┏━┓ ┏━━┓
 ┃┃ ┃┏┓┓┃┏┓┃┃┃┃┃┃┏━┛┃┏┓┃┃┏┓┃     ┃┃ ┃━━┫    ┃┃ ┃┃┃┏┓┓┃┃ ┣┫┃┏┓┓┃┏┓┃
┏┫┣┓┃┃┃┃┃┗┛┃┃┗┛┃┃┗━┓┃┃━┫┃┗┛┃    ┏┫┣┓┣━━┃    ┃┗━┛┃┃┃┃┃┃┗┓┃┃┃┃┃┃┃┃━┫
┗━━┛┗┛┗┛┗━━┛┗━━┛┗━━┛┗━━┛┗━━┛    ┗━━┛┗━━┛    ┗━━━┛┗┛┗┛┗━┛┗┛┗┛┗┛┗━━┛
Induced Adding Started Sucessfully........
""")
if len(sys.argv) not in (1, 3, 4):
    try:
        client.disconnect()
    except Exception as e:
            pass
else:
    try:
        client.run_until_disconnected()
    except Exception as e:
        pass
