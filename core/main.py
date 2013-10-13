#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cmd
import argparse
import os
from core.show import show
from core.config import config
host="Router"
class main():
    def init(self):
        os.system('clear && cat motd')

    def prompt(self):
    
        while True:
           userinput = input(host +  ": ")
           spl = userinput
           if spl == "config":
                config(spl) 
           else:
                show(spl)

