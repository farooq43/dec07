import os
import time

# This will Copy the files, Encrypt and Deccrypt the files
def heading():
    print('------------------------------------------------------')
    print("\033[1;31m  __                   _____            _____        \n"
          " / ()  _              () | _    _|_    () |_ o |\  _ \n"
          "|     / \_|/\_|  |       ||/ /\/ |       /| || |/ |/ \n"
          " \___/\_/ |_/  \/|/    (/ |_/ /\/|_/    (/   |/|_/|_/\n"
          "         (|     (|                                   \033[0m")
    print('-------------------------------------------------------\n')
    print('\033[1;31mFORTIFY \033[0mSOLUTIONS')
    print('\033[32m', time.asctime(), '\033[0mversion:1.0\nrelease date:15-Nov-2019')


def create():
    ls1 = open('LogSheet.txt', 'a')
    ls2 = open('test.txt', 'a')

    ls1.write("ls1 write the information\nend line")
    ls2.write("ls2 ............\n2nd..")
    ls1.close()
    ls2.close()


def copytestfile():
    ls1 = open('LogSheet.txt', 'r')
    ls2 = open('test.txt', 'a')
    ls2.write('\n')
    for i in ls1:
        for j in i:
            print(j, end="")
            ls2.write(j)
    print('\n')
    ls1.close()
    ls2.close()


def encrypttext(x, y):
    ls1 = open(x, 'r')
    ls2 = open(y, 'a')
    ls2.write('\n')
    for p in ls1:
        ls2.write('\n')
        for k in p:
            q = chr(ord(k) - 7)
            ls2.write(q)
            # print(q, end="")
    ls1.close()
    ls2.close()


def Decrypttext(x, y):
    ls1 = open(x, 'r')
    ls2 = open(y, 'a')
    ls2.write('\n')
    for p in ls1:
        ls2.write('\n')
        for k in p:
            q = chr(ord(k) + 7)
            ls2.write(q)
            # print(q, end="")
    ls1.close()
    ls2.close()

def directorylocation():
    while True:
        print(os.path.realpath(__file__))
        x2 = input('Enter Directory :')
        print(os.listdir(x2))
        x22 = input('Enter 1 to continue or enter any key to search in other directory')
        if x22 == 1:
            x1 = input('Enter file name :').strip()
            x3 = os.path.join(x2, x1)
            break
    return x3


def copytestfile1(y, y1):
    ls1 = open(y, 'r')
    ls2 = open(y1, 'a')
    ls2.write('\n')
    for i in ls1:
        for j in i:
            # print(j, end="")
            ls2.write(j)
    print('\n')
    ls1.close()
    ls2.close()


def body():    #Start from here:
    print('\033[34mSelect 1st file, which you want to copied in Second File\n')
    print('----------------------------------------------------------------')
    count = 0
    while True:
        print('Path: ',os.path.realpath(__file__))
        try:
            dpath1 = input('\033[31mEnter Directory :')
        except NotADirectoryError:
            print('Enter Correct path')
        print('\033[0m-----------------------------------')
        x = os.listdir(dpath1)
        for i in x:
            count += 1
            print(f"{count} > {i}")
        print('----------------------------------------------------------------\n')
        x22 = input('\033[31mEnter [1] to continue or Search file in other directory enter any other key :')
        count = 0
        if x22 == '1':
            p1 = int(input('Enter File Number: '))
            print(f'{x[p1-1]}')
            filename1 = x[p1-1]
            filepath1 = os.path.join(dpath1, filename1)
            break
    print(f"\n\033[34mSelect 2nd file in which you want to copy the \'{filename1}\' file")
    print('----------------------------------------------------------------')
    count = 0
    while True:
        print(os.path.realpath(__file__))
        dpath2 = input('\033[31mEnter Directory :')
        x1 = os.listdir(dpath2)
        for i in x1:
            count += 1
            print(f"{count} > {i}")
        print('----------------------------------------------------------------')
        x122 = input('Enter [1] to continue or Search file in other directory enter any other key :')
        count = 0
        if x122 == '1':
            p2 = int(input('Enter file Number :'))
            filename2 = x1[p2-1]
            filepath2 = os.path.join(dpath2, filename2)
            break
    return filepath1, filepath2, filename1, filename2


def body2(filepath1, filepath2, filename1,filename2):
    if os.path.isfile(filepath1):
        print(f'\033[0m[1] To Copy\033[31m {filename1}\033[0m to \033[31m{filename2}\033[0m \n[2] To Encrypt & Copy\033[31m {filename1}\033[0m to \033[31m{filename2}\033[0m\n[3] To Decrypt & Copy\033[31m {filename1}\033[0m to \033[31m{filename2}\033[0m')
        option = int(input())
        if option == 1:
            copytestfile1(filename1,filename2)
                #copytestfile1(filepath1, filepath2) # You called files
        elif option == 2:
            encrypttext(filename1,filename2)
        elif option ==3:
            Decrypttext(filename1,filename2)
        time.sleep(3)
        print(f"\033[34mFile:'{filename1}' is copied in File:'{filename2}'")
        print(f"\033[0m{filename2} path is {filepath2}")
            # encrypttext(filepath1,filepath2)
    else:
        time.sleep(2)
        print('\nPlease select correct file')


def main():
    heading()
    x, y, f1, f2 = body()
    body2(x,y,f1,f2)
    time.sleep(4)
    print('\n-------------------------------------------------------------------------')
    print('\033[31mFORTIFY\033[0m SOLUTIONS, Thanks to all members for its support and contributions')

main()