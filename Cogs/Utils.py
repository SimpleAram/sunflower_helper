from discord.ext import commands
from discord import app_commands
import discord
from Domisol import *


class Utils(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		self.Image, self.Board, self.Settings, self.RankingFormat = loadJson()

	# /도움말
	@app_commands.command(name="도움말", description="명령어 리스트를 확인합니다.")
	async def commandlist(self, interaction: discord.Interaction):
		embed = discord.Embed(title=None, description=None, color=0x8adaff)
		embed.add_field(
		 name="명령어 리스트",
		 value=
		 '- `/채널` : 실시간 채널 리스트를 확인합니다.\n- `/랭킹` : 실시간 랭킹을 확인합니다.\n- `/링크` : 좀비고등학교의 온라인 커뮤니티를 확인합니다.\n- `/연구실` : 연구실 시뮬레이션',
		 inline=False)
		# embed.add_field(name="명령어 리스트", value= '- `/채널` : 실시간 채널 리스트를 확인합니다.\n- `/랭킹` : 실시간 랭킹을 확인합니다.\n- `/링크` : 좀비고등학교의 온라인 커뮤니티를 확인합니다.\n- `/연구실` : 연구실 시뮬레이션\n- `/어썸팩` : 어썸팩 시뮬레이션', inline=False)
		await interaction.response.send_message(embed=embed, ephemeral=True)

	# /링크
	@app_commands.command(name="링크", description="좀비고등학교의 온라인 커뮤니티를 확인합니다.")
	async def links(self, interaction: discord.Interaction):
		embed = discord.Embed(title=f"**좀비고등학교**",
		                      description="링크 클릭 시 해당 페이지로 이동합니다.",
		                      color=0xc0c0c0)
		embed.add_field(
		 name="리스트",
		 value=
		 '_ _• [홈페이지](https://awesomepiece.com/)\n • [네이버 카페](https://cafe.naver.com/onimobile)\n • [트위터](https://twitter.com/AWESOMEPIECE)\n • [페이스북](https://ko-kr.facebook.com/AwesomePiece/)\n • [유튜브](https://www.youtube.com/c/Awesomepiece)',
		 inline=False)
		embed.add_field(
		 name="다운로드",
		 value=
		 '_ _• [Google Play](https://play.google.com/store/apps/details?id=net.kernys.aooni&hl=ko&gl=KR)\n • [원스토어](https://m.onestore.co.kr/mobilepoc/apps/appsDetail.omp?prodId=0000761446)\n • [App Store](https://goo.gl/tpOVfY)'
		)
		embed.set_thumbnail(
		 url=
		 "https://media.discordapp.net/attachments/1045295528973434880/1045295881538252881/unknown.png"
		)
		await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot):
	await bot.add_cog(Utils(bot))
