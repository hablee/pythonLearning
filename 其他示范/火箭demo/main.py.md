```python
import sys
import pygame

from settings import Settings
from rocket import Rocket
import game_function as gf

def run_game():
    """初始化并创建一个屏幕对象"""
    pygame.init()
    r_settings = Settings()
    screen = pygame.display.set_mode((r_settings.screen_width,r_settings.screen_height))
    pygame.display.set_caption("rockt demo")

    # 创建一个火箭
    rocket = Rocket(r_settings,screen)

    # 开始游戏主循环
    while True:
        gf.chek_events(rocket)
        rocket.update()
        gf.update_screen(r_settings,screen,rocket)

if __name__ == '__main__':
    run_game()
```
