from ssl import CHANNEL_BINDING_TYPES
import discord
from discord.ext import commands
import random

intents = discord.Intents.all()
intents.members = True
game = discord.Game("방구뿡뿡띠") #봇 상태 지정
bot = commands.Bot(command_prefix='!', intents = intents)
 
@bot.event #봇 온라인
async def on_ready():
    print('Done')
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event #지정되지 않은 명령어를 입력하면 대답
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("명령어를 찾지 못했습니다")

@bot.event
async def on_member_join(member):
    chans=member.guild.text_channels
    msg = "ㅎㅇ ㅋㅋ 님머임"
    await member.send(msg) #개인 DM으로 보내기
    channel = bot.get_channel([i.id for i in chans][0]) #숫자로 채널 지정
    await channel.send(msg) # channel에 보내기

@bot.event
async def on_member_remove(member):
    msg = "바보간다 ㅋㅋ"
    channel = bot.get_channel([i.id for i in chans][0])
    await channel.send(msg)

@bot.command(aliases=['안녕','hi','안녕하세요']) #!hello 치면 대답
async def hello(ctx):
    await ctx.reply(f'{ctx.author.mention} Hello I am Bot!')

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

@bot.command(aliases=['도움말','h'])
async def 도움(ctx):
    embed = discord.Embed(title="bot test", description="반자자짱", color=0x4432a8)
    embed.add_field(name="1. 인사", value="!안녕", inline=False)
    embed.add_field(name="2. 주사위", value="!주사위 [범위숫자]", inline=False)
    embed.add_field(name="3. 앵무새", value="!앵무새 [따라할 말]", inline=False)
    embed.add_field(name="4. 음성채널 입장/퇴장", value="!join / !leave (초대자가 입장된 상태에만 가능)", inline=False)
    embed.add_field(name="5. 음악", value="!play [Youtube URL] : 음악을 재생\n!pause : 일시정지\n!resume : 다시 재생\n!stop : 중지", inline=False)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/420880499704332290/1010172441710051378/d78a5e2c-4cc4-4b22-89d6-9786c7bc2253.jpg")
    embed.set_image(url="https://cdn.discordapp.com/attachments/420880499704332290/1010172441710051378/d78a5e2c-4cc4-4b22-89d6-9786c7bc2253.jpg")
    await ctx.send(embed=embed)

bot.run('MTAwNzE4ODY1MDQ1NjUyMjc2Mw.GJPvrD.nIB2O9oTw-hKX5fQ8qUp3IFQ0I3rJ9LfYTwalY')
