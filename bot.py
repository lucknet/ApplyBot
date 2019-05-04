import discord
from discord.utils import get

client = discord.Client()

@client.event
async def on_ready():
 print('Discord へ接続しました。')

#@client.event
#async def on_message(message):
    #if message.content == '!accept':
    #    role = get(message.server.roles, id='305606623882248192')
    #    await client.add_roles(message.author, role)
    #    embed=discord.Embed(title="Luck Network Discordサーバーへようこそ！", description="{0} さんのアカウントは認証されました。\nルールを守って利用してください ☺".format(message.author),# color=0xb5157d)
    #    embed.set_thumbnail(url="https://cdn.lucknetwork.jp/img/kawaii_1.png")
    #    await client.send_message(message.channel, embed=embed)
    #if message.content == '!debug':
    #    test=discord.Embed(title="デバッグメッセージ", description=":white_medium_small_square: :white_medium_square:  :white_large_square:  リンク", color=0xb5157d)
    #    test.set_thumbnail(url="https://cdn.lucknetwork.jp/img/kawaii_1.png")
    #    await client.send_message(message.channel, test=embed)
    #if message.content == '!welcome':
    #    welcomechannel=discord.Embed(title="Luck Network 公式Discordサーバー へようこそ！", description="当Discordサーバーではプレイヤー同士・運営チームの交流、運営によるサポート対応が行われています。\n最初に参加された方は全てのチャンネルが表示されていません。\n参加された方は必ず [サーバールール](https://wiki.lucknetwork.jp/rules) と [Discordの利用方法](https://wiki.lucknetwork.jp/discord) に目を通してください。\n\n**サーバーIP** `lucknetwork.jp`\n**バージョン** `1.7.x - 1.13.x`", color=0xb5157d)
    #    welcomechannel.add_field(name="リンク", value="[Web](https://lucknetwork.jp/) | [YouTube](https://youtube.com/channel/UCaXASkxWEBA-W9noD76f1uQ) | [Twitter](https://twitter.com/McLuckServer) | [Discord](https://discord.gg/23pJDKK) | [Vote](https://minecraft.jp/servers/lucknetwork.jp/vote)", inline=False)
    #    welcomechannel.add_field(name="**新規参加者の方へ**", value="このチャンネル `(#📌ようこそ♪｜welcome)` に書いてあることにすべて同意できたら、ゲーム内のロビーサーバーのチャットにて `/code` を実行して表示されるコードを `ApplyBot#7934 (このアカウント)` のダイレクトメッセージに送信してください。あなたのMinecraftアカウントとDiscordアカウントが紐づけされます。", inline=False)
    #    welcomechannel.set_thumbnail(url="https://cdn.lucknetwork.jp/img/kawaii_1.png")
    #    await client.send_message(message.channel, embed=welcomechannel)

@client.event
async def on_member_join(member):
    welcome=discord.Embed(title="Luck Network 公式Discord へようこそ！", description="このグループでは運営への質問や報告、プレイヤーとの交流ができます。\n最初に参加された方は全てのチャンネルが表示されていません。\n`#📌ようこそ♪｜welcome` に書いてあることにすべて同意できたら、ゲーム内のロビーサーバーのチャットにて `/code` を実行して表示されるコードを `ApplyBot#7934 (このアカウント)` のダイレクトメッセージに送信してください。あなたのMinecraftアカウントとDiscordアカウントが紐づけされます。", color=0xb5157d)
    welcome.set_thumbnail(url="https://cdn.lucknetwork.jp/img/kawaii_1.png")
    print(member.name + " がサーバーへ参加しました。")
    welcome.add_field(name="リンク", value="[Web](https://lucknetwork.jp/) | [YouTube](https://youtube.com/channel/UCaXASkxWEBA-W9noD76f1uQ) | [Twitter](https://twitter.com/McLuckServer) | [Discord](https://discord.gg/23pJDKK) | [Vote](https://minecraft.jp/servers/lucknetwork.jp/vote)", inline=False)
    await client.send_message(member, embed=welcome)
    print("Welcome メッセージを " + member.name +" へ送信しました。")

client.run('<Bot の Token>')
