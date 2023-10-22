import discord
from discord.ui import View


class PomodoroMenu(View):
    def __init__(self):
        super().__init__()
        self.value = None


    @discord.ui.button(label="5", style=discord.ButtonStyle.grey)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"You are now in **FOCUS**! Enjoy your progress, **BREAK** starts in {button.label} mins")
        self.value = 5
        self.stop()

    @discord.ui.button(label="25", style=discord.ButtonStyle.grey)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"You are now in **FOCUS**! Enjoy your progress, **BREAK** starts in {button.label} mins")
        self.value = 25
        self.stop()


    @discord.ui.button(label="50", style=discord.ButtonStyle.grey)
    async def menu3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"You are now in **FOCUS**! Enjoy your progress, **BREAK** starts in {button.label} mins")
        self.value = 50
        self.stop()


    @discord.ui.button(label="60", style=discord.ButtonStyle.grey)
    async def menu4(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"You are now in **FOCUS**! Enjoy your progress, **BREAK** starts in {button.label} mins")
        self.value = 60
        self.stop()


    @discord.ui.button(label="75", style=discord.ButtonStyle.grey)
    async def menu5(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"You are now in **FOCUS**! Enjoy your progress, **BREAK** starts in {button.label} mins")
        self.value = 75
        self.stop()


    @discord.ui.button(label="100", style=discord.ButtonStyle.grey)
    async def menu6(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"You are now in **FOCUS**! Enjoy your progress, **BREAK** starts in {button.label} mins")
        self.value = 100
        self.stop()


    @discord.ui.button(label="180", style=discord.ButtonStyle.grey)
    async def menu7(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"You are now in **FOCUS**! Enjoy your progress, **BREAK** starts in {button.label} mins")
        self.value = 180
        self.stop()
