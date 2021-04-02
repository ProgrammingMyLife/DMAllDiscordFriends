import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send(open("message.txt", "r"))
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.friends}")
        
if __name__ == "__main__": # Because this is an async function we need to use if __name == "__main__"
  client.run(open("token.txt", "r").readline(), bot=False)

