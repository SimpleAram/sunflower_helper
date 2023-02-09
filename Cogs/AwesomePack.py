from discord.ext import commands
from discord import app_commands
import discord
from Helper_Sol import *


def awesomepackRarity(user: str, rarity: str, skin: str, _: int):
	if _ == None:
		if rarity == "7일":
			embed = discord.Embed(title=f"{skin} ({rarity})",
			                      description=f"",
			                      color=0xfeff05)
		elif rarity == "30일":
			embed = discord.Embed(title=f"{skin} ({rarity})",
			                      description=f"",
			                      color=0xe2731d)
		elif rarity == "무제한":
			embed = discord.Embed(title=f"{skin} ({rarity})",
			                      description=f"",
			                      color=0xd939d2)

	elif _ > 0:
		# class LeftTime(discord.ui.View):

		#     def __init__(self):
		#         super().__init__()
		#         self.value = None

		#     @discord.ui.button(label="다음",
		#                     style=discord.ButtonStyle.gray)
		#     async def next(self, interaction: discord.Interaction,
		#                 button: discord.ui.Button):

		if rarity == "7일":
			embed = discord.Embed(title=f"{skin} ({rarity})",
			                      description=f"{_}번 남음",
			                      color=0xfeff05)
		elif rarity == "30일":
			embed = discord.Embed(title=f"{skin} ({rarity})",
			                      description=f"{_}번 남음",
			                      color=0xe2731d)
		elif rarity == "무제한":
			embed = discord.Embed(title=f"{skin} ({rarity})",
			                      description=f"{_}번 남음",
			                      color=0xd939d2)

		_ -= 1
		#         print(_)
		#         # await interaction.response.edit_message(embed=embed,
		#         #                                         view=LeftTime(),
		#         #                                         ephemeral=True)

	elif _ == 0:

		if rarity == "7일":
			embed = discord.Embed(title=f"{skin} ({rarity})",
			                      description=f"남아있지 않음",
			                      color=0xfeff05)
		elif rarity == "30일":
			embed = discord.Embed(title=f"{skin} ({rarity})",
			                      description=f"남아있지 않음",
			                      color=0xe2731d)
		elif rarity == "무제한":
			embed = discord.Embed(title=f"{skin} ({rarity})",
			                      description=f"남아있지 않음",
			                      color=0xd939d2)

	embed.set_footer(icon_url=user.avatar, text=user.name)

	return embed


class AwesomePack(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		self.Image, self.Board, self.Settings, self.RankingFormat = loadJson()
		self.NormalSkins = json.loads(
		 open("AwesomePack.json", "r", encoding="UTF-8").read())["Normal"]
		self.ElfSkins = json.loads(
		 open("AwesomePack.json", "r", encoding="UTF-8").read())["Elf"]

	# /어썸팩
	@app_commands.command(name="어썸팩", description="어썸팩 시뮬레이션")
	async def awesomepacks(self, interaction: discord.Interaction):
		Image, NormalSkins, ElfSkins = self.Image, self.NormalSkins, self.ElfSkins

		class Select(discord.ui.Select):

			def __init__(self):
				options = [
				 discord.SelectOption(label="AwesomePack [Normal]",
				                      emoji="📦",
				                      description="어썸팩"),
				 discord.SelectOption(label="AwesomePack [Elf]",
				                      emoji="📦",
				                      description="엘프고 어썸팩"),
				]
				super().__init__(placeholder="메뉴를 선택해주세요.",
				                 max_values=1,
				                 min_values=1,
				                 options=options)

			async def callback(self, interaction: discord.Interaction):

				if self.values[0] == "AwesomePack [Normal]":
					embed = discord.Embed(
					 title=f"어썸팩",
					 description=
					 f"7일 (88%), 30일 (10%), 무제한 (2%)\n모든 스킨의 등장 확률은 동일합니다. (1/n)\n`2022.11.01` 기준 데이터이며, [여기](https://cafe.naver.com/onimobile/13134904)를 참고했습니다.",
					 color=0xcfb384)
					embed.set_thumbnail(url=Image['normal_awesomepack_url'])

					class SelectTime(discord.ui.View):

						def __init__(self):
							super().__init__()
							self.value = None

						@discord.ui.button(label="1", style=discord.ButtonStyle.gray, emoji='📦')
						async def time_1(self, interaction: discord.Interaction,
						                 button: discord.ui.Button):

							user = interaction.user

							skin = random.choice(NormalSkins)
							pick = random.choices(range(3), weights=[0.88, 0.1, 0.02])

							if pick == [0]: rarity = "7일"
							elif pick == [1]: rarity = "30일"
							elif pick == [2]: rarity = "무제한"
							_ = None

							embed = awesomepackRarity(user, rarity, skin, _)
							await interaction.response.send_message(embed=embed, ephemeral=False)

						@discord.ui.button(label="10 + 1",
						                   style=discord.ButtonStyle.gray,
						                   emoji='📦')
						async def time_11(self, interaction: discord.Interaction,
						                  button: discord.ui.Button):

							user = interaction.user

							skin = random.choice(NormalSkins)
							pick = random.choices(range(3), weights=[0.88, 0.1, 0.02])

							if pick == [0]: rarity = "7일"
							elif pick == [1]: rarity = "30일"
							elif pick == [2]: rarity = "무제한"
							_ = 10

							embed = awesomepackRarity(user, rarity, skin, _)

							class Next(discord.ui.View):

								def __init__(self):
									super().__init__()
									self.value = None

								@discord.ui.button(label="다음",
								                   style=discord.ButtonStyle.gray,
								                   emoji='📦')
								async def time_1(self, interaction: discord.Interaction,
								                 button: discord.ui.Button):

									# print(interaction.message.embeds[0].description.replace("번 남음", ""))
									_ = int(interaction.message.embeds[0].description.replace("번 남음",
									                                                          "")) - 1

									user = interaction.user

									skin = random.choice(NormalSkins)
									pick = random.choices(range(3), weights=[0.88, 0.1, 0.02])

									if pick == [0]: rarity = "7일"
									elif pick == [1]: rarity = "30일"
									elif pick == [2]: rarity = "무제한"

									embed = awesomepackRarity(user, rarity, skin, _)
									if embed.description == "남아있지 않음":
										await interaction.response.edit_message(embed=embed, view=None)

									else:
										await interaction.response.edit_message(embed=embed, view=Next())

							await interaction.response.send_message(embed=embed,
							                                        view=Next(),
							                                        ephemeral=False)

					await interaction.response.send_message(embed=embed,
					                                        view=SelectTime(),
					                                        ephemeral=True)
				if self.values[0] == "AwesomePack [Elf]":
					embed = discord.Embed(
					 title=f"엘프고 어썸팩",
					 description=
					 f"7일 (86%), 30일 (10%), 무제한 (4%)\n모든 스킨의 등장 확률은 동일합니다. (1/n)\n`2022.11.01` 기준 데이터이며, [여기](https://cafe.naver.com/onimobile/13134910)를 참고했습니다.",
					 color=0xcfb384)
					embed.set_thumbnail(url=Image['elf_awesomepack_url'])

					class SelectTime(discord.ui.View):

						def __init__(self):
							super().__init__()
							self.value = None

						@discord.ui.button(label="1", style=discord.ButtonStyle.gray, emoji='📦')
						async def time_1(self, interaction: discord.Interaction,
						                 button: discord.ui.Button):

							user = interaction.user

							skin = random.choice(ElfSkins)
							pick = random.choices(range(3), weights=[0.86, 0.1, 0.04])

							if pick == [0]: rarity = "7일"
							elif pick == [1]: rarity = "30일"
							elif pick == [2]: rarity = "무제한"
							_ = None

							embed = awesomepackRarity(user, rarity, skin, _)
							await interaction.response.send_message(embed=embed, ephemeral=False)

						@discord.ui.button(label="10 + 1",
						                   style=discord.ButtonStyle.gray,
						                   emoji='📦')
						async def time_11(self, interaction: discord.Interaction,
						                  button: discord.ui.Button):

							user = interaction.user

							skin = random.choice(ElfSkins)
							pick = random.choices(range(3), weights=[0.86, 0.1, 0.04])

							if pick == [0]: rarity = "7일"
							elif pick == [1]: rarity = "30일"
							elif pick == [2]: rarity = "무제한"
							_ = 10

							embed = awesomepackRarity(user, rarity, skin, _)

							class Next(discord.ui.View):

								def __init__(self):
									super().__init__()
									self.value = None

								@discord.ui.button(label="다음",
								                   style=discord.ButtonStyle.gray,
								                   emoji='📦')
								async def time_1(self, interaction: discord.Interaction,
								                 button: discord.ui.Button):

									# print(interaction.message.embeds[0].description.replace("번 남음", ""))
									_ = int(interaction.message.embeds[0].description.replace("번 남음",
									                                                          "")) - 1

									user = interaction.user

									skin = random.choice(ElfSkins)
									pick = random.choices(range(3), weights=[0.86, 0.1, 0.04])

									if pick == [0]: rarity = "7일"
									elif pick == [1]: rarity = "30일"
									elif pick == [2]: rarity = "무제한"

									embed = awesomepackRarity(user, rarity, skin, _)
									if embed.description == "남아있지 않음":
										await interaction.response.edit_message(embed=embed, view=None)

									else:
										await interaction.response.edit_message(embed=embed, view=Next())

							await interaction.response.send_message(embed=embed,
							                                        view=Next(),
							                                        ephemeral=False)

					await interaction.response.send_message(embed=embed,
					                                        view=SelectTime(),
					                                        ephemeral=True)

		class SelectView(discord.ui.View):

			def __init__(self, *, timeout=120):
				super().__init__(timeout=timeout)
				self.add_item(Select())

		await interaction.response.send_message(view=SelectView(), ephemeral=True)


async def setup(bot):
	await bot.add_cog(AwesomePack(bot))
