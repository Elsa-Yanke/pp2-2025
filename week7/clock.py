import pygame
import datetime


pygame.init()

clock2 = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 600))
done = False

clock = pygame.image.load("clock.png")
clock = pygame.transform.scale(clock, (1200, 600))
leftarm = pygame.image.load("leftarm.png")
rightarm = pygame.image.load("rightarm.png")
leftarm = pygame.transform.scale(leftarm, (40, 600))
rightarm = pygame.transform.scale(rightarm, (1200, 600))

image = pygame.transform.scale(clock, screen.get_size())

angle_left = (600, 300) 
angle_right = (600, 300)



def get_angle():
    now = datetime.datetime.now()
    second_angle = -(now.second*6)
    minute_angle = -(now.minute * 6)  
    return second_angle, minute_angle

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        second_angle, minute_angle = get_angle() 

        rotated_image1 = pygame.transform.rotate(leftarm, minute_angle)
        rotated_image2 = pygame.transform.rotate(rightarm, second_angle)

        r1_w, r1_h = rotated_image1.get_size()
        r2_w, r2_h = rotated_image2.get_size()

        draw_pos1 = (angle_left[0] - r1_w // 2, angle_left[1] - r1_h // 2)
        draw_pos2 = (angle_right[0] - r2_w // 2, angle_right[1] - r2_h // 2)      

        screen.fill((0, 0, 0))  
        screen.blit(image, (0, 0))  
        screen.blit(rotated_image1, draw_pos1)  
        screen.blit(rotated_image2, draw_pos2)  

        pygame.display.flip()  
        clock2.tick(1)  

pygame.quit()


