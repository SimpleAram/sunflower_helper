# -*- coding: utf-8 -*-
import discord
from discord.ext import commands, tasks
from Helper_Sol import *
from cmath import log
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.environ['TOKEN']

intents = discord.Intents.default()

bot = commands.Bot(command_prefix = ["!"],
                   intents = intents,
                   help_command = None)

cogs_path = 'Cogs'
abs_cogs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                             cogs_path)


def floadJson():
	global Image, Board, Settings
	Image, Board, Settings = loadJson()


@bot.event
async def on_ready():
	guild = bot.get_guild(1073107247212793976)
	channel = guild.get_channel(1073107247212793979)
	await channel.send(
	 datetime.now(KST).strftime(
	  "> :small_blue_diamond: %Y-%m-%d %p %I:%M:%S".encode(
	   'unicode-escape').decode()).encode().decode("unicode-escape").replace(
	    'PM', '오후').replace('AM', '오전'))

	printf("온라인으로 활성화가 되었습니다.")
	printf(f"> {bot.user}{Fore.YELLOW} (ID: {bot.user.id})")
	printf(f" • 감지된 활동 중인 서버 수 : {Fore.YELLOW}{format(len(bot.guilds), ',d')}")
	printf(f" • 디스코드 버전 : {Fore.YELLOW}{discord.__version__}")

	try:
		floadJson()

		for ext in os.listdir(abs_cogs_path):
			if ext.endswith(".py"):
				await bot.load_extension(f"Cogs.{ext.split('.')[0]}")

	except Exception as e:
		print(f'{Fore.RED}{e}{Fore.WHITE}')


@bot.event
async def on_command_error(ctx, error):
	pass


# !리로드
@bot.command(name="리로드", description="리로드", pass_context=True)
async def reload(ctx):
	if isAdmin(ctx.message.author.id, Settings):
		try:
			floadJson()

			for ext in os.listdir(abs_cogs_path):
				if ext.endswith(".py"):
					printf(ext.split('.')[0])
					try:
						await bot.unload_extension(f"Cogs.{ext.split('.')[0]}")
					except Exception as E:
						await ctx.reply(f"리로드 실패\n `{E}`")
					await bot.load_extension(f"Cogs.{ext.split('.')[0]}")

			printf("리로드 성공")
			await ctx.reply("리로드 성공")

		except Exception as E:
			printf("리로드 실패")
			await ctx.reply(f"리로드 실패\n`{E}`")

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
