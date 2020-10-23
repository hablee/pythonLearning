```python
class Settings():
    """存储火箭的所有设置的类"""
    def __init__(self):
        """初始化设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,255)

        # 移动速度设置
        self.rocket_speed_factor = 1.5
```
