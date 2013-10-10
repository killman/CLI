#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cmd
import argparse
import os
host="Router"
class main():
    def init(self):
        os.system('clear && cat motd')

    def prompt(self):
    
        while True:
           userinput = input(host +  " #> ")
           spl = userinput
    
           if spl == "show user":
               user = os.getlogin()
               print (user)
    
           if spl == "clear":
               os.system('clear && cat motd') 

           if spl == 'show hostname':
               os.system('hostname')

           if spl == 'show os':
               os.system('uname -sr')
 
           if spl == 'exit':
                exit()
           if spl == 'show time':
                os.system('date')

           if spl == 'show arch':	
                os.system('uname -p')

           if spl == 'show system':
                 os.system('sysctl hw')
           
           if spl == 'show memory':
                 os.system('sysctl hw | grep mem')
	   
           if spl == 'show disk':
                 os.system('df -h')
          
           if spl == 'show routing':
                 os.system('netstat -nr')

           if spl == 'show connection':
                 os.system('netstat -nt')
	
           if spl == 'show gateway':
                 os.system('cat /etc/mygate')
           
           if spl == 'show ip public':
                 os.system('curl ifconfig.me')

           if spl == 'show run':
                 os.system('pfctl -sr')
