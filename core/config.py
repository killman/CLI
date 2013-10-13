#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
def config(spl):

    if spl == "config user":
        user = os.getlogin()
        print (user)

