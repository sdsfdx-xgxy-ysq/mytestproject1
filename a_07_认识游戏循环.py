import pygame

# 游戏的初始化
pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1> 加载图像数据
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

# 绘制英雄图像
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (185, 500))

# 可以在所有绘制工作完成之后， 同一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环 -> 意味着游戏的正式开始
i = 0

while True:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    print(i)
    i += 1

    pass

pygame.quit()