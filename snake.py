import pygame, random

pygame.init()
width = 700
height = 500
screen = pygame.display.set_mode((700, 500))
x = 700 / 2
y = 500 / 2
snake = [(x, y)]
length = 1
snake_size = (30,30)
food_size = (15, 15)
dx = 0
dy = 0
clock = pygame.time.Clock()
running = True

class Food:
    def __init__(self):
        self.size = (15,15)
        self.spawn()
    
    def spawn(self):
        self.x = random.randint(0, (700 - self.size[0]) // self.size[0]) * self.size[0]
        self.y = random.randint(0, (500 - self.size[1]) // self.size[1]) * self.size[1]

    def draw(self, screen):
        pygame.draw.rect(screen, 'red', (self.x, self.y, self.size[0], self.size[1]))


food = Food()
while running:
    
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = +1
                dy = 0
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = 1
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -1
            

    x += dx * snake_size[0]
    y += dy *snake_size[1]

    snake.append((x, y))


    for i, j in snake:
        pygame.draw.rect(screen, 'green', (i, j, snake_size[0] - 1, snake_size[1] - 1))

    pygame.display.update()
    clock.tick(5)

pygame.quit()
