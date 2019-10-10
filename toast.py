import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("ready")
    game = discord.Game("토스트의 채팅봇 작동중")
    await client.change_presence(status=discord.Status.online, activity=game)




@client.event
async def on_message(message):
    if message.content.startswith("토스트 안녕"):
        await client.send_message(message.channel, ("ㅎㅇ"))

    if message.content.startswith("동혁이"):
        await client.send_message(message.channel, ("빡빡이"))

    if message.content.startswith("스트야"):
        await client.send_message(message.channel, ("왜불러"))

    if message.content.startswith("토스트 잘했어"):
        await client.send_message(message.channel, ("헤헤"))
        
    if message.content.startswith("라라라"):
        await client.send_message(message.channel, ("룰루"))
        
    if message.content.startswith("자라"):
        await client.send_message(message.channel, ("자자"))

    if message.content.startswith("안자"):
        await client.send_message(message.channel, ("난 안자"))

    if message.content.startswith("그냥"):
        await client.send_message(message.channel, ("ㅇㅋ..."))

    if message.content.startswith("토스트 섹스"):
        await client.send_message(message.channel, ("하읏"))

    if message.content.startswith("토스트 강아지"):
        await client.send_message(message.channel, ("멍멍"))

    if message.content.startswith("토스트 미쳤어?"):
        await client.send_message(message.channel, ("아닝"))

    if message.content.startswith("토스트 멈춰"):
        await client.send_message(message.channel, ("넹 주인님"))

    if message.content.startswith("토스트 ㅄ"):
        await client.send_message(message.channel, ("ㅋ"))

    if message.content.startswith("토스트 시발새끼"):
        await client.send_message(message.channel, ("히잉"))

    if message.content.startswith("토스트 맛있다"):
        await client.send_message(message.channel, ("히이이익"))

    if message.content.startswith("건후형"):
        await client.send_message(message.channel, ("돌아와"))

    if message.content.startswith("들어와"):
        await client.send_message(message.channel, ("빨리와아아아"))

    if message.content.startswith("토스트 콩진호"):
        await client.send_message(message.channel, ("콩진호가 간다 ! "
                                   "콩진호가 간다 !"))

    if message.content.startswith("토스트 닥쳐"):
        await client.send_message(message.channel, ("알았어..."))

    if message.content.startswith("토스트 조용히 해"):
        await client.send_message(message.channel, ("싫어!"))

    if message.content.startswith("토스트 꺼져"):
        await client.send_message(message.channel, ("네..."))

    if message.content.startswith("토스트 쉿"):
        await client.send_message(message.channel, ("쉿..."))

    if message.content.startswith("토스트 미워"):
        await client.send_message(message.channel, ("나 미워?"))

    if message.content.startswith("화평씨"):
        await client.send_message(message.channel, ("나 우유 안머거!!!"))

    if message.content.startswith("묻고"):
        await client.send_message(message.channel, ("더블로 가!"))

    if message.content.startswith("토스트 싫어"):
        await client.send_message(message.channel, ("난 좋은데...ㅎ"))

    if message.content.startswith("토스트 하지마"):
        await client.send_message(message.channel, ("알았엉"))

    if message.content.startswith("깡패"):
        await client.send_message(message.channel, ("나 깡패 아니다. 나도 적금 붓고 보험들고 살고 그런다."))

    if message.content.startswith("토스트 바보"):
        await client.send_message(message.channel, ("메렁"))

    if message.content.startswith("토스트 사랑해"):
        await client.send_message(message.channel, ("나두><"))

    if message.content.startswith("달건이"):
        await client.send_message(message.channel, ("내가 달건이 생활을 열일곱에 시작했다. 그 나이 때 달건이 시작한 놈들이 백 명이다 치면은 지금 나만큼 사는 놈은 나 혼자 뿐이야. 나는 어떻게 여기까지 왔느냐? 잘난 놈 제끼고 못난 놈 보내고. 안경잽이같이 배신하는 새끼들... 다 죽였다. 고니야 담배 하나 찔러봐라"))

    if message.content.startswith("올림픽대로"):
        await client.send_message(message.channel, ("마포대교는 무너졌냐 새끼야?"))

    if message.content.startswith("화란아"):
        await client.send_message(message.channel, ("나도 순정이 있다. 니가 이런식으로 내 순정을 짓밟으면 임마 그때는 깡패가 되는거야! 내가 널 깡패처럼 납치라도 하랴? 앉어!"))

    if message.content.startswith("토스트 명령어"):
        await client.send_message(message.channel, ("!play 노래 제목, 링크"))
        await client.send_message(message.channel, ("!queue 리스트"))
        await client.send_message(message.channel, ("!skip 스킵"))
        await client.send_message(message.channel, ("!clear 노래 재생목록 삭제"))
        await client.send_message(message.channel, ("!summon 소환"))

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
