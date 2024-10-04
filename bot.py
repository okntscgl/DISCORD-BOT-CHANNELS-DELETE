import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= "!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("I'm ready")

@bot.command
@commands.has_permissions(administrator=True)
async def delete_channels(ctx):

    if not ctx.guild.channels:
        await ctx.send("No channels to delete.")
        return

    await ctx.send(f"{len(ctx.guild.channels)} channels are being deleted...")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            await ctx.send(f"{channel.name} channel has been deleted.")
        except Exception as e:
            await ctx.send(f"Could not delete the {channel.name} channel: {e}")


@bot.command
@commands.has_permissions(administrator=True)
async def create_role(ctx, role_name: str):

    if role_name in [role.name for role in ctx.guild.roles]:
        await ctx.send(f"The role {role_name} already exists.")
        return

    try:
        new_role = await ctx.guild.create_role(name=role_name)
        await ctx.send(f"The role {new_role.name} has been created.")
    except Exception as e:
        await ctx.send(f"An error occurred while creating the role: {e}")


@bot.command
@commands.has_permissions(administrator=True)
async def change_server_name(ctx, *, new_name: str):

    if new_name == ctx.guild.name:
        await ctx.send("The server name is already this.")
        return

    try:
        await ctx.guild.edit(name=new_name)
        await ctx.send(f"The server name has been changed to {new_name}.")
    except Exception as e:
        await ctx.send(f"The server name could not be changed: {e}")


bot.run("YOUR_TOKEN_HERE")