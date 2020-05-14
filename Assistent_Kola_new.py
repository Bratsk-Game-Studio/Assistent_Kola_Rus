import pygame
import datetime
import tkinter
from tkinter import Tk, Canvas
import random 
from pygame.locals import *
import sys
from math import pi
import math
from ctypes import *
import time
from tkinter import *
from tkinter import messagebox
from random import randint
import os
import math

# Начало работы

windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))

def color(c):
	windll.Kernel32.SetConsoleTextAttribute(h, c)

def colorLine(c, s):
	color(c)
	print("*" * (len(s) + 2))
	print(" " + s)
	print("*" * (len(s) + 2))
	
print("---")

colorLine(3, "Ассистент - Коля!")

color(7)

print("Добро пожаловать! Вы используете программу Ассистент.Коля")

print("Список команд - : commands(for assistent)")

while True:
	
	user = input("Что вы ищите? (* Для помощи введите - commands(for assistent) *)\n> ")

	if user == "commands(for assistent)":
		print("=" * 42)
		print("commands(standard) - стандартные команды")
		print("commands(game) - игровые команды")
		print("commands(users) - пользовательские команды")
		print("commands(other) - другие команды")
		print("=" * 42)

	elif user == "commands(standard)":
		print("=" * 29)
		print("stop - завершит всю работу")
		print("author - авторы")
		print("bugs - показывает баги")
		print("calculator - калькулятор")
		print("what is time? - время")
		print("version - версия Ассистента")
		print("=" * 29)

	elif user == "commands(game)":
		print("=" * 77)
		print("game_one - игра 'Угадайка'.")
		print("game_two - игра 'Memory puzzels' (если нет модуля pygame, то не используете).")
		print("game_three - игра 'Камень, Ножницы, Бумага'.")
		print("game_four - игра 'Учись считать'.")
		print("game_five - игра 'Змейка'.")
		print("game_six - игра 'Ping-Pong'.")
		print("game_seven - игра 'Сапер'.")
		print("=" * 77)

	elif user == "commands(users)":
		print("=" * 76)
		print("NEWS - новости Ассистента!")
		print("update - скорые обновления")
		print("secret - шифровка сообщений (шифр Цезаря) (На русском!)")
		print("table - таблица умножения")
		print("joke - шутки")
		print("=" * 76)

	elif user == "commands(other)":
		print("=" * 107)
		print("Command - <имя команды> - поможет узнать, что это за команда (название команды пишется маленькими буквами!)")
		print("year on planets - узнать сколько длится год на планетах")
		print("number(1) - Число четное или нечетное")
		print("info(assistent) - информация об Ассистенте!")
		print("info(games) - информация о играх!")
		print("@SETTINGS_ASSISTENT - настройки ассистента.")
		print("=" * 107)

	elif user == "stop":
		break

	elif user == "exit":
		break

	elif user == "ыещз":
		break

	elif user == "учше":
		break

	elif user == "0":
		break

	elif user == "Assistent_Kola_StopWork(true)":
		time.sleep(11)
		break

	elif user == "clear":
		os.system("cls")

	elif user == "cls":
		os.system("cls")

	elif user == "author":
		print("=" * 25)
		print("Программисты : Денис Л.")
		print("Разработана на : Sublime Text 3")
		print("Помощь : Виктор Трофимов, Интернет")
		print("=" * 25)

	elif user == "bugs":
		print("-" * 100)
		print("1) После завершения игры 'Memory puzzels' работа Ассистента завершается.")
		print("2) Если в игре 'Учись считать' нажать на Enter, то работа Ассистента завершается.")
		print("3) После завершения некоторых игр работа Ассистента завершается")
		print("-" * 100)

	elif user == "Словарь/Русский":
		print()
		while True:
			print("Добро пожаловать в Русский Список! Для выхода напишите 0")
			print()
			slovo = input("Какое слово вам нужно? : ")

			if slovo == "0":
				print()
				break

			if slovo == "Атрибут" or "Атрибуты":
				print("""Атрибут:
				 				1. Постоянный признак
								2. В грамматике : то же, что и опредиление
								3. В программирование : свойство объекта, файла
								4. В философии : необходимое, существенное, неотъемлемое свойство предмета или явления""")

	elif user == "calculator":
		print("Ноль завершает работу калькулятора")
		print("Другие операции - info")
		print()

		while True:
			d = input("Знак (+, -, /, *, **, %, //), Чтобы считать введите count: ")
			print()
			if d == '0': 
				break
			elif d == "count":
				x = float(input("x = "))
				y = float(input("y = "))

				print()
				znak = input("Выберите знак > \n")
				if znak == "+":
					print()
					print("Ответ - ", x + y)
					print()
				elif znak == "-":
					print()
					print("Ответ - ", x - y)
					print()
				elif znak == "/":
					if y == 0:
						print()
						print("=" * 22)
						print("Делить на ноль нельзя!")
						print("=" * 22)
						print()
					else:
						print()
						print("Ответ - ", x / y)
						print()
				elif znak == "*":
					print()
					print("Ответ - ", x * y)
					print()
				elif znak == "**":
					print()
					print("Ответ - ", x ** y)
					print()
				elif znak == "%":
					print()
					print("Ответ - ", x & y)
					print()
				elif znak == "//":
					print()
					print("Ответ - ", x // y)
					print()
				else:
					print()
					print("Ошибочка вышла... :(")
					print()
			
			elif d == "info":
				print()
				print("bin() - Преобразование целого числа в бинарный код.")
				print("hex() - Преобразование целого числа в шестнадцатеричную строку.")
				print("oct() - Преобразование целого числа в восьмеричную строку.")
				print("Вы включили режим доп. операций. Чтобы выйти, напишите - exit")
				print()
				other = input("Какую опрацию вы выберите? > ")
				while other == "exit":
					if other == "exit":
						break
					elif other == "bin()":
						num1 = int(input("x = "))
						print()
						print(bin(num1))
						print()
					elif other == "hex()":
						num2 = int(input("x = "))
						print()
						print(hex(num2))
						print()
					elif other == "oct()":
						num3 = int(input("x = "))
						print()
						print(oct(num3))
						print()
					else:
						print("Ошибка!")
			else:
				print("Неверный знак операции!")

	elif user == "NEWS":
		print("=" * 85)
		print("Готовим, кое-что интересное)")
		print("Хмм... Ассистент Коля рад вас снова видеть ! :)")
		print("=" * 85)

	elif user == "update":
		print("Текущая версия - 2.41")
		print("Следующая версия - 2.41.5")
		print("Дата обновления (ver - 2.41.5) : - 17.04.2020")
		print("Дата крупного обновления (ver 2.50) : - 10.05.2020 ИЛИ 10.06.2020 НО НЕ ПОЗЖЕ начало июля (от 1 до 6)")

	elif user == "version":
		print("Версия Ассистента - 2.40.5")

	elif user == "1.06.20":
		print("Новая программа от разработчиков Ассистента Коли компании Bratsk Game!")

	elif user == "18.05.20":
		print("нОвая программа от разработчиков аСистента коли компании Bratsk Game!")

	elif user == "15.05.20":
		print("Не за горами новая версия программы [ВНИМАНИЕ СПОЙЛЕР!] от Bratsk Game...")

	elif user == "what is time?":
		now = datetime.datetime.now()
		print("Текущий год: %d" % now.year)
		print("Текущий месяц: %d"% now.month)
		print("Текущий день: %d" % now.day)
		print("Текущий час: %d" % now.hour)
		print("Текущая минута: %d" % now.minute)
		print("Текущая секунда: %d" % now.second)

	elif user == "secret":
		alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
		stringToEncrypt = input("Пожалуйства, введите сообщение для шифрования\n> ")
		stringToEncrypt = stringToEncrypt.upper()
		shiftAmount = int(input("Пожалуйста, введите целое число от 1 до 25, чтобы быть вашим ключом. \n> "))
		encryptedString = ""
		for currentCharacter in stringToEncrypt:
			position = alphabet.find(currentCharacter)
			newPostition = position + shiftAmount
			if currentCharacter in alphabet:
				encryptedString = encryptedString + alphabet[newPostition]
			else:
				encryptedString = encryptedString + currentCharacter
			encryptedString = encryptedString + alphabet[newPostition]
			
		print("Ваше зашифрованное сообщение :", encryptedString)
		print()

	elif user == "table":
		table = int(input("Пожалуйства, введите множитель!\n: "))
		time.sleep(1.5)
		for x in range(0,13):
			print(x, "x", table, "=", x * table)
			print("-------------")

	elif user == "joke":
		print("Есть шутки о <Программисты> . Код категории шуток : #FRES")
		time.sleep(0.5)
		whatjoke = input("Какие шутки вы хотите?\n> ")
		if whatjoke == "#FRES":
			while True:
				joke = input("Есть 10 шуток о программистов, код шуток : 1) #FRES1 2) #FRES2 ... 10) #FRES10 (Для остановки пишите - 0) \n> ")
				if joke == "0":
					print()
					break
					print()
				elif joke == "#FRES1":
					print("""Опытный разработчик всегда посмотрит направо и налево, даже если переходит улицу с односторонним движением. """)
				elif joke == "#FRES2":
					print("""Программа получилась плохой, а сроки горят, и заказчик ругается? Не волнуйтесь, смело выпускайте релиз. Просто назовите его версией 1.0. """)
				elif joke == "#FRES3":
					print("""Не работает код? Не нужно переживать! Если все будет работать, то вы можете оказаться безработным. """)
				elif joke == "#FRES4":
					print("""Основные изменения в новой версии программы: исправлены старые баги, добавлены новые.""")
				elif joke == "#FRES5":
					print("""Программисты - самые ленивые! Они используют один и тоже код, а для другим таким же программистам оставляют подсказки в виде комментариев! Ну зачем?""")
				elif joke == "#FRES6":
					print("""Обычно на написание 90% программного кода разработчикам требуется 90% отведенного на проект времени. А дальше случается парадокс: оставшиеся 10% работы требуют … 90 или даже 100% времени.""")
				elif joke == "#FRES7":
					print("""Что самое сложное в дизайне? Удержаться от фич.""")
				elif joke == "#FRES8":
					print("""Как смеются программисты? EXE EXE EXE""")
				elif joke == "#FRES9":
					print("""Легенда гласит, что Lunix может делить на 0, компилировать код у себя в голове не запуская его...""")
				elif joke == "#FRES10":
					print("""Говорю программисту : - Что лучше MasOS или Windows? Ответ убил : - Lunix. """)
		else:
			print("Ошибка")

	elif user == "year on planets":
		print("-" * 5)

		r = float(input("Радиус орбиты (млн. км): "))
		v = float(input("Орбитальная скорость (км/с): "))

		r = r * 1000000

		year = 2 * pi * r / v
		year = year / (60 * 60 * 24)

		print(round(year))
		print("-" * 5)

	elif user == "number(1)":
		a = int(input('Введите число = '))

		if a % 2 == 0:
			print("Четное")
		else:
			print("Нечетное")

	elif user == "math(1_type)":
		print()
		AB = input("Длина первого катета : ")
		AC = input("Длина второго катета : ")

		AB = float(AB)
		AC = input(AC)

		BC = math.sqrt(AB ** 2 + AC ** 2)

		S = (AB * AC) / 2
		P = AB + AC + BC

		print(f"Площадь треугольника: {S}")
		print(f"Пермметр треугольника: {P}")
		print()

	elif user == "info(assistent)":
		print("-" * 55)
		print("Имя : Assistent_Kola")
		print("Расширение : .py")
		print("Модули : pygame, datetime, tkinter, random, sys, math, ctypes, time, os")
		print("Язык программирования : Python")
		print("Язык системы : Русский")
		print("Сколько языков : 1 (Русский)")
		print("Сколько человек создавали : 1 человек")
		print("Сколько создавали (дней) : 3 дня (приближительно)")
		print("-" * 55)

	elif user == "game_one":
		lowDight = 10
		highDoigit = 50
		digit = 0 

		countInput = 0
		win = False
		playGame = True
		x = 0
		startScore = 100
		score = 0
		maxScore = 0

		while (playGame):
			digit = random.randint(lowDight, highDoigit)
			print("-" * 25)
			countInput = 0
			score = startScore
			print("Компьютер загадал число, попробуйте отгадать!")
			while (not win and score > 0):
				print("-" * 25)
				print(f"Заработано очков : {score}")
				print(f"Рекорд : {maxScore}")

				x = ""
				while (not x.isdigit()):
					x = input(f"Введите число от {lowDight} до {highDoigit} : ")
					if (not x.isdigit()):
						print("." * 27 + " Введите, пожалуйста, число.")

				x = int(x)
				if (x == digit):
					win = True
				else:
					length = abs(x - digit)
					if (length < 3):
						print("ОЧЕНЬ горячо!")
					elif (length < 5):
						print("Горячо!")
					elif (length < 10):
						print("Тепло")
					elif (length < 15):
						print("Прохладно")
					elif (length < 20):
						print("Холодно")
					else:
						print("ОЧЕНЬ холодно!")

					if (countInput == 7):
						score -= 10
						if (digit % 2 == 0):
							print("Число четное")
						else:
							print("Число нечетное")
					elif (countInput == 6):
						score -= 8
						if (digit % 3 == 0):
							print("Число делится на 3")
						else:
							print("Число не делится на 3")
					elif (countInput == 5):
						score -= 4
						if (digit % 4 == 0):
							print("Число делится на 4")
						else:
							print("Число не делится на 4")
					elif (countInput > 2 and countInput < 5):
						score -= 2
						if (x > digit):
							print("Загаданное число МЕНЬШЕ вашего.")
						else:
							print("Загаданное число БОЛЬШЕ вашего.")
					score -= 5
				countInput += 1

			print("*" * 35)
			if (x == digit):
				print("Победа! Поздравляю!")
			else:
				print("Ой, у вас закончились очки. Вы проиграли :(")

			if (input("Enter - сыграть ещё раз, 0 - выход ") == "0"):
				playGame = False
			else:
				win = False

			if (score > maxScore):
				maxScore = score

		print("*" * 35)
		print("""Спасибо за то, что поиграли в игру! P.S. Вы хорошо держались :P """)

	elif user == "game_two":
		while True:
			FPS = 30 # frames per second, the general speed of the program
			WINDOWWIDTH = 640 # size of window's width in pixels
			WINDOWHEIGHT = 480 # size of windows' height in pixels
			REVEALSPEED = 8 # speed boxes' sliding reveals and covers
			BOXSIZE = 40 # size of box height & width in pixels
			GAPSIZE = 10 # size of gap between boxes in pixels
			BOARDWIDTH = 10 # number of columns of icons
			BOARDHEIGHT = 7 # number of rows of icons
			assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
			XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
			YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

			#            R    G    B
			GRAY     = (100, 100, 100)
			NAVYBLUE = ( 60,  60, 100)
			WHITE    = (255, 255, 255)
			RED      = (255,   0,   0)
			GREEN    = (  0, 255,   0)
			BLUE     = (  0,   0, 255)
			YELLOW   = (255, 255,   0)
			ORANGE   = (255, 128,   0)
			PURPLE   = (255,   0, 255)
			CYAN     = (  0, 255, 255)

			BGCOLOR = NAVYBLUE
			LIGHTBGCOLOR = GRAY
			BOXCOLOR = WHITE
			HIGHLIGHTCOLOR = BLUE

			DONUT = 'donut'
			SQUARE = 'square'
			DIAMOND = 'diamond'
			LINES = 'lines'
			OVAL = 'oval'

			ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
			ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
			assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."

			def main():
			    global FPSCLOCK, DISPLAYSURF
			    pygame.init()
			    FPSCLOCK = pygame.time.Clock()
			    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

			    mousex = 0 # used to store x coordinate of mouse event
			    mousey = 0 # used to store y coordinate of mouse event
			    pygame.display.set_caption('Memory Game')

			    mainBoard = getRandomizedBoard()
			    revealedBoxes = generateRevealedBoxesData(False)

			    firstSelection = None # stores the (x, y) of the first box clicked.

			    DISPLAYSURF.fill(BGCOLOR)
			    startGameAnimation(mainBoard)

			    while True: # main game loop
			        mouseClicked = False

			        DISPLAYSURF.fill(BGCOLOR) # drawing the window
			        drawBoard(mainBoard, revealedBoxes)

			        for event in pygame.event.get(): # event handling loop
			            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
			                pygame.quit()
			                sys.exit()
			            elif event.type == MOUSEMOTION:
			                mousex, mousey = event.pos
			            elif event.type == MOUSEBUTTONUP:
			                mousex, mousey = event.pos
			                mouseClicked = True

			        boxx, boxy = getBoxAtPixel(mousex, mousey)
			        if boxx != None and boxy != None:
			            # The mouse is currently over a box.
			            if not revealedBoxes[boxx][boxy]:
			                drawHighlightBox(boxx, boxy)
			            if not revealedBoxes[boxx][boxy] and mouseClicked:
			                revealBoxesAnimation(mainBoard, [(boxx, boxy)])
			                revealedBoxes[boxx][boxy] = True # set the box as "revealed"
			                if firstSelection == None: # the current box was the first box clicked
			                    firstSelection = (boxx, boxy)
			                else: # the current box was the second box clicked
			                    # Check if there is a match between the two icons.
			                    icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
			                    icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)

			                    if icon1shape != icon2shape or icon1color != icon2color:
			                        # Icons don't match. Re-cover up both selections.
			                        pygame.time.wait(1000) # 1000 milliseconds = 1 sec
			                        coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
			                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
			                        revealedBoxes[boxx][boxy] = False
			                    elif hasWon(revealedBoxes): # check if all pairs found
			                        gameWonAnimation(mainBoard)
			                        pygame.time.wait(2000)

			                        # Reset the board
			                        mainBoard = getRandomizedBoard()
			                        revealedBoxes = generateRevealedBoxesData(False)

			                        # Show the fully unrevealed board for a second.
			                        drawBoard(mainBoard, revealedBoxes)
			                        pygame.display.update()
			                        pygame.time.wait(1000)

			                        # Replay the start game animation.
			                        startGameAnimation(mainBoard)
			                    firstSelection = None # reset firstSelection variable

			        # Redraw the screen and wait a clock tick.
			        pygame.display.update()
			        FPSCLOCK.tick(FPS)


			def generateRevealedBoxesData(val):
			    revealedBoxes = []
			    for i in range(BOARDWIDTH):
			        revealedBoxes.append([val] * BOARDHEIGHT)
			    return revealedBoxes


			def getRandomizedBoard():
			    # Get a list of every possible shape in every possible color.
			    icons = []
			    for color in ALLCOLORS:
			        for shape in ALLSHAPES:
			            icons.append( (shape, color) ) # <= 666! > : )

			    random.shuffle(icons) # randomize the order of the icons list
			    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2) # calculate how many icons are needed
			    icons = icons[:numIconsUsed] * 2 # make two of each
			    random.shuffle(icons)

			    # Create the board data structure, with randomly placed icons.
			    board = []
			    for x in range(BOARDWIDTH):
			        column = []
			        for y in range(BOARDHEIGHT):
			            column.append(icons[0])
			            del icons[0] # remove the icons as we assign them
			        board.append(column)
			    return board


			def splitIntoGroupsOf(groupSize, theList):
			    # splits a list into a list of lists, where the inner lists have at
			    # most groupSize number of items.
			    result = []
			    for i in range(0, len(theList), groupSize):
			        result.append(theList[i:i + groupSize])
			    return result


			def leftTopCoordsOfBox(boxx, boxy):
			    # Convert board coordinates to pixel coordinates
			    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
			    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
			    return (left, top)


			def getBoxAtPixel(x, y):
			    for boxx in range(BOARDWIDTH):
			        for boxy in range(BOARDHEIGHT):
			            left, top = leftTopCoordsOfBox(boxx, boxy)
			            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
			            if boxRect.collidepoint(x, y):
			                return (boxx, boxy)
			    return (None, None)


			def drawIcon(shape, color, boxx, boxy):
			    quarter = int(BOXSIZE * 0.25) # syntactic sugar
			    half =    int(BOXSIZE * 0.5)  # syntactic sugar

			    left, top = leftTopCoordsOfBox(boxx, boxy) # get pixel coords from board coords
			    # Draw the shapes
			    if shape == DONUT:
			        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
			        pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter - 5)
			    elif shape == SQUARE:
			        pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
			    elif shape == DIAMOND:
			        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))
			    elif shape == LINES:
			        for i in range(0, BOXSIZE, 4):
			            pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))
			            pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + i))
			    elif shape == OVAL:
			        pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOXSIZE, half))


			def getShapeAndColor(board, boxx, boxy):
			    # shape value for x, y spot is stored in board[x][y][0]
			    # color value for x, y spot is stored in board[x][y][1]
			    return board[boxx][boxy][0], board[boxx][boxy][1]


			def drawBoxCovers(board, boxes, coverage):
			    # Draws boxes being covered/revealed. "boxes" is a list
			    # of two-item lists, which have the x & y spot of the box.
			    for box in boxes:
			        left, top = leftTopCoordsOfBox(box[0], box[1])
			        pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
			        shape, color = getShapeAndColor(board, box[0], box[1])
			        drawIcon(shape, color, box[0], box[1])
			        if coverage > 0: # only draw the cover if there is an coverage
			            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, coverage, BOXSIZE))
			    pygame.display.update()
			    FPSCLOCK.tick(FPS)


			def revealBoxesAnimation(board, boxesToReveal):
			    # Do the "box reveal" animation.
			    for coverage in range(BOXSIZE, (-REVEALSPEED) - 1, -REVEALSPEED):
			        drawBoxCovers(board, boxesToReveal, coverage)


			def coverBoxesAnimation(board, boxesToCover):
			    # Do the "box cover" animation.
			    for coverage in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED):
			        drawBoxCovers(board, boxesToCover, coverage)


			def drawBoard(board, revealed):
			    # Draws all of the boxes in their covered or revealed state.
			    for boxx in range(BOARDWIDTH):
			        for boxy in range(BOARDHEIGHT):
			            left, top = leftTopCoordsOfBox(boxx, boxy)
			            if not revealed[boxx][boxy]:
			                # Draw a covered box.
			                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
			            else:
			                # Draw the (revealed) icon.
			                shape, color = getShapeAndColor(board, boxx, boxy)
			                drawIcon(shape, color, boxx, boxy)


			def drawHighlightBox(boxx, boxy):
			    left, top = leftTopCoordsOfBox(boxx, boxy)
			    pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)


			def startGameAnimation(board):
			    # Randomly reveal the boxes 8 at a time.
			    coveredBoxes = generateRevealedBoxesData(False)
			    boxes = []
			    for x in range(BOARDWIDTH):
			        for y in range(BOARDHEIGHT):
			            boxes.append( (x, y) )
			    random.shuffle(boxes)
			    boxGroups = splitIntoGroupsOf(8, boxes)

			    drawBoard(board, coveredBoxes)
			    for boxGroup in boxGroups:
			        revealBoxesAnimation(board, boxGroup)
			        coverBoxesAnimation(board, boxGroup)


			def gameWonAnimation(board):
			    # flash the background color when the player has won
			    coveredBoxes = generateRevealedBoxesData(True)
			    color1 = LIGHTBGCOLOR
			    color2 = BGCOLOR

			    for i in range(13):
			        color1, color2 = color2, color1 # swap colors
			        DISPLAYSURF.fill(color1)
			        drawBoard(board, coveredBoxes)
			        pygame.display.update()
			        pygame.time.wait(300)


			def hasWon(revealedBoxes):
			    # Returns True if all the boxes have been revealed, otherwise False
			    for i in revealedBoxes:
			        if False in i:
			            return False # return False if any boxes are covered.
			    return True


			if __name__ == '__main__':
			    main()

			pygame.quit()

	elif user == "game_three":
		while True:
			print("--- Игра --- ")
			print("Камень/Ножницы/Бумага")

			print("Чтобы выйти напишите Stop - > ")
		
			app = random.randint(1,3)

			yo = ""

			if app == 1:
				yo = "Камень"
			elif app == 2:
				yo == "Ножницы"
			else:
				yo == "Бумага"

			print("1) Камень")
			print("2) Ножницы")
			print("3) Бумага")

			try:
				x = int(input("Введите число \n> "))

				if x == 1:
					print("")
					print("Вы выбрали : Камень")
					print("Оппонент выбрал : " + str(yo))
					print("")

					if app == 1:
						print("Ничья :/")
					elif app == 2:
						print("Победа ! :3")
					else:
						print("Проигрыш! Оппонент выиграл! :(")

				elif x == "Stop":
					break
					
				elif x == 2:
					print("")
					print("Вы выбрали : Ножницы")
					print("Оппонент выбрал : " + str(yo))
					print("") 

					if app == 1:
						print("Проигрыш! Оппонент выиграл! :(")
					elif app == 2:
						print("Ничья :/")
					else:
						print("Победа ! :3")
					print("")
				elif x == 3:
					print("")
					print("Вы выбрали : Бумага")
					print("Оппонент выбрал : " + str(yo))
					print("")

					if app == 1:
						print("Победа ! :3")
					elif app == 2:
						print("Проигрыш! Оппонент выиграл! :(")
					else:
						print("Ничья :/")
					print("")
				else:
					print("Введите только числа! : 1/2/3")
			except:

				print("ОШИБКА! Введите только ЦЕЛЫЕ числа!")

	elif user == "game_four":
		lowDiapazon = 10
		highDiapazon = 1000
		sign = 0
		playGame1 = True
		count = 0
		right = 0
		score1 = 0

		print("""Компьютер составляет пример. Для равершения работы введите STOP.""")
		print("*" * 40)

		while (playGame1):
			print(f"Ваши очки : {score1}")
			print(f"Очков заработано : {count}")
			print(f"Правильных ответов : {right}")
			print("-" * 20)

			sign = random.randint(0, 3)

			if (sign == 0):
				z = random.randint(lowDiapazon, highDiapazon)
				x = random.randint(lowDiapazon, z)
				y = z - x

				if (random.randint(0, 1) == 0):
					print(f"{x} + {y} = ?")
				else:
					print(f"{y} + {x} = ?")

			elif (sign == 1):
				x = random.randint(lowDiapazon, highDiapazon)
				y = random.randint(0, x - lowDiapazon)
				z = x - y

				print(f"{x} - {y} = ?")

			elif (sign == 2):
				x = random.randint(1, (highDiapazon - lowDiapazon) //
					random.randint(1, highDiapazon // 10) + 1)
				y = random.randint(lowDiapazon, highDiapazon) // x
				z = x * y
				print(f"{x} * {y} = ?")

			elif (sign == 3):
				x = random.randint(1, (highDiapazon - lowDiapazon) //
					random.randint(1, highDiapazon // 10) + 1)
				y = random.randint(lowDiapazon, highDiapazon) // x
				if (y == 0):
					y = 1
				x = x * y
				z = x / y
				print(f"{x} / {y} = ?")

			USER = ""
			while (not USER.isdigit() and USER.upper() != "STOP" and USER.upper() != "S" and USER.upper() != "Ы" and USER.upper() != "ЫЕЩЗ"):

				USER = input("Ваш ответ? ")

				if (USER.upper() == "HELP" or USER == "?" or USER == "," or USER.upper() == "РУДЗ"):

					if (z > 9):
						print(f"Последняя цифра ответа : {z % 10}")
					else:
						print(f("Ответ состоит из одной цифры, подсказка невозможна."))
					score1 -=10

				if (USER.upper() == "STOP" or USER.upper() == "S" or USER.upper() == "Ы" or USER.upper() == "ЫЕЩЗ"):
					playGame1 = False
				else:
					count += 1

					if (int(USER) == z):
						print("\nПравильно!\n")
						right += 1
						score1 += 10
					else:
						print(f"\nОтвет неправильный... Правильно : {z}")
						print(f"Вы можете ввести команду HELP или ? чтобы увидеть последнюю цифру ответа (-10 очков)\n")
						score1 -=20



		print("*" * 45)
		print("СТАТИСТИКА ИГРЫ : ")
		print(f"Всего примеров : {count}")
		print(f"Правильных ответов : {right}")
		print(f"Неправильных ответов : {count - right}")

		if (count > 0):
			print(f"Процент верных ответов : {int(right / count * 100)} %")
		else:
			print(f"Процент верных ответов : 0 %")
		print("Возвращайтесь!")

	elif user == "Command - append":
		print("Это команда для cmd windows")
		print("Позволяет программам открывать файлы в указанных каталогах так, словно они находятся в текущем каталоге.")
	elif user == "Command - arp":
		print("Это команда для cmd windows")
		print("Отображение и изменение таблиц преобразования IP-адресов в физические, используемые протоколом разрешения адресов.")
	elif user == "Command - assos":
		print("Это команда для cmd windows")
		print("Вывод либо изменение сопоставлений по расширениям имён файлов.")
	elif user == "Command - at":
		print("Это команда для cmd windows")
		print("Команда предназначена для запуска программ в указанное время.")
	elif user == "Command - atmsdm":
		print("Это команда для cmd windows")
		print("Контроль подключений и адресов, зарегистрированных диспетчером вызовов ATM в сетях с асинхронным режимом передачи (ATM).")
	elif user == "Command - attrib":
		print("Это команда для cmd windows")
		print("Изменение атрибутов файлов и папок.")
	elif user == "Command - auditusr":
		print("Это команда для cmd windows")
		print("Задаёт политику аудита пользователей.")
	elif user == "Command - break":
		print("Это команда для cmd windows")
		print("Включение режима обработки клавиш CTRL+C.")
	elif user == "Command - bootcfg":
		print("Это команда для cmd windows")
		print("Эта программа командной строки может быть использована для настройки , извлечения , изменения или удаления параметров командной строки в файле Boot.ini.")
	elif user == "Command - calcs":
		print("Это команда для cmd windows")
		print("Просмотр изменение таблиц управления доступом ACL к файлам.")
	elif user == "Command - call":
		print("Это команда для cmd windows")
		print("Вызов одного пакетного файла из другого.")
	elif user == "Command - cd":
		print("Это команда для cmd windows")
		print("Вывод имени либо изменение текущей папки.")
	elif user == "Command - chcp":
		print("Это команда для cmd windows")
		print("Вывод либо изменение активной кодовой страницы.")
	elif user == "Command - chdir":
		print("Это команда для cmd windows")
		print("Вывод либо смена текущей папки.")
	elif user == "Command - chkdsk":
		print("Это команда для cmd windows")
		print("Проверка диска и вывод отчёта.")
	elif user == "Command - chkntfs":
		print("Это комаенда для cmd windows")
		print("Выводит или изменяет параметры проверки диска во время загрузки.")
	elif user == "Command - ciddaemon":
		print("Это команда для cmd windows")
		print("Сервис индексации файлов.")
	elif user == "Command - cipher":
		print("Это команда для cmd windows")
		print("Программа шифрования файлов.")
	elif user == "Command - cls":
		print("Это команда для cmd windows")
		print("Очистка экрана интерпретатора.")
	elif user == "Command - cmd":
		print("Это команда для cmd windows")
		print("Запуск нового окна командной строки.")
	elif user == "Command - cmstp":
		print("Это команда для cmd windows")
		print("Установка профилей диспетчера подключений.")
	elif user == "Command - color":
		print("Это команда для cmd windows")
		print("Устанавливает цвет для текста и фона в текстовых окнах.")
	elif user == "Command - comp":
		print("Это команда для cmd windows")
		print("Сравнение содержимого двух файлов или наборов файлов.")
	elif user == "Command - compact":
		print("Это команда для cmd windows")
		print("Просмотр и изменение параметров сжатия файлов в разделах NTFS.")
	elif user == "Command - convert":
		print("Это команда для cmd windows")
		print("Преобразование файловой системы тома FAT в NTFS.")
	elif user == "Command - copy":
		print("Это команда для cmd windows")
		print("Копирование одного или нескольких файлов.")
	elif user == "Command - date":
		print("Это команда для cmd windows")
		print("Вывод либо установка текущей даты.")
	elif user == "Command - debug":
		print("Это команда для cmd windows")
		print("Средство для отладки и редактирования программ.")
	elif user == "Command - defrag":
		print("Это команда для cmd windows")
		print("Дефрагментация диска.")
	elif user == "Command - del":
		print("Это команда для cmd windows")
		print("Удаление одного или нескольких файлов.")
	elif user == "Command - devcon":
		print("Это команда для cmd windows")
		print("Альтернатива диспетчера устройств.")
	elif user == "Command - diantz":
		print("Это команда для cmd windows")
		print("То же, что и makecab.")
	elif user == "Command - dir":
		print("Это команда для cmd windows")
		print("Вывод списка файлов и подпапок из указанного каталога.")
	elif user == "Command - diskcomp":
		print("Это команда для cmd windows")
		print("Сравнение содержимого двух гибких дисков.")
	elif user == "Command - diskcopy":
		print("Это команда для cmd windows")
		print("Копирование содержимого одного гибкого диска на другой.")
	elif user == "Command - diskpart":
		print("Это команда для cmd windows")
		print("Использования сценария diskpart.")
	elif user == "Command - diskperf":
		print("Это команда для cmd windows")
		print("Счетчик производительности дисков.")
	elif user == "Command - doskey":
		print("Это команда для cmd windows")
		print("Редактирование и повторный вызов команд Windows; создание макросов DOSKey.")
	elif user == "Command - driverquery":
		print("Это команда для cmd windows")
		print("Просмотр списка установленных драйверов устройств и их свойства.")
	elif user == "Command - echo":
		print("Это команда для cmd windows")
		print("Вывод сообщений и переключение режима отображения команд на экране.")
	elif user == "Command - edit":
		print("Это команда для cmd windows")
		print("Запуск редактора MS-DOS.")
		print("Примечание! На windows 10 почему-то не работает эта команда!")
	elif user == "Command - endlocal":
		print("Это команда для cmd windows")
		print("Завершение локализации изменений среды в пакетном файле.")
	elif user == "Command - edlin":
		print("Это команда для cmd windows")
		print("Запуск построчного текстового редактора.")
		print("Примечание! На windows 10 почему-то не работает эта команда!")
	elif user == "Command - erase":
		print("Это команда для cmd windows")
		print("Удаление одного или нескольких файлов.")
	elif user == "Command - esentutl":
		print("Это команда для cmd windows")
		print("Обслуживание утилит для Microsoft (R) баз данных Windows.")
	elif user == "Command - eventcreate":
		print("Это команда дял cmd windows")
		print("Эта команда дает возможность администратору создать запись об особом событии в указанном журнале событий.")
	elif user == "Command - eventtriggers":
		print("Это команда для cmd windows")
		print("Позволяет администратору отобразить и настроить триггеры событий в локальной или удаленной системе.")
	elif user == "Command - exe2bin":
		print("Это команда для cmd windows")
		print("Преобразование EXE-файлов в двоичный формат")
	elif user == "Command - exit":
		print("Это команда для cmd windows")
		print("Завершение командной строки.")
	elif user == "Command - expand":
		print("Это команда для cmd windows")
		print("Распаковка сжатых файлов.")
	elif user == "Command - fc":
		print("Это команда для cmd windows")
		print("Сравнение двух файлов или двух наборов файлов и вывод различий между ними.")
	elif user == "Command - find ":
		print("Это команда для cmd windows")
		print("Поиск текстовой строки в одном или нескольких файлах.")
	elif user == "Command - findstr":
		print("Это команда для cmd windows")
		print("Поиск строк в файлах.")
	elif user == "Command - finger":
		print("Это команда для cmd windows")
		print("Вывод сведений о пользователях указанной системы.")
	elif user == "Command - fltmc":
		print("Это команда для cmd windows")
		print("Работа с фильтром нагрузки драйверов.")
	elif user == "Command - for":
		print("Это команда для cmd windows")
		print("Выполнение указанной команды для каждого файла набора.")
	elif user == "Command - forcedos":
		print("Это команда для cmd windows")
		print("Сопоставление приложений MS-DOS, которые не распознаются системой Microsoft Windows XP.")
	elif user == "Command - format":
		print("Это команда для cmd windows")
		print("Форматирование диска для работы с Windows.")
	elif user == "Command - fontview":
		print("Это команда для cmd windows")
		print("Программа просмотра шрифтов.")
	elif user == "Command - fsutil":
		print("Это команда для cmd windows")
		print("Управление точками повторной обработки, управление разрежнными файлами, отключение тома или расширение тома.")
	elif user == "Command - ftype":
		print("Это команда для cmd windows")
		print("Просмотр и изменение типов файлов, сопоставленных с расширением имен файлов.")
	elif user == "Command - getmac":
		print("Это команда для сmd windows")
		print("Отображает MAC-адрес одного или нескольких сетевых адаптеров компьютера.")
	elif user == "Command - goto":
		print("Это команда для cmd windows")
		print("Передача управления содержащей метку строке пакетного файла.")
	elif user == "Command - gpresult":
		print("Это команда для cmd windows")
		print("Отображает результирующую политику (RSoP) для указанного пользователя и компьютера.")
	elif user == "Command - help":
		print("Это команда для cmd windows")
		print("Выводит не полный список команд, которые используются в cmd.")
	elif user == "Command - hostname":
		print("Это команда для cmd windows")
		print("Отображение имени компьютера.")
	elif user == "Command - if":
		print("Это команда для cmd windows")
		print("Оператор условного выполнения команд в пакетном файле.")
	elif user == "Command - ipconfig":
		print("Это команда для cmd windows")
		print("Вывод маску подсети, стандартный шлюз и информацию о вашем IP.")
	elif user == "Command - ipxroute":
		print("Это команда для cmd windows")
		print("Программа управления маршрутизацией NWLink IPX.")
	elif user == "Command - label":
		print("Это команда для cmd windows")
		print("Создание, изменение и удаление меток тома для диска.")
	elif user == "Command - lodctr":
		print("Это команда для cmd windows")
		print("Обновление имен счётчиков и поясняющего текста для расширенного счётчика.")
	elif user == "Command - logman":
		print("Это команда для cmd windows")
		print("Управление расписанием для счетчиков производительности и журнала трассировки событий.")
	elif user == "Command - logoff":
		print("Это команда для cmd windows")
		print("Завершение сеанса Windows")

	# Скоро обновление!
	# Minecraft \ Detroit : Bechome Human
	# Люблю бутерброды с колбосой
	# Chicha \\\ Извините,..
	# Coronovirus is heeer
	# Подпишись на мой канал - Stickmen Mickmen

	elif user == "game_six":
		# глобальные переменные
		# настройки окна
		WIDTH = 900
		HEIGHT = 300
		 
		# настройки ракеток
		 
		# ширина ракетки
		PAD_W = 10
		# высота ракетки
		PAD_H = 100
		 
		# настройки мяча
		# Насколько будет увеличиваться скорость мяча с каждым ударом
		BALL_SPEED_UP = 1.05
		# Максимальная скорость мяча
		BALL_MAX_SPEED = 40
		# радиус мяча
		BALL_RADIUS = 30

		INITIAL_SPEED = 20
		BALL_X_SPEED = INITIAL_SPEED
		BALL_Y_SPEED = INITIAL_SPEED

		# Счет игроков
		PLAYER_1_SCORE = 0
		PLAYER_2_SCORE = 0

		# Добавим глобальную переменную отвечающую за расстояние
		# до правого края игрового поля
		right_line_distance = WIDTH - PAD_W

		def update_score(player):
		    global PLAYER_1_SCORE, PLAYER_2_SCORE
		    if player == "right":
		        PLAYER_1_SCORE += 1
		        c.itemconfig(p_1_text, text=PLAYER_1_SCORE)
		    else:
		        PLAYER_2_SCORE += 1
		        c.itemconfig(p_2_text, text=PLAYER_2_SCORE)
		 
		def spawn_ball():
		    global BALL_X_SPEED
		    # Выставляем мяч по центру
		    c.coords(BALL, WIDTH/2-BALL_RADIUS/2,
		             HEIGHT/2-BALL_RADIUS/2,
		             WIDTH/2+BALL_RADIUS/2,
		             HEIGHT/2+BALL_RADIUS/2)
		    # Задаем мячу направление в сторону проигравшего игрока,
		    # но снижаем скорость до изначальной
		    BALL_X_SPEED = -(BALL_X_SPEED * -INITIAL_SPEED) / abs(BALL_X_SPEED)

		# функция отскока мяча
		def bounce(action):
		    global BALL_X_SPEED, BALL_Y_SPEED
		    # ударили ракеткой
		    if action == "strike":
		        BALL_Y_SPEED = random.randrange(-10, 10)
		        if abs(BALL_X_SPEED) < BALL_MAX_SPEED:
		            BALL_X_SPEED *= -BALL_SPEED_UP
		        else:
		            BALL_X_SPEED = -BALL_X_SPEED
		    else:
		        BALL_Y_SPEED = -BALL_Y_SPEED

		# устанавливаем окно
		root = Tk()
		root.title("PythonicWay Pong")
		 
		# область анимации
		c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
		c.pack()
		 
		# элементы игрового поля
		 
		# левая линия
		c.create_line(PAD_W, 0, PAD_W, HEIGHT, fill="white")
		# правая линия
		c.create_line(WIDTH-PAD_W, 0, WIDTH-PAD_W, HEIGHT, fill="white")
		# центральная линия
		c.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, fill="white")
		 
		# установка игровых объектов
		 
		# создаем мяч
		BALL = c.create_oval(WIDTH/2-BALL_RADIUS/2,
		                     HEIGHT/2-BALL_RADIUS/2,
		                     WIDTH/2+BALL_RADIUS/2,
		                     HEIGHT/2+BALL_RADIUS/2, fill="white")
		 
		# левая ракетка
		LEFT_PAD = c.create_line(PAD_W/2, 0, PAD_W/2, PAD_H, width=PAD_W, fill="yellow")
		 
		# правая ракетка
		RIGHT_PAD = c.create_line(WIDTH-PAD_W/2, 0, WIDTH-PAD_W/2, 
		                          PAD_H, width=PAD_W, fill="yellow")


		p_1_text = c.create_text(WIDTH-WIDTH/6, PAD_H/4,
		                         text=PLAYER_1_SCORE,
		                         font="Arial 20",
		                         fill="white")
		 
		p_2_text = c.create_text(WIDTH/6, PAD_H/4,
		                          text=PLAYER_2_SCORE,
		                          font="Arial 20",
		                          fill="white")

		# добавим глобальные переменные для скорости движения мяча
		# по горизонтали
		BALL_X_CHANGE = 20
		# по вертикали
		BALL_Y_CHANGE = 0
		 
		def move_ball():
		    # определяем координаты сторон мяча и его центра
		    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
		    ball_center = (ball_top + ball_bot) / 2
		 
		    # вертикальный отскок
		    # Если мы далеко от вертикальных линий - просто двигаем мяч
		    if ball_right + BALL_X_SPEED < right_line_distance and \
		            ball_left + BALL_X_SPEED > PAD_W:
		        c.move(BALL, BALL_X_SPEED, BALL_Y_SPEED)
		    # Если мяч касается своей правой или левой стороной границы поля
		    elif ball_right == right_line_distance or ball_left == PAD_W:
		        # Проверяем правой или левой стороны мы касаемся
		        if ball_right > WIDTH / 2:
		            # Если правой, то сравниваем позицию центра мяча
		            # с позицией правой ракетки.
		            # И если мяч в пределах ракетки делаем отскок
		            if c.coords(RIGHT_PAD)[1] < ball_center < c.coords(RIGHT_PAD)[3]:
		                bounce("strike")
		            else:
		                # Иначе игрок пропустил - тут оставим пока pass, его мы заменим на подсчет очков и респаун мячика
		                update_score("left")
		                spawn_ball()
		        else:
		            # То же самое для левого игрока
		            if c.coords(LEFT_PAD)[1] < ball_center < c.coords(LEFT_PAD)[3]:
		                bounce("strike")
		            else:
		                update_score("right")
		                spawn_ball()
		    # Проверка ситуации, в которой мячик может вылететь за границы игрового поля.
		    # В таком случае просто двигаем его к границе поля.
		    else:
		        if ball_right > WIDTH / 2:
		            c.move(BALL, right_line_distance-ball_right, BALL_Y_SPEED)
		        else:
		            c.move(BALL, -ball_left+PAD_W, BALL_Y_SPEED)
		    # горизонтальный отскок
		    if ball_top + BALL_Y_SPEED < 0 or ball_bot + BALL_Y_SPEED > HEIGHT:
		        bounce("ricochet")

		# зададим глобальные переменные скорости движения ракеток
		# скорось с которой будут ездить ракетки
		PAD_SPEED = 20
		# скорость левой платформы
		LEFT_PAD_SPEED = 0
		# скорость правой ракетки
		RIGHT_PAD_SPEED = 0
		 
		# функция движения обеих ракеток
		def move_pads():
		    # для удобства создадим словарь, где ракетке соответствует ее скорость
		    PADS = {LEFT_PAD: LEFT_PAD_SPEED, 
		            RIGHT_PAD: RIGHT_PAD_SPEED}
		    # перебираем ракетки
		    for pad in PADS:
		        # двигаем ракетку с заданной скоростью
		        c.move(pad, 0, PADS[pad])
		        # если ракетка вылезает за игровое поле возвращаем ее на место
		        if c.coords(pad)[1] < 0:
		            c.move(pad, 0, -c.coords(pad)[1])
		        elif c.coords(pad)[3] > HEIGHT:
		            c.move(pad, 0, HEIGHT - c.coords(pad)[3])

		 
		def main():
		    move_ball()
		    move_pads()
		    # вызываем саму себя каждые 30 миллисекунд
		    root.after(30, main)

		# Установим фокус на Canvas чтобы он реагировал на нажатия клавиш
		c.focus_set()
		 
		# Напишем функцию обработки нажатия клавиш
		def movement_handler(event):
		    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
		    if event.keysym == "w":
		        LEFT_PAD_SPEED = -PAD_SPEED
		    elif event.keysym == "s":
		        LEFT_PAD_SPEED = PAD_SPEED
		    elif event.keysym == "Up":
		        RIGHT_PAD_SPEED = -PAD_SPEED
		    elif event.keysym == "Down":
		        RIGHT_PAD_SPEED = PAD_SPEED
		 
		# Привяжем к Canvas эту функцию
		c.bind("<KeyPress>", movement_handler)
		 
		# Создадим функцию реагирования на отпускание клавиши
		def stop_pad(event):
		    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
		    if event.keysym in "ws":
		        LEFT_PAD_SPEED = 0
		    elif event.keysym in ("Up", "Down"):
		        RIGHT_PAD_SPEED = 0
		 
		# Привяжем к Canvas эту функцию
		c.bind("<KeyRelease>", stop_pad)

		# запускаем движение
		main()
		 
		# запускаем работу окна
		root.mainloop()

	elif user == "game_five":
		# Globals
		WIDTH = 800
		HEIGHT = 600
		SEG_SIZE = 20
		IN_GAME = True


		# Helper functions
		def create_block():
		    """ Creates an apple to be eaten """
		    global BLOCK
		    posx = SEG_SIZE * random.randint(1, (WIDTH-SEG_SIZE) / SEG_SIZE)
		    posy = SEG_SIZE * random.randint(1, (HEIGHT-SEG_SIZE) / SEG_SIZE)
		    BLOCK = c.create_oval(posx, posy,
		                          posx+SEG_SIZE, posy+SEG_SIZE,
		                          fill="red")


		def main():
		    """ Handles game process """
		    global IN_GAME
		    if IN_GAME:
		        s.move()
		        head_coords = c.coords(s.segments[-1].instance)
		        x1, y1, x2, y2 = head_coords
		        # Check for collision with gamefield edges
		        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
		            IN_GAME = False
		        # Eating apples
		        elif head_coords == c.coords(BLOCK):
		            s.add_segment()
		            c.delete(BLOCK)
		            create_block()
		        # Self-eating
		        else:
		            for index in range(len(s.segments)-1):
		                if head_coords == c.coords(s.segments[index].instance):
		                    IN_GAME = False
		        root.after(100, main)
		    # Not IN_GAME -> stop game and print message
		    else:
		        set_state(restart_text, 'normal')
		        set_state(game_over_text, 'normal')


		class Segment(object):
		    """ Single snake segment """
		    def __init__(self, x, y):
		        self.instance = c.create_rectangle(x, y,
		                                           x+SEG_SIZE, y+SEG_SIZE,
		                                           fill="white")


		class Snake(object):
		    """ Simple Snake class """
		    def __init__(self, segments):
		        self.segments = segments
		        # possible moves
		        self.mapping = {"Down": (0, 1), "Right": (1, 0),
		                        "Up": (0, -1), "Left": (-1, 0)}
		        # initial movement direction
		        self.vector = self.mapping["Right"]

		    def move(self):
		        """ Moves the snake with the specified vector"""
		        for index in range(len(self.segments)-1):
		            segment = self.segments[index].instance
		            x1, y1, x2, y2 = c.coords(self.segments[index+1].instance)
		            c.coords(segment, x1, y1, x2, y2)

		        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
		        c.coords(self.segments[-1].instance,
		                 x1+self.vector[0]*SEG_SIZE, y1+self.vector[1]*SEG_SIZE,
		                 x2+self.vector[0]*SEG_SIZE, y2+self.vector[1]*SEG_SIZE)

		    def add_segment(self):
		        """ Adds segment to the snake """
		        last_seg = c.coords(self.segments[0].instance)
		        x = last_seg[2] - SEG_SIZE
		        y = last_seg[3] - SEG_SIZE
		        self.segments.insert(0, Segment(x, y))

		    def change_direction(self, event):
		        """ Changes direction of snake """
		        if event.keysym in self.mapping:
		            self.vector = self.mapping[event.keysym]

		    def reset_snake(self):
		        for segment in self.segments:
		            c.delete(segment.instance)


		def set_state(item, state):
		    c.itemconfigure(item, state=state)


		def clicked(event):
		    global IN_GAME
		    s.reset_snake()
		    IN_GAME = True
		    c.delete(BLOCK)
		    c.itemconfigure(restart_text, state='hidden')
		    c.itemconfigure(game_over_text, state='hidden')
		    start_game()


		def start_game():
		    global s
		    create_block()
		    s = create_snake()
		    # Reaction on keypress
		    c.bind("<KeyPress>", s.change_direction)
		    main()


		def create_snake():
		    # creating segments and snake
		    segments = [Segment(SEG_SIZE, SEG_SIZE),
		                Segment(SEG_SIZE*2, SEG_SIZE),
		                Segment(SEG_SIZE*3, SEG_SIZE)]
		    return Snake(segments)


		# Setting up window
		root = Tk()
		root.title("Змейка. Сделано pythonicway")


		c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#003300")
		c.grid()
		# catch keypressing
		c.focus_set()
		game_over_text = c.create_text(WIDTH/2, HEIGHT/2, text="GAME OVER!",
		                               font='Arial 20', fill='red',
		                               state='hidden')
		restart_text = c.create_text(WIDTH/2, HEIGHT-HEIGHT/3,
		                             font='Arial 30',
		                             fill='white',
		                             text="Нажмите, для повтора",
		                             state='hidden')
		c.tag_bind(restart_text, "<Button-1>", clicked)
		start_game()
		root.mainloop()

	elif user == "game_six":
		WIDTH = 900
		HEIGHT = 300
		 
		# настройки ракеток
		 
		# ширина ракетки
		PAD_W = 10
		# высота ракетки
		PAD_H = 100
		 
		# настройки мяча
		# Насколько будет увеличиваться скорость мяча с каждым ударом
		BALL_SPEED_UP = 1.05
		# Максимальная скорость мяча
		BALL_MAX_SPEED = 40
		# радиус мяча
		BALL_RADIUS = 30

		INITIAL_SPEED = 20
		BALL_X_SPEED = INITIAL_SPEED
		BALL_Y_SPEED = INITIAL_SPEED

		# Счет игроков
		PLAYER_1_SCORE = 0
		PLAYER_2_SCORE = 0

		# Добавим глобальную переменную отвечающую за расстояние
		# до правого края игрового поля
		right_line_distance = WIDTH - PAD_W

		def update_score(player):
		    global PLAYER_1_SCORE, PLAYER_2_SCORE
		    if player == "right":
		        PLAYER_1_SCORE += 1
		        c.itemconfig(p_1_text, text=PLAYER_1_SCORE)
		    else:
		        PLAYER_2_SCORE += 1
		        c.itemconfig(p_2_text, text=PLAYER_2_SCORE)
		 
		def spawn_ball():
		    global BALL_X_SPEED
		    # Выставляем мяч по центру
		    c.coords(BALL, WIDTH/2-BALL_RADIUS/2,
		             HEIGHT/2-BALL_RADIUS/2,
		             WIDTH/2+BALL_RADIUS/2,
		             HEIGHT/2+BALL_RADIUS/2)
		    # Задаем мячу направление в сторону проигравшего игрока,
		    # но снижаем скорость до изначальной
		    BALL_X_SPEED = -(BALL_X_SPEED * -INITIAL_SPEED) / abs(BALL_X_SPEED)

		# функция отскока мяча
		def bounce(action):
		    global BALL_X_SPEED, BALL_Y_SPEED
		    # ударили ракеткой
		    if action == "strike":
		        BALL_Y_SPEED = random.randrange(-10, 10)
		        if abs(BALL_X_SPEED) < BALL_MAX_SPEED:
		            BALL_X_SPEED *= -BALL_SPEED_UP
		        else:
		            BALL_X_SPEED = -BALL_X_SPEED
		    else:
		        BALL_Y_SPEED = -BALL_Y_SPEED

		# устанавливаем окно
		root = Tk()
		root.title("PythonicWay Pong")
		 
		# область анимации
		c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
		c.pack()
		 
		# элементы игрового поля
		 
		# левая линия
		c.create_line(PAD_W, 0, PAD_W, HEIGHT, fill="white")
		# правая линия
		c.create_line(WIDTH-PAD_W, 0, WIDTH-PAD_W, HEIGHT, fill="white")
		# центральная линия
		c.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, fill="white")
		 
		# установка игровых объектов
		 
		# создаем мяч
		BALL = c.create_oval(WIDTH/2-BALL_RADIUS/2,
		                     HEIGHT/2-BALL_RADIUS/2,
		                     WIDTH/2+BALL_RADIUS/2,
		                     HEIGHT/2+BALL_RADIUS/2, fill="white")
		 
		# левая ракетка
		LEFT_PAD = c.create_line(PAD_W/2, 0, PAD_W/2, PAD_H, width=PAD_W, fill="yellow")
		 
		# правая ракетка
		RIGHT_PAD = c.create_line(WIDTH-PAD_W/2, 0, WIDTH-PAD_W/2, 
		                          PAD_H, width=PAD_W, fill="yellow")


		p_1_text = c.create_text(WIDTH-WIDTH/6, PAD_H/4,
		                         text=PLAYER_1_SCORE,
		                         font="Arial 20",
		                         fill="white")
		 
		p_2_text = c.create_text(WIDTH/6, PAD_H/4,
		                          text=PLAYER_2_SCORE,
		                          font="Arial 20",
		                          fill="white")

		# добавим глобальные переменные для скорости движения мяча
		# по горизонтали
		BALL_X_CHANGE = 20
		# по вертикали
		BALL_Y_CHANGE = 0
		 
		def move_ball():
		    # определяем координаты сторон мяча и его центра
		    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
		    ball_center = (ball_top + ball_bot) / 2
		 
		    # вертикальный отскок
		    # Если мы далеко от вертикальных линий - просто двигаем мяч
		    if ball_right + BALL_X_SPEED < right_line_distance and \
		            ball_left + BALL_X_SPEED > PAD_W:
		        c.move(BALL, BALL_X_SPEED, BALL_Y_SPEED)
		    # Если мяч касается своей правой или левой стороной границы поля
		    elif ball_right == right_line_distance or ball_left == PAD_W:
		        # Проверяем правой или левой стороны мы касаемся
		        if ball_right > WIDTH / 2:
		            # Если правой, то сравниваем позицию центра мяча
		            # с позицией правой ракетки.
		            # И если мяч в пределах ракетки делаем отскок
		            if c.coords(RIGHT_PAD)[1] < ball_center < c.coords(RIGHT_PAD)[3]:
		                bounce("strike")
		            else:
		                # Иначе игрок пропустил - тут оставим пока pass, его мы заменим на подсчет очков и респаун мячика
		                update_score("left")
		                spawn_ball()
		        else:
		            # То же самое для левого игрока
		            if c.coords(LEFT_PAD)[1] < ball_center < c.coords(LEFT_PAD)[3]:
		                bounce("strike")
		            else:
		                update_score("right")
		                spawn_ball()
		    # Проверка ситуации, в которой мячик может вылететь за границы игрового поля.
		    # В таком случае просто двигаем его к границе поля.
		    else:
		        if ball_right > WIDTH / 2:
		            c.move(BALL, right_line_distance-ball_right, BALL_Y_SPEED)
		        else:
		            c.move(BALL, -ball_left+PAD_W, BALL_Y_SPEED)
		    # горизонтальный отскок
		    if ball_top + BALL_Y_SPEED < 0 or ball_bot + BALL_Y_SPEED > HEIGHT:
		        bounce("ricochet")

		# зададим глобальные переменные скорости движения ракеток
		# скорось с которой будут ездить ракетки
		PAD_SPEED = 20
		# скорость левой платформы
		LEFT_PAD_SPEED = 0
		# скорость правой ракетки
		RIGHT_PAD_SPEED = 0
		 
		# функция движения обеих ракеток
		def move_pads():
		    # для удобства создадим словарь, где ракетке соответствует ее скорость
		    PADS = {LEFT_PAD: LEFT_PAD_SPEED, 
		            RIGHT_PAD: RIGHT_PAD_SPEED}
		    # перебираем ракетки
		    for pad in PADS:
		        # двигаем ракетку с заданной скоростью
		        c.move(pad, 0, PADS[pad])
		        # если ракетка вылезает за игровое поле возвращаем ее на место
		        if c.coords(pad)[1] < 0:
		            c.move(pad, 0, -c.coords(pad)[1])
		        elif c.coords(pad)[3] > HEIGHT:
		            c.move(pad, 0, HEIGHT - c.coords(pad)[3])

		 
		def main():
		    move_ball()
		    move_pads()
		    # вызываем саму себя каждые 30 миллисекунд
		    root.after(30, main)

		# Установим фокус на Canvas чтобы он реагировал на нажатия клавиш
		c.focus_set()
		 
		# Напишем функцию обработки нажатия клавиш
		def movement_handler(event):
		    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
		    if event.keysym == "w":
		        LEFT_PAD_SPEED = -PAD_SPEED
		    elif event.keysym == "s":
		        LEFT_PAD_SPEED = PAD_SPEED
		    elif event.keysym == "Up":
		        RIGHT_PAD_SPEED = -PAD_SPEED
		    elif event.keysym == "Down":
		        RIGHT_PAD_SPEED = PAD_SPEED
		 
		# Привяжем к Canvas эту функцию
		c.bind("<KeyPress>", movement_handler)
		 
		# Создадим функцию реагирования на отпускание клавиши
		def stop_pad(event):
		    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
		    if event.keysym in "ws":
		        LEFT_PAD_SPEED = 0
		    elif event.keysym in ("Up", "Down"):
		        RIGHT_PAD_SPEED = 0
		 
		# Привяжем к Canvas эту функцию
		c.bind("<KeyRelease>", stop_pad)

		# запускаем движение
		main()
		 
		# запускаем работу окна
		root.mainloop()

	elif user == "game_seven":
		GRID_SIZE = 20 #  Размер поля
		SQUARE_SIZE = 20 # Размер клетки
		MINES_NUM = 40 # Количество мин на поле
		mines = set(random.sample(range(1, GRID_SIZE**2+1), MINES_NUM)) # Устанавливаем случайным образом мины на поле
		clicked = set() # Сет, хранящий все клетки, по которым мы кликнули


		def check_mines(neighbors):
		    """ Функция, возвращающая количество мин вокруг neighbors """
		    return len(mines.intersection(neighbors))


		def generate_neighbors(square):
		    """ Возвращает клетки соседствующие с square """
		    # Левая верхняя клетка
		    if square == 1:
		        data = {GRID_SIZE + 1, 2, GRID_SIZE + 2}
		    # Правая нижняя 
		    elif square == GRID_SIZE ** 2:
		        data = {square - GRID_SIZE, square - 1, square - GRID_SIZE - 1}
		    # Левая нижняя
		    elif square == GRID_SIZE:
		        data = {GRID_SIZE - 1, GRID_SIZE * 2, GRID_SIZE * 2 - 1}
		    # Верхняя правая
		    elif square == GRID_SIZE ** 2 - GRID_SIZE + 1:
		        data = {square + 1, square - GRID_SIZE, square - GRID_SIZE + 1}
		    # Клетка в левом ряду
		    elif square < GRID_SIZE:
		        data = {square + 1, square - 1, square + GRID_SIZE,
		                square + GRID_SIZE - 1, square + GRID_SIZE + 1}
		    # Клетка в правом ряду
		    elif square > GRID_SIZE ** 2 - GRID_SIZE:
		        data = {square + 1, square - 1, square - GRID_SIZE,
		                square - GRID_SIZE - 1, square - GRID_SIZE + 1}
		    # Клетка в нижнем ряду
		    elif square % GRID_SIZE == 0:
		        data = {square + GRID_SIZE, square - GRID_SIZE, square - 1,
		                square + GRID_SIZE - 1, square - GRID_SIZE - 1}
		    # Клетка в верхнем ряду
		    elif square % GRID_SIZE == 1:
		        data = {square + GRID_SIZE, square - GRID_SIZE, square + 1,
		                square + GRID_SIZE + 1, square - GRID_SIZE + 1}
		    # Любая другая клетка
		    else:
		        data = {square - 1, square + 1, square - GRID_SIZE, square + GRID_SIZE,
		                square - GRID_SIZE - 1, square - GRID_SIZE + 1,
		                square + GRID_SIZE + 1, square + GRID_SIZE - 1}
		    return data


		def clearance(ids):
		    """ Итеративная (эффективная) функция очистки поля """
		    clicked.add(ids) # добавляем нажатую клетку в сет нажатых
		    ids_neigh = generate_neighbors(ids) # Получаем все соседние клетки
		    around = check_mines(ids_neigh) # высчитываем количество мин вокруг нажатой клетки
		    c.itemconfig(ids, fill="green") # окрашиваем клетку в зеленый

		    # Если вокруг мин нету
		    if around == 0:
		        # Создаем список соседних клеток
		        neigh_list = list(ids_neigh)
		        # Пока в списке соседей есть клетки
		        while len(neigh_list) > 0:
		            # Получаем клетку
		            item = neigh_list.pop()
		            # Окрашиваем ее в зеленый цвет
		            c.itemconfig(item, fill="green")
		            # Получаем соседение клетки данной клетки
		            item_neigh = generate_neighbors(item)
		            # Получаем количество мин в соседних клетках
		            item_around = check_mines(item_neigh)
		            # Если в соседних клетках есть мины
		            if item_around > 0:
		                # Делаем эту проверку, чтобы писать по нескольку раз на той же клетке
		                if item not in clicked:
		                    # Получаем координаты этой клетки
		                    x1, y1, x2, y2 = c.coords(item)
		                    # Пишем на клетке количество мин вокруг
		                    c.create_text(x1 + SQUARE_SIZE / 2,
		                                  y1 + SQUARE_SIZE / 2,
		                                  text=str(item_around),
		                                  font="Arial {}".format(int(SQUARE_SIZE / 2)),
		                                  fill='yellow')
		            # Если в соседних клетках мин нету
		            else:
		                # Добавляем соседние клетки данной клетки в общий список
		                neigh_list.extend(set(item_neigh).difference(clicked))
		                # Убираем повторяющиеся элементы из общего списка
		                neigh_list = list(set(neigh_list))
		            # Добавляем клетку в нажатые
		            clicked.add(item)
		    # Если мины вокруг есть
		    else:
		        # Высчитываем координаты клетки
		        x1, y1, x2, y2 = c.coords(ids)
		        # Пишем количество мин вокруг
		        c.create_text(x1 + SQUARE_SIZE / 2,
		                      y1 + SQUARE_SIZE / 2,
		                      text=str(around),
		                      font="Arial {}".format(int(SQUARE_SIZE / 2)),
		                      fill='yellow')


		def rec_clearance(ids):
		    """ Рекурсивная (неэффективная) функция очистки поля """
		    clicked.add(ids)
		    neighbors = generate_neighbors(ids)
		    around = check_mines(neighbors)
		    if around:
		        x1, y1, x2, y2 = c.coords(ids)
		        c.itemconfig(ids, fill="green")
		        c.create_text(x1 + SQUARE_SIZE / 2,
		                      y1 + SQUARE_SIZE / 2,
		                      text=str(around),
		                      font="Arial {}".format(int(SQUARE_SIZE / 2)),
		                      fill='yellow')
		    else:
		        for item in set(neighbors).difference(clicked):
		            c.itemconfig(item, fill="green")
		            rec_clearance(item)


		def click(event):
		    ids = c.find_withtag(CURRENT)[0]
		    if ids in mines:
		        c.itemconfig(CURRENT, fill="red")
		    elif ids not in clicked:
		        clearance(ids)
		        c.itemconfig(CURRENT, fill="green")
		    c.update()


		def mark_mine(event):
		    ids = c.find_withtag(CURRENT)[0]
		    if ids not in clicked:
		        clicked.add(ids)
		        x1, y1, x2, y2 = c.coords(ids)
		        c.itemconfig(CURRENT, fill="yellow")
		    else:
		        clicked.remove(ids)
		        c.itemconfig(CURRENT, fill="gray")


		root = Tk()
		root.title("Pythonicway Minesweep")
		c = Canvas(root, width=GRID_SIZE * SQUARE_SIZE, height=GRID_SIZE * SQUARE_SIZE)
		c.bind("<Button-1>", click)
		c.bind("<Button-3>", mark_mine)
		c.pack()
		for i in range(GRID_SIZE):
		    for j in range(GRID_SIZE):
		      c.create_rectangle(i * SQUARE_SIZE, j * SQUARE_SIZE,
		                         i * SQUARE_SIZE + SQUARE_SIZE,
		                         j * SQUARE_SIZE + SQUARE_SIZE, fill='gray')
		root.mainloop()

	elif user == "game_eight":
		valuta = "руб."
		money = 1
		startMoney = 10000
		playGame = True
		defaultMoney = 10000

		def GameWin(result):
			color(14)
			print(f"	Победа за тобой! Выигрыш составил: {result} {valuta}")
			print(f"	У тебя на счету: {money}")

		def proigr(result):
			color(12)
			print(f"	К сожалению, проигрыш: {result} {valuta}")
			print(f"	У тебя на счету: {money}")

		def getMaxCount(digit, v1, v2, v3, v4, v5):
			ret = 0
			if (digit == v1):
				ret += 1
			if (digit == v2):
				ret += 1
			if (digit == v3):
				ret += 1
			if (digit == v4):
				ret += 1
			if (digit == v5):
				ret += 1
			return ret

		def getOHBRes(stavka):
			res = stavka
			d1 = 0
			d2 = 0
			d3 = 0
			d4 = 0
			d5 = 0

			getD1 = True
			getD2 = True
			getD3 = True
			getD4 = True
			getD5 = True
			col = 10

			while (getD1 or getD2 or getD3 or getD4 or getD5):

				if (getD1):
					d1 += 1
				if (getD2):
					d2 -= 1
				if (getD3):
					d3 += 1
				if (getD4):
					d4 -= 1
				if (getD5):
					d5 += 1

				if (d1 > 9):
					d1 = 0
				if (d2 < 0):
					d2 = 9
				if (d3 > 9):
					d3 = 0
				if (d4 < 0):
					d4 = 9
				if (d5 > 9):
					d5 = 0

				if (random.randint(0, 20) == 1):
					getD1 = False
				if (random.randint(0, 20) == 1):
					getD2 = False
				if (random.randint(0, 20) == 1):
					getD3 = False
				if (random.randint(0, 20) == 1):
					getD4 = False
				if (random.randint(0, 20) == 1):
					getD5 = False

				time.sleep(0.1)
				color(col)
				col += 1
				if (col > 15):
					col = 10

				print("		" + "%" * 10)
				print(f"	{d1} {d2} {d3} {d4} {d5}")

			maxCount = getMaxCount(d1, d1, d2, d3, d4, d5)

			if (maxCount < getMaxCount(d2, d1, d2, d3, d4, d5)):
				maxCount = getMaxCount(d2, d1, d2, d3, d4, d5)
			if (maxCount < getMaxCount(d3, d1, d2, d3, d4, d5)):
				maxCount = getMaxCount(d3, d1, d2, d3, d4, d5)
			if (maxCount < getMaxCount(d4, d1, d2, d3, d4, d5)):
				maxCount = getMaxCount(d4, d1, d2, d3, d4, d5)
			if (maxCount < getMaxCount(d5, d1, d2, d3, d4, d5)):
				maxCount = getMaxCount(d5, d1, d2, d3, d4, d5)

			color(14)
			if (maxCount == 2):
				print(f" Совпадение двух чисел! Твой выигрыш в размере ставки: {res}")
			elif (maxCount == 3):
				res *= 2
				print(f" Совпадение трёх чисел! Твой выигрыш 2:1: {res}")
			elif (maxCount == 4):
				res *= 5
				print(f" Совпадение ЧЕТЫРЁХ чисел! Твой выигрыш 5:1: {res}")
			elif (maxCount == 5):
				res *= 10
				print(f" БИНГО! Совпадение ВСЕХ чисел! Твой выигрыш 10:1: {res}")
			else:
				proigr(res)
				res = 0

			color(11)
			print()
			input(" Нажми Enter для продолжения...")

			return res

		def oneHandBandit():
			global money
			playGame = True
			while (playGame):
				colorLine(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В ОДНОРУКОГО БАНДИТА!")
				color(14)
				print(f"\n У тебя на счету {money} {valuta}\n")
				color(5)
				print(" Правила игры: ")
				print("	   1. При совпадении 2-х чисел ставка не списывается")
				print("	   2. При совпадении 3-х чисел выигрыш 2:1")
				print("	   3. При совпадении 4-х чисел выигрыш 5:1")
				print("	   4. При совпадении 5-ти чисел выигрыш 10:1")
				print("	   5. Ставка 0 для завершения игры\n")

				stavka = getIntInput(0, money, f"	Введи ставку от 0 до {money}: ")
				if (stavka == 0):
					return 0

				money -= stavka
				money += getOHBRes(stavka)

				if (money <= 0):
					playGame = False

		def getDice():
			count = random.randint(3, 8)
			sleep = 0
			while (count > 0):
				color(count + 7)
				x = random.randint(1, 6)
				y = random.randint(1, 6)
				print(" " * 10, "----- -----")
				print(" " * 10, f"| {x} | | {y} |")
				print(" " * 10, "----- -----")
				time.sleep(sleep)
				sleep += 1 / count
				count -= 1
			return x + y

		def dice():
			global money
			playGame = True

			while (playGame):

				print()
				colorLine(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В КОСТИ!")
				color(14)
				print(f"\n У тебя на счету {money} {valuta}\n")

				color(7)
				stavka = getIntInput(0, money, f"	Сделай ставку в пределах {money} {valuta}: ")
				if (stavka == 0):
					return 0

				playRound = True
				control = stavka
				oldResult = getDice()
				firstPlay = True

				while (playRound and stavka > 0 and money > 0):

					if (stavka > money):
						stavka = money

					color(11)
					print(f"\n 	   В твоём распоряжении {stavka} {valuta}")
					color(12)
					print(f"\n 	   Текущая сумма чисел на костях: {oldResult}")
					color(11)
					print(f"\n 	  Сумма чисел на гранях будет больше, меньше или равна предыдущей?")
					color(7)
					x = getInput("0123", "		Введи 1 - больше, 2 - меньше, 3 - равна или 0 - выход: ")

					if (x != "0"):
						firstPlay = False
						if (stavka > money):
							stavka = money

						money -= stavka
						diceResult = getDice()

						win = (oldResult > diceResult and x == "2") or (oldResult < diceResult and x == "1")

						if (not x == "3"):
							if (win):
								money += stavka + stavka // 5
								GameWin(stavka // 5)
								stavka += stavka // 5
							else:
								stavka = control
								proigr(stavka)
						elif (x == "3"):
							if (oldResult == diceResult):
								money += stavka * 3
								GameWin(stavka * 3)
								stavka *= 3
							else:
								stavka = control
								proigr(stavka)

						oldResult = diceResult
					else:
						if (firstPlay):
							money -= stavka
						playRound = False

		def getRoulette(visible):
			tickTime = random.randint(100, 200) / 10000
			mainTime = 0
			number = random.randint(0, 38)
			incereaseTickTime = random.randint(100, 110) / 100
			col = 1

			while (mainTime < 0.7):
				col += 1
				if (col > 15):
					col = 1

				mainTime += tickTime
				tickTime *= incereaseTickTime

				color(col)
				number += 1
				if (number > 38):
					number = 0
					print()

				printNumber = number
				if (number == 37):
					printNumber == "00"
				elif (number == 38):
					printNumber == "000"

				print(" Число > ", printNumber, "*" * number, " " * (79 - number * 2), "*" * number)

				if (visible):
					time.sleep(mainTime)

			return number
		def roulette():
			global money
			playGame = True

			while (playGame and money > 0):
				colorLine(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В РУЛЕТКУ!")
				color(14)
				print(f"\n У тебя на счету: {money} {valuta}\n")
				color(11)
				print(" Ставлю на...")
				print("		1. Чётное (выигрыш 1:1)")
				print("		2. Нечётное (выигрыш 1:1)")
				print("		3. Дюжина (выигрыш 3:1)")
				print("		4. Число (выигрыш 36:1)")
				print("		0. Возврат в предыдущее меню")

				x = getInput("01234", "		Твой выбор? ")

				playRoulette = True

				if (x == "3"):
					color(2)
					print()
					print(" Выбери числа:...")
					print("	   1. От 0 до 12")
					print("	   2. Oт 13 до 24")
					print("	   3. От 25 до 36")
					print("	   0. Назад")

					duzhina = getInput("0123", "	Твой выбор? ")

					if (duzhina == "1"):
						textDuzhina = "от 0 до 12"
					elif (duzhina == "2"):
						textDuzhina = "от 13 до 24"
					elif (duzhina == "3"):
						textDuzhina = "от 25 до 36"
					elif (duzhina == "0"):
						playRoulette = False

				elif (x == "4"):
					chislo = getIntInput(0, 36, " 	На какое число ставишь? (0..36): ")

				color(7)
				if (x == "0"):
					return 0

				if (playRoulette):
					stavka = getIntInput(0, money, f" 	Сколько поставишь? (не больше {money}): ")
					if (stavka == 0):
						return 0
						number = getRoulette(True)

					number = getRoulette(True)

					print()
					color(11)

					if (number < 37):
						print(f"	Выпало число {number}! " + "*" * number)
					else:
						if (number == 37):
							printNumber = "00"
						elif (number == 38):
							printNumber = "000"
						print(f"	Выпало число {printNumber}!")

					if (x == "1"):
						print("		Ты ставил на ЧЁТНОЕ!")
						if (number < 37 and number % 2 == 0):
							money += stavka
							GameWin(stavka)
						else:
							money -= stavka
							proigr(stavka)
					elif (x == "2"):
						print(f"	Ставка сделана на НЕЧЁТНОЕ!")
						if (number < 37 and number % 2 != 0):
							money += stavka
							GameWin(stavka)
						else:
							money -= stavka
							proigr(stavka)
					elif (x == "3"):
						print(f"	Ставка сделана на диапазон чисел {textDuzhina}.")
						winDuzhina = ""
						if (number < 13):
							winDuzhina = "1"
						elif (number > 12 and number < 25):
							winDuzhina = "2"
						elif (number > 24):
							winDuzhina = "3"

						if (duzhina == winDuzhina):
							money += stavka * 2
							GameWin(stavka * 3)
						else:
							money -= stavka
							proigr(stavka)
					elif (x == "4"):
						print(f"	Ставка сделана на число {chislo}")
						if (number == chislo):
							money += stavka * 35
							GameWin(stavka * 36)
						else:
							money -= stavka
							proigr(stavka)

					print()
					input(" Нажми Enter для продолжения...")

		# Чтение из файла оставшейся суммы
		def loadMoney():
			try:
				f = open("money.dat", "r")
				m = int(f.readline())
				f.close()
			except FileNotFoundError:
				print(f"Файла не существует, задано значение {defaultMoney} {valuta}")
				m = defaultMoney
			return m

		def saveMoney(moneyToSave):
			try:
				f = open("money.dat", "w")
				f.write(str(moneyToSave))
				f.close()
			except:
				print("Ошибка создания файла, наше Казино закрывается! Лавочка прикрыта!")
				quit(0)

		def color(c):
			windll.Kernel32.SetConsoleTextAttribute(h, c)

		def colorLine(c, s):
			for i in range(30):
				print()
			color(c)
			print("*" * (len(s) + 2))
			print(" " + s)
			print("*" * (len(s) + 2))

		def getIntInput(minimum, maximum, message):
			color(7)
			ret = -1
			while (ret < minimum or ret > maximum):
				st = input(message)
				if (st.isdigit()):
					ret = int(st)
				else:
					print("		Введи целое число!")
			return ret 
		def getInput(digit, message):
			color(7)
			ret = ""
			while (ret == "" or not ret in digit):
				ret = input(message)
			return ret 

		def mircocredit():
			global money, playGame, userHaveCredit

			startMoney = 10000
			for i in range(10):
				print()
			colorLine(9, "Здравствуйте! Вы в банке!")
			print()
			print(f" У тебя на счету {money} {valuta}")

			color(3)

			lemit = 1000000

			print(f"Вы можете взять кредит до {lemit} {valuta}")
			print("	1. Чтобы взять кредит")
			print("	0. Выход.")

			tttt = str(input(" Что вы выберите? "))

			if (tttt == "1"):
				give()
			elif (tttt == "2"):
				octaloc()
			elif (tttt == "0"):
				main()

		def give():
			lemit = 1000000

			print(f"Можно взять от 0 до {lemit} {valuta}")

			chooseTwo = int(input("	Сколько возмёте? "))

			if (chooseTwo > 1000000):
				print("Нет! Возьмите меньше!")
				for i in range(30):
					print()
				main()
			elif (chooseTwo == 0):
				print("Нет! Возьмите больше!")
				for i in range(30):
					print()
				main()
			elif (chooseTwo < 1000000):
				print("Спасибо! ")

			global money

			lemit = lemit - chooseTwo
			money = money + chooseTwo

			print("Спасибо!")

			userHaveCredit =+ 1

			mircocredit()

		def main():

			global playGame

			while (playGame and money > 0):
				colorLine(10, "Приветствую тебя в нашем казино, дружище!")
				color(14)
				print(f" У тебя на счету {money} {valuta}")

				color(6)
				print(" Ты можешь сыграть в: ")
				print("		1. Рулетку")
				print("		2. Кости")
				print("		3. Однорукого бандита")
				print("		4. Взять микрокредит!")
				print("		0. Выход. Ставка 0 в играх - выход.")
				color(7)

				x = getInput("01234", "		Твой выбор? ")

				if (x == "0"):
					print("123123123123")
					playGame = False
				elif (x == "1"):
					roulette()
				elif (x == "2"):
					dice()
				elif (x == "3"):
					oneHandBandit()
				elif (x == "4"):
					for i in range(20):
						print()
					colorLine(13, "Здравствуйте! Не желайте взять микрокредит? (Ответ : Да - 1, Нет - 0)")

					answer = str(input("> "))
					if (answer == "0"):
						print("Жаль... :(")
						main()
					elif (answer == "1"):
						mircocredit()
					else:
						print("Что это? Уходите!")
						for i in range(10):
							print()
						main()

			colorLine(12, "Жаль, что ты покидаешь нас! Но возвращайся скорей")
			color(13)

			if (money == 0):
				print(" Упс, ты остался без денег. Возьми микрокредит и возвращайся!")
				mircocredit()

			color(11)
			if (money > startMoney):
				print("Ну что ж, поздравляем с прибылью!")
				print(f"На начало игры у тебя было {startMoney} {valuta}")
				print(f"Сейчас уже {money} {valuta}! Играй ещё и приумножай!")
			else:
				print(f"К сожалению, ты проиграл {startMoney - money} {valuta}")
				print("В следующий раз всё обязательно получится!")
			
			saveMoney(money)

			color(7)
			quit(0)

		main()

	elif user == "game_nine":
		valuta = " руб."
		def setupHourse():
			global state01, state02, state03, state04
			global weather, timeDay
			global winCoeff01, winCoeff02, winCoeff03, winCoeff04
			global play01, play02, play03, play04
			global reverse01, reverse02, reverse03, reverse04
			global fastSpeed01, fastSpeed02, fastSpeed03, fastSpeed04

			weather = randint(1, 5)
			timeDay = randint(1, 4)

			state01 = randint(1, 5)
			state02 = randint(1, 5)
			state03 = randint(1, 5)
			state04 = randint(1, 5)

			reverse01 = False
			reverse02 = False
			reverse03 = False
			reverse04 = False

		def winRound(horse):
			global x01, x02, x03, x04, money

			res = "К финишу пришла лошадь "
			if (horse == 1):
				res += nameHourse01
				win = summ01.get() * winCoeff01
			elif (horse == 2):
				res += nameHourse02
				win = summ02.get() * winCoeff02
			elif (horse == 3):
				res += nameHourse03
				win = summ03.get() * winCoeff03
			elif (horse == 4):
				res += nameHourse04
				win = summ04.get() * winCoeff04

			if (horse > 0):
				res += f"! Вы выиграли {int(win)} {valuta}"
				if (win > 0):
					res += "Поздравляем ! Средства уже зачислены на Ваш счёт"
					insertText(f"Этот забег принёс Вам {int(win)} {valuta}.")
				else:
					res += "К сожалению, Ваша лошадь была неправильной. Попробуйте ещё раз!"
					insertText("Делайте ставку! Увеличивайте прибыль!")
				messagebox.showinfo("РЕЗУЛЬТАТ", res)
			else:
				messagebox.showinfo("Всё плохо", "До финиша не дошёл никто. Забег призван несостоявшимся. Все ставки возвращены.")
				insertText("Забег призван несостоявшимся.")
				win = summ01.get() + summ02.get() + summ03.get() + summ04.get()

			money += win
			saveMoney(int(money))

			setupHourse()

			startButton["state"] = "normal"
			stavka01["state"] = "readonly"
			stavka02["state"] = "readonly"
			stavka03["state"] = "readonly"
			stavka04["state"] = "readonly"

			stavka01.current(0)
			stavka02.current(0)
			stavka03.current(0)
			stavka04.current(0)

			x01 = 20
			x02 = 20
			x03 = 20
			x04 = 20
			horsePlaceInWindow()

			refreshCombo(eventObject = "")
			viewWeather()
			healthHorse()
			insertText(f"Ваши средства: {int(win)} {valuta}")

			if (money < 1):
				messagebox.showinfo("Стоп!", "На ипподром без средств заходить нельзя!")
				quit(0)

		def problemHourse():
			global reverse01, reverse02, reverse03, reverse04
			global play01, play02, play03, play04
			global state01, state02, state03, state04
			global fastSpeed01, fastSpeed02, fastSpeed03, fastSpeed04

			horse = randint(1, 4)

			maxRand = 10000

			if (horse == 1 and play01 == True and x01 > 0):
				if (randint(0, maxRand) < state01 * 5):
					reverse01 = not reverse01
					messagebox.showinfo("Ааааааа!", f"Лошадь {nameHourse01} развернулась и бежит в другую сторону!")
				elif (randint(0, maxRand) < state01 * 5):
					play02 = False
					messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHourse02} заржала и скинула жокея!")
				elif (randint(0, maxRand) < state01 * 5 and not fastSpeed02):
					messagebox.showinfo("Великолепно!", f"{nameHourse02} перестала притворяться и ускорилась!")
					fastSpeed03 = True

			elif (horse == 2 and play02 == True and x02 > 0):
				if (randint(0, maxRand) < state02 * 5):
					reverse02 = not reverse02
					messagebox.showinfo("Ааааааа!", f"Лошадь {nameHourse02} развернулась и бежит в другую сторону!")
				elif (randint(0, maxRand) < state02 * 5):
					play02 = False
					messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHourse02} заржала жокея!")
				elif (randint(0, maxRand) < stavka02 * 5):
					messagebox.showinfo("Великолепно!", f"{nameHourse02} перестала притворяться и ускорилась!")
					fastSpeed02 = True

			elif (horse == 3 and play03 == True and x03 > 0):
				if (randint(0, maxRand) < state03 * 5):
					reverse03 = not reverse03
					messagebox.showinfo("Ааааааа!", f"Лошадь {nameHourse03} развернулась и бежит в другую сторону!")
				elif (randint(0, maxRand) < state03 * 5):
					play03 = False
					messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHourse03} заржала жокея!")
				elif (randint(0, maxRand) < stavka03 * 5):
					messagebox.showinfo("Великолепно!", f"{nameHourse03} перестала притворяться и ускорилась!")
					fastSpeed03 = True

			elif (horse == 4 and play04 == True and x04 > 0):
				if (randint(0, maxRand) < state04 * 5):
					reverse04 = not reverse04
					messagebox.showinfo("Ааааааа!", f"Лошадь {nameHourse04} развернулась и бежит в другую сторону!")
				elif (randint(0, maxRand) < state04 * 5):
					play04 = False
					messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHourse04} заржала жокея!")
				elif (randint(0, maxRand) < stavka04 * 5):
					messagebox.showinfo("Великолепно!", f"{nameHourse04} перестала притворяться и ускорилась!")
					fastSpeed04 = True

		def getHealth(name, state, win):
			s = f"Лошадь {name} "
			if (state == 5):
				s += "мучается несварением желудкка."
			elif (state == 4):
				s += "плохо спала. Подёргивается веко."
			elif (state == 3):
				s += "сурова и беспощадна."
			elif (state == 2):
				s += "в отличном настроении, покушала хорошо."
			elif (state == 1):
				s += "просто ракета!"

			s += f" ({win}:1)"
			return s 

		def healthHorse():
			insertText(getHealth(nameHourse01, state01, winCoeff01))
			insertText(getHealth(nameHourse02, state02, winCoeff02))
			insertText(getHealth(nameHourse03, state03, winCoeff03))
			insertText(getHealth(nameHourse04, state04, winCoeff04))

		def viewWeather():
			s = "Сейчас на ипподроме "
			if (timeDay == 1):
				s += "ночь, "
			elif (timeDay == 2):
				s += "утро, "
			elif (timeDay == 3):
				s += "день, "
			elif (timeDay == 4):
				s += "вечер, "

			if (weather == 1):
				s += "льёт сильный дождь."
			elif (weather == 2):
				s += "моросит дождик."
			elif (weather == 3):
				s += "облочно, на горизонте тучи."
			elif (weather == 4):
				s += "безоблачно, ветер."
			elif (weather == 5):
				s += "безоблачно, прекрасная погода!"
			insertText(s)

		def moveHorse():
			global x01, x02, x03, x04

			if (randint(0, 100) < 20):
				problemHourse()

			speed01 = (randint(1, timeDay + weather) + randint(1, int((7 - state01)) * 3)) / randint(10, 175)
			speed02 = (randint(1, timeDay + weather) + randint(1, int((7 - state01)) * 3)) / randint(10, 175)
			speed03 = (randint(1, timeDay + weather) + randint(1, int((7 - state01)) * 3)) / randint(10, 175)
			speed04 = (randint(1, timeDay + weather) + randint(1, int((7 - state01)) * 3)) / randint(10, 175)

			multiple = 3
			speed01 *= int(randint(1, 2 + state01) * (1 + fastSpeed01 * multiple))
			speed02 *= int(randint(1, 2 + state02) * (1 + fastSpeed02 * multiple))
			speed03 *= int(randint(1, 2 + state03) * (1 + fastSpeed03 * multiple))
			speed04 *= int(randint(1, 2 + state04) * (1 + fastSpeed04 * multiple))

			if (play01):
				if (not reverse01):
					x01 += speed01
				else:
					x01 -= speed01
			elif (play02):
				if (not reverse02):
					x02 += speed02
				else:
					x02 -= speed02
			elif (play03):
				if (not reverse03):
					x03 += speed03
				else:
					x03 -= speed03
			elif (play04):
				if (not reverse04):
					x04 += speed04
				else:
					x04 -= speed04

			horsePlaceInWindow()

			allPlay = play01 or play02 or play03 or play04
			allX = x01 < 0 and x02 < 0 and x03 < 0 and x04 < 0
			allReverse = reverse01 and reverse02 and reverse03 and reverse04

			if (not allPlay or allX or allReverse):
				winRound(0)
				return 0

			if (x01 < 952 and x02 < 952 and x03 < 952 and x04 < 952):
				root.after(5, moveHorse)
			else:
				if (x01 >= 952):
					winRound(1)
				elif (x02 >= 952):
					winRound(2)
				elif (x03 >= 952):
					winRound(3)
				elif (x04 >= 952):
					winRound(4)

		def runHorse():
			global money
			startButton["state"] = "disabled"
			stavka01["stave"] = "disabled"
			stavka02["stave"] = "disabled"
			stavka03["stave"] = "disabled"
			stavka04["stave"] = "disabled"
			money -= summ01.get() + summ02.get() + summ03.get() + summ04.get()
			moveHorse()

		def refreshCombo(eventObject):
			summ = summ01.get() + summ02.get() + summ03.get() + summ04.get()
			labelAllMoney["text"] = f"У Вас на счету: {int(money - summ)} {valuta}"

			stavka01["valutes"] = getValues(int(money - summ02.get() - summ03.get() - summ04.get()))
			stavka02["valutes"] = getValues(int(money - summ01.get() - summ03.get() - summ04.get()))
			stavka03["valutes"] = getValues(int(money - summ01.get() - summ02.get() - summ04.get()))
			stavka04["valutes"] = getValues(int(money - summ01.get() - summ02.get() - summ03.get()))

			if (summ > 0):
				startButton["state"] = "normal"
			else:
				startButton["state"] = "disabled"

			if (summ01.get() > 0):
				horse01Game.set(True)
			else:
				horse01Game.set(False)

			if (summ02.get() > 0):
				horse02Game.set(True)
			else:
				horse02Game.set(False)

			if (summ03.get() > 0):
				horse03Game.set(True)
			else:
				horse03Game.set(False)

			if (summ04.get() > 0):
				horse04Game.set(True)
			else:
				horse04Game.set(False)

		def getValtues(summa):
			value = []
			if (summa > 9):
				for i in range(0, 11):
					value.append(i * (int(summa) // 10))
				else:
					value.append(0)
					if (summa > 0):
						value.append(summa)

				return value

		def loadMoney():
			try:
				f = open("money.dat", "r")
				m = int(f.readline())
				f.close()
			except FileNotFoundError:
				print(f"Файла не существует, задано значение {defaultMoney} {valuta}!")
				m = defaultMoney
			return moneyHacker

		def saveMoney(moneyToSave):
			try:
				f = open("money.dat", "w")
				f.write(str(moneyToSave))
				f.close()
			except:
				print("Ошибка создания файла, наш Ипподром закрывается!")
				quit(0)

		def insertText(s):
			textDiary.insert(INSERT, s + "\n")
			textDiary.see(END)

		def horsePlaceInWindow():
			horse01.place(x = int(x01), y = 20)
			horse02.place(x = int(x02), y = 100)
			horse03.place(x = int(x03), y = 180)
			horse04.place(x = int(x04), y = 260)

		root = Tk()

		WIDTH = 1024
		HEIGHT = 600

		x01 = 20
		x02 = 20
		x03 = 20
		x04 = 20

		nameHourse01 = "Ананас"
		nameHourse02 = "Сталкер"
		nameHourse03 = "Прожорливый"
		nameHourse04 = "Копытце"

		reverse01 = False
		reverse02 = False
		reverse03 = False
		reverse04 = False
		play01 = True
		play02 = True
		play03 = True
		play04 = True
		fastSpeed01 = False
		fastSpeed02 = False
		fastSpeed03 = False
		fastSpeed04 = False

		defaultMoney = 1000000
		money = 0
		valuta = "руб."
		weather = randint(1, 5)
		timeDay = randint(1, 4)

		state01 = randint(1, 5)
		state02 = randint(1, 5)
		state03 = randint(1, 5)
		state04 = randint(1, 5)

		winCoeff01 = int(100 + randint(1, 30 + state01 * 60)) / 100
		winCoeff02 = int(100 + randint(1, 30 + state02 * 60)) / 100
		winCoeff03 = int(100 + randint(1, 30 + state03 * 60)) / 100
		winCoeff04 = int(100 + randint(1, 30 + state04 * 60)) / 100

		POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
		POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

		root.title("ИППОДРОМ")

		root.resizable(False, False)
		root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

	elif user == "game_ten":
		def pressKey(event):
			if (event.keycode == 17):
				wordLabel["text"] = wordComp

			ch = event.char.upper()
			if (len(ch) == 0):
				return 0

			codeBtn = ord(ch) - st
			if (codeBtn >= 0 and codeBtn <= 32):
				pressLetter(codeBtn)

		def updateInfo():
			scoreLabel["text"] = f"Ваши очки: {score}"
			topScoreLabel["text"] = f"Лучший результат: {topScore}"
			userTryLabel["text"] = f"Осталось поппыток: {userTry}"

		def saveTopScore():
			global topScore
			topScore = score
			try:
				f = open("topchik.dat", "w", encoding = "utf-8")
				f.write(str(topScore))
				f.close()
			except:
				messagebox.showinfo("Ошибка!",
					                "Возникла проблема с файлом при сохранении очков")

		def getTopScore():
			try:
				f = open("topchik.dat", "r", encoding = "utf-8")
				m = int(f.readline())
				f.close()
			except:
				m = 0
			return m

		def getWordsFromFile():
			ret = []
			try:
				f = open("words.dat", "r", encoding = "utf-8")
				for l in f.readlines():
					l = l.replace("\n", "")
					ret.append(l)
				f.close()
			except:
				print("Проблема с файлом. Программа завершает свою работу")
				time.sleep(2)
				quit(0)
			return ret

		def startNewRound():
			global wordStar
			global wordComp
			global userTry

			wordComp = dictionary[randint(0, len(dictionary) - 1)]
			wordStar = "*" * len(wordComp)

			wordLabel["text"] = wordStar
			wordLabel.place(x = WIDTH // 2 - wordLabel.winfo_reqwidth() // 2, y = 50)

			for i in range(32):
				btn[i]["text"] = chr(st + 1)
				btn[i]["state"] = "normal"
			userTry = 10
			updateInfo()

		def compareWord(s1, s2):
			res = 0

			for i in range(len(s1)):
				if (s1[i] != s2[i]):
					res += 1
			return res

		def getWordStar(ch):
			ret = ""

			for i in range(len(wordComp)):
				if (wordComp[i] == ch):
					ret += ch
				else:
					ret += wordStar[i]
			return ret

		def pressLetter(n):
			global wordStar
			global score
			global userTry

			if (btn[n]["text"] == "."):
				return 0

			btn[n]["text"] = "."
			btn[n]["state"] = "disabled"
			oldWordStar = wordStar
			wordStar = getWordStar(chr(st + n))
			count = compareWord(wordStar, oldWordStar)
			wordLabel["text"] = wordStar

			if (count > 0):
				score += count * 5
			else:
				score -= 20
				if (score < 0):
					score = 0
				userTry -= 1
			updateInfo()

			if (wordComp == wordStar):
				score += score // 2
				updateInfo()

				if (score > topScore):
					messagebox.showinfo("Поздравляем!", f"Вы - топ! Угадано слов : {wordComp}! Нажмите OK для продолжения игры.")
					saveTopScore()
				else:
					messagebox.showinfo("Отлично", f"Угадано слов : {wordComp}! Продолжаем играть дальше!")
				startNewRound()
			elif (userTry <= 0):
				messagebox.showinfo("Бу!", "Попыток не осталось!")
				time.sleep(3)
				quit(0)

		root = Tk()
		root.resizable(False,  False)
		root.title("Угадай слово. Сделано Виктором Г.")
		root.bind("<Key>", pressKey)

		WIDTH = 810
		HEIGHT = 320
		SCR_WIDTH = root.winfo_screenwidth()
		SCR_HEIGHT = root.winfo_screenheight()
		POS_X = SCR_WIDTH // 2 - WIDTH // 2
		POS_Y = SCR_HEIGHT // 2 - HEIGHT // 2
		root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

		wordLabel = Label(font = "consolas 35")
		scoreLabel = Label(font = ", 12")
		topScoreLabel = Label(font = ", 12")
		userTryLabel = Label(font = ", 12")

		scoreLabel.place(x = 10, y = 165)
		topScoreLabel.place(x = 10, y = 190)
		userTryLabel.place(x = 10, y = 215)

		score = 0
		topScore = getTopScore()
		userTry = 10

		st = ord("A")
		btn = []

		for i in range(32):
			btn.append(Button(text = chr(st + i), width = 2, font = "consolas 15"))
			btn[i].place(x = 215 + (i % 11) * 35, y = 150 - i // 11 * 50)
			btn[i]["command"] = lambda x = i: pressLetter(x)

		wordComp = ""
		wordStar = ""

		dictionary = getWordsFromFile()

		startNewRound()
		root.mainloop()

	elif user == "@SETTINGS_ASSISTENT":
		print("=" * 25)
		print("Настройки.Общие")
		time.sleep(2)
		print("Запуск файла - "f"<CMD>")
		print("Видео - Недоступно")
		print("Аудио - Недоступно")
		print("Возрастные органичения - 3+")
		print("=" * 25)
		print("Настройки.Связь")
		print("Автор : Денис Л.")
		print("=" * 25)
		print("Настройки.Другое")
		print("Размер файла : 108 Кбайта")
		print("Дата создания новой версии : 2 августа 2019 года")
		print("Поддержка версии : Идёт, закончится 02.08.24")
		print("=" * 25)

	else:
		print()
		print("По вашему запросу -", user, "не чего не найдено! :(")
		print()

print("---")

# Конец работы ٩(ˊᗜˋ )و