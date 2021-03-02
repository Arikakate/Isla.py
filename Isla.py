from typing import NoReturn
import discord
from discord.ext import commands
import random 
from random import randint, choice
from discord.utils import get
from discord import mentions
from discord.voice_client import VoiceClient




intents = discord.Intents.default()

intents.members = True  
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix = ';')
#######
#EVENTS
#######

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="hentaihaven"))
    print("Bot is live!")

@client.event
async def on_message(message):
    await client.process_commands(message)
    me =  '<@!' + str(767208094525947924) + '>' 
    u = message.guild.get_member(767208094525947924)
    member = '<@' + str(message.author.id) + '>' 
    member_id = message.author.id
    isla_id = '<@!781331025783160833>'

    if message.content == ('.rob %s' % me):
        await message.channel.send('.rob %s' % member_id)
    elif message.content == "%s" % isla_id:
        if member_id == 767208094525947924:
            return
        else:
            await message.channel.send("%s stop mentioning me!" % member)    
    else:
        return

#######
#COMMANDS
#######

###JOIN CALL###
@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

###LEAVE CALL###
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
  
@client.command()
async def nani(ctx):
    await ctx.send("Commands:")
    await ctx.send("joke, ping, cal, ran")
    
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(pass_context=True)
async def cal(ctx, num : int, meth, num2 : int):
    if meth == '*':
        await ctx.send(num * num2)
    elif meth == '/':
        await ctx.send(num / num2)
    elif meth == '+':
        await ctx.send(num + num2)
    elif meth == '-':
        await ctx.send(num - num2)
    elif meth == '^':
        await ctx.send(num ** num2)
    else:
        await ctx.send('i cant do that smh')

@client.command()
async def joke(ctx):
    with open('why.txt') as f:
        lines = [line.rstrip('\n') for line in f]
        jokes = choice(lines)
        await ctx.send(jokes)

@client.command()
async def s(ctx,message):
    if ctx.author.id == 767208094525947924:
        await ctx.send(message)
        await ctx.send(message)
        await ctx.send(message)
        await ctx.send(message)
        await ctx.send(message)
    else:
        await ctx.send("you can't use that bro...sorry❤️")



@client.command(pass_context=True)
async def ran(ctx, num : int or float, num2 : int or float):
    if num < num2:
        if num2 == int or float and num == int or float:
            num1 = random.randint(num, num2)
            await ctx.send(num1)
        elif num2 < num:
            await ctx.send("ur dumb aren't u")
        elif num == num2:
            await ctx.send("ur dumb aren't u")
        else:
            await ctx.send("ur dumb aren't u")
    else:
        await ctx.send("ur dumb aren't u")


@client.command()
async def nice(ctx):
    member_id = '<@!' + str(ctx.author.id) + '>' 
    await ctx.send('%s is the best ❤️!' % member_id)

@client.command()
async def thank(ctx):
    myid = '<@767208094525947924>'
    await ctx.send("thx %s" % myid)

@client.command()
async def b(ctx):
    if ctx.author.id == 767208094525947924:
        await ctx.send(".beg")
    else:
        await ctx.send("you can't use that bro...sorry❤️")

@client.command()
async def week(ctx):
    if ctx.author.id == 767208094525947924:
        await ctx.send(".weekly")
    else:
        await ctx.send("you can't use that bro...sorry❤️")

@client.command()
async def bal(ctx):
    if ctx.author.id == 767208094525947924:
        await ctx.send(".bal")
    else:
        await ctx.send("you can't use that bro...sorry❤️")

@client.command()
async def r(ctx):
    if ctx.author.id == 767208094525947924:
        await ctx.send(".rob 485489103870230528")
    else:
        await ctx.send("you can't use that bro...sorry❤️")

@client.command()
async def n(ctx):
    isla_id = '<@!781331025783160833>'
    await ctx.send("%s" % isla_id)

@client.command()
async def give(ctx):
    if ctx.author.id == 767208094525947924:
        await ctx.send(".give 767208094525947924 1294")
    else:
        await ctx.send("you can't use that bro...sorry❤️")

#######
#PEOPLE
#######

@client.command()
async def ibby(ctx):
    await ctx.send("https://tenor.com/view/fortnite-pro-gif-18473015")

@client.command()
async def subhan(ctx):
    await ctx.send("https://tenor.com/view/special-ralph-the-simpsons-football-gif-5491308")

@client.command()
async def hamza(ctx):
    await ctx.send("https://tenor.com/view/sexy-hot-cooking-crazy-gif-5559513")

@client.command()
async def blapy(ctx):
    await ctx.send("https://tenor.com/view/get-off-valorant-valorant-get-on-valorant-eliwtf-gif-19885317")


@client.command()
async def emad(ctx):
    await ctx.send("https://tenor.com/view/sweaty-sweat-tryhard-minecraft-pvp-coolxd312-gif-18319749")

@client.command()
async def hashir(ctx):
    await ctx.send("https://tenor.com/view/what-blink-big-eyes-stare-glasses-gif-16970879")

@client.command()
async def fahad(ctx):
    await ctx.send("https://tenor.com/view/tacos-which-one-choose-look-unsure-gif-5387595")

@client.command()
async def saad(ctx):
    await ctx.send("https://tenor.com/view/silly-funny-dance-fat-boy-cool-gif-13985203")

@client.command()
async def taheer(ctx):
    await ctx.send("https://tenor.com/view/nav-goat-first-brown-boy-nav-goat-rapper-gif-17552383")

@client.command()
async def ahmed(ctx):
    await ctx.send("https://tenor.com/view/when-ur-friends-aimbot-gif-19868385")

@client.command()
async def usman(ctx):
    await ctx.send("https://tenor.com/view/all-rounder-cricketer-handsome-stoinis-gif-19124479")

@client.command()
async def farhan(ctx):
    await ctx.send("https://tenor.com/view/hotz-hacker-anonymous-mask-gif-16447135")

@client.command()
async def maalik(ctx):
    await ctx.send("https://tenor.com/view/derp-giraffe-baby-giraffe-gif-11032602")

@client.command()
async def atiyeh(ctx):
    await ctx.send("https://tenor.com/view/robbie-rotten-stefan-karl-lazy-town-laugh-hard-le-squeak-gif-12379064")

@client.command()
async def taha(ctx):
    await ctx.send("https://tenor.com/view/woman-of-culture-gif-20099443")

@client.command()
async def fatima(ctx):
    await ctx.send("https://tenor.com/view/robbie-rotten-stefan-karl-lazy-town-laugh-hard-le-squeak-gif-12379064")

@client.command()
async def basim(ctx):
    await ctx.send("https://tenor.com/view/mc-bride-choc-simp-spotted-gif-16386102")

@client.command()
async def rayan(ctx):
    await ctx.send("https://tenor.com/view/smart-thinking-thoughts-think-ponder-gif-7713620")

@client.command()
async def sheikh(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/696097632501760112/816033096163393576/tenor.gif")

@client.command()
async def sarah(ctx):
    await ctx.send("https://tenor.com/view/spongebob-meme-smile-gif-13533313")


@client.command()
async def sex(ctx):
    await ctx.send("before marriage is haraam")

@client.command()
async def pokemon(ctx):
    await ctx.send("gotta catch em all!")

@client.command()
async def anime(ctx):
    await ctx.send("is better than tv shows fr")

@client.command()
async def hentai(ctx):
    await ctx.send("is cool")


client.run('<bot_key>')