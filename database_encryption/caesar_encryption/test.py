# 資訊二甲 10627109 陳力維 2019/7/24
# 資訊二乙 10627229 陳寬祐 
import random
import string

def Caesar_Encryption(str, offset) :
    """
    :parameter str : string
    :parameter offset : int
    :return : string
    """
    upper_limit = ord('~')
    lower_limit = ord(' ')
    length = upper_limit - lower_limit                # 超出上限時應縮減的固定長度
    i = 0
    newStr = ""
    newASCii = 0
    while i < len(str) - 1 :
        newASCii = ord(str[i]) + offset                # 未超出上限
        if newASCii > upper_limit:                     # 超出上限時
            newASCii -=  length                        # 縮減固定長度
        # 以上作法僅限於offset <= length
        # 若offset > length, 應該改用%取餘數
        newStr += chr(newASCii)
        i += 1

    print(newStr)
    return newStr

def Caesar_Decryption(str, offset) :
    """
    :parameter str : string
    :parameter offset : int
    :return : string
    """
    upper_limit = ord('~')
    lower_limit = ord(' ')
    length = upper_limit - lower_limit                # 低於下限時應增加的固定長度
    i = 0
    newStr = ""
    newASCii = 0
    while i < len(str) - 1 :
        newASCii = ord(str[i]) - offset                # 未低於下限
        if newASCii < lower_limit:                     # 低於下限時
            newASCii +=  length                        # 增加固定長度
        # 以上作法僅限於offset <= length
        # 若offset > length, 應該改用%取餘數
        newStr += chr(newASCii)
        i += 1

    print(newStr)
    return newStr

def Initialize_Passcode() :
    """

    """
    length = Password_length()
    upper_case = False
    lower_case = False
    digits = False
    symbol = False
    repeat = False

    x = input("If you want to have the uppercased letters, please enter 'y' : ")
    y = input("If you want to have the lowercased letters, please enter 'y' : ")
    z = input("If you want to have the digits, please enter 'y' : ")
    w = input("If you want to have the symbol('_'), please enter 'y' : ")
    m = input("If you want to repeat letters, please enter 'y' : ")
    if x == 'y' or x == 'Y' :
        upper_case = True
    if y == 'y' or y == 'Y' :
        lower_case = True
    if z == 'y' or z == 'Y' :
        digits = True
    if w == 'y' or w == 'Y' :
        symbol = True
    if m == 'y' or m == 'Y' :
        repeat = True

    uppercased_upper_limit = ord('Z')                           #uppercased letter ASCii from 'A' to 'Z'
    uppercased_lower_limit = ord('A')
    lowercased_upper_limit = ord('z')                           #lowercased letter ASCii from 'a' to 'z'
    lowercased_lower_limit = ord('a')
    number_upper_limit = ord('9')                               #number letter ASCii from '0' to '9'
    number_lower_limit = ord('0')
    underline = ord('_')                                        #underline ASCii '_'

    words = []
    if upper_case :
        i = uppercased_lower_limit
        while i <= uppercased_upper_limit :
            words.insert(0, chr(i))
            i += 1
    if lower_case :
        i = lowercased_lower_limit
        while i <= lowercased_upper_limit :
            words.insert(0, chr(i))
            i += 1
    if digits :
        i = number_lower_limit
        while i <= number_upper_limit :
            words.insert(0, chr(i))
            i += 1
    if symbol :
        words.insert(0, chr(underline))

    if repeat :
        i = 0
        while i < length :
            temp += random.sample(words, 1)
            i += 1
        print(temp)
    else :
        print( ''.join(random.sample(words, length)))

def Password_length() :
    """
    :return length
    """
    while True :
        while True :
            length = input("Please enter the length of passcode you want (8~16): ")
            if length.isdigit() :
                break
            else :
                print("!!! Please enter an integer. !!!")
        length = int(length)
        if length >= 8 and length <= 16 :
            return length
        else :
            print("!!! You enter a wrong length of passcode. !!!")

number = 0
while True :
    print("**********Caesar Encryption**********")
    print("* 1. Caesar Encryption              *")
    print("* 2. Caesar Decryption              *")
    print("* 3. Initialize Passcode            *")
    print("*************************************")
    number = input("Please enter a number(1, 2, ... Quit[0]) : ")
    if number == '1' or number == '2' :
        while True :
            filename = input("input a filename : ")
            if filename == "0" :
                break
            file = open(filename + ".txt", "r")
            if file :
                break

        if filename == "0" :
            break
        line = file.readline()
        offset = input("enter a offset : ")
        offset = int(offset)
        if number == '1' :
            encrypt = open("encrypted.txt", "w")
            while line :
                encrypt.write(Caesar_Encryption(line, offset) + '\n')
                line = file.readline()
            encrypt.close()
        else :
            decrypt = open("decrypted.txt", "w")
            while line :
                decrypt.write(Caesar_Decryption(line, offset) + '\n')
                line = file.readline()
            decrypt.close()
        file.close()

    elif number == '3' :
        Initialize_Passcode()

    elif number == '0' :
        break
    else :
        print("A wrong input!")


#print(x, end = "")
