import copy
import time
import sys
import termios
import tty
import signal

from input import input_to
from colorama import Fore, Back, Style
from constants import ROW,COL,TP
from layout import layout
from buildings import hut, town_Hall
from attackers import king

class Game:
    def __init__(self):
        self.board = []
        self.map = []
        self.layout = layout(self)
        self.time_Running = 0
        self.king_Count = 0

    def start(self):
        for obj in self.layout.existing_Building:
            obj.show()

    def show(self):
        for row in self.board:
            for c in row:
                print(c, end='')

    def run(self):
        self.time_Start = time.time()
        while True:
            ch = input_to()
            self.time_Running = float(time.time() - self.time_Start)
            self.show()
            self.king_Count == 0
            
            if(ch == 'j'):
                if(self.king_Count == 0):
                    self.layout.attackers.append(king(self,0,12))
                    self.king_Count = 1
            elif(ch == 'k'):
                if(self.king_Count == 0):
                    self.layout.attackers.append(king(self,13,0))
                    self.king_Count = 1
            elif(ch == 'l'):
                if(self.king_Count == 0):
                    self.layout.attackers.append(king(self,29,12))
                    self.king_Count = 1
       
            if(ch == 'a'):
                if(self.king_Count == 1):
                    self.layout.attackers[0].left_move()
            elif(ch == 'd'):
                if(self.king_Count == 1):
                    self.layout.attackers[0].right_move()
            elif(ch == 'w'):
                if(self.king_Count == 1):
                    self.layout.attackers[0].up_move()
            elif(ch == 's'):
                if(self.king_Count == 1):
                    self.layout.attackers[0].down_move()
            elif(ch == ' '):
                if(self.king_Count == 1):
                    self.layout.attackers[0].attack()
            print("\033[H\033[J", end="")
            self.show()
            time.sleep(TP)
            

            