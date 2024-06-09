# Welcome Phia to Hangman!
# You have 5 Lives to guess the correct letter for the word
# Hiragana/Katakana letter will  be shown
# Please enter category: 2
#     [1] - Animals
#     [2] - Things
#     [3] - Places
# Please enter (H) forHiragana(ひらがな) or (K) for Katakana(カタカナ): H
# /******************************************************************/
#  Lives:　❤️❤️❤️❤️❤️
#  Topic: Animals
#  Guess the word: _ _ _
#           ----------------------
#           *                    *
#           *                    *
#           *                ---------
#           *                | ＞﹏＜ |
#           *                ---------
#           *                   /|\
#           *                  / \ \
#           *                 /  |  \
#           *                    \
#           *                    |
#           *                    \
#           *                   | \
#           *                  |   \
#           *                 |     \
#           *
#           *
#           *
#           *
#           *
#      ***********
#
#   あ　か　さ　た　な　は　ま　や　ら　わ　ん　が　ざ　だ　ば　ぱ
# 　い　き　し　ち　ひ　み　り　ぎ　じ　dzi　び　ぴ
#   う　く　す　つ　ぬ　む　ゆ　る　ぐ　ず　dzu　ぶ　ぷ
#   え　け　せ　て　ね　へ　め　れ　げ　ぜ　で　べ　ぺ
# 　お　こ　そ　と　の　ほ　も　よ　ろ　を　ご　ぞ　ど　ぼ　ぽ
#
# Enter the letter:
#
# /******************************************************************/

import sys, random, os

Animals = ["ねこ", "いぬ", "とり", "さかな"]
Things = ["いつ", "つくえ", "かばん", "ほん"]
Places = ["びゅおいん", "こんびに", "でぱと"]
MissingWord = []


def displayHangman():
    headPart = ["---------", "| ＞﹏＜ |", "---------"]
    bodyPart = ["|", "/", "\\"]

    #  head
    for i in headPart:
        print(i)

    # upper body
    n = 2
    m = 0
    a = 0
    while a < 3:
        print(f" {" " * n}{bodyPart[1]}{" "*m}{bodyPart[0]}{" " * m}{bodyPart[2]}")
        n = n - 1
        m = m + 1
        a = a + 1

    # bottom half
    a = 0
    while a < 3:
        print(f"    {bodyPart[0]}")
        a = a + 1

    # legs
    a = 0
    m = 1
    n = 2
    while a < 3:
        print(f" {" " * n }{bodyPart[1]}{" "*m}{bodyPart[2]}")
        n = n - 1
        m = m + 2
        a = a + 1


def menu(name="PlayerOne"):
    while True:
        # name = input("What is is your name?: ")
        print(f"Welcome {name} to Hangman!!!\n")
        word, topic = askCategory(name)
        # hangMan(word)
        displayHangman(topic, word)  # TODO: add lives here
        os.system("pause")
        os.system("cls")


def hangMan(word):
    lenWord = len(word)
    for i in word:
        MissingWord.append(i)
    print(f"This is: {MissingWord}")
    print(lenWord)
    # ! Should initialize at the end of the game kasi when not it add and adds
    MissingWord.clear()


def displayHangman(topic, word):
    print("/******************************************************************/")
    lives = 5
    print(f"\t LIVES:{lives}")
    print(f"\t TOPIC:{topic}")
    print("\t Guess the word:")
    for i in range(len(word)):
        print("\t __", end=" ")
    print("\n")

    # print(f"\t GUESS THE WORD:{word}")


def askCategory(name="PlayerOne"):
    print("Categories:\n [1]Animals\n [2]Things\n [3]Places\n")
    category = input(f"{name}, choose a category:")
    checkIfOk = checkFormat(1, category)

    if checkIfOk == 1:
        sys.exit()
    if category == "1":
        # TODO: get db for animals
        print("You choose Animals")
        randWord = random.choice(Animals)
        topic = "Animals"

    elif category == "2":
        # TODO: get db for things and stuff
        print("You choose Things")
        randWord = random.choice(Things)
        topic = "Things"

    else:
        # TODO: get db for places
        print("You choose Places")
        randWord = random.choice(Places)
        topic = "Places"

    return randWord, topic


def checkFormat(format, userInput):
    # * if format is 1 meaning check if number from 1 to 3 is inputted correctly
    if format == 1:
        if userInput == "1" or userInput == "2" or userInput == "3":
            return 0
        else:
            print("Wrong format. Please enter number 1 to 3 only!!!")
            # return 1
            sys.exit()


# def mainGame():

# menu()
