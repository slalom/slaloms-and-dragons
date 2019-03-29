import emoji
import sys
import time
import pyfiglet
from colorama import Fore, Back, Style

def show_intro():
  color = Fore.MAGENTA
  font_bold = Style.BRIGHT
  result = pyfiglet.figlet_format("S L A L O M S  &  D R A G O N S", font="mini")
  print(color + font_bold + result)

  animation = emoji.emojize(color + font_bold +
                            "Let's play SLALOMS & DRAGONS :dragon:")

  for i in animation:
      time.sleep(0.1)
      sys.stdout.write(i)
      sys.stdout.flush()
  print("\n")
  print(Style.RESET_ALL)