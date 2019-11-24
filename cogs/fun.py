import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import Bot


class Cmd(commands.Cog, name="Cmd"):
    def __init__(self, bot):
        self.bot = bot
        with open('gifs/hug.txt') as f:
            self.choices_hug = f.readlines()
        with open('gifs/kiss.txt') as f:
            self.choices_kiss = f.readlines()
        with open('gifs/pat.txt') as f:
            self.choices_pat = f.readlines()
        with open('gifs/slap.txt') as f:
            self.choices_slap = f.readlines()
        with open('gifs/error.txt') as f:
            self.choices_error = f.readlines()
        with open('gifs/yui.txt') as f:
            self.choices_yui = f.readlines()

    @commands.command()
    async def yui(self, ctx):
        author = ctx.message.author.mention
        image = random.choice(self.choices_yui)
        embed = discord.Embed(
            description="***{0} Here's a pic of yui!***".format(author),
            colour=discord.Colour.blue()
        )
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        author = ctx.message.author.mention
        mention = member.mention

        if author == mention:
            image = random.choice(self.choices_error)
            embed = discord.Embed(
                description="***{0} you can't hug yourself***".format(author),
                colour=discord.Colour.blue()
            )
            embed.set_image(url=image)
            await ctx.send(embed=embed)
        elif author == author:
            hug = "***{0} gave {1} a hug!***"
            image = random.choice(self.choices_hug)
            embed = discord.Embed(
                description=hug.format(author, mention),
                colour=discord.Colour.blue()
            )
            embed.set_image(url=image)
            await ctx.send(embed=embed)

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            author = ctx.message.author.mention
            hug = "***{0} You have to hug someone!***"
            image = random.choice(self.choices_error)
            embed = discord.Embed(
                description=hug.format(author),
                colour=discord.Colour.blue()
            )
            embed.set_image(url=image)
            await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, member: discord.Member):
        author = ctx.message.author.mention
        mention = member.mention
        if author == mention:
            image = random.choice(self.choices_error)
            embed = discord.Embed(
                description="***{0} you can't kiss yourself***".format(author),
                colour=discord.Colour.blue()
            )
            embed.set_image(url=image)
            await ctx.send(embed=embed)
        elif author == author:
            kiss = "***{0} gave {1} a kiss!***"
            image = random.choice(self.choices_kiss)
            embed = discord.Embed(
                description=kiss.format(author, mention),
                colour=discord.Colour.blue()
            )
            embed.set_image(url=image)
            await ctx.send(embed=embed)

    @kiss.error
    async def kiss_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            author = ctx.message.author.mention
            kiss = "***{0} You have to kiss someone!***"
            image = random.choice(self.choices_error)
            embed = discord.Embed(
                description=kiss.format(author),
                colour=discord.Colour.blue()
            )
            embed.set_image(url=image)
            await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx, member: discord.Member):
        author = ctx.message.author.mention
        mention = member.mention
        if author == mention:
            image = random.choice(self.choices_error)
            embed = discord.Embed(
                description="***{0} you can't pat yourself***".format(author),
                colour=discord.Colour.blue()
            )
            embed.set_image(url=image)
            await ctx.send(embed=embed)
        elif author == author:
            kiss = "***{0} patted {1}!***"
            image = random.choice(self.choices_pat)
            embed = discord.Embed(
                description=kiss.format(author, mention),
                colour=discord.Colour.blue()
            )
            embed.set_image(url=image)
            await ctx.send(embed=embed)

    @pat.error
    async def pat_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            author = ctx.message.author.mention
            pat = "***{0} You have to pat someone!***"
            image = random.choice(self.choices_error)
            embed = discord.Embed(
                description=pat.format(author),
                colour=discord.Colour.blue()
            )
            embed.set_image(url=image)
            await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, member: discord.Member):
        author = ctx.message.author.mention
        mention = member.mention
        if author == mention:
            image = random.choice(self.choices_error)
            embed = discord.Embed(
                description="***{0} you can't slap yourself***".format(author),
                colour=discord.Colour.blue()
            )
            embed.set_image(url=image)
            await ctx.send(embed=embed)
        elif author == author:
            slap = "***{0} patted {1}!***"
            image = random.choice(self.choices_slap)
            embed = discord.Embed(
                description=slap.format(author, mention),
                colour=discord.Colour.blue()
            )
            embed.set_image(url=image)
            await ctx.send(embed=embed)

    @slap.error
    async def slap_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            author = ctx.message.author.mention
            pat = "***{0} You have to slap someone!***"
            image = random.choice(self.choices_error)
            embed = discord.Embed(
                description=pat.format(author),
                colour=discord.Colour.blue()
            )
            embed.set_image(url=image)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Cmd(bot))
