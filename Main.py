import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '?')

clear = lambda: os.system('cls')

@client.event
async def on_ready():
    clear()
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Meatball v0.1'))
    logo = open('logo.txt', 'r').read()
    print(logo)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Hoom")
    await discord.Member.add_roles(member, role)


@client.command(aliases = ['kick'])
@commands.has_permissions(administrator = True)
async def _kick(ctx, member: discord.Member, *, MsgReason):
    await ctx.send(f"Kicked {member}, reason {MsgReason}")
    channel = await member.create_dm()
    await channel.send(f"You have been kicked, reason {MsgReason}")
    await channel.send('https://media.discordapp.net/attachments/758256181415641088/760489357164806204/IMG-20200929-WA0000.jpg?width=619&height=350')
    await member.kick(reason = None)

client.run('NzA3NTcxMDQwMzg1MTA2MDMw.XrKu4g.QYyPtpyvIfHMIRvu1NehF1cBazk')