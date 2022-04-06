import discord
import random
import time
import asyncio

from discord import channel
from discord.utils import get

# Make bot say controversial things from a list - Done
# Make Bot tell Everyone to stop being horny -WIP
# React to based comments - Done
# Make bot do Vide checks - Done
# Make bot post cursed motivational images
# recite weightlifters prayer - Done
# 8ball - Done
# Gamer Chant - Done
# (maybe) @ people active in the last 14 days.
# set custom status

Controversy = [
    "Dark Souls 2 is better than Dark Souls 1",
    "30 year olds that still play Nintendo games are closeted pedophiles",
    "Far Cry 3 is not that great",
    "Epic Games Store is not that terrible",
    "Nintendo is the Disney of gaming",
    "Fallout 4 handles the sentient android debate better than Detroit: Become Human",
    "COD Vanguard is not that bad of a COD",
    "Cyberpunk was a good game that got fucked by the investors, not the developers",

]

ball = [
    "Yes",
    "Hit maxes, Evade taxes",
    "Yes, according to myself (I know everything)",
    "perhaps",
    "Find out yourself",
    "No",
    "My lawyer (me) advised me to not answer that question",
    "At the gym, try again",
    "Sorry king, I can't tell you that right now",
    "I can't read the future",
    "That's a no from me",
    "I've never been more doubtful",
]

based = [
    "Your mom",
    "It came to me in a dream",
    "based on FBI crimes statistics",
]

Vibe = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"

]
TOKEN = "OTYwMjgzMzU3OTQwNDI4ODAw.YkoLkQ.5S7eq2b04JcZjy2-1zr1QYLCM6E"

client = discord.Client()


# This is what makes the bot react to BASED
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("based"):
        await message.channel.send("VERY based")

    if message.content.startswith(".Controversy"):
        await message.channel.send(random.choice(Controversy))

    if message.content.startswith(".Chant"):
        await message.channel.send("Scooters, are not motorcycles\n"
                                   "Women, are not people\n"
                                   "These, are facts\n"
                                   "We, are gamers\n"
                                   "Rise Up!")

    if message.content.startswith(".8ball"):
        await message.channel.send(random.choice(ball))

    if message.content.startswith(".Pray"):
        await message.channel.send("Our gains. Who art in Lifting.\n"
                                   "Hallowed be thy veins.\n"
                                   "Thy gains will come.\n"
                                   "Thy will be done on leg day as it is on Chest\n"
                                   "Give us this day our daily macros abd forgive our cheat meals.\n"
                                   "AS we forgive those who have great genetics.\n"
                                   "Lead us not into cardio,\n"
                                   "But deliver us form curling in the squat rack.\n"
                                   "Wheymen\n"
                                   "The Gospel According to Masshew 6:9-13")

    if message.content.startswith(".Vibe"):
        await message.channel.send("Let me check your vibe, king")
        msg1 = await message.channel.send(random.choice(Vibe))
        x = int(msg1.content)
        y = 5
        if x < y:
            await message.channel.send("Shit vibe")
        if x > y:
            await message.channel.send("Vibe check passed")

    if message.content.startswith(".Help"):
        embed = discord.Embed(title="__Commands__", color=0x992d22)
        embed.add_field(name=".help", value="Shows this message")
        embed.add_field(name=".Controversy", value="Causes Controversy")
        embed.add_field(name=".Chant", value="Recites the Gamer Chant")
        embed.add_field(name=".8ball", value="8ball")
        embed.add_field(name=".Pray", value="Recites the Weightlifters prayer")
        embed.add_field(name=".Vibe", value="Checks a persons vibe")
        await message.channel.send(content=None, embed=embed)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(".Help for commands"))
    print("RUNNING")


client.run(TOKEN)
