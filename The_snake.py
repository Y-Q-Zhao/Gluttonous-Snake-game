'''
author:yiqunzhao
email:13456591503@163.com
'''

import random
import sys
import pygame
import time
from pygame.locals import *

def snake():
    # pygame初始化
    pygame.init()

    # 窗口长宽
    width = 960
    height = 640

    # 颜色定义
    Red = pygame.Color(255, 0, 0)
    Green = pygame.Color(0, 255, 0)
    Blue = pygame.Color(0, 0, 255)
    White = pygame.Color(255, 255, 255)
    Black = pygame.Color(0, 0, 0)

    #时钟
    fpsclock=pygame.time.Clock()

    # 建立窗口
    window = pygame.display.set_mode([width, height])
    pygame.display.set_caption('snake test 2')
    snake_body = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    food = [480, 320]
    direction = 'down'

    while True:
        direction_get = direction

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    direction_get = 'up'
                if event.key == K_DOWN:
                    direction_get = 'down'
                if event.key == K_LEFT:
                    direction_get = 'left'
                if event.key == K_RIGHT:
                    direction_get = 'right'

        if direction_get == 'up' and not direction == 'down':
            direction = direction_get
        if direction_get == 'down' and not direction == 'up':
            direction = direction_get
        if direction_get == 'left' and not direction == 'right':
            direction = direction_get
        if direction_get == 'right' and not direction == 'left':
            direction = direction_get

        if direction == 'up':
            xlabel = snake_body[-1][0]
            ylabel = snake_body[-1][1] - 20
            if ylabel < 0:
                ylabel = ylabel + height
            next_point = [xlabel, ylabel]
        if direction == 'down':
            xlabel = snake_body[-1][0]
            ylabel = snake_body[-1][1] + 20
            if ylabel >= height:
                ylabel = ylabel - height
            next_point = [xlabel, ylabel]
        if direction == 'left':
            xlabel = snake_body[-1][0] - 20
            ylabel = snake_body[-1][1]
            if xlabel < 0:
                xlabel = xlabel + width
            next_point = [xlabel, ylabel]
        if direction == 'right':
            xlabel = snake_body[-1][0] + 20
            ylabel = snake_body[-1][1]
            if xlabel >= width:
                xlabel = xlabel - width
            next_point = [xlabel, ylabel]

        #判断是否吃掉了自己
        if next_point not in snake_body:
            # 判断苹果是否被吃
            if next_point != food:
                snake_body.append(next_point)
                snake_body.pop(0)
            else:
                snake_body.append(next_point)
                x = random.randrange(1, width / 20)
                y = random.randrange(1, height / 20)
                food = [int(x * 20), int(y * 20)]

            window.fill(Black)
            for body in snake_body:
                pygame.draw.rect(window, Red, Rect(body[0], body[1], 20, 20))
            pygame.draw.rect(window, Green, Rect(food[0], food[1], 20, 20))
            pygame.display.flip()
            fpsclock.tick(5)
        else:
            print('game over !')

            font = pygame.font.SysFont('arial', 96)
            text_to_show = font.render('game over !', True, (0, 0, 255), (0, 0, 0))
            text_rect = text_to_show.get_rect()
            text_rect.center = (width / 2, height / 2)
            window.fill(Black)
            window.blit(text_to_show, text_rect)

            pygame.display.flip()
            time.sleep(5)
            pygame.quit()
            sys.exit()
snake()

