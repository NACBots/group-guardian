from pyrogram import Client,filters
import requests
import re
import config 

url = "https://api.safone.me/nsfw"
slangf = 'slang_words.txt'
with open(slangf, 'r') as f:
    slang_words = set(line.strip().lower() for line in f)

Bot = Client(
    "antinude",
    bot_token=config.BOT_TOKEN,
    api_id=config.API_ID,
    api_hash=config.API_HASH
)

#-----------------------------------------------------------------

@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    await update.reply("""Hi there! I'm the Telegram Group Guardian bot. I'm here to help you keep your group clean and safe for everyone. Here are the main features I offer:

• **Word Slagging:** I can detect and remove inappropriate language messages in your group. 

• **Image Filtering:** I can also automatically detect and remove pornographic or NSFW images in your group. 

To get started, simply add me to your Telegram group and promote me to admin 

Thanks for using Telegram Group Guardian! Let's keep your group safe and respectful. Powered by @NACBOTS""")

#-----------------------------------------------------------------

@Bot.on_message(filters.group & filters.photo)
async def image(bot, message):
    sender = await Bot.get_chat_member(message.chat.id, message.from_user.id)
    isadmin = sender.privileges
    if not isadmin:
        x = await message.download()
        files = {"image": open(x, "rb")}
        roi = requests.post(url, files=files)
        data = roi.json()
        nsfw = data["data"]["is_nsfw"]
        porn = data["data"]["porn"]
        if nsfw:
            name = message.from_user.first_name
            await message.delete()
            await message.reply_photo(x, caption=f"""**WARNING ⚠️** (nude photo)

 **{name}** sent a nude photo

{porn}% porn""", has_spoiler = True)


#-----------------------------------------------------------------

@Bot.on_message(filters.group & filters.text)
async def slang(bot, message):
    sender = await Bot.get_chat_member(message.chat.id, message.from_user.id)
    isadmin = sender.privileges
    if not isadmin:
        sentence = message.text
        sent = re.sub(r'\W+', ' ', sentence)
        isslang = False
        for word in sent.split():
            if word.lower() in slang_words:
                isslang = True
                await message.delete()
                sentence = sentence.replace(word, f'||{word}||')
        if isslang:
            name = message.from_user.first_name
            msgtxt = f"""{name} your message has been deleted due to the presence of inappropriate language. Here is a censored version of your message:
            
{sentence}
            """
            await message.reply(msgtxt)

#--------------------------------------------------------------------------------------------------

Bot.run()
