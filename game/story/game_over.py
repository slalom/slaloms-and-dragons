from asciimatics.renderers import FigletText, Fire
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.exceptions import ResizeScreenError
from pyfiglet import Figlet
import sys


def game_over(screen):
    scenes = []

    effects = [
        Print(screen,
              Fire(screen.height, 80, "*" * 70, 0.8, 60, screen.colours,
                   bg=screen.colours >= 256),
              0,
              speed=1,
              transparent=False),
        Print(screen,
              FigletText("\nGame", "banner3"),
              (screen.height - 4) // 2,
              colour=Screen.COLOUR_BLACK,
              speed=1,
              start_frame=30,
              stop_frame=50),
        Print(screen,
              FigletText("\nOver", "banner3"),
              (screen.height - 4) // 2,
              colour=Screen.COLOUR_BLACK,
              speed=1,
              start_frame=50,
              stop_frame=70),
        Print(screen,
              FigletText("BWA\n  HA\n HA\nHA!!!", "banner3"),
              (screen.height - 4) // 2,
              colour=Screen.COLOUR_BLACK,
              speed=1,
              start_frame=70),
        
    ]
    scenes.append(Scene(effects, 100))

    screen.play(scenes, stop_on_resize=True, repeat=False)


def play_game_over():  
    while True:
        try:
            Screen.wrapper(game_over)
            sys.exit(0)
        except ResizeScreenError:
            pass    


# if __name__ == "__main__":
