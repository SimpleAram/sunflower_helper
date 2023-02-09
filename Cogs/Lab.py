from discord.ext import commands
from discord import app_commands
import discord
from Domisol import *

def getLabSkins(skins: json, Level: int) -> list:
	# skins와 Level를 필요로 함.
	# skins는 LabFormat.json을 불러올때 선언된 변수
	# Level은 LabFormat.json에 몇레벨을 불러올지
	# -> list == return 값을 list로 한다.

	Level = f"Level{Level}" # json은 Level숫자 형태로 되어있기때문에 Level변수를 변화시켜주기
	# int -> str

	randomInt = random.randrange(0, len(skins[Level])) # 스킨 갯수를 숫자로 변환한후 랜덤 숫자 뽑기
	# range를 이용했기때문에 0 ~ 스킨갯수-1 까지의 값이 나온다.

	skin = "" # 어떤 스킨이 뽑혔는지 확인할 변수 (없어도 되긴 함)
	counting = 0 # For문 횟수 세기
	for s in skins[Level]: # For문
		if randomInt == counting: # 만약 스킨 갯수중 랜덤 숫자 range (0 ~ 스킨갯수) 가 For문 횟수랑 같다?
			skin = s # 지금 For문으로 반복되고있는 s라는 변수를 skin이라는 변수로 선언함
			break # for문 탈출
		
		# 아니면
		counting += 1 # 횟수 + 1

	return [skin, skins[Level][skin]]
	# 반환
	# [스킨이름, 스킨이름에 들어가있는 리스트]



class Lab(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		self.Image, self.Board, self.Settings, self.RankingFormat = loadJson()
		self.LabFormat = json.loads(open("LabFormat.json", "r", encoding="UTF-8").read())

	# /연구실
	@app_commands.command(name="연구실", description="연구실 시뮬레이션")
	async def lab(self, interaction: discord.Interaction, level: int):
		LabFormat = self.LabFormat

		# skinData = getLabSkins(LabFormat, 9)
		# skin = skinData[0]
		# type = skinData[1][0]
		# rarity = skinData[1][1]

		# print(skinData)
		# print(skin, type, rarity)


		if 1 <= level <= 15:

			# 2022.11.01 기준 데이터
			# https://cafe.naver.com/ArticleList.nhn?search.clubid=27131930&search.menuid=89&search.boardtype=L

			class reResearch(discord.ui.View):

				def __init__(self):
					super().__init__()
					self.value = None

				# user = interaction.user

				@discord.ui.button(label="재연구", style=discord.ButtonStyle.gray)
				async def reResearch(self, interaction: discord.Interaction, button: discord.ui.Button):
					
					if level == 1:

						skinData = getLabSkins(LabFormat, 1)

						skin = skinData[0]
						type = skinData[1][0]
						rarity = skinData[1][1]

						embed = labSkinsRarity(level, type, rarity, skin)

					elif level == 2:

						pick = random.choices(range(2), weights=[0.6, 0.4])

						if pick == [0]:
							skinData = getLabSkins(LabFormat, 1)
						elif pick == [1]:
							skinData = getLabSkins(LabFormat, 2)

						skin = skinData[0]
						type = skinData[1][0]
						rarity = skinData[1][1]

						embed = labSkinsRarity(level, type, rarity, skin)

					elif level == 3:

						pick = random.choices(range(3), weights=[0.5, 0.3, 0.2])

						if pick == [0]:
							skinData = getLabSkins(LabFormat, 1)
						elif pick == [1]:
							skinData = getLabSkins(LabFormat, 2)
						elif pick == [2]:
							skinData = getLabSkins(LabFormat, 3)

						skin = skinData[0]
						type = skinData[1][0]
						rarity = skinData[1][1]

						embed = labSkinsRarity(level, type, rarity, skin)

					elif level == 4:

						pick = random.choices(range(4), weights=[0.4, 0.3, 0.2, 0.1])

						if pick == [0]:
							skinData = getLabSkins(LabFormat, 1)
						elif pick == [1]:
							skinData = getLabSkins(LabFormat, 2)
						elif pick == [2]:
							skinData = getLabSkins(LabFormat, 3)
						elif pick == [3]:
							skinData = getLabSkins(LabFormat, 4)

						skin = skinData[0]
						type = skinData[1][0]
						rarity = skinData[1][1]

						embed = labSkinsRarity(level, type, rarity, skin)

					elif level == 5:

						pick = random.choices(range(5), weights=[0.3, 0.25, 0.2, 0.15, 0.1])

						if pick == [0]:
							skinData = getLabSkins(LabFormat, 1)
						elif pick == [1]:
							skinData = getLabSkins(LabFormat, 2)
						elif pick == [2]:
							skinData = getLabSkins(LabFormat, 3)
						elif pick == [3]:
							skinData = getLabSkins(LabFormat, 4)
						elif pick == [4]:
							skinData = getLabSkins(LabFormat, 5)

						skin = skinData[0]
						type = skinData[1][0]
						rarity = skinData[1][1]

						embed = labSkinsRarity(level, type, rarity, skin)

					elif level == 6:

						pick = random.choices(range(4), weights=[0.4, 0.3, 0.2, 0.1])

						if pick == [0]:
							skinData = getLabSkins(LabFormat, 2)
						elif pick == [1]:
							skinData = getLabSkins(LabFormat, 3)
						elif pick == [2]:
							skinData = getLabSkins(LabFormat, 4)
						elif pick == [3]:
							skinData = getLabSkins(LabFormat, 5)

						skin = skinData[0]
						type = skinData[1][0]
						rarity = skinData[1][1]

						embed = labSkinsRarity(level, type, rarity, skin)

					elif level == 7:

						pick = random.choices(range(5), weights=[0.3, 0.25, 0.2, 0.15, 0.1])

						if pick == [0]:
							skinData = getLabSkins(LabFormat, 2)
						elif pick == [1]:
							skinData = getLabSkins(LabFormat, 3)
						elif pick == [2]:
							skinData = getLabSkins(LabFormat, 4)
						elif pick == [3]:
							skinData = getLabSkins(LabFormat, 5)
						elif pick == [4]:
							skinData = getLabSkins(LabFormat, 6)

						skin = skinData[0]
						type = skinData[1][0]
						rarity = skinData[1][1]

						embed = labSkinsRarity(level, type, rarity, skin)

					elif level == 8:

						pick = random.choices(range(6), weights=[0.25, 0.25, 0.2, 0.15, 0.1, 0.05])

						if pick == [0]:
							skinData = getLabSkins(LabFormat, 2)
						elif pick == [1]:
							skinData = getLabSkins(LabFormat, 3)
						elif pick == [2]:
							skinData = getLabSkins(LabFormat, 4)
						elif pick == [3]:
							skinData = getLabSkins(LabFormat, 5)
						elif pick == [4]:
							skinData = getLabSkins(LabFormat, 6)
						elif pick == [5]:
							skinData = getLabSkins(LabFormat, 7)

						skin = skinData[0]
						type = skinData[1][0]
						rarity = skinData[1][1]

						embed = labSkinsRarity(level, type, rarity, skin)

					elif level == 9:

						pick = random.choices(range(7), weights=[0.2, 0.25, 0.2, 0.15, 0.1, 0.05, 0.05])

						if pick == [0]:
							skinData = getLabSkins(LabFormat, 2)
						elif pick == [1]:
							skinData = getLabSkins(LabFormat, 3)
						elif pick == [2]:
							skinData = getLabSkins(LabFormat, 4)
						elif pick == [3]:
							skinData = getLabSkins(LabFormat, 5)
						elif pick == [4]:
							skinData = getLabSkins(LabFormat, 6)
						elif pick == [5]:
							skinData = getLabSkins(LabFormat, 7)
						elif pick == [6]:
							skinData = getLabSkins(LabFormat, 8)

						skin = skinData[0]
						type = skinData[1][0]
						rarity = skinData[1][1]

						embed = labSkinsRarity(level, type, rarity, skin)

					elif level == 10:

						pick = random.choices(range(7), weights=[0.1, 0.25, 0.2, 0.15, 0.15, 0.1, 0.05])

						if pick == [0]:
							skinData = getLabSkins(LabFormat, 2)
						elif pick == [1]:
							skinData = getLabSkins(LabFormat, 3)
						elif pick == [2]:
							skinData = getLabSkins(LabFormat, 4)
						elif pick == [3]:
							skinData = getLabSkins(LabFormat, 5)
						elif pick == [4]:
							skinData = getLabSkins(LabFormat, 6)
						elif pick == [5]:
							skinData = getLabSkins(LabFormat, 7)
						elif pick == [6]:
							skinData = getLabSkins(LabFormat, 8)

						skin = skinData[0]
						type = skinData[1][0]
						rarity = skinData[1][1]

						embed = labSkinsRarity(level, type, rarity, skin)

					elif level == 11:

						pick = random.choices(range(8), weights=[0.05, 0.2, 0.2, 0.2, 0.15, 0.1, 0.05, 0.05])

						if pick == [0]:
							skinData = getLabSkins(LabFormat, 2)
						elif pick == [1]:
							skinData = getLabSkins(LabFormat, 3)
						elif pick == [2]:
							skinData = getLabSkins(LabFormat, 4)
						elif pick == [3]:
							skinData = getLabSkins(LabFormat, 5)
						elif pick == [4]:
							skinData = getLabSkins(LabFormat, 6)
						elif pick == [5]:
							skinData = getLabSkins(LabFormat, 7)
						elif pick == [6]:
							skinData = getLabSkins(LabFormat, 8)
						elif pick == [7]:
							skinData = getLabSkins(LabFormat, 9)

						skin = skinData[0]
						type = skinData[1][0]
						rarity = skinData[1][1]

						embed = labSkinsRarity(level, type, rarity, skin)

					elif level == 12:

						pick = random.choices(range(8), weights=[0.04, 0.06, 0.2, 0.2, 0.15, 0.15, 0.1, 0.1])

						if pick == [0]:
							skinData = getLabSkins(LabFormat, 2)
						elif pick == [1]:
							skinData = getLabSkins(LabFormat, 3)
						elif pick == [2]:
							skinData = getLabSkins(LabFormat, 4)
						elif pick == [3]:
							skinData = getLabSkins(LabFormat, 5)
						elif pick == [4]:
							skinData = getLabSkins(LabFormat, 6)
						elif pick == [5]:
							skinData = getLabSkins(LabFormat, 7)
						elif pick == [6]:
							skinData = getLabSkins(LabFormat, 8)
						elif pick == [7]:
							skinData = getLabSkins(LabFormat, 9)

						skin = skinData[0]
						type = skinData[1][0]
						rarity = skinData[1][1]

						embed = labSkinsRarity(level, type, rarity, skin)

					elif level == 13:

						pick = random.choices(range(9), weights=[0.03, 0.05, 0.1, 0.2, 0.15, 0.15, 0.15, 0.1, 0.07])

						if pick == [0]:
							skinData = getLabSkins(LabFormat, 2)
						elif pick == [1]:
							skinData = getLabSkins(LabFormat, 3)
						elif pick == [2]:
							skinData = getLabSkins(LabFormat, 4)
						elif pick == [3]:
							skinData = getLabSkins(LabFormat, 5)
						elif pick == [4]:
							skinData = getLabSkins(LabFormat, 6)
						elif pick == [5]:
							skinData = getLabSkins(LabFormat, 7)
						elif pick == [6]:
							skinData = getLabSkins(LabFormat, 8)
						elif pick == [7]:
							skinData = getLabSkins(LabFormat, 9)
						elif pick == [8]:
							skinData = getLabSkins(LabFormat, 10)

						skin = skinData[0]
						type = skinData[1][0]
						rarity = skinData[1][1]

						embed = labSkinsRarity(level, type, rarity, skin)

					elif level == 14:

						pick = random.choices(range(9), weights=[0.02, 0.03, 0.03, 0.15, 0.2, 0.15, 0.2, 0.12, 0.1])

						if pick == [0]:
							skinData = getLabSkins(LabFormat, 2)
						elif pick == [1]:
							skinData = getLabSkins(LabFormat, 3)
						elif pick == [2]:
							skinData = getLabSkins(LabFormat, 4)
						elif pick == [3]:
							skinData = getLabSkins(LabFormat, 5)
						elif pick == [4]:
							skinData = getLabSkins(LabFormat, 6)
						elif pick == [5]:
							skinData = getLabSkins(LabFormat, 7)
						elif pick == [6]:
							skinData = getLabSkins(LabFormat, 8)
						elif pick == [7]:
							skinData = getLabSkins(LabFormat, 9)
						elif pick == [8]:
							skinData = getLabSkins(LabFormat, 10)

						skin = skinData[0]
						type = skinData[1][0]
						rarity = skinData[1][1]

						embed = labSkinsRarity(level, type, rarity, skin)

					elif level == 15:

						pick = random.choices(range(9), weights=[0.01, 0.02, 0.02, 0.1, 0.15, 0.15, 0.2, 0.2, 0.15])

						if pick == [0]:
							skinData = getLabSkins(LabFormat, 2)
						elif pick == [1]:
							skinData = getLabSkins(LabFormat, 3)
						elif pick == [2]:
							skinData = getLabSkins(LabFormat, 4)
						elif pick == [3]:
							skinData = getLabSkins(LabFormat, 5)
						elif pick == [4]:
							skinData = getLabSkins(LabFormat, 6)
						elif pick == [5]:
							skinData = getLabSkins(LabFormat, 7)
						elif pick == [6]:
							skinData = getLabSkins(LabFormat, 8)
						elif pick == [7]:
							skinData = getLabSkins(LabFormat, 9)
						elif pick == [8]:
							skinData = getLabSkins(LabFormat, 10)

						skin = skinData[0]
						type = skinData[1][0]
						rarity = skinData[1][1]

						embed = labSkinsRarity(level, type, rarity, skin)

					await interaction.response.edit_message(embed = embed)
								
					###

			if level == 1:

				skinData = getLabSkins(LabFormat, 1)

				skin = skinData[0]
				type = skinData[1][0]
				rarity = skinData[1][1]

				embed = labSkinsRarity(level, type, rarity, skin)

			elif level == 2:

				pick = random.choices(range(2), weights=[0.6, 0.4])

				if pick == [0]:
					skinData = getLabSkins(LabFormat, 1)
				elif pick == [1]:
					skinData = getLabSkins(LabFormat, 2)

				skin = skinData[0]
				type = skinData[1][0]
				rarity = skinData[1][1]

				embed = labSkinsRarity(level, type, rarity, skin)

			elif level == 3:

				pick = random.choices(range(3), weights=[0.5, 0.3, 0.2])

				if pick == [0]:
					skinData = getLabSkins(LabFormat, 1)
				elif pick == [1]:
					skinData = getLabSkins(LabFormat, 2)
				elif pick == [2]:
					skinData = getLabSkins(LabFormat, 3)

				skin = skinData[0]
				type = skinData[1][0]
				rarity = skinData[1][1]

				embed = labSkinsRarity(level, type, rarity, skin)

			elif level == 4:

				pick = random.choices(range(4), weights=[0.4, 0.3, 0.2, 0.1])

				if pick == [0]:
					skinData = getLabSkins(LabFormat, 1)
				elif pick == [1]:
					skinData = getLabSkins(LabFormat, 2)
				elif pick == [2]:
					skinData = getLabSkins(LabFormat, 3)
				elif pick == [3]:
					skinData = getLabSkins(LabFormat, 4)

				skin = skinData[0]
				type = skinData[1][0]
				rarity = skinData[1][1]

				embed = labSkinsRarity(level, type, rarity, skin)

			elif level == 5:

				pick = random.choices(range(5), weights=[0.3, 0.25, 0.2, 0.15, 0.1])

				if pick == [0]:
					skinData = getLabSkins(LabFormat, 1)
				elif pick == [1]:
					skinData = getLabSkins(LabFormat, 2)
				elif pick == [2]:
					skinData = getLabSkins(LabFormat, 3)
				elif pick == [3]:
					skinData = getLabSkins(LabFormat, 4)
				elif pick == [4]:
					skinData = getLabSkins(LabFormat, 5)

				skin = skinData[0]
				type = skinData[1][0]
				rarity = skinData[1][1]

				embed = labSkinsRarity(level, type, rarity, skin)

			elif level == 6:

				pick = random.choices(range(4), weights=[0.4, 0.3, 0.2, 0.1])

				if pick == [0]:
					skinData = getLabSkins(LabFormat, 2)
				elif pick == [1]:
					skinData = getLabSkins(LabFormat, 3)
				elif pick == [2]:
					skinData = getLabSkins(LabFormat, 4)
				elif pick == [3]:
					skinData = getLabSkins(LabFormat, 5)

				skin = skinData[0]
				type = skinData[1][0]
				rarity = skinData[1][1]

				embed = labSkinsRarity(level, type, rarity, skin)

			elif level == 7:

				pick = random.choices(range(5), weights=[0.3, 0.25, 0.2, 0.15, 0.1])

				if pick == [0]:
					skinData = getLabSkins(LabFormat, 2)
				elif pick == [1]:
					skinData = getLabSkins(LabFormat, 3)
				elif pick == [2]:
					skinData = getLabSkins(LabFormat, 4)
				elif pick == [3]:
					skinData = getLabSkins(LabFormat, 5)
				elif pick == [4]:
					skinData = getLabSkins(LabFormat, 6)

				skin = skinData[0]
				type = skinData[1][0]
				rarity = skinData[1][1]

				embed = labSkinsRarity(level, type, rarity, skin)

			elif level == 8:

				pick = random.choices(range(6), weights=[0.25, 0.25, 0.2, 0.15, 0.1, 0.05])

				if pick == [0]:
					skinData = getLabSkins(LabFormat, 2)
				elif pick == [1]:
					skinData = getLabSkins(LabFormat, 3)
				elif pick == [2]:
					skinData = getLabSkins(LabFormat, 4)
				elif pick == [3]:
					skinData = getLabSkins(LabFormat, 5)
				elif pick == [4]:
					skinData = getLabSkins(LabFormat, 6)
				elif pick == [5]:
					skinData = getLabSkins(LabFormat, 7)

				skin = skinData[0]
				type = skinData[1][0]
				rarity = skinData[1][1]

				embed = labSkinsRarity(level, type, rarity, skin)

			elif level == 9:

				pick = random.choices(range(7), weights=[0.2, 0.25, 0.2, 0.15, 0.1, 0.05, 0.05])

				if pick == [0]:
					skinData = getLabSkins(LabFormat, 2)
				elif pick == [1]:
					skinData = getLabSkins(LabFormat, 3)
				elif pick == [2]:
					skinData = getLabSkins(LabFormat, 4)
				elif pick == [3]:
					skinData = getLabSkins(LabFormat, 5)
				elif pick == [4]:
					skinData = getLabSkins(LabFormat, 6)
				elif pick == [5]:
					skinData = getLabSkins(LabFormat, 7)
				elif pick == [6]:
					skinData = getLabSkins(LabFormat, 8)

				skin = skinData[0]
				type = skinData[1][0]
				rarity = skinData[1][1]

				embed = labSkinsRarity(level, type, rarity, skin)

			elif level == 10:

				pick = random.choices(range(7), weights=[0.1, 0.25, 0.2, 0.15, 0.15, 0.1, 0.05])

				if pick == [0]:
					skinData = getLabSkins(LabFormat, 2)
				elif pick == [1]:
					skinData = getLabSkins(LabFormat, 3)
				elif pick == [2]:
					skinData = getLabSkins(LabFormat, 4)
				elif pick == [3]:
					skinData = getLabSkins(LabFormat, 5)
				elif pick == [4]:
					skinData = getLabSkins(LabFormat, 6)
				elif pick == [5]:
					skinData = getLabSkins(LabFormat, 7)
				elif pick == [6]:
					skinData = getLabSkins(LabFormat, 8)

				skin = skinData[0]
				type = skinData[1][0]
				rarity = skinData[1][1]

				embed = labSkinsRarity(level, type, rarity, skin)

			elif level == 11:

				pick = random.choices(range(8), weights=[0.05, 0.2, 0.2, 0.2, 0.15, 0.1, 0.05, 0.05])

				if pick == [0]:
					skinData = getLabSkins(LabFormat, 2)
				elif pick == [1]:
					skinData = getLabSkins(LabFormat, 3)
				elif pick == [2]:
					skinData = getLabSkins(LabFormat, 4)
				elif pick == [3]:
					skinData = getLabSkins(LabFormat, 5)
				elif pick == [4]:
					skinData = getLabSkins(LabFormat, 6)
				elif pick == [5]:
					skinData = getLabSkins(LabFormat, 7)
				elif pick == [6]:
					skinData = getLabSkins(LabFormat, 8)
				elif pick == [7]:
					skinData = getLabSkins(LabFormat, 9)

				skin = skinData[0]
				type = skinData[1][0]
				rarity = skinData[1][1]

				embed = labSkinsRarity(level, type, rarity, skin)

			elif level == 12:

				pick = random.choices(range(8), weights=[0.04, 0.06, 0.2, 0.2, 0.15, 0.15, 0.1, 0.1])

				if pick == [0]:
					skinData = getLabSkins(LabFormat, 2)
				elif pick == [1]:
					skinData = getLabSkins(LabFormat, 3)
				elif pick == [2]:
					skinData = getLabSkins(LabFormat, 4)
				elif pick == [3]:
					skinData = getLabSkins(LabFormat, 5)
				elif pick == [4]:
					skinData = getLabSkins(LabFormat, 6)
				elif pick == [5]:
					skinData = getLabSkins(LabFormat, 7)
				elif pick == [6]:
					skinData = getLabSkins(LabFormat, 8)
				elif pick == [7]:
					skinData = getLabSkins(LabFormat, 9)

				skin = skinData[0]
				type = skinData[1][0]
				rarity = skinData[1][1]

				embed = labSkinsRarity(level, type, rarity, skin)

			elif level == 13:

				pick = random.choices(range(9), weights=[0.03, 0.05, 0.1, 0.2, 0.15, 0.15, 0.15, 0.1, 0.07])

				if pick == [0]:
					skinData = getLabSkins(LabFormat, 2)
				elif pick == [1]:
					skinData = getLabSkins(LabFormat, 3)
				elif pick == [2]:
					skinData = getLabSkins(LabFormat, 4)
				elif pick == [3]:
					skinData = getLabSkins(LabFormat, 5)
				elif pick == [4]:
					skinData = getLabSkins(LabFormat, 6)
				elif pick == [5]:
					skinData = getLabSkins(LabFormat, 7)
				elif pick == [6]:
					skinData = getLabSkins(LabFormat, 8)
				elif pick == [7]:
					skinData = getLabSkins(LabFormat, 9)
				elif pick == [8]:
					skinData = getLabSkins(LabFormat, 10)

				skin = skinData[0]
				type = skinData[1][0]
				rarity = skinData[1][1]

				embed = labSkinsRarity(level, type, rarity, skin)

			elif level == 14:

				pick = random.choices(range(9), weights=[0.02, 0.03, 0.03, 0.15, 0.2, 0.15, 0.2, 0.12, 0.1])

				if pick == [0]:
					skinData = getLabSkins(LabFormat, 2)
				elif pick == [1]:
					skinData = getLabSkins(LabFormat, 3)
				elif pick == [2]:
					skinData = getLabSkins(LabFormat, 4)
				elif pick == [3]:
					skinData = getLabSkins(LabFormat, 5)
				elif pick == [4]:
					skinData = getLabSkins(LabFormat, 6)
				elif pick == [5]:
					skinData = getLabSkins(LabFormat, 7)
				elif pick == [6]:
					skinData = getLabSkins(LabFormat, 8)
				elif pick == [7]:
					skinData = getLabSkins(LabFormat, 9)
				elif pick == [8]:
					skinData = getLabSkins(LabFormat, 10)

				skin = skinData[0]
				type = skinData[1][0]
				rarity = skinData[1][1]

				embed = labSkinsRarity(level, type, rarity, skin)

			elif level == 15:

				pick = random.choices(range(9), weights=[0.01, 0.02, 0.02, 0.1, 0.15, 0.15, 0.2, 0.2, 0.15])

				if pick == [0]:
					skinData = getLabSkins(LabFormat, 2)
				elif pick == [1]:
					skinData = getLabSkins(LabFormat, 3)
				elif pick == [2]:
					skinData = getLabSkins(LabFormat, 4)
				elif pick == [3]:
					skinData = getLabSkins(LabFormat, 5)
				elif pick == [4]:
					skinData = getLabSkins(LabFormat, 6)
				elif pick == [5]:
					skinData = getLabSkins(LabFormat, 7)
				elif pick == [6]:
					skinData = getLabSkins(LabFormat, 8)
				elif pick == [7]:
					skinData = getLabSkins(LabFormat, 9)
				elif pick == [8]:
					skinData = getLabSkins(LabFormat, 10)

				skin = skinData[0]
				type = skinData[1][0]
				rarity = skinData[1][1]

				embed = labSkinsRarity(level, type, rarity, skin)

			await interaction.response.send_message(embed=embed, view=reResearch(), ephemeral=False)
						
		else:
			embed = discord.Embed(title="오류 발생",
								description="유효하지 않은 레벨이 입력되었습니다.",
								color=0xfa2616)
			await interaction.response.send_message(embed=embed, ephemeral=True, delete_after=4)


def labSkinsRarity(level: int, type: str, rarity: str, skin: str):
	
	if rarity == "일반":
		embed = discord.Embed(title=f"{skin}",
							description=f"[{rarity}] {type} 스킨",
							color=0xa39ea0)

	elif rarity == "고급":
		embed = discord.Embed(title=f"{skin}",
							description=f"[{rarity}] {type} 스킨",
							color=0x2f832e)

	elif rarity == "희귀":
		embed = discord.Embed(title=f"{skin}",
							description=f"[{rarity}] {type} 스킨",
							color=0x2f6ca2)

	elif rarity == "특수":
		embed = discord.Embed(title=f"{skin}",
							description=f"[{rarity}] {type} 스킨",
							color=0x99212c)

	elif rarity == "연구실전용":
		embed = discord.Embed(title=f"{skin}",
							description=f"[{rarity}] {type} 스킨",
							color=0x841699)

	embed.set_footer(text=f'- 연구실 레벨 : {level}')

	return embed

async def setup(bot):
	await bot.add_cog(Lab(bot))