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
Hiragana = [
    "あ",
    "か",
    "さ",
    "た",
    "な",
    "は",
    "ま",
    "や",
    "ら",
    "わ",
    "ん",
    "が",
    "ざ",
    "だ",
    "ば",
    "ぱ",
    "い",
    "き",
    "し",
    "ち",
    "ひ",
    "み",
    "り",
    "ぎ",
    "じ",
    "dzi",
    "び",
    "ぴ",
    "え",
    "け",
    "せ",
    "て",
    "ね",
    "へ",
    "め",
    "れ",
    "げ",
    "ぜ",
    "で",
    "べ",
    "ぺ",
    "お",
    "こ",
    "そ",
    "と",
    "の",
    "ほ",
    "も",
    "よ",
    "ろ",
    "を",
    "ご",
    "ぞ",
    "ど",
    "ぼ",
    "ぽ",
]
MissingWord = []


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


def drawHead(status="a"):
    headPart = ["---------", "| ＞﹏＜ |", "---------"]
    if status == "d":
        # remove head
        headPart = []

    for i in headPart:
        print(f"\t {i}")


def drawingHangman(choice, status):
    bodyPart = ["|", "*", "*", "*", "*"]

    # pole
    print("--------------")
    print("\t     |\n\t     |\n\t     |")
    # *THIS COULD BE IMPROVED USE LOOP instead of brute force
    if choice == "remove":
        if status == 5:  # left leg
            bodyPart[3] = " "
        elif status == 4:  # right leg
            bodyPart[3] = " "
            bodyPart[4] = " "
        elif status == 3:  # left arm
            bodyPart[3] = " "
            bodyPart[4] = " "
            bodyPart[1] = " "
        elif status == 2:  # right arm
            bodyPart[3] = " "
            bodyPart[4] = " "
            bodyPart[1] = " "
            bodyPart[2] = " "
        elif status == 1:  # body
            bodyPart[3] = " "
            bodyPart[4] = " "
            bodyPart[1] = " "
            bodyPart[2] = " "
            bodyPart[0] = " "
        elif status == 0:
            bodyPart[3] = " "
            bodyPart[4] = " "
            bodyPart[1] = " "
            bodyPart[2] = " "
            bodyPart[0] = " "

    # upper body
    n = 2
    m = 0
    a = 0
    if status == 0:
        drawHead("d")
    else:
        drawHead()

    while a < 3:
        print(f"\t  {" " * n}{bodyPart[1]}{" "*m}{bodyPart[0]}{" " * m}{bodyPart[2]}")
        n = n - 1
        m = m + 1
        a = a + 1
    # lower body
    a = 0
    while a < 3:
        print(f"\t     {bodyPart[0]}")
        a = a + 1
    # legs
    a = 0
    m = 1
    n = 2
    while a < 3:
        print(f"\t  {" " * n }{bodyPart[3]}{" "*m}{bodyPart[4]}")
        n = n - 1
        m = m + 2
        a = a + 1
    print("\n\n----------------------")


def displayLives(lives):
    print("LIVES:", end=" ")
    if lives == 0:
        print("No More Lives 💀")
    print(lives * "💜")


def displayGame(topic, word, MissingWord):
    print(f"TOPIC:{topic}")
    print(f"Guess the word (Number of letter:{len(word)}):", end=" ")
    if not MissingWord:
        for i in range(len(word)):
            print("__", end=" ")
        print("\n")
    else:
        for i in range(len(word)):
            if not MissingWord:
                print("_", end=" ")
            else:
                print(i)

        print("\n")


def hangman(word, topic):
    lenWord = len(word)
    cntLetter = 0
    cntWrong = 6
    cntCorrect = 0

    while True:
        displayGame(topic, word, MissingWord)
        # print(f"This is: {MissingWord}")
        if cntLetter == lenWord:
            break
        if cntWrong <= 0:
            print("You exceeded 6 lives")
            displayLives(0)
            drawingHangman("remove", 0)
            os.system("pause")
            MissingWord.clear()
            break

        if cntWrong < 6:
            displayLives(cntWrong)
            drawingHangman("remove", cntWrong)
        else:
            displayLives(cntWrong)
            drawingHangman("add", "none")

        for i in Hiragana:
            print(i, end="  ")

        cmpLetter = input("\n\nEnter letter:")

        for index, element in enumerate(word):
            if cmpLetter == element:
                print("Found correct letter")
                MissingWord.insert(index, element)
                cntLetter += 1
                cntCorrect += 1

        if cntCorrect > 0:
            cntCorrect = 0
        else:
            cntWrong -= 1

        for index, element in enumerate(Hiragana):
            if element == cmpLetter:
                Hiragana[index] = "x"
                break


def menu(name="PlayerOne"):
    while True:
        # name = input("What is is your name?: ")
        print(f"Welcome {name} to Hangman!!!\n")
        word, topic = askCategory(name)
        hangman(word, topic)
        # os.system("pause")
        # os.system("cls")


if __name__ == "__main__":
    menu()
