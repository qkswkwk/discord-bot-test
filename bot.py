from ssl import CHANNEL_BINDING_TYPES
import discord
from discord.ext import commands
import random
import youtube_dl
from youtubesearchpython import VideosSearch

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
    msg = "ㅎㅇ ㅋㅋ 님머임"
    await member.send(msg) #개인 DM으로 보내기
    channel = bot.get_channel([i.id for i in chans][0]) #숫자로 채널 지정
    await channel.send(msg) # channel에 보내기

@bot.event
async def on_member_remove(member):
    msg = "바보간다 ㅋㅋ"
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
   
@bot.command()
async def song_start(voice, i):
    try:
        if not voice.is_playing() and not voice.is_paused():
            ydl_opts = {'format':'bestaudio'}
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(f'https://www.youtube.com{playlist[i][1]}', download=False)
                URL = info['formats'][0]['url']
           
            voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        #voice.play(discord.FFmpegPCMAudio(executable = './ffmpeg-4.4-full_build-shared/bin/ffmpeg.exe', source='./song.mp3'))
            
        while voice.is_playing() or voice.is_paused():
            await asyncio.sloop(0.1)
    except:
        return
       
@bot.command(aliases = ['p'])
async def play(ctx,*, keyword):
    try:
        result = YoutubeSearch(keyword, max_results=1).to_dict()
        
        global playlist
        playlist.append([results[0]['title'], results[0]['url_suffix']]) #플레이리스트에 노래 추가
        await ctx.send(embed=set_Embed(title='노래 추가',description=f"{results[0]['title']}"))
      
        channel = ctx.author.voice.channel
        if bot.voice_clients == []:
            await channel.connect()
            await ctx.send("<" + str(bot.voice_clients[0].channel) + ">에 들어갑니다.")
        voice = bot.voice_clients[0]
        
        if not voice.is_playing() and not voice.is_paused():
            global i
            i = 0
            while True:
                await song_start(voice, i)
                if loop:
                    if i < len(playlist) - 1:
                        i = i + 1
                    else:
                        i = 0
                    continue
                elif i < len(playlist) - 1:
                    i = i + 1
                    continue
                playlist = [[]]
                break
        #await voice.disconnect()
    except:
        await ctx.send("Play Error")
      
@bot.command(aliases=['도움말','h'])
async def 도움(ctx):
    embed = discord.Embed(title="bot test", description="반자자짱", color=0x4432a8)
    embed.add_field(name="1. 인사", value="!안녕", inline=False)
    embed.add_field(name="2. 주사위", value="!주사위 [범위숫자]", inline=False)
    embed.add_field(name="3. 앵무새", value="!앵무새 [따라할 말]", inline=False)
    embed.add_field(name="4. 핑 확인", value="!핑", inline=False)
    embed.add_field(name="5. 음성채널 입장/퇴장", value="!join / !leave (초대자가 입장된 상태에만 가능)", inline=False)
    embed.add_field(name="6. 음악", value="!play [Youtube URL] : 음악을 재생\n!pause : 일시정지\n!resume : 다시 재생\n!stop : 중지", inline=False)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/420880499704332290/1010172441710051378/d78a5e2c-4cc4-4b22-89d6-9786c7bc2253.jpg")
    embed.set_image(url="https://cdn.discordapp.com/attachments/420880499704332290/1010172441710051378/d78a5e2c-4cc4-4b22-89d6-9786c7bc2253.jpg")
    await ctx.send(embed=embed)

bot.run('token')
