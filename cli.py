#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cls.main import main
import os
host = 'Router'
initialization=main()
initialization.init()

if __name__ == '__main__':
    shell=main()
    shell.init()
    shell.prompt()
