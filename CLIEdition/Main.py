import os
from os import _exit as exit
import logging as log
import os.path as p
from time import sleep as sl
def Main():
    wavfile_input = input("Please Write full path with .wav in the end")
    xwmaencode_inp = input("Write you're own name in the end .xwma file")
    if(p.exists(wavfile_input)):
        os.system("xwmaencode {} {}".format(wavfile_input, xwmaencode_inp))
        sl(4)
        if(p.exists(xwmaencode_inp)):
            print("Successfully Converted into {}".format(xwmaencode_inp))
            exit(335)
        exit(332)
    else:
        print("This is Not You're Full path or you're write wrong path!!!")
        exit(445)

if __name__ == "__main__":

    Main()
