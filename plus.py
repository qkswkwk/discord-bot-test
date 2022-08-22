@bot.command() #유저가 음성채널이 있는지 확인, 들어가기
async def join(ctx)
	if ctx.author.voice and ctx.author.voice.channel:
    	channel = ctx.author.voice.channel
    	await channel.connect()
    else:
    	await ctx.send("음성채널 없음")
      
@bot.command() #뭐가 더 나을까
async def play(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
  
python3 -m pip install -U youtube_dl #유튜브 다운로드 라이브러리 설치
import youtube_dl

@bot.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    if bot.voice_clients == []:
    	await channel.connect()
    	await ctx.send("connected to the voice channel, " + str(bot.voice_clients[0].channel))

    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))

@bot.command() #봇 퇴장
async def leave(ctx):
    await bot.voice_clients[0].disconnect()
    
@bot.command()
async def pause(ctx):
    if not bot.voice_clients[0].is_paused():
        bot.voice_clients[0].pause()
    else:
        await ctx.send("already paused")

@bot.command()
async def resume(ctx):
    if bot.voice_clients[0].is_paused():
        bot.voice_clients[0].resume()
    else:
        await ctx.send("already playing")
        
@bot.command()
async def stop(ctx):
	if bot.voice_clients[0].is_playing():
    	bot.voice_clients[0].stop()
    else:
    	await ctx.send("not playing")
