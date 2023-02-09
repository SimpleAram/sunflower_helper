from discord.ext import commands
from discord import app_commands
import discord
from Domisol import *

class Channel(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.Image, self.Board, self.Settings, self.RankingFormat = loadJson()

    # /채널
    @app_commands.command(name="채널", description="실시간 채널 리스트를 확인합니다.")
    async def channels(self, interaction: discord.Interaction):

        channel_url = requests.get("https://zh-kr-g-web.awesomepiece.com/api/server-list?version={0}")
        channels_data = channel_url.json()

        allUserCount = 0
        viewlist = f"""현재 시각의 채널 정보를 불러옵니다.\n{datetime.now(KST).strftime("%Y.%m.%d • %p %I:%M:%S".encode('unicode-escape').decode()).encode().decode("unicode-escape").replace('PM', '오후').replace('AM', '오전')}\n\n"""

        for i in channels_data:
            users = i['userCount']
            users_P = round(i['userCount'] * 100 / i['maxUserCount'], 2)
            allUserCount += i['userCount']

            if users_P < 85:
                state = "◇"
            elif 85 <= users_P <= 98:
                state = "◈"
            elif 99 <= users_P:
                state = "◆"

            viewlist += f"""**{i['name']}** {state} {format(users, ",d")} 명 ({users_P}%)\n"""

        embed = discord.Embed(title="**실시간 채널 리스트**", description=viewlist, color=0x8cc63f)
        embed.set_footer(text=f'• 모든 동시 접속자 수 : {format(allUserCount, ",d")}명')

        await interaction.response.send_message(embed=embed, ephemeral=False)

async def setup(bot):
    await bot.add_cog(Channel(bot))