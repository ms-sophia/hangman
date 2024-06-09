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


def drawHead(status):
    headPart = ["---------", "| ＞﹏＜ |", "---------"]
    if status == "d":
        # remove head
        headPart.clear
    else:
        for i in headPart:
            print(f"\t {i}")


def drawBodyParts(status):
    # index 0 : body
    # index 1 : left arm
    # index 2 : right arm
    # index 3 : left leg
    # index 4 : right leg

    bodyPart = ["|", "*", "*", "*", "*"]

    n = 2
    m = 0
    a = 0
    if status == 1:  # left leg
        drawHead("a")
        bodyPart.insert(3, " ")
    elif status == 2:  # right leg
        drawHead("a")
        bodyPart.insert(3, " ")
        bodyPart.insert(4, " ")
    elif status == 3:  # left arm
        drawHead("a")
        bodyPart.insert(3, " ")
        bodyPart.insert(4, " ")
        bodyPart.insert(1, " ")
    elif status == 4:  # right arm
        drawHead("a")
        bodyPart.insert(3, " ")
        bodyPart.insert(4, " ")
        bodyPart.insert(1, " ")
        bodyPart.insert(2, " ")
    elif status == 5:  # body
        drawHead("a")
        bodyPart.insert(3, " ")
        bodyPart.insert(4, " ")
        bodyPart.insert(1, " ")
        bodyPart.insert(2, " ")
        bodyPart.insert(0, " ")

    # upper body
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


def drawingHangman(choice, part):
    # pole
    print("--------------")
    print("\t     |\n\t     |\n\t     |")

    if choice == "remove":
        if part == 1:
            drawBodyParts(1)  # remove left leg
        elif part == 2:
            drawBodyParts(2)  # remove right leg
        elif part == 3:
            drawBodyParts(3)  # remove left arm
        elif part == 4:
            drawBodyParts(4)  # remove right arm
        elif part == 5:
            drawBodyParts(5)  # remove body
        elif part == 6:
            drawHead("d")
    else:
        # show all
        drawHead(0)
        drawBodyParts(0)

    print("\n\n----------------------")

    # /\must save the last current status of hangman


def displayLives(lives):
    print("LIVES:", end=" ")
    if lives == 5:
        print("💜💜💜💜💜")
    elif lives == 4:
        print("💜💜💜💜")
    elif lives == 3:
        print("💜💜💜")
    elif lives == 2:
        print("💜💜💜")
    elif lives == 1:
        print("💜")
    else:
        print("No More Lives 💀")


def displayHangman(topic, word):
    print("/******************************************************************/")
    displayLives(5)
    print(f"TOPIC:{topic}")
    print(f"Guess the word (Number of letter:{len(word)}):", end=" ")
    for i in range(len(word)):
        print("__", end=" ")
    print("\n")
    drawingHangman("remove", 2)


def hangMan(word):
    lenWord = len(word)
    for i in word:
        MissingWord.append(i)
    print(f"This is: {MissingWord}")
    print(lenWord)
    # ! Should initialize at the end of the game kasi when not it add and adds
    MissingWord.clear()


def menu(name="PlayerOne"):
    while True:
        # name = input("What is is your name?: ")
        print(f"Welcome {name} to Hangman!!!\n")
        word, topic = askCategory(name)
        hangMan(word)
        displayHangman(topic, word)  # TODO: add lives here
        os.system("pause")
        os.system("cls")


menu()
# drawingHangman()
