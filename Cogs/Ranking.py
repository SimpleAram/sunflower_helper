from discord.ext import commands
from discord import app_commands
import discord
from Domisol import *
import typing


def get_ranking_links(mode: int):
	return f"https://zh-kr-g-web.awesomepiece.com/api/rankings?idx={mode}&area=kr"


def get_LM_ranking_links(mode: int):
	return f"https://zh-kr-g-web.awesomepiece.com/api/rankings/last-month-winner?idx={mode}&area=kr"


# get_ranking(ranking_data, None, "레벨", "레벨", 0, 20, 1, 5)
def get_ranking(RankingFormat, Image, current_data, lastmonth_data, mode: str,
                page: int):

	viewlist = ""

	if RankingFormat["Format"][mode]["lastmonth_data"] == False:
		embed = discord.Embed(
		 title=f"**【 {RankingFormat['Format'][mode]['title']} 】**",
		 color=int(RankingFormat['Format'][mode]['color'], 16))

	else:
		lastmonth_data = lastmonth_data[0]
		if mode in ["검은 주방", "마녀", "소울메이트"]:
			LMR_name = lastmonth_data['name'].replace("_", "\_").replace(
			 "`", "\`").replace("~", "\~").replace("|", "\|").replace("*", "\*")
			LMR_timeMinute = str(int(lastmonth_data['time'] / 60))
			LMR_timeSecond = str(
			 int(lastmonth_data['time'] - (int(LMR_timeMinute) * 60)))

			if len(LMR_timeMinute) == 1:
				LMR_timeMinute = f"0{LMR_timeMinute}"

			if len(LMR_timeSecond) == 1:
				LMR_timeSecond = f"0{LMR_timeSecond}**\n"

			lastmonth = f"**> • 지난 달 1위 # {LMR_timeMinute}:{LMR_timeSecond}\n> {LMR_name}**\n\n"
			viewlist += lastmonth

		elif mode.find("진격의좀비") & mode.find("히어로즈") & mode.find("아포칼립스") & mode.find(
		  "디비전") != -1:
			LMR_members = lastmonth_data['members'].replace("_", "\_").replace(
			 "`", "\`").replace("~", "\~").replace("|", "\|").replace("*", "\*")
			LMR_score = format(lastmonth_data['score'], ",d")

			lastmonth = f" : {LMR_score} 점**\n> {LMR_members}"

		embed = discord.Embed(
		 title=f"**【 {RankingFormat['Format'][mode]['title']} 】**",
		 description=f'> ** • 지난 달 1위 {lastmonth}',
		 color=int(RankingFormat['Format'][mode]['color'], 16))

	addcount = 0
	tier = ""
	tierNumber = ""

	for i in range(RankingFormat["Page"][str(page)][0],
	               RankingFormat["Page"][str(page)][1]):
		try:
			ranking = current_data[i]

			if mode == "레벨":
				rank = ranking['rank']
				name = ranking['name'].replace("_", "\_").replace("`", "\`").replace(
				 "~", "\~").replace("|", "\|").replace("*", "\*")
				exp = ranking['exp']

				embed.add_field(name=f"{rank}위 : {name}",
				                value=f"{format(exp, ',d')} EXP",
				                inline=False)

			elif mode in ["개인 래더"]:
				ranking = current_data[i]
				rank = ranking['rank']
				name = ranking['name'].replace("_", "\_").replace("`", "\`").replace(
				 "~", "\~").replace("|", "\|").replace("*", "\*")
				value = ranking['value']

				if value >= 90000:
					if rank == 1:
						tier = "<:tier_champion:1059094729553362985>"
					elif rank <= 10:
						tier = "<:tier_challenger:1059094712016973895>"
					else:
						tier = "<:tier_master:1059094695239749772>"
						tierNumber = ""
				else:
					if value >= 58000:
						tier = "<:tier_diamond:1059094677200052326>"
						if 80000 <= value:
							tierNumber = "ɪ"
						elif 72000 <= value <= 79999:
							tierNumber = "ɪɪ"
						elif 65000 <= value <= 71999:
							tierNumber = "ɪɪɪ"
						elif 58000 <= value <= 64999:
							tierNumber = "ɪᴠ"
					elif value >= 36000:
						tier = "<:tier_platinum:1059094658061438994>"
						if 52000 <= value <= 57999:
							tierNumber = "ɪ"
						elif 46000 <= value <= 51999:
							tierNumber = "ɪɪ"
						elif 41000 <= value <= 45999:
							tierNumber = "ɪɪɪ"
						elif 36000 <= value <= 40999:
							tierNumber = "ɪᴠ"
					elif value >= 22000:
						tier = "<:tier_gold:1059094639883337738>"
						if 32000 <= value <= 35999:
							tierNumber = "ɪ"
						elif 28000 <= value <= 31999:
							tierNumber = "ɪɪ"
						elif 25000 <= value <= 27999:
							tierNumber = "ɪɪɪ"
						elif 22000 <= value <= 24999:
							tierNumber = "ɪᴠ"
					elif value >= 13000:
						tier = "<:tier_silver:1059094621080264704>"
						if 19500 <= value <= 21999:
							tierNumber = "ɪ"
						elif 17000 <= value <= 19499:
							tierNumber = "ɪɪ"
						elif 15000 <= value <= 16999:
							tierNumber = "ɪɪɪ"
						elif 13000 <= value <= 14999:
							tierNumber = "ɪᴠ"
					elif value >= 6000:
						tier = "<:tier_bronze:1059094602629529661>"
						if 11000 <= value <= 12999:
							tierNumber = "ɪ"
						elif 9000 <= value <= 10999:
							tierNumber = "ɪɪ"
						elif 7500 <= value <= 8999:
							tierNumber = "ɪɪɪ"
						elif 6000 <= value <= 7499:
							tierNumber = "ɪᴠ"
					elif value >= 1000:
						tier = "<:tier_iron:1059094583381852211>"
						if 4500 <= value <= 5999:
							tierNumber = "ɪ"
						elif 3000 <= value <= 4499:
							tierNumber = "ɪɪ"
						elif 2000 <= value <= 2999:
							tierNumber = "ɪɪɪ"
						elif 1000 <= value <= 1999:
							tierNumber = "ɪᴠ"
					else:
						tier = "<:tier_unll:1059094566009053214>"

				viewlist += f'**#{rank}** ▸ {tier}{tierNumber} `[{format(value, ",d")} 점]` {name}\n'

			elif mode in ["클랜 래더"]:
				ranking = current_data[i]
				rank = ranking['rank']
				name = ranking['name'].replace("_", "\_").replace("`", "\`").replace(
				 "~", "\~").replace("|", "\|").replace("*", "\*")
				value = ranking['value']

				if rank == 1:
					tier = "<:clan_champion:1059080738097602560>"
				elif 2 <= rank <= 3:
					tier = "<:clan_challenger:1059080717369348096>"
				elif 4 <= rank <= 10:
					tier = "<:clan_diamond:1059080616580235346>"
				elif 11 <= rank <= 25:
					tier = "<:clan_platinum:1059080596263030835>"
				elif 26 <= rank <= 45:
					tier = "<:clan_gold:1059080509885526046>"
				elif 46 <= rank <= 70:
					tier = "<:clan_silver:1059080490553983066>"
				elif 71 <= rank <= 100:
					tier = "<:clan_bronze:1059080463005777950>"
				elif value == 0:
					tier = "<:tier_unll:1059094566009053214>"

				viewlist += f'{tier} **#{rank}** ▸ `[{format(value, ",d")} 점]` {name}\n'

			elif mode in ["검은 주방", "마녀", "소울메이트"]:
				rank = ranking['rank']
				name = ranking['name'].replace("_", "\_").replace("`", "\`").replace(
				 "~", "\~").replace("|", "\|").replace("*", "\*")

				timeMinute = str(int(ranking['time'] / 60))
				timeSecond = str(int(ranking['time'] - (int(timeMinute) * 60)))

				if len(timeMinute) == 1:
					timeMinute = f"0{timeMinute}"
				if len(timeSecond) == 1:
					timeSecond = f"0{timeSecond}"

				viewlist += f'**#{rank}** {name} [{timeMinute}:{timeSecond}]\n'

			elif mode.find("진격의좀비") & mode.find("히어로즈") & mode.find(
			  "아포칼립스") & mode.find("디비전") != -1:
				rank = ranking['rank']
				members = ranking['members'].replace("_", "\_").replace("`", "\`").replace(
				 "~", "\~").replace("|", "\|").replace("*", "\*")

				score = format(ranking['score'], ",d")

				embed.add_field(name=f'{rank}위 : {score} 점',
				                value=f'{members}',
				                inline=False)

			addcount += 1
		except:
			pass

	if not len(viewlist) == 0:
		embed = discord.Embed(
		 title=f"**【 {RankingFormat['Format'][mode]['title']} 】**",
		 description=f"{viewlist}",
		 color=int(RankingFormat['Format'][mode]['color'], 16))
	if addcount == 0:
		embed = discord.Embed(
		 title=f"**【 {RankingFormat['Format'][mode]['title']} 】**",
		 description="랭킹이 존재하지 않습니다.",
		 color=int(RankingFormat['Format'][mode]['color'], 16))

	embed.set_footer(text=f"페이지 • {page} / 5")
	embed.set_thumbnail(url=Image[RankingFormat['Format'][mode]["image"]])

	return embed


class Ranking(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		self.Image, self.Board, self.Settings, self.RankingFormat = loadJson()

	async def rankingsAutoComplextion(
	  self, interaction: discord.Interaction,
	  currnet: str) -> typing.List[app_commands.Choice[str]]:
		data = []
		for rankingChoice in ['레벨', '래더', '싱글스토리', '진격의좀비', '히어로즈', '아포칼립스', '디비전']:
			if currnet.lower() in rankingChoice.lower():
				data.append(app_commands.Choice(name=rankingChoice, value=rankingChoice))

		return data

	# /랭킹
	@app_commands.command(name="랭킹", description="실시간 랭킹을 확인합니다.")
	@app_commands.autocomplete(mode=rankingsAutoComplextion)
	async def rankings(self, interaction: discord.Interaction, mode: str):
		RankingFormat = self.RankingFormat
		Image = self.Image
		lastmonthranking_data = None

		# 레벨
		if mode == "레벨":
			try:
				ranking_url = requests.get(get_ranking_links(RankingFormat["Urls"][mode]))
				ranking_data = ranking_url.json()

				embed = get_ranking(RankingFormat, Image, ranking_data,
				                    lastmonthranking_data, mode, 1)

				class SelectPage(discord.ui.View):

					def __init__(self):
						super().__init__()
						self.value = None

					@discord.ui.button(label="1",
					                   style=discord.ButtonStyle.blurple,
					                   emoji='📄')
					async def page_1(self, interaction: discord.Interaction,
					                 button: discord.ui.Button):
						embed = get_ranking(RankingFormat, Image, ranking_data,
						                    lastmonthranking_data, mode, 1)
						await interaction.response.edit_message(embed=embed)

					@discord.ui.button(label="2",
					                   style=discord.ButtonStyle.blurple,
					                   emoji='📄')
					async def page_2(self, interaction: discord.Interaction,
					                 button: discord.ui.Button):
						embed = get_ranking(RankingFormat, Image, ranking_data,
						                    lastmonthranking_data, mode, 2)
						await interaction.response.edit_message(embed=embed)

					@discord.ui.button(label="3",
					                   style=discord.ButtonStyle.blurple,
					                   emoji='📄')
					async def page_3(self, interaction: discord.Interaction,
					                 button: discord.ui.Button):
						embed = get_ranking(RankingFormat, Image, ranking_data,
						                    lastmonthranking_data, mode, 3)
						await interaction.response.edit_message(embed=embed)

					@discord.ui.button(label="4",
					                   style=discord.ButtonStyle.blurple,
					                   emoji='📄')
					async def page_4(self, interaction: discord.Interaction,
					                 button: discord.ui.Button):
						embed = get_ranking(RankingFormat, Image, ranking_data,
						                    lastmonthranking_data, mode, 4)
						await interaction.response.edit_message(embed=embed)

					@discord.ui.button(label="5",
					                   style=discord.ButtonStyle.blurple,
					                   emoji='📄')
					async def page_5(self, interaction: discord.Interaction,
					                 button: discord.ui.Button):
						embed = get_ranking(RankingFormat, Image, ranking_data,
						                    lastmonthranking_data, mode, 5)
						await interaction.response.edit_message(embed=embed)

				await interaction.response.send_message(embed=embed,
				                                        view=SelectPage(),
				                                        ephemeral=True)

			except Exception as E:
				embed = discord.Embed(title="오류 발생",
				                      description="불러올 수 있는 랭킹 정보가 존재하지 않습니다.",
				                      color=0xfa2616)
				await interaction.response.send_message(embed=embed,
				                                        ephemeral=True,
				                                        delete_after=4)
				print(E)

		# 래더
		elif mode == "래더":

			class Select(discord.ui.Select):

				def __init__(self):
					options = [
					 discord.SelectOption(label="개인 래더",
					                      emoji="☝️",
					                      description="[개인 래더] 순위를 확인합니다."),
					 discord.SelectOption(label="클랜 래더",
					                      emoji="🤝",
					                      description="[클랜 래더] 순위를 확인합니다.")
					]
					super().__init__(placeholder="확인하실 랭킹을 선택해주세요.",
					                 max_values=1,
					                 min_values=1,
					                 options=options)

				async def callback(self, interaction: discord.Interaction):
					try:
						mode = self.values[0]
						ranking_url = requests.get(get_ranking_links(
						 RankingFormat["Urls"][mode]))
						ranking_data = ranking_url.json()

						embed = get_ranking(RankingFormat, Image, ranking_data,
						                    lastmonthranking_data, mode, 1)

						class SelectPage(discord.ui.View):

							def __init__(self):
								super().__init__()
								self.value = None

							@discord.ui.button(label="1",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_1(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 1)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="2",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_2(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 2)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="3",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_3(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 3)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="4",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_4(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 4)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="5",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_5(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 5)
								await interaction.response.edit_message(embed=embed)

						await interaction.response.send_message(embed=embed,
						                                        view=SelectPage(),
						                                        ephemeral=True)

					except Exception as E:
						embed = discord.Embed(title="오류 발생",
						                      description="불러올 수 있는 랭킹 정보가 존재하지 않습니다.",
						                      color=0xfa2616)
						await interaction.response.send_message(embed=embed,
						                                        ephemeral=True,
						                                        delete_after=4)
						print(E)

			class SelectView(discord.ui.View):

				def __init__(self, *, timeout=120):
					super().__init__(timeout=timeout)
					self.add_item(Select())

			await interaction.response.send_message(view=SelectView(), ephemeral=True)

		# 싱글스토리
		elif mode == "싱글스토리":

			class Select(discord.ui.Select):

				def __init__(self):
					options = [
					 discord.SelectOption(label="검은 주방",
					                      emoji="📕",
					                      description="[검은 주방] 순위를 확인합니다."),
					 discord.SelectOption(label="마녀",
					                      emoji="📕",
					                      description="[마녀] 순위를 확인합니다."),
					 discord.SelectOption(label="소울메이트",
					                      emoji="📕",
					                      description="[소울메이트] 순위를 확인합니다.")
					]
					super().__init__(placeholder="확인하실 랭킹을 선택해주세요.",
					                 max_values=1,
					                 min_values=1,
					                 options=options)

				async def callback(self, interaction: discord.Interaction):
					try:
						mode = self.values[0]
						lastmonthranking_url = requests.get(
						 get_LM_ranking_links(RankingFormat["Urls"][mode]))
						lastmonthranking_data = lastmonthranking_url.json()
						ranking_url = requests.get(get_ranking_links(
						 RankingFormat["Urls"][mode]))
						ranking_data = ranking_url.json()
						embed = get_ranking(RankingFormat, Image, ranking_data,
						                    lastmonthranking_data, mode, 1)

						class SelectPage(discord.ui.View):

							def __init__(self):
								super().__init__()
								self.value = None

							@discord.ui.button(label="1",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_1(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 1)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="2",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_2(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 2)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="3",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_3(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 3)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="4",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_4(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 4)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="5",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_5(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 5)
								await interaction.response.edit_message(embed=embed)

						await interaction.response.send_message(embed=embed,
						                                        view=SelectPage(),
						                                        ephemeral=True)

					except Exception as E:
						embed = discord.Embed(title="오류 발생",
						                      description="불러올 수 있는 랭킹 정보가 존재하지 않습니다.",
						                      color=0xfa2616)
						await interaction.response.send_message(embed=embed,
						                                        ephemeral=True,
						                                        delete_after=4)
						print(E)

			class SelectView(discord.ui.View):

				def __init__(self, *, timeout=120):
					super().__init__(timeout=timeout)
					self.add_item(Select())

			await interaction.response.send_message(view=SelectView(), ephemeral=True)

		# 진격의좀비
		elif mode == "진격의좀비":

			class Select(discord.ui.Select):

				def __init__(self):
					options = [
					 discord.SelectOption(label="Episode.0 [Normal]",
					                      emoji="🎫",
					                      description="에피소드 제로 [노멀]"),
					 discord.SelectOption(label="Episode.1 [Normal]",
					                      emoji="🎫",
					                      description="에피소드 1 [노멀]"),
					 discord.SelectOption(label="Episode.1 [Hard]",
					                      emoji="🎟️",
					                      description="에피소드 1 [하드]"),
					 discord.SelectOption(label="Episode.2 [Normal]",
					                      emoji="🎫",
					                      description="에피소드 2 [노멀]"),
					 discord.SelectOption(label="Episode.2 [Hard]",
					                      emoji="🎟️",
					                      description="에피소드 2 [하드]"),
					 discord.SelectOption(label="Episode.3 [Normal]",
					                      emoji="🎫",
					                      description="에피소드 3 [노멀]"),
					 discord.SelectOption(label="Episode.3 [Hard]",
					                      emoji="🎟️",
					                      description="에피소드 3 [하드]")
					]
					super().__init__(placeholder="확인하실 랭킹을 선택해주세요.",
					                 max_values=1,
					                 min_values=1,
					                 options=options)

				async def callback(self, interaction: discord.Interaction):
					try:
						mode = f"진격의좀비 {self.values[0]}"
						lastmonthranking_url = requests.get(
						 get_LM_ranking_links(RankingFormat["Urls"][mode]))
						lastmonthranking_data = lastmonthranking_url.json()
						ranking_url = requests.get(get_ranking_links(
						 RankingFormat["Urls"][mode]))
						ranking_data = ranking_url.json()
						embed = get_ranking(RankingFormat, Image, ranking_data,
						                    lastmonthranking_data, mode, 1)

						class SelectPage(discord.ui.View):

							def __init__(self):
								super().__init__()
								self.value = None

							@discord.ui.button(label="1",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_1(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 1)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="2",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_2(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 2)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="3",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_3(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 3)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="4",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_4(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 4)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="5",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_5(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 5)
								await interaction.response.edit_message(embed=embed)

						await interaction.response.send_message(embed=embed,
						                                        view=SelectPage(),
						                                        ephemeral=True)

					except Exception as E:
						embed = discord.Embed(title="오류 발생",
						                      description="불러올 수 있는 랭킹 정보가 존재하지 않습니다.",
						                      color=0xfa2616)
						await interaction.response.send_message(embed=embed,
						                                        ephemeral=True,
						                                        delete_after=4)
						print(E)

			class SelectView(discord.ui.View):

				def __init__(self, *, timeout=120):
					super().__init__(timeout=timeout)
					self.add_item(Select())

			await interaction.response.send_message(view=SelectView(), ephemeral=True)

		# 히어로즈
		elif mode == "히어로즈":

			class Select(discord.ui.Select):

				def __init__(self):
					options = [
					 discord.SelectOption(label="Heroes.1 [Normal]",
					                      emoji="🎫",
					                      description="히어로즈 1 [노멀]"),
					 discord.SelectOption(label="Heroes.1 [Hard]",
					                      emoji="🎟️",
					                      description="히어로즈 1 [하드]"),
					 discord.SelectOption(label="Heroes.2 [Normal]",
					                      emoji="🎫",
					                      description="히어로즈 2 [노멀]"),
					 discord.SelectOption(label="Heroes.2 [Hard]",
					                      emoji="🎟️",
					                      description="히어로즈 2 [하드]"),
					 discord.SelectOption(label="Heroes.3 [Normal]",
					                      emoji="🎫",
					                      description="히어로즈 3 [노멀]"),
					 discord.SelectOption(label="Heroes.3 [Hard]",
					                      emoji="🎟️",
					                      description="히어로즈 3 [하드]"),
					 discord.SelectOption(label="Heroes.4 [Normal]",
					                      emoji="🎫",
					                      description="히어로즈 4 [노멀]"),
					 discord.SelectOption(label="Heroes.4 [Hard]",
					                      emoji="🎟️",
					                      description="히어로즈 4 [하드]")
					]
					super().__init__(placeholder="확인하실 랭킹을 선택해주세요.",
					                 max_values=1,
					                 min_values=1,
					                 options=options)

				async def callback(self, interaction: discord.Interaction):
					try:
						mode = f"히어로즈 {self.values[0]}"
						lastmonthranking_url = requests.get(
						 get_LM_ranking_links(RankingFormat["Urls"][mode]))
						lastmonthranking_data = lastmonthranking_url.json()
						ranking_url = requests.get(get_ranking_links(
						 RankingFormat["Urls"][mode]))
						ranking_data = ranking_url.json()
						embed = get_ranking(RankingFormat, Image, ranking_data,
						                    lastmonthranking_data, mode, 1)

						class SelectPage(discord.ui.View):

							def __init__(self):
								super().__init__()
								self.value = None

							@discord.ui.button(label="1",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_1(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 1)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="2",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_2(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 2)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="3",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_3(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 3)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="4",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_4(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 4)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="5",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_5(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 5)
								await interaction.response.edit_message(embed=embed)

						await interaction.response.send_message(embed=embed,
						                                        view=SelectPage(),
						                                        ephemeral=True)

					except Exception as E:
						embed = discord.Embed(title="오류 발생",
						                      description="불러올 수 있는 랭킹 정보가 존재하지 않습니다.",
						                      color=0xfa2616)
						await interaction.response.send_message(embed=embed,
						                                        ephemeral=True,
						                                        delete_after=4)
						print(E)

			class SelectView(discord.ui.View):

				def __init__(self, *, timeout=120):
					super().__init__(timeout=timeout)
					self.add_item(Select())

			await interaction.response.send_message(view=SelectView(), ephemeral=True)

		# 아포칼립스
		elif mode == "아포칼립스":

			class Select(discord.ui.Select):

				def __init__(self):
					options = [
					 discord.SelectOption(label="Apocalypse [Normal]",
					                      emoji="🎫",
					                      description="아포칼립스 [노멀]"),
					 discord.SelectOption(label="Apocalypse [Hard]",
					                      emoji="🎟️",
					                      description="아포칼립스 [하드]")
					]
					super().__init__(placeholder="확인하실 랭킹을 선택해주세요.",
					                 max_values=1,
					                 min_values=1,
					                 options=options)

				async def callback(self, interaction: discord.Interaction):
					try:
						mode = f"아포칼립스 {self.values[0]}"
						lastmonthranking_url = requests.get(
						 get_LM_ranking_links(RankingFormat["Urls"][mode]))
						lastmonthranking_data = lastmonthranking_url.json()
						ranking_url = requests.get(get_ranking_links(
						 RankingFormat["Urls"][mode]))
						ranking_data = ranking_url.json()
						embed = get_ranking(RankingFormat, Image, ranking_data,
						                    lastmonthranking_data, mode, 1)

						class SelectPage(discord.ui.View):

							def __init__(self):
								super().__init__()
								self.value = None

							@discord.ui.button(label="1",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_1(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 1)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="2",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_2(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 2)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="3",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_3(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 3)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="4",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_4(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 4)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="5",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_5(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 5)
								await interaction.response.edit_message(embed=embed)

						await interaction.response.send_message(embed=embed,
						                                        view=SelectPage(),
						                                        ephemeral=True)

					except Exception as E:
						embed = discord.Embed(title="오류 발생",
						                      description="불러올 수 있는 랭킹 정보가 존재하지 않습니다.",
						                      color=0xfa2616)
						await interaction.response.send_message(embed=embed,
						                                        ephemeral=True,
						                                        delete_after=4)
						print(E)

			class SelectView(discord.ui.View):

				def __init__(self, *, timeout=120):
					super().__init__(timeout=timeout)
					self.add_item(Select())

			await interaction.response.send_message(view=SelectView(), ephemeral=True)

		# 디비전
		elif mode == "디비전":

			class Select(discord.ui.Select):

				def __init__(self):
					options = [
					 discord.SelectOption(label="Dɪᴠision.1 [Normal]",
					                      emoji="🎫",
					                      description="디비전 1 [노멀]"),
					 discord.SelectOption(label="Dɪᴠision.1 [Hard]",
					                      emoji="🎟️",
					                      description="디비전 1 [하드]"),
					 discord.SelectOption(label="Dɪᴠision.2 [Normal]",
					                      emoji="🎫",
					                      description="디비전 2 [노멀]"),
					 discord.SelectOption(label="Dɪᴠision.3 [Normal]",
					                      emoji="🎫",
					                      description="디비전 3 [노멀]")
					]
					super().__init__(placeholder="확인하실 랭킹을 선택해주세요.",
					                 max_values=1,
					                 min_values=1,
					                 options=options)

				async def callback(self, interaction: discord.Interaction):
					try:
						mode = f"디비전 {self.values[0]}"
						lastmonthranking_url = requests.get(
						 get_LM_ranking_links(RankingFormat["Urls"][mode]))
						lastmonthranking_data = lastmonthranking_url.json()
						ranking_url = requests.get(get_ranking_links(
						 RankingFormat["Urls"][mode]))
						ranking_data = ranking_url.json()
						embed = get_ranking(RankingFormat, Image, ranking_data,
						                    lastmonthranking_data, mode, 1)

						class SelectPage(discord.ui.View):

							def __init__(self):
								super().__init__()
								self.value = None

							@discord.ui.button(label="1",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_1(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 1)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="2",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_2(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 2)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="3",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_3(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 3)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="4",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_4(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 4)
								await interaction.response.edit_message(embed=embed)

							@discord.ui.button(label="5",
							                   style=discord.ButtonStyle.blurple,
							                   emoji='📄')
							async def page_5(self, interaction: discord.Interaction,
							                 button: discord.ui.Button):
								embed = get_ranking(RankingFormat, Image, ranking_data,
								                    lastmonthranking_data, mode, 5)
								await interaction.response.edit_message(embed=embed)

						await interaction.response.send_message(embed=embed,
						                                        view=SelectPage(),
						                                        ephemeral=True)

					except Exception as E:
						embed = discord.Embed(title="오류 발생",
						                      description="불러올 수 있는 랭킹 정보가 존재하지 않습니다.",
						                      color=0xfa2616)
						await interaction.response.send_message(embed=embed,
						                                        ephemeral=True,
						                                        delete_after=4)
						print(E)

			class SelectView(discord.ui.View):

				def __init__(self, *, timeout=120):
					super().__init__(timeout=timeout)
					self.add_item(Select())

			await interaction.response.send_message(view=SelectView(), ephemeral=True)


async def setup(bot):
	await bot.add_cog(Ranking(bot))
