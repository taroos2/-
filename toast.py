import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("토스트의 채팅봇 작동중")
    await client.change_presence(status=discord.Status.online, activity=game)




@client.event
async def on_message(message):
    if message.content.startswith("토스트 안녕"):
        await message.channel.send("ㅎㅇ")

    if message.content.startswith("스트야"):
        await message.channel.send("왜불러")

    if message.content.startswith("그냥"):
        await message.channel.send("ㅇㅋ...")

    if message.content.startswith("토스트 섹스"):
        await message.channel.send("하읏")

    if message.content.startswith("토스트 강아지"):
        await message.channel.send("멍멍")

    if message.content.startswith("토스트 미쳤어?"):
        await message.channel.send("아닝")

    if message.content.startswith("토스트 멈춰"):
        await message.channel.send("넹 주인님")

    if message.content.startswith("토스트 ㅄ"):
        await message.channel.send("ㅋ")

    if message.content.startswith("토스트 시발새끼"):
        await message.channel.send("히잉")

    if message.content.startswith("토스트 맛있다"):
        await message.channel.send("히이이익")

    if message.content.startswith("건후형"):
        await message.channel.send("돌아와")

    if message.content.startswith("들어와"):
        await message.channel.send("빨리와아아아")

    if message.content.startswith("토스트 콩진호"):
        await message.channel.send("콩진호가 간다 ! "
                                   "콩진호가 간다 !")

    if message.content.startswith("토스트 닥쳐"):
        await message.channel.send("알았어...")

    if message.content.startswith("토스트 조용히 해"):
        await message.channel.send("싫어!")

    if message.content.startswith("토스트 꺼져"):
        await message.channel.send("네...")

    if message.content.startswith("토스트 쉿"):
        await message.channel.send("쉿...")

    if message.content.startswith("토스트 미워"):
        await message.channel.send("나 미워?")

    if message.content.startswith("화평씨"):
        await message.channel.send("나 우유 안머거!!!")

    if message.content.startswith("묻고"):
        await message.channel.send("더블로 가!")

    if message.content.startswith("토스트 싫어"):
        await message.channel.send("난 좋은데...ㅎ")

    if message.content.startswith("토스트 하지마"):
        await message.channel.send("알았엉")

    if message.content.startswith("깡패"):
        await message.channel.send("나 깡패 아니다. 나도 적금 붓고 보험들고 살고 그런다.")

    if message.content.startswith("토스트 바보"):
        await message.channel.send("메렁")

    if message.content.startswith("토스트 사랑해"):
        await message.channel.send("나두><")

    if message.content.startswith("달건이"):
        await message.channel.send("내가 달건이 생활을 열일곱에 시작했다. 그 나이 때 달건이 시작한 놈들이 백 명이다 치면은 지금 나만큼 사는 놈은 나 혼자 뿐이야. 나는 어떻게 여기까지 왔느냐? 잘난 놈 제끼고 못난 놈 보내고. 안경잽이같이 배신하는 새끼들... 다 죽였다. 고니야 담배 하나 찔러봐라")

    if message.content.startswith("올림픽대로"):
        await message.channel.send("마포대교는 무너졌냐 새끼야?")

    if message.content.startswith("화란아"):
        await message.channel.send("나도 순정이 있다. 니가 이런식으로 내 순정을 짓밟으면 임마 그때는 깡패가 되는거야! 내가 널 깡패처럼 납치라도 하랴? 앉어!")

    if message.content.startswith("토스트 명령어"):
        await message.channel.send("!play 노래 제목, 링크")
        await message.channel.send("!queue 리스트")
        await message.channel.send("!skip 스킵")
        await message.channel.send("!clear 노래 재생목록 삭제")
        await message.channel.send("!summon 소환")

client.run("NjMwNDA0Njc3ODI5MjYzMzcw.XZn0iw.WymJFQkXODd-ifooKI-c6_XVlS4")