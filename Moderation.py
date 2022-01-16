import nextcord 
from nextcord.ext import commands 

class Moderation(commands.Cog):

   def __init__(self, client):
       self.client = client

   @commands.command(description="Bans a member")
   @commands.has_permissions(ban_members=True)
   async def ban(self, ctx, member: nextcord.Member, *, reason=None):
      await member.ban(reason=reason)
      await ctx.send(f"{member} was banned!")

   @commands.command()
   @commands.has_permissions(kick_members=True)
   async def kick(self, ctx, member: nextcord.Member, *, reason=None):
       if member == ctx.author:
           await ctx.send("You cannot Kick yourself!")
       else:
           kickEmbed = nextcord.Embed(title="Kicked", description=f"{member} was kicked for {reason}", color=nextcord.Color.red())
           await member.kick(reason=reason)
           await ctx.send(embed=kickEmbed)

   @commands.command(description="Unbans a member")
   @commands.has_permissions(ban_members=True)
   async def unban(self, ctx, *, member):
      bannedUsers = await ctx.guild.bans()
      name, discriminator = member.split("#")

      for ban in bannedUsers:
          user = ban.user

          if(user.name, user.discriminator) == (name, discriminator):
             await ctx.guild.unban(user)
             await ctx.send(f"{user.mention} was unbanned.")
             return

   @commands.command()
   async def changelog(self,ctx):
      #You don't need to have this command
      changelogEmbed=nextcord.Embed(title="Changelog for NAME OF YOUR BOT")
      changelogEmbed.add_field(name="Date for the changelog goes here", value="Any changes with your bot go here", inline=True)
      await ctx.send(embed=changelogEmbed)

   @commands.command()
   async def warn(self,ctx,member : nextcord.Member, *, reason=None):
      if member == ctx.author:
         await ctx.send("You cannot warn yourself.")
      else:
          warnEmbed = nextcord.Embed(title="Warned", description=f"{member} was warned because {reason}", color=nextcord.Color.red())
          warnEmbed2 = nextcord.Embed(title="Warned", description=f"You have been warned because {reason}", color=nextcord.Color.red())
          await member.send(embed=warnEmbed2)
          await ctx.send(embed=warnEmbed)

   @commands.command()
   @commands.guild_only()
   @commands.has_permissions(manage_messages=True)
   async def clear(self, ctx, amount = 0):
      await ctx.channel.purge(limit=amount + 1)
      await ctx.send(f'Deleted {amount} message(s)')

   @commands.command(aliases=["nick"])
   @commands.guild_only()
   @commands.has_permissions(manage_nicknames=True)
   async def nickname(self, ctx, member: nextcord.Member, *, name: str = None):
      await member.edit(nick=name)
      message = f"Changed {member.mention}'s nickname to **{name}**"
      if name is None:
         message = f"Reset {member.mention}'s nickname"
      await ctx.reply(message)

def setup(client):
    client.add_cog(Moderation(client))
