import pygame

_songs = ['song1.mp3', 'song2.mp3', 'song3.mp3']

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]]  
    pygame.mixer.music.load(_songs[0]) 
    pygame.mixer.music.play()           


def play_previous_song():
    global _songs
    if _songs:
        _songs = [_songs[-1]] + _songs[:-1]
        pygame.mixer.music.load(_songs[0])
        pygame.mixer.music.play()

pygame.init()
screen = pygame.display.set_mode((1200, 600))
done = False
is_playing = False
font = pygame.font.Font(None, 62)
font1 = pygame.font.Font(None, 42)
font2 = pygame.font.Font(None, 42)
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                      play_next_song()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                      if not is_playing:
                            pygame.mixer.music.load(_songs[0])
                            pygame.mixer.music.play()
                            is_playing = True
                      else:
                            if pygame.mixer.music.get_busy():
                                  pygame.mixer.music.pause()
                            else:
                                  pygame.mixer.music.unpause()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                      play_previous_song()

        screen.fill("black")
        text = font.render("Press SPACE to Play or Pause", True, (255, 255, 255)) 
        screen.blit(text, (300, 40))
        text1 = font1.render("Press LEFT Key to play next song", True, (255,255,255))
        screen.blit(text1, (70, 370))
        text2 = font2.render("Press RIGHT Key to play next song", True, (255,255,255))
        screen.blit(text2, (670, 370))
        pygame.display.flip() 