# Group Guardian
<img src="https://te.legra.ph/file/d96c5ab85f759efae0c26.jpg">
Group Guardian is an open source Telegram bot designed to help group administrators maintain a clean and safe environment for their communities. The bot offers two main functionalities:

- **Word Slagging:** With the word slagging feature, the bot can detect and remove inappropriate language or spam messages in a group.You can define a list of banned words or phrases in [slang words file](slang_words.txt), and the bot will automatically delete any message containing them.

- **Image Filtering:** The bot also includes an image filtering feature that can automatically detect and remove pornographic or NSFW images in a group and sent a censored version of the image. 

## Getting Started

To use Group Guardianship, simply add the bot to your Telegram group and promote to admin.If anyone sends a message containing offensive language or an NSFW image, the bot will automatically delete the message and send a censored version of it instead.


## Required Configs
 - `BOT_TOKEN` - Get from [@BotFather](https://t.me/BotFather)
 - `API_ID` - Get it from [telegram.org](https://my.telegram.org/auth)
 - `API_HASH` - Get it from [telegram.org](https://my.telegram.org/auth)

## Deploy 🚀

### Easiest Heroku Deploy 🤭

<p align="center">
    <a href="https://heroku.com/deploy?template=https://github.com/nacbots/group-guardian">
    <img src="https://github.com/nacbots/broadcastbot/blob/main/herokudeploy-01.svg" alt="herokudeploy-01" border="0" height="90" width="285"></a>
</p>

### Host Locally 🤕

1. Clone this repository to your local machine using:

    ```
    git clone https://github.com/nacbots/group-guardian
    ```

2. Install the required dependencies using pip:

    ```
    cd group-guardian
    pip install -r requirements.txt
    ```

3. Create a new bot in Telegram and get your API token (you can follow the instructions [here](https://core.telegram.org/bots#creating-a-new-bot)).

4. Configure the bot's settings by editing the `config.py` file. 

5. Start the bot by running:

    ```
    python3 main.py
    ```

6. Add the bot to your Telegram group and enjoy a clean and safe environment!

## Support Group:

<a href="https://t.me/NACBots"><img src="https://img.shields.io/badge/Telegram-Updates%20Channel-blue.svg?logo=telegram"></a><a href="https://t.me/n_a_c_bot_developers"><img src="https://img.shields.io/badge/Telegram-Support%20Group-blue.svg?logo=telegram"></a>

## Contributors

 - [@NikhilEashy](https://github.com/nikhileashy)

 - [@Muhsina-km](https://github.com/muhsina-km)

<a href="https://pyrogram.org"><img src="https://i.ibb.co/SVLD5k8/Document-1222546317.png" alt="pyrogram" border="0"></a>

## Contributing

If you find a bug or have a suggestion for a new feature, please open an issue on this repository or submit a pull request. We welcome contributions from the community!
