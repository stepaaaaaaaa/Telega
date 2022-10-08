from email.mime import image
from turtle import title
from telebot import types
import telebot
import urllib
import json
import random
import requests
from requests.models import Response

import config


bot = telebot.TeleBot(token=config.TOKEN)



@bot.message_handler(commands=['anime'])
def help (message: telebot.types.Message):
    helper: str = '''
    Выберите аниме: 
    /Death_Note, 
    /Onepunchman_1_season,
    /Onepunchman_2_season, 
    /Inuyashiki,
    /Attack_on_Titan_1_season,
    /Attack_on_Titan_2_season,
    /Attack_on_Titan_3_season,
    /Attack_on_Titan_4_season,
    /Naruto_1_season,
    /Naruto_2_season,
    /Akame_ga_kill,
    /Boku_dake_ga_Inai_Machi,
    /Mirai_nikki,
    /Parasyte,
    /Cowboy_Bibop,
    /Another
    '''
    bot.send_message(message.chat.id, helper)


@bot.message_handler(commands=['Death_Note'])
def anime1 (message: telebot.types.Message):
    enote: str = "Выберите серию \n /choose_series1"
    img: image = open("Death_Note.png", "rb")
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['choose_series1'])
def onime1 (message: telebot.types.Message):
    for i in range(1, 38):
        enote = (f"https://jut.su/bookofd/episode-{i}.html")
        bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['Onepunchman_1_season'])
def anime2 (message: telebot.types.Message):
    enote: str = "Выберите серию \n /choose_series2"
    img: image = open("one_punch_man.png", "rb")
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['choose_series2'])
def onime2 (message: telebot.types.Message):
    for i in range(1, 13):
        enote = (f"https://jut.su/onepunchman/season-1/episode-{i}.html")
        bot.send_message(message.chat.id, enote)


@bot.message_handler(commands=['Onepunchman_2_season'])
def anime3 (message: telebot.types.Message):
    enote: str = "Выберите серию \n /choose_series3"
    img: image = open("one_punch_man.png", "rb")
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['choose_series3'])
def onime3 (message: telebot.types.Message):
    for i in range(1, 13):
        enote = (f"https://jut.su/onepunchman/season-2/episode-{i}.html")
        bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['Inuyashiki'])
def anime4 (message: telebot.types.Message):
    enote: str = "Выберите серию \n /choose_series4"
    img: image = open("inu.png", "rb")
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['choose_series4'])
def onime4 (message: telebot.types.Message):
    for i in range(1, 12):
        enote = (f"https://jut.su/inu-hero/episode-{i}.html")
        bot.send_message(message.chat.id, enote)


@bot.message_handler(commands=['Attack_on_Titan_1_season'])
def anime5 (message: telebot.types.Message):
    enote: str = "Выберите серию \n /choose_series5"
    img: image = open("Attack_on_Titan.png", "rb")
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['choose_series5'])
def onime5 (message: telebot.types.Message):
    for i in range(1, 26):
        enote = (f"https://jut.su/shingekii-no-kyojin/season-1/episode-{i}.html")
        bot.send_message(message.chat.id, enote)


@bot.message_handler(commands=['Attack_on_Titan_2_season'])
def anime6 (message: telebot.types.Message):
    enote: str = "Выберите серию \n /choose_series6"
    img: image = open("Attack_on_Titan.png", "rb")
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['choose_series6'])
def onime6 (message: telebot.types.Message):
    for i in range(1, 13):
        enote = (f"https://jut.su/shingekii-no-kyojin/season-2/episode-{i}.html")
        bot.send_message(message.chat.id, enote)


@bot.message_handler(commands=['Attack_on_Titan_3_season'])
def anime7 (message: telebot.types.Message):
    enote: str = "Выберите серию \n /choose_series7"
    img: image = open("Attack_on_Titan.png", "rb")
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['choose_series7'])
def onime7 (message: telebot.types.Message):
    for i in range(1, 23):
        enote = (f"https://jut.su/shingekii-no-kyojin/season-3/episode-{i}.html")
        bot.send_message(message.chat.id, enote)


@bot.message_handler(commands=['Attack_on_Titan_4_season'])
def anime8 (message: telebot.types.Message):
    enote: str = "Выберите серию. Данный тайтл еще не закончился \n /choose_series8"
    img: image = open("Attack_on_Titan.png", "rb")
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['choose_series8'])
def onime8 (message: telebot.types.Message):
    for i in range(1, 29):
        enote = (f"https://jut.su/shingekii-no-kyojin/season-4/episode-{i}.html")
        bot.send_message(message.chat.id, enote)


@bot.message_handler(commands=['Naruto_1_season'])
def anime9 (message: telebot.types.Message):
    enote: str = "Выберите серию. \n /choose_series9"
    img: image = open("naruto.png", "rb")
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['choose_series9'])
def onime9 (message: telebot.types.Message):
    for i in range(1, 221):
        enote = (f"https://jut.su/naruuto/season-1/episode-{i}.html")
        bot.send_message(message.chat.id, enote)


@bot.message_handler(commands=['Naruto_2_season'])
def anime10 (message: telebot.types.Message):
    enote: str = "Выберите серию. \n /choose_series10"
    img: image = open("naruto2.png", "rb")
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['choose_series10'])
def onime10 (message: telebot.types.Message):
    for i in range(1, 501):
        enote = (f"https://jut.su/naruuto/season-2/episode-{i}.html")
        bot.send_message(message.chat.id, enote)


@bot.message_handler(commands=['Akame_ga_kill'])
def anime11 (message: telebot.types.Message):
    enote: str = "Выберите серию. \n /choose_series11"
    img: image = open("akame.png", "rb")
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['choose_series11'])
def onime11 (message: telebot.types.Message):
    for i in range(1, 25):
        enote = (f"https://jut.su/akaame-ga-kill/episode-{i}.html")
        bot.send_message(message.chat.id, enote)


@bot.message_handler(commands=['Boku_dake_ga_Inai_Machi'])
def anime12 (message: telebot.types.Message):
    enote: str = "Выберите серию. \n /choose_series12"
    img: image = open("boku.png", "rb")
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['choose_series12'])
def onime12 (message: telebot.types.Message):
    for i in range(1, 13):
        enote = (f"https://jut.su/boku-dake/episode-{i}.html")
        bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['Mirai_nikki'])
def anime13 (message: telebot.types.Message):
    enote: str = "Выберите серию. \n /choose_series13"
    img: image = open("mirai.png", "rb")
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['choose_series13'])
def onime13 (message: telebot.types.Message):
    for i in range(1, 27):
        enote = (f"https://jut.su/mirai-nikki/episode-{i}.html")
        bot.send_message(message.chat.id, enote)


@bot.message_handler(commands=['Parasyte'])
def anime14 (message: telebot.types.Message):
    enote: str = "Выберите серию. \n /choose_series14"
    img: image = open("parasyte.png", "rb")
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['choose_series14'])
def onime14 (message: telebot.types.Message):
    for i in range(1, 25):
        enote = (f"https://jut.su/kiseijuu/episode-{i}.html")
        bot.send_message(message.chat.id, enote)



@bot.message_handler(commands=['Cowboy_Bibop'])
def anime15 (message: telebot.types.Message):
    enote: str = "Выберите серию. \n /choose_series15"
    img: image = open("bibop.png", "rb")
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['choose_series15'])
def onime15 (message: telebot.types.Message):
    for i in range(1, 27):
        enote = (f"https://jut.su/cowboy-bebop/episode-{i}.html")
        bot.send_message(message.chat.id, enote)


    
@bot.message_handler(commands=['Another'])
def anime16 (message: telebot.types.Message):
    enote: str = "Выберите серию. \n /choose_series16"
    img: image = open("another.png", "rb")
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, enote)

@bot.message_handler(commands=['choose_series16'])
def onime16 (message: telebot.types.Message):
    for i in range(1, 14):
        enote = (f"https://jut.su/another/episode-{i}.html")
        bot.send_message(message.chat.id, enote)











bot.polling(non_stop=True)