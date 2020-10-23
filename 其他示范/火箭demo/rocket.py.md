```python
import pygame

class Rocket():
    def __init__(self,r_settings,screen):
        self.r_settings = r_settings
        self.screen = screen

        # 加载火箭图像并获取其外接矩形
        self.image = pygame.image.load('image/rocket2.png')
        # main = pygame.transform.scale(self.image, (1, 1))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将火箭放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # 在火箭的属性center中存储小数值
        self.xloc = float(self.rect.centerx)
        self.yloc = float(self.rect.centery)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整火箭位置"""
        if self.moving_left and self.rect.left>0:
            self.xloc -= self.r_settings.rocket_speed_factor
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.xloc += self.r_settings.rocket_speed_factor
        if self.moving_up and self.rect.top>self.screen_rect.top:
            self.yloc -= self.r_settings.rocket_speed_factor
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.yloc += self.r_settings.rocket_speed_factor

        # 根据self.xloc，self.yloc更新rect对象
        self.rect.centerx = self.xloc
        self.rect.centery = self.yloc

    def blitme(self):
        """指定位置绘制火箭"""
        self.screen.blit(self.image,self.rect)
```
