from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.renderers import FigletText

def demo(screen):
    scenes = []
    effects = [
        Print(screen,
            FigletText("Hello World!"),
              screen.height // 2 - 3)
    ]
    scenes.append(Scene(effects, -1))
    screen.play(scenes, stop_on_resize=True, repeat=False)

Screen.wrapper(demo)