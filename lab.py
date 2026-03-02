from art import *
from colorama import *

def main():
    print(art("random"))
    phrase1 =text2art("BELIEVE AND ACHEIVE",font='block')
    print(phrase1)
    phrase2="HELLO"
    tprint(phrase2,font="sub-zero",chr_ignore=True)

    phrase3 = "Yin and Yang"
    phrase3 = phrase3.split(" ")
    phrase3 = [text2art(phrase3[0],font="soft",chr_ignore=True), text2art(phrase3[1],font="soft",chr_ignore=True), text2art(phrase3[2],font="soft",chr_ignore=True)]
    print(f"{Back.BLACK + phrase3[0]}{Back.WHITE+phrase3[2]}")
    print(Back.RESET)

if __name__ == "__main__":
    main()