import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '?') #Bot prefix

clear = lambda: os.system('cls')

@client.event
async def on_ready():
    clear()
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Meatball v0.1'))
    logo = open('logo.txt', 'r').read()
    print(logo)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name = "") #Auto rank rank name
    await discord.Member.add_roles(member, role)


@client.command(aliases = ['kick'])
@commands.has_permissions(administrator = True)
async def _kick(ctx, member: discord.Member, *, MsgReason):
    await ctx.send(f"Kicked {member}, reason {MsgReason}")
    await member.kick(reason = None)
    channel = await member.create_dm()
    await channel.send(f"You have been kicked, reason {MsgReason}")

@client.command(aliases = ['ban'])
@commands.has_permissions(administrator = True)
async def _ban(ctx, member: discord.Member, *, MsgBReason):
    await ctx.send(f"Banned {member}, reason {MsgBReason}")
    await member.ban(reason = None)
    channel = await member.create_dm()
    await channel.send(f"You have been banned, reason {MsgBReason}")

client.run('')
