import keep_alive
import os
import Bot

client = Bot.MyClient()

#keeps the bot running on the server
keep_alive.keep_alive()

try:
    client.run(os.environ['token'])
except:
    keep_alive.kill()
    exit(1)
