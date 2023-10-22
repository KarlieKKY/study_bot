import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv
from pomodoro.pomodoro_menu import *
from pomodoro.pomodoro_timer import *

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
    @app_commands.describe(start_dm="Start a direct message!")
    async def dm(interaction: discord.Interaction, start_dm: str):
        channel = await interaction.user.create_dm()
        await channel.send("Here is a dm!!")
        await interaction.response.send_message("A dm has been sent.", ephemeral=True)


    @bot.tree.command(name="help", description="See a brief summary of commands in BearBot.")
    async def help(interaction: discord.Interaction):
        await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command", ephemeral=True)


    @bot.tree.command(name="pomodoro", description="Start a pomodoro timer.")
    async def pomodoro(interaction: discord.Interaction):
        view = PomodoroMenu()
        await interaction.response.send_message(f"How long you want to keep focus? **CHOOSE** one below", view=view)
        await view.wait()

        valid_values = [5, 25, 50, 60, 75, 100, 180]

        if view.value in valid_values:
            print(view.value)
            timer = PomodoroTimer(view.value)
            timer.start()
            while timer.get_status():
                timer.inc_second()
                if timer.get_seconds() >= timer.max_seconds:
                    timer.stop()
            



    bot.run(TOKEN)