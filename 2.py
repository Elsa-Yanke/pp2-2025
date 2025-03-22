import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 700))
done = False

# Загружаем изображения
clock = pygame.image.load("clock.png")
clock = pygame.transform.scale(clock, (800, 520))

leftarm = pygame.image.load("leftarm.png")
rightarm = pygame.image.load("rightarm.png")
leftarm = pygame.transform.scale(leftarm, (200, 100))  # Уменьшил размер
rightarm = pygame.transform.scale(rightarm, (200, 100))

# Центр часов
clock_x, clock_y = 200, 90  
clock_center = (clock_x + 400, clock_y + 260)  # Центр = середина изображения

# Координаты крепления рук (примерно от плеч)
leftarm_pos = (clock_center[0] - 20, clock_center[1] - 50)  
rightarm_pos = (clock_center[0] + 20, clock_center[1] - 50)  

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    
    # Отображаем фон часов
    screen.blit(clock, (clock_x, clock_y))

    # Рисуем руки
    screen.blit(leftarm, leftarm_pos)
    screen.blit(rightarm, rightarm_pos)

    pygame.display.flip()
