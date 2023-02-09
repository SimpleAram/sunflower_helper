import json
from colorama import Fore, Style
from datetime import datetime
from pytz import timezone
import requests
import discord
import random

KST = timezone('Asia/Seoul')
prefix = (Style.BRIGHT + Fore.GREEN + datetime.now(KST).strftime("%H:%M:%S") +
          Style.NORMAL + Fore.WHITE)


def printf(msg):
  print(f"{prefix} | {msg}{Fore.WHITE}")


def loadJson():
  ImagesJson = open("Images.json", "r", encoding="UTF-8")
  Image = json.loads(ImagesJson.read())

  LastBoardJson = open("LastBoard.json", "r", encoding="UTF-8")
  Board = json.loads(LastBoardJson.read())

  SettingsJson = open("Settings.json", "r", encoding="UTF-8")
  Settings = json.loads(SettingsJson.read())

  RankingFormatJson = open("RankingFormat.json", "r", encoding="UTF-8")
  RankingFormat = json.loads(RankingFormatJson.read())

  return Image, Board, Settings, RankingFormat


def isAdmin(id, Settings):
  return id in Settings["Admins"]


def lastBoards(Board):
  Boards = []

  for url in Board["urls"]:
    req = requests.get(Board['urls'][url])

    try:
      dJson = req.json()["message"]["result"]["articleList"][0]["item"]
      articleId = dJson["articleId"]
      try:
        headName = dJson["headName"]
      except:
        headName = "!"

      subject = dJson["subject"]
      writerNickname = dJson["writerNickname"]
      writeDateTimestamp = int(dJson["writeDateTimestamp"] / 1000)
      try:
        representImage = dJson["representImage"]
      except:
        representImage = None

      Boards.append([
        articleId, headName, subject, writerNickname, writeDateTimestamp,
        representImage
      ])

    except:
      print(req.json())

  return Boards
