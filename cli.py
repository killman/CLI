#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.main import main
import os
initialization=main()
initialization.init()

if __name__ == '__main__':
    shell=main()
    shell.init()
    shell.prompt()
