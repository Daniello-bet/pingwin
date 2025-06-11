import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import io
import os

intents = discord.Intents.default()
intents.message_content = True  # <--- to jest wymagane!
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def pingwin(ctx, *, tekst: str):
    obraz = Image.open("pin.png").convert("RGBA")
    draw = ImageDraw.Draw(obraz)
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()
    x, y = 410, 100
    max_width = 210

    def wrap_text(text, font, max_width):
        lines = []
        words = text.split()
        line = ""
        for word in words:
            test_line = f"{line} {word}".strip()
            if draw.textlength(test_line, font=font) <= max_width:
                line = test_line
            else:
                lines.append(line)
                line = word
        lines.append(line)
        return lines

    linie = wrap_text(tekst, font, max_width)

    for i, line in enumerate(linie):
        draw.text((x, y + i * 28), line, font=font, fill="black")

    with io.BytesIO() as buffer:
        obraz.save(buffer, format="PNG")
        buffer.seek(0)
        file = discord.File(fp=buffer, filename="pingwin_z_tekstem.png")
        await ctx.send(file=file)

bot.run(os.getenv("TOKEN"))
