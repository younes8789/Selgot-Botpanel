import discord
from discord.ext import commands
from discord.ui import Button, View

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)

class TicketView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="BUY PANEL", style=discord.ButtonStyle.success, emoji="🛒")
    async def buy_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel_id = 1456686042680660100
        await interaction.response.send_message(f"🎫 **Open your ticket here:** <#{1456686042680660100}>", ephemeral=True)

@bot.command()
async def panel(ctx):
    embed = discord.Embed(
        title="ꜱᴇʟɢᴏᴛ xɪᴛᴇʀ ! | ᴘʀᴇᴍɪᴜᴍ ᴘᴀɴᴇʟ <:emoji_12:1469842267618672713>", 
        color=0xFF0000 
    )
    
    # الفكرة الجديدة: Software Status (Glow Blue)
    status = (
        "```md\n"
        "# Status   : Working / Undetected\n"
        "# Version  : v4.2 [Latest]\n"
        "# Security : Anti-Cheat Bypass Active\n"
        "```"
    )
    embed.add_field(name=" System Status <:emoji_6:1469842172315439215>", value=status, inline=False)
    
    # قسم المميزات (Clean Text)
    functions = (
        "```text\n"
        "╰┈➤ ᴀʟʟ ᴄʜᴀᴍꜱ\n"
        "╰┈➤ ᴀʟʟ ᴇꜱᴘ\n"
        "╰┈➤ ꜱɪʟᴇɴᴛ ᴀɪᴍ\n"
        "╰┈➤ ʀᴀɢᴇ ᴀɪᴍ\n"
        "╰┈➤ ᴘᴜʟʟ ᴇɴᴇᴍʏ\n"
        "╰┈➤ ᴡᴀʟʟʜᴀᴄᴋ\n"
        "╰┈➤ ꜱᴘᴇᴇᴅ\n"
        "╰┈➤ ᴛᴇʟᴇᴘᴏʀᴛ\n"
        "╰┈➤ ɴᴏ ʀᴇᴄᴏɪʟ\n"
        "╰┈➤ ꜰᴀꜱᴛ ꜰɪʀᴇ\n"  # زدناها هنا مورا No Recoil
        "╰┈➤ ᴀɪᴍʙᴏᴛ ʙᴏᴅʏ\n"
        "╰┈➤ ᴀɴᴅ ᴍᴏʀᴇ ꜰᴜɴᴄᴛɪᴏɴꜱ....\n"
        "```"
    )
    embed.add_field(name="──────────────────────────────", value=f"**Functions :**\n{functions}", inline=False)
    
    # قسم الأثمنة (Glow Green)
    prices = (
        "```diff\n"
        "+ 1 Day      : 1.00$ USD\n"
        "+ 7 Days     : 4.00$ USD\n"
        "+ 15 Days    : 7.00$ USD\n"
        "+ 1 Month    : 15.00$ USD\n"
        "+ Lifetime   : 40.00$ USD\n"
        "```"
    )
    embed.add_field(name="Price :", value=f"{prices}───────────@everyone────────────", inline=False)

    gif_url = "https://cdn.discordapp.com/attachments/1456772931702100091/1472775879502594293/giphy_2.gif?ex=6993ccec&is=69927b6c&hm=67e4dc0b7926ce799046d4e336bc90738978fe8e602ee5c33e080ca9ebae033d&" 
    embed.set_image(url=gif_url)
    embed.set_footer(text="Selgot Offciel License System • Secured by Selgot")
    
    await ctx.send(embed=embed, view=TicketView())

bot.run('MTQ3Mjc1NDk4MjE2MzA1NDcyNQ.Gg98e3.g8wvsYu4Fa20kTWKFAmK_Edv1Wxib88rGN5VTQ')