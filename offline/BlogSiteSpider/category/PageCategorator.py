#!/usr/bin/python2.7
#coding=utf-8

#category range: low 8bits category level 3, middle 8bits level 2, high 8bits level 1
#000000001111111100000000
LEVEL1_MASK = 0xff0000
LEVEL2_MASK = 0x00ff00
LEVEL3_MASK = 0x0000ff

class PageCategorator:
    def __init__(self):
        pass
    def analyze(self, paper):
        tags = []
        pass
