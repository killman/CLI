#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cmd
import argparse
import os
from core.show import show
from core.config import config
host = "Router"
conf = "0"
class main():
    def init(self):
        os.system('clear && cat motd')

    def prompt(self):
        global conf
        global host
        while True:
           userinput = input(host +  ": ")
           spl = userinput
           if spl == "save":
                conf = "0"
                host ="Router"
           if (spl == "config" or conf == "1"):
                config(spl)
                conf = "1"
                host = "Router config"
           else:
                show(spl)

