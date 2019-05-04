import discord
from discord.utils import get

client = discord.Client()

@client.event
async def on_ready():
 print('Discord へ接続しました。')

@client.event
async def on_message(message):
    if message.content == '!accept':
        role = get(message.server.roles, id='<認証チャンネルのID>')
        await client.add_roles(message.author, role)
        embed=discord.Embed(title="Luck Network Discordサーバーへようこそ！", description="{0} さんのアカウントは認証されました。\nルールを守って利用してください ☺".format(message.author), color=0xb5157d)
        embed.set_thumbnail(url="https://cdn.lucknetwork.jp/img/kawaii_1.png")
        await client.send_message(message.channel, embed=embed)

        welcome=discord.Embed(title="Luck Network 公式Discord へようこそ！", description="このグループでは運営への質問や報告、プレイヤーとの交流ができます。\nまた、最初に参加された方は全てのチャンネルが表示されていません。\n**参加された方は必ず[サーバールール](https://wiki.lucknetwork.jp/rules)に目を通し、**__**`💁認証｜apply` チャンネルにて**__ `!accept` __**と発言してください。**__\n\n\n\n", color=0xb5157d)
        welcome.set_thumbnail(url="https://cdn.lucknetwork.jp/img/kawaii_1.png")

@client.event
async def on_member_join(member):
    print(member.name + " がサーバーへ参加しました。")
    welcome.add_field(name="リンク", value="[Web](https://lucknetwork.jp/) | [YouTube](https://youtube.com/channel/UCaXASkxWEBA-W9noD76f1uQ) | [Twitter](https://twitter.com/McLuckServer) | [Discord](https://discord.gg/23pJDKK) | [Vote](https://minecraft.jp/servers/lucknetwork.jp/vote)", inline=False)
    await client.send_message(member, embed=welcome)
    print("Welcome メッセージを " + member.name +" へ送信しました。")

client.run('<Bot の Token>')
