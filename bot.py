import discord
from discord.utils import get

client = discord.Client()

@client.event
async def on_ready():
 print('Discord へ接続しました。')

@client.event
async def on_message(message):
    if message.content == '!accept':
        #role = get(message.server.roles, id='305606623882248192')
        #await client.add_roles(message.author, role)
        #embed=discord.Embed(title="Luck Network Discordサーバーへようこそ！", description="{0} さんのアカウントは認証されました。\nルールを守って利用してください ☺".format(message.author), color=0xb5157d)
        embed=discord.Embed(title="Sorry!", description="こちらのコマンドは、現在使用不可となっております。\nアカウントの認証方法につきましては、 [こちら](https://wiki.lucknetwork.jp/discord) をご覧ください。", color=0xb5157d)
        embed.set_thumbnail(url="https://cdn.lucknetwork.jp/img/kawaii_1.png")
        await client.send_message(message.channel, embed=embed)
    if message.content == '!debug':
        if(message.author.id == "116124230243975173" or "246544597117960193"):
            test=discord.Embed(title="デバッグメッセージ", description="message.author.id = {0}".format(message.author.id), color=0xb5157d)
            test.set_thumbnail(url="https://cdn.lucknetwork.jp/img/kawaii_1.png")
            await client.send_message(message.channel, embed=test)
        else:
            welcomechannel=discord.Embed(title="Sorry!", description="あなたには、このコマンドを実行する権限がありません。", color=0xb5157d)
            welcomechannel.set_thumbnail(url="https://cdn.lucknetwork.jp/img/kawaii_1.png")
            await client.send_message(message.channel, embed=welcomechannel)
    if message.content == "!welcome":
        if(message.author.id == "116124230243975173" or "246544597117960193"):
            welcomechannel=discord.Embed(title="Luck Network 公式Discordサーバー へようこそ！", description="当Discordサーバーではプレイヤー同士・運営チームの交流、運営によるサポート対応が行われています。\n最初に参加された方は全てのチャンネルが表示されていません。\n参加された方は必ず [サーバールール](https://wiki.lucknetwork.jp/rules) と [Discordの利用方法](https://wiki.lucknetwork.jp/discord) に目を通してください。\n\n**サーバーIP** `lucknetwork.jp`\n**バージョン** `1.7.x - 1.13.x`", color=0xb5157d)
            welcomechannel.add_field(name="リンク", value="[Web](https://lucknetwork.jp/) | [YouTube](https://youtube.com/channel/UCaXASkxWEBA-W9noD76f1uQ) | [Twitter](https://twitter.com/McLuckServer) | [Discord](https://discord.gg/23pJDKK) | [Vote](https://minecraft.jp/servers/lucknetwork.jp/vote)", inline=False)
            welcomechannel.add_field(name="**新規参加者の方へ**", value="このチャンネル `(#📌ようこそ♪｜welcome)` に書いてあることにすべて同意できたら、ゲーム内のロビーサーバーのチャットにて `/code` を実行して表示されるコードを [ApplyBot#7934 (このアカウント)](http://discordapp.com/users/528352239836856320) のダイレクトメッセージに送信してください。あなたのMinecraftアカウントとDiscordアカウントが紐づけされます。", inline=False)
            welcomechannel.add_field(name="**認証できない場合**", value="万が一サーバーもしくは認証システムがダウンして正しく認証できない場合、 [Twitter(@MLS_Support)](https://twitter.com/MLS_Support) もしくは [dedetyan#2670](http://discordapp.com/users/246544597117960193) までメッセージを送ってください。", inline=False)
            welcomechannel.set_thumbnail(url="https://cdn.lucknetwork.jp/img/kawaii_1.png")
            await client.send_message(message.channel, embed=welcomechannel)
        else:
            welcomechannel=discord.Embed(title="Sorry!", description="あなたには、このコマンドを実行する権限がありません。", color=0xb5157d)
            welcomechannel.set_thumbnail(url="https://cdn.lucknetwork.jp/img/kawaii_1.png")
            await client.send_message(message.channel, embed=welcomechannel)

@client.event
async def on_member_join(member):
    welcome=discord.Embed(title="Luck Network 公式Discord へようこそ！", description="このグループでは運営への質問や報告、プレイヤーとの交流ができます。\n最初に参加された方は全てのチャンネルが表示されていません。\n`#📌ようこそ♪｜welcome` に書いてあることにすべて同意できたら、ゲーム内のロビーサーバーのチャットにて `/code` を実行して表示されるコードを `[ApplyBot#7934 (このアカウント)](http://discordapp.com/users/528352239836856320)` のダイレクトメッセージに送信してください。あなたのMinecraftアカウントとDiscordアカウントが紐づけされます。", color=0xb5157d)
    welcome.set_thumbnail(url="https://cdn.lucknetwork.jp/img/kawaii_1.png")
    print(member.name + " がサーバーへ参加しました。")
    welcome.add_field(name="**新規参加者の方へ**", value="このチャンネル `(#📌ようこそ♪｜welcome)` に書いてあることにすべて同意できたら、ゲーム内のロビーサーバーのチャットにて `/code` を実行して表示されるコードを ApplyBot#7934 (このアカウント)` のダイレクトメッセージに送信してください。あなたのMinecraftアカウントとDiscordアカウントが紐づけされます。", inline=False)
    welcome.add_field(name="**認証できない場合**", value="万が一サーバーもしくは認証システムがダウンして正しく認証できない場合、 [Twitter(@MLS_Support)](https://twitter.com/MLS_Support) もしくは [dedetyan#2670](http://discordapp.com/users/246544597117960193) までメッセージを送ってください。", inline=False)
    welcome.add_field(name="リンク", value="[Web](https://lucknetwork.jp/) | [YouTube](https://youtube.com/channel/UCaXASkxWEBA-W9noD76f1uQ) | [Twitter](https://twitter.com/McLuckServer) | [Discord](https://discord.gg/23pJDKK) | [Vote](https://minecraft.jp/servers/lucknetwork.jp/vote)", inline=False)
    await client.send_message(member, embed=welcome)
    print("Welcome メッセージを " + member.name +" へ送信しました。")

client.run('<Bot の Token>')
