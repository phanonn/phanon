import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents = nextcord.Intents().all()
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready!")

logging = True
logschannel = (channel_id)

@bot.slash_command()
async def kick(interaction: nextcord.Interaction, user: nextcord.Member, reason: str):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("lol nt loser not happening.", ephemeral=True)
    else:
        await interaction.response.send_message(f"kicked {user.mention}", ephemeral=True) 
        if logging is True: 
            log_channel = bot.get_channel(channel_id)
            await log_channel.send(f"{user.mention} *was kicked by {interaction.user.mention} for* *{reason}*")
        await user.kick(reason=reason) 

@bot.slash_command()
async def ban(interaction: nextcord.Interaction, user: nextcord.Member, reason: str):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("lol nt loser not happening.", ephemeral=True)
    else:
        await interaction.response.send_message(f"banned {user.mention}", ephemeral=True) 
        if logging is True: 
            log_channel = bot.get_channel(channel_id)
            await log_channel.send(f"{user.mention} *was banned by {interaction.user.mention} for* *{reason}*")
        await user.ban(reason=reason)            

@bot.slash_command()
async def unban(interaction: nextcord.Interaction, user: nextcord.Member):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("lol nt loser not happening.", ephemeral=True)
    else:
        await interaction.response.send_message(f"unbanned {user.mention}", ephemeral=True) 
        if logging is True: 
            log_channel = bot.get_channel(channel_id)
            await log_channel.send(f"{user.mention} *was unbanned by {interaction.user.mention}")
        await interaction.guild.unban(user)
        
bot.run("insert_discord_bot_token")
