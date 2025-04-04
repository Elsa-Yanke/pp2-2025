import pygame, pygame.gfxdraw

pygame.init()
screen = pygame.display.set_mode((700, 700))
screen.fill('white')
last_pos = (0, 0)
radius = 5 

color = ('black') #автоматически черный цвет, далее рисуем блоки с цветами(палитру)
pygame.draw.rect(screen, 'red', (0, 20, 30, 30))
pygame.draw.rect(screen, 'pink', (30, 20, 30, 30))
pygame.draw.rect(screen, 'yellow', (0, 50, 30, 30))
pygame.draw.rect(screen, 'green', (30, 50, 30, 30))
pygame.draw.rect(screen, 'blue', (0, 80, 30, 30))
pygame.draw.rect(screen, 'black', (30, 80, 30, 30))
eraser = pygame.image.load('eraser.png')
screen.blit(eraser, [0, 110])
running = True
drawing = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN: #когда мышка находится на координатах определенного цвета и юзер нажимает на него, то значение цвета меняется
            mousepos = pygame.mouse.get_pos()
            if mousepos[0] < 30 and 20 < mousepos[1] < 50:
                color = 'red'
            if 30 < mousepos[0] < 60 and 20 < mousepos[1] < 50:
                color = 'pink'
            if mousepos[0] < 30 and 50 < mousepos[1] < 80:
                color = 'yellow'
            if 30 < mousepos[0] < 50 and 50 < mousepos[1] < 80:
                color = 'green'
            if mousepos[0] < 30 and 80 < mousepos[1] < 120:
                color = 'blue'
            if 30 < mousepos[0] < 50 and 80 < mousepos[1] < 120:
                color = 'black'
            if mousepos[0] < 60 and 120 < mousepos[1] < 180:
                color = 'white'

        if event.type == pygame.MOUSEBUTTONDOWN:  #ивент для рисования свободной линией
            drawing = True
            last_pos = pygame.mouse.get_pos() #запоминаем позицию где была мышка в последний раз 

        if event.type == pygame.MOUSEBUTTONUP:  #если отпустили мышку, значит юзер не рисует
            drawing = False
            last_pos = None 

        if event.type == pygame.MOUSEMOTION and drawing: #если мышка двигается и drawing == true значит юзер рисует
            mousepos = pygame.mouse.get_pos()
            if last_pos:  
                pygame.draw.line(screen, color, last_pos, mousepos, radius* 2) #если ласт поз тру и она есть( а она есть всегда при условии drawing = true) то рисуем линию
            last_pos = mousepos

        if event.type == pygame.KEYDOWN: #если кнопка зажата
            mousepos = pygame.mouse.get_pos() #получаем заново позицию мышки, чтобы задавать значение для начала фигуры( с левого угла)
            if mousepos:
                if event.key == pygame.K_s:
                    pygame.draw.rect(screen, color, (mousepos[0], mousepos[1], 100, 100)) #drawing square
                elif event.key == pygame.K_t: #drawing right triangle
                   pygame.draw.polygon(screen, color, [(mousepos[0], mousepos[1]), (mousepos[0] - 60, mousepos[1] + 100), (mousepos[0] + 60, mousepos[1] + 100)])
                elif event.key == pygame.K_r: #drawing rectangle
                    rect_size = 100
                    pygame.draw.rect(screen, color, (mousepos[0], mousepos[1], rect_size, rect_size + 100))
                elif event.key == pygame.K_c: #drawing circle
                    circle_radius = 50
                    pygame.draw.circle(screen, color, (mousepos[0], mousepos[1]), circle_radius)
                elif event.key == pygame.K_j: #drawing rectangle with 2 same sides and one the biggest (isosceles)
                   pygame.draw.polygon(screen, color, [(mousepos[0], mousepos[1]), (mousepos[0] - 120, mousepos[1] + 100), (mousepos[0] + 120, mousepos[1] + 100)])
                elif event.key == pygame.K_d: #drawing rhombus
                    pygame.draw.polygon(screen, color, [
                    (mousepos[0], mousepos[1] - 100 // 2),  # up
                    (mousepos[0] + 50 // 2, mousepos[1]),  # right
                    (mousepos[0], mousepos[1] + 100 // 2),  # down
                    (mousepos[0] - 50 // 2, mousepos[1])   # left
                ])
    pygame.display.update()


pygame.quit()