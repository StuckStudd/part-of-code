import time
from colorama import Fore, Style
import os 


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()
print(Fore.GREEN + "Welcome this is Artems road map." + Style.RESET_ALL)
time.sleep(2)

class RoadMap:
    def __init__ (self, value):
        self.val = value
        self.next = None
    

roadmap1 = RoadMap("Hard work")
roadmap2 = RoadMap("Learning speak")
roadmap3 = RoadMap("Learnint Matematik")
roadmap4 = RoadMap("High School")
roadmap5gi = RoadMap("Job in google")

roadmap1.next = roadmap2
roadmap2.next = roadmap3
roadmap3.next = roadmap4

current = roadmap1

while current is not None:
    print(f"Road map : {current.val}")
    time.sleep(2)
    clear_console()
    current = current.next