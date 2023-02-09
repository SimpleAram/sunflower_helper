from discord.ext import commands, tasks
import discord
import requests
from Domisol import *
import urllib


class LoopTasks(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		self.Image, self.Board, self.Settings, self.RankingFormat = loadJson()
		self.SendGuild = self.Board["SendGuild"]
		self.SendChannel = self.Board["SendChannel"]
		self.syncGameActivity.start()
		self.loadingBoards.start()

	@tasks.loop(seconds=60)
	async def syncGameActivity(self):
		channel_url = requests.get(
		 "https://zh-kr-g-web.awesomepiece.com/api/server-list?version={0}")

		allUserCount = 0
		for i in channel_url.json():
			allUserCount += i['userCount']

		activity = discord.Game(f"{format(allUserCount, ',d')} 명과 함께 좀비고")
		await self.bot.change_presence(status=discord.Status.online,
		                               activity=activity)

	@tasks.loop(seconds=10)
	async def loadingBoards(self):
		Boards = lastBoards(self.Board)
		Notice = Boards[0]
		Event = Boards[1]
		Selfstudy = Boards[2]

		if self.Board["lastNotice"] != Notice[0]:
			Title = Notice[2].replace('&lt;', '<')
			Title = Title.replace('&gt;', '>')
			embed = discord.Embed(title=f'**「 {Notice[1]} 」**',
			                      description=Title,
			                      color=0x01c73c)

			embed.add_field(name=f'https://cafe.naver.com/onimobile/{Notice[0]}',
			                value=f'_ _',
			                inline=False)

			embed.set_footer(text=Notice[3], icon_url=self.Image['cafe_url'])

			embed.timestamp = datetime.now(KST)

			try:
				previewPicture = urllib.parse.quote(Notice[5].replace(
				 '?type=f100_100', ''))
				embed.set_thumbnail(url=previewPicture.replace('https%3A', 'https:'))
			except:
				pass

			guild = self.bot.get_guild(self.SendGuild)
			channel = guild.get_channel(self.SendChannel)
			await channel.send(embed=embed)
			print(f"\n ┌ 새로운 게시글이 감지되었습니다.")
			print(f" └ 감지된 게시글 : [{Notice[1]}] {Title}")
			self.Board["lastNotice"] = Notice[0]
			json.dump(self.Board, open("LastBoard.json", "w"), indent=4)

		if self.Board["lastEvent"] != Event[0]:
			Title = Event[2].replace('&lt;', '<')
			Title = Title.replace('&gt;', '>')
			embed = discord.Embed(title=f'**「 {Event[1]} 」**',
			                      description=Title,
			                      color=0x01c73c)

			embed.add_field(name=f'https://cafe.naver.com/onimobile/{Event[0]}',
			                value=f'_ _',
			                inline=False)

			embed.set_footer(text=Event[3], icon_url=self.Image['cafe_url'])

			embed.timestamp = datetime.now(KST)

			try:
				previewPicture = urllib.parse.quote(Event[5].replace('?type=f100_100', ''))
				embed.set_thumbnail(url=previewPicture.replace('https%3A', 'https:'))
			except:
				pass

			guild = self.bot.get_guild(self.SendGuild)
			channel = guild.get_channel(self.SendChannel)
			await channel.send(embed=embed)
			print(f"\n ┌ 새로운 게시글이 감지되었습니다.")
			print(f" └ 감지된 게시글 : [{Event[1]}] {Title}")
			self.Board["lastEvent"] = Event[0]
			json.dump(self.Board, open("LastBoard.json", "w"), indent=4)

		if self.Board["lastSelfstudy"] != Selfstudy[0]:
			Title = Selfstudy[2].replace('&lt;', '<')
			Title = Title.replace('&gt;', '>')
			embed = discord.Embed(title=f'**「 자율학습 」**',
			                      description=Title,
			                      color=0x01c73c)

			embed.add_field(name=f'https://cafe.naver.com/onimobile/{Selfstudy[0]}',
			                value=f'_ _',
			                inline=False)

			embed.set_footer(text=Selfstudy[3], icon_url=self.Image['cafe_url'])

			embed.timestamp = datetime.now(KST)

			try:
				previewPicture = urllib.parse.quote(Selfstudy[5].replace(
				 '?type=f100_100', ''))
				embed.set_thumbnail(url=previewPicture.replace('https%3A', 'https:'))
			except:
				pass

			guild = self.bot.get_guild(self.SendGuild)
			channel = guild.get_channel(self.SendChannel)
			await channel.send(embed=embed)
			print(f"\n ┌ 새로운 게시글이 감지되었습니다.")
			print(f" └ 감지된 게시글 : [자율학습] {Title}")
			self.Board["lastSelfstudy"] = Selfstudy[0]
			json.dump(self.Board, open("LastBoard.json", "w"), indent=4)


async def setup(bot):
	await bot.add_cog(LoopTasks(bot))
