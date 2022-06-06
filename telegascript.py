import random
import pickle
import asyncio
from time import sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import textwrap
import os
import colorama
from colorama import Fore, Back, Style

app = Client('admin', api_id=8445029, api_hash='ab4bfdd09082169ad2062ebf97d77a16')

if os.sys.platform == "win64":
	os.system("cls")
else:
	os.system("clear")

colorama.init()
print(Fore.GREEN + Style.BRIGHT + ">>> Руководство по авторизации в скрипте @Nepalli")
print("")
print(Fore.BLUE + Style.BRIGHT + ">> Ввод своих данных:")
print(Fore.WHITE + Style.RESET_ALL + "1. Вводите свой номер телефона")
print("2. Ввод Y для подтверждения номера")
print("3. Вводите код который придёт в телеграме")
print("4. Пароль от двухэтапной авторизации (если он есть) ")
print("(Если вы авторизовывались то просто подождите)")
print(Fore.YELLOW + "")

app.start()
app.stop()

if os.sys.platform == "win64":
	os.system("cls")
else:
	os.system("clear")

print(Fore.BLUE + Style.BRIGHT +'''
▀█▀ █▀▀ █▀ █▀▀ █▀█ █ █▀█ ▀█▀   █▀█ █▄█
░█░ █▄█ ▄█ █▄▄ █▀▄ █ █▀▀ ░█░ ▄ █▀▀ ░█░''')
print(Fore.RED + Style.BRIGHT +'''				v.1.2.8
''')

print(Fore.GREEN + Style.BRIGHT + ">>> Информация: ")
print(Fore.YELLOW + Style.BRIGHT +"Напишите в любой телеграм чат команду .help, \nдля просмотра всех команд!")
print("\nАвтор скрипта -\nTelegram: @Nepalli\nВ других соц.сетях нас нет!\n")

print(Fore.GREEN + Style.BRIGHT + ">> Скорость: ")
cool = int(input(Fore.WHITE + Style.RESET_ALL + "<*> Введите скорость от 3 до 10 (Норма 8): "))

global number
number = 0

while cool == 0:
	print(Fore.RED + Style.BRIGHT +"Слишком быстро!")
	cool = int(input(Fore.WHITE + Style.RESET_ALL + "<*> Введите скорость от 3 до 10 (Норма 8): "))

while cool == 1:
	print(Fore.RED + Style.BRIGHT +"Слишком быстро!")
	cool = int(input(Fore.WHITE + Style.RESET_ALL + "<*> Введите скорость от 3 до 10 (Норма 8): "))

while cool == 2:
	print(Fore.RED + Style.BRIGHT +"Слишком быстро!")
	cool = int(input(Fore.WHITE + Style.RESET_ALL + "<*> Введите скорость от 3 до 10 (Норма 8): "))

while cool >= 11:
	print(Fore.RED + Style.BRIGHT +"Слишком медленно!")
	cool = int(input(Fore.WHITE + Style.RESET_ALL + "<*> Введите скорость от 3 до 10 (Норма 8): "))

while cool < 0:
	print(Fore.RED + Style.BRIGHT +"ОЧЕНЬ БЫСТРО........")
	cool = int(input(Fore.WHITE + Style.RESET_ALL + "<*> Введите скорость от 3 до 10 (Норма 8): "))

print(Fore.GREEN + Style.BRIGHT + "Готово! Скрипт запущен.")
print(Fore.WHITE + Style.RESET_ALL + "Напишите в любой чат телеграмма -help \n(В закрытых чатах команда не работает)")


@app.on_message(filters.command("heart2", prefixes=".") & filters.me)
async def valentine(app, msg):
	heart2 = 0
	while heart2 <= 1:
		await msg.edit(f'''
			❤''')
		sleep(0.5)
		await msg.edit(f'''
			🧡''')
		sleep(0.5)
		await msg.edit(f'''
			💛''')
		sleep(0.5)
		await msg.edit(f'''
			💚''')
		sleep(0.5)
		await msg.edit(f'''
			💙''')
		sleep(0.5)
		await msg.edit(f'''
			💜''')
		sleep(0.5)
		await msg.edit(f'''
			🤎''')
		sleep(0.5)
		await msg.edit(f'''
			🖤''')
		sleep(0.5)
		await msg.edit(f'''
			🤍''')
		sleep(0.5)
		await msg.edit(f'''
			💖''')
		sleep(0.5)
		await msg.edit(f'''
			💗''')
		sleep(0.5)
		await msg.edit(f'''
			💘''')
		sleep(0.5)
		await msg.edit(f'''
			💝''')
		sleep(0.5)
		heart2 += 1
	if heart2 >= 2:
		sleep(5)
		await msg.edit(f'''
			🍃 author: @tgscriptss''')
		sleep(5)
		await msg.delete()
	global number
	number = number + 1
