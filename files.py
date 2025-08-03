#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 10:36:02 2024

@author: francescolucarelli
"""

lorem = "./lorem.txt"

def leggi(filepath):
    with open(filepath, encoding="utf8", mode="r") as FIN:
        # testo = FIN.readlines()
        counter = 0
        # for counter, line in enumerate(FIN, start=1):
        #     print(f"{counter}: {line}")
        # metodo 2
        for lines in FIN:
            counter+=1
            print(f"{counter}: {lines.strip()}")

leggi(lorem)