import os

MissingWord = ["a", "p", "p", "l", "e"]
cntLetter = 0
cntCorrect = 0
cntWrong = 6
while cntLetter < len(MissingWord):
    print(f"You have {cntWrong} lives !!!!!")
    cmp = input("enter:")

    for index, element in enumerate(MissingWord):
        if cmp == element:
            print("correct found letter")
            # MissingWord.pop(index)
            MissingWord[index] = " "
            cntCorrect += 1
        print(element)

    # for index, element in enumerate(MissingWord):
    #     if cmp
    # print("this is it")
    # for i in MissingWord:
    #     print(i)
    print(f"Found {cntCorrect} letter!!!!")
    if cntCorrect > 0:
        cntCorrect = 0
    else:
        cntWrong -= 1
        print(f"Oh no 😭 you have now {cntWrong}")

    cntLetter += 1
