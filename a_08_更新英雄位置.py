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
# screen.blit(hero, (185, 500))

# 可以在所有绘制工作完成之后， 同一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1.定义rect记录飞机的初试位置
hero_rect = pygame.Rect(185, 500, 102, 126)

# 游戏循环 -> 意味着游戏的正式开始
while True:

    clock.tick(120)

    # 捕获事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)

    for event in pygame.event.get():

        # 判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏...")
            pygame.quit()
            # 直接退出游戏系统
            exit()

    # 2. 修改飞机位置
    hero_rect.y -= 1

    # 判断飞机位置
    if hero_rect.y <= -126:
        hero_rect.y = 700

    # 3.调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 4.使用update方法更新显示
    pygame.display.update()

pygame.quit()