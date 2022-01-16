from operator import truediv
import nextcord 
import os
from nextcord.ext import commands

Intents = nextcord.Intents.all()

client = commands.Bot(command_prefix = "!", Intents=Intents)
client.remove_command("help")


@client.event
async def on_ready():
    await client.change_presence(status=nextcord.Status.online, activity=nextcord.Game('!'))
    print('Celia bot is ready')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def help(ctx):
    user = ctx.author

    embed=nextcord.Embed(title="Help", color=user.color)
    embed.add_field(name="Moderation", value="Bring up info yourself", inline=True)
    embed.add_field(name="Information", value="Bring up info on the server", inline=True)
    embed.add_field(name="Fun and Misc", value="Bring up info on the server", inline=True)
    embed.add_field(name="Links", value='[Support server](https://discord.gg/dKBgKYUw)\
        [Click here to invite me!](https://discord.com/api/oauth2/authorize?client_id=931664099232845854&permissions=1635782753526&scope=applications.commands%20bot)', inline=True)
    
    await ctx.message.delete()
    await ctx.author.send(embed=embed)

@client.command()
async def userinfo(ctx, *, user: nextcord.Member = None):
    user = user or ctx.author

    embed=nextcord.Embed(title="Userinfo", description=f"Here is the info i retrieved about {user.mention}", color=user.color)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="Nickname", value=user.nick, inline=True)
    embed.add_field(name="Id", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Top role", value=user.top_role.name, inline=True)
    await ctx.send(embed=embed)

@client.command()
async def serverinfo(ctx):
    role_count = len(ctx.guild.roles)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
    user = ctx.author

    serverinfoEmbed=nextcord.Embed(title="Server Info", color=user.color)
    serverinfoEmbed.add_field(name="Name", value=f"{ctx.guild.name}", inline=True)
    serverinfoEmbed.add_field(name="Member Count", value=ctx.guild.member_count, inline=True)
    serverinfoEmbed.add_field(name="Highest Role", value=ctx.guild.roles[-2], inline=True)
    serverinfoEmbed.add_field(name="Number Of Roles", value=str(role_count), inline=True)
    serverinfoEmbed.add_field(name="Bots", value=','.join(list_of_bots), inline=True)

    await ctx.send(embed=serverinfoEmbed)




client.run("Your token Goes Here")
