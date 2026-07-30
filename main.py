import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'⚡ บอท {bot.user} พร้อมล้างและสร้าง 10 ช่องแล้ว!')

@bot.command()
@commands.is_owner()
async def build(ctx):
    guild = ctx.guild
    
    await ctx.send("🚨 **กำลังลบห้องเก่าและสร้าง 10 ช่องพูดคุยใหม่ใน 3 วินาที...**")
    await asyncio.sleep(3)

    # 1. ลบช่องเดิมทั้งหมดที่มีอยู่
    for channel in guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            print(f"ไม่สามารถลบ {channel.name} ได้: {e}")

    # 2. สร้างหมวดหมู่ที่ 1: ข้อความ (5 ช่อง)
    cat_text = await guild.create_category("ข้อความ")
    await guild.create_text_channel("ข่าวสาร-ประกาศ", category=cat_text)  # ช่องที่ 1
    await guild.create_text_channel("พูดคุยทั่วไป", category=cat_text)    # ช่องที่ 2
    await guild.create_text_channel("คำสั่งบอท", category=cat_text)      # ช่องที่ 3
    await guild.create_text_channel("แชร์รูปภาพ-คลิป", category=cat_text)  # ช่องที่ 4
    await guild.create_text_channel("พิมพ์คำถาม-ช่วยตอบ", category=cat_text) # ช่องที่ 5

    # 3. สร้างหมวดหมู่ที่ 2: พูดคุยเสียง (5 ช่อง)
    cat_voice = await guild.create_category("พูดคุยเสียง")
    await guild.create_voice_channel("ห้องพูดคุย 1", category=cat_voice) # ช่องที่ 6
    await guild.create_voice_channel("ห้องพูดคุย 2", category=cat_voice) # ช่องที่ 7
    await guild.create_voice_channel("ห้องพูดคุย 3", category=cat_voice) # ช่องที่ 8
    await guild.create_voice_channel("ฟังเพลง-นั่งชิล", category=cat_voice) # ช่องที่ 9
    await guild.create_voice_channel("ห้องพัก-AFK", category=cat_voice)   # ช่องที่ 10

    print("สร้างครบ 10 ช่องเรียบร้อยแล้ว!")

TOKEN = 'ใส่_TOKEN_ของคุณตรงนี้'
bot.run(TOKEN)
