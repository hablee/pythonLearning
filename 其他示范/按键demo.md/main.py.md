```python
import sys
import pygame
from settings import Settings
import program_functions

def run_program():
    # 初始化并创建一个屏幕对象
    pygame.init()
    program_settings = Settings()
    screen = pygame.display.set_mode((program_settings.screen_width,program_settings.screen_height))

    pygame.display.set_caption("一个程序")

    # 展示屏幕
    screen.fill(program_settings.bg_color)
    pygame.display.flip()

    # 监控鼠标键盘事件
    program_functions.check_events()

if __name__ == '__main__':
    while True:
        run_program()
```
