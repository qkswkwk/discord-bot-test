@bot.command()
async def join(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("음성채널 없음")
        
@bot.command()
async def leave(ctx):
    await bot.voice_clients[0].disconnect()
    
되는지 테스트 안해봄
