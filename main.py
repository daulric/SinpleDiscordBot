import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

#Bot Config
Prefix = "!"
bot = commands.Bot(command_prefix=Prefix)
Token = os.environ['Token'] #Paste Your Token in Repl.it Secrets

#Few Commands
@bot.command()
async def test(ctx):
  await ctx.send("We are Online!")

@bot.command()
async def on_message(message):
  if message.content.startswith('Ulric'):
    await message.send("Ulric is Helping Here")

keep_alive()
bot.run(Token)