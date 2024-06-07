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
#  Guess the word: _ く え
#           ----------------------
#           *                    *
#           *                    *
#           *                ---------
#           *                \ ＞﹏＜ |
#           *                ---------
#           *                    |
#           *             ------ \------
#           *                    |
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

import sys


def menu(name="PlayerOne"):
    while True:
        name = input("What is is your name?: ")
        print(f"Welcome {name} to Hangman!!!\n")
        askCategory(name)


def askCategory(name="PlayerOne"):
    print("Categories:\n [1]Animals\n [2]Things\n [3]Places\n")
    category = input(f"{name}, choose a category:")
    checkIfOk = checkFormat(1, category)
    if checkIfOk == 1:
        sys.exit()
    if category == "1":
        # get db for animals
        print("You choose Animals")
    elif category == "2":
        # get db for things
        print("You choose Things")
    else:
        # get db for places
        print("You choose Places")


def checkFormat(format, userInput):
    # if format is 1 meaning check if number from 1 to 3 is inputted correctly
    if format == 1:
        if int(userInput) == 1 or int(userInput) == 2 or int(userInput) == 3:
            return 0
        else:
            print("Wrong format. Please enter number only!!!")
            return 1


# def mainGame():

menu()
