import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    bot = commands.Bot(command_prefix='/', intents=intents)


    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')
        try:
            synced = await bot.tree.sync()
        except Exception as e:
            print(e)


    @bot.tree.command(name="dm", description="Send me a DM hohoho!")
    async def dm(interaction: discord.Interaction):
        channel = await interaction.user.create_dm()
        await channel.send("Here is a dm!!")
        await interaction.response.send_message("A dm has been sent.", ephemeral=True)


    @bot.tree.command(name="help", description="See a brief summary of commands in BearBot.")
    async def help(interaction: discord.Interaction):
        await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command", ephemeral=True)


    @bot.tree.command(name="pomodoro", description="Start a pomodoro timer.")
    @app_commands.describe(start_timer="Starts a Pomodoro timer!")
    async def pomodoro(interaction: discord.Interaction, start_timer: str):
        await interaction.response.send_message(f"You're in **FOCUS** now, enjoy your progress! **BREAK** starts in {start_timer} min(s)")


    bot.run(TOKEN)