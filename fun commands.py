import nextcord 
import random
from nextcord.ext import commands 

class Fun_commands(commands.Cog):

   def __init__(self, client):
       self.client = client

   @commands.command(aliases=["howhot", "hot"])
   async def hotcalc(self, ctx, *, user: nextcord.Member = None):
       """ Returns a random percent for how hot is a discord user """
       user = user or ctx.author

       random.seed(user.id)
       r = random.randint(1, 100)
       hot = r / 1.17

       if hot > 75:
          emoji = "💞"
       elif hot > 50:
            emoji = "💖"
       elif hot > 25:
            emoji = "❤"
       else:
            emoji = "💔"

       await ctx.send(f"**{user.name}** is **{hot:.2f}%** hot {emoji}")

     
   @commands.command(aliases=["slots", "bet"])
   @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
   async def slot(self, ctx):
      """ Roll the slot machine """
      emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
      a = random.choice(emojis)
      b = random.choice(emojis)
      c = random.choice(emojis)

      slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

      if (a == b == c):
          await ctx.send(f"{slotmachine} All matching, you won! 🎉")
      elif (a == b) or (a == c) or (b == c):
          await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
      else:
          await ctx.send(f"{slotmachine} No match, you lost 😢")

   @commands.command(aliases=["flip", "coin"])
   async def coinflip(self, ctx):
      """ Coinflip! """
      coinsides = ["Heads", "Tails"]
      await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")

   @commands.command()
   async def diceroll(self, ctx):
      dicesides = ["1", "2", "3", "4", "5", "6"]
      await ctx.send(f"**{ctx.author.name}** rolled a dice and got **{random.choice(dicesides)}**!")

def setup(client):
    client.add_cog(Fun_commands(client))
