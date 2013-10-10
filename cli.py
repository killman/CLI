#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cls.main import main
import os
host = 'Router'
initialization=main()
initialization.init()

"""while True:
    user_input = raw_input(host +  " #> ")
    splitit = user_input
    
    if splitit == "show user":
        user = os.getlogin()
        print (user)
    
    if splitit == "clear":
        os.system('clear && cat motd') 

    if splitit == 'show hostname':
         os.system('hostname')

    if splitit == 'show os':
         os.system('uname -sr')
    if splitit == 'exit':
         exit()
"""
if __name__ == '__main__':
    shell=main()
    shell.init()
    shell.prompt()
