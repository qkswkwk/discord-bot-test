from ast import alias
from ssl import CHANNEL_BINDING_TYPES
import discord
from discord.ext import commands
import random
import math

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents = intents)

def set_Embed(title = '', description = ''):
    #embed = discord.Embed(title="메인 제목", description="설명", color=0x62c1cc)
    return discord.Embed(title=title, description=description)

@bot.event #봇 온라인
async def on_ready():
    print('bot login')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name='VALORANT', type=1))

@bot.event #지정되지 않은 명령어를 입력하면 대답
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("명령어를 찾지 못했습니다")

@bot.event
async def on_member_join(member):
    chans=member.guild.text_channels
    msg = "환영합니다"
    await member.send(msg) #개인 DM으로 보내기
    channel = bot.get_channel([i.id for i in chans][0]) #숫자로 채널 지정
    await channel.send(msg) # channel에 보내기

@bot.event
async def on_member_remove(member):
    msg = "잘가요"
    channel = bot.get_channel([i.id for i in chans][0])
    await channel.send(msg)

@bot.command(aliases=['안녕','hi','안녕하세요'])
async def hello(ctx):
    await ctx.reply(f'{ctx.author.mention} 안녕하세요!')
  
@bot.command(aliases=['기분어때'])
async def condition(ctx):
    randonNum = random.randrange(1,3)
    if randonNum == 1:
        await ctx.send("좋음")
    else:
        await ctx.send("나쁨")

@bot.command(aliases=['주사위']) #!roll (숫자) 치면 주사위 굴리기
async def roll(ctx, number:int):
    await ctx.send(f'주사위를 굴려 {random.randint(1,int(number))}이(가) 나왔습니다 (1~{number})')
@roll.error #!roll 명령어 잘못 칠 시 알림
async def roll_error(ctx,error):
    await ctx.send('명령어 오류!')

@bot.command(aliases=['앵무새']) #!repeat (아무말) 치면 따라하기
async def repeat(ctx, *, txt):
    await ctx.send(txt)

@bot.command(aliases=['핑'])
async def ping(ctx):
    await ctx.reply(f'pong! {round(round(bot.latency, 4)*1000)}ms')
  
@bot.command()
async def join(ctx):
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send("<" + str(bot.voice_clients[0].channel) + ">에 들어갑니다.")
    except:
        await ctx.send("음성채널을 찾을 수 없습니다.")
      
@bot.command()
async def leave(ctx):
    await ctx.send("<" + str(bot.voice_clients[0].channel) + ">에서 나갑니다.")
    await bot.voice_clients[0].disconnect()
    
@bot.command(aliases=['사인'])
async def sin(ctx, number:int):
    await ctx.send(f"sin{number} = {round(math.sin(math.radians(number)), 2)}")

@bot.command(aliases=["코사인"])
async def cos(ctx, number:int):
    await ctx.send(f"cos{number} = {round(math.cos(math.radians(number)), 2)}")

@bot.command(aliases=["탄젠트"])
async def tan(ctx, number:int):
    await ctx.send(f"tan{number} = {round(math.tan(math.radians(number)), 2)}")

@bot.command(aliases=["역사인"])
async def asin(ctx, number:float):
    if number<-1 or number>1:
        await ctx.send("구간을 [-1, 1]로 지정해주세요")
    else:
        await ctx.send(f"{number} = sin{int(round(math.degrees(math.asin(number)), 0))}")

@bot.command(aliases=["역코사인"])
async def acos(ctx, number:float):
    if number<-1 or number>1:
        await ctx.send("구간을 [-1, 1]로 지정해주세요")
    else:
        await ctx.send(f"{number} = cos{int(round(math.degrees(math.acos(number)), 0))}")

@bot.command(aliases=["역탄젠트"])
async def atan(ctx, number:int):
    await ctx.send(f"{number} = tan{int(round(math.degrees(math.atan(number)), 0))}")

@bot.command(aliases=['도움말','h'])
async def 도움(ctx):
    embed = discord.Embed(title="bot test", description="반자자짱", color=0x4432a8)
    embed.add_field(name="1. 인사", value="!안녕", inline=False)
    embed.add_field(name="2. 주사위", value="!주사위 [범위숫자]", inline=False)
    embed.add_field(name="3. 앵무새", value="!앵무새 [따라할 말]", inline=False)
    embed.add_field(name="4. 핑 확인", value="!핑", inline=False)
    embed.add_field(name="5. 음성채널 입장/퇴장", value="!join / !leave (초대자가 입장된 상태에만 가능)", inline=False)
    embed.add_field(name="6. 삼각함수 계산", value="!사인, !코사인, !탄젠트, !역사인, !역코사인, !역탄젠트", inline=False)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/420880499704332290/1010172441710051378/d78a5e2c-4cc4-4b22-89d6-9786c7bc2253.jpg")
    embed.set_image(url="https://cdn.discordapp.com/attachments/420880499704332290/1010172441710051378/d78a5e2c-4cc4-4b22-89d6-9786c7bc2253.jpg")
    await ctx.send(embed=embed)

bot.run('token is here')
