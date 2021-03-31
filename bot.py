import discord
import asyncio
import requests
import os
from discord.ext import commands

from PIL import Image
from io import BytesIO

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('A.help'))
    print('Bot is ready you dum dum.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Your Ping is {round(client.latency * 1000)}ms')


@client.command()
async def nuke(ctx, amount = 900):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Channel Nuked!")

    
client.run('ODI2NjA2OTU0NTYyMDYwMzE4.YGO7tw.AM33L5m66i4sPLO_MLvKGUSmtps')
