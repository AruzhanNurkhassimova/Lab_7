import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Music")
done = True

_songs = ['mecano.mp3', 'Russian cover _ Poems of a Machine _ Mili.mp3', 'Downfall 2016 OST - Revelations.mp3']
flag = 0
pygame.mixer.music.load(_songs[flag])
pygame.mixer.music.play(-1)

font = pygame.font.SysFont("comicsansms", 30)
text1 = font.render("key up - unpause, key down - pause", True, (0, 128, 0))
text2 = font.render("key left - next song, key right - previous song", True, (0, 128, 0))

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: pygame.mixer.music.unpause()
        if pressed[pygame.K_DOWN]: pygame.mixer.music.pause()
        if pressed[pygame.K_RIGHT]:
            if flag == len(_songs) - 1:
                flag = 0
            else:
                flag += 1
            pygame.mixer.music.load(_songs[flag])
            pygame.mixer.music.play(-1)
        if pressed[pygame.K_LEFT]:
            if flag == 0:
                flag = len(_songs) - 1
            else:
                flag -= 1
            pygame.mixer.music.load(_songs[flag])
            pygame.mixer.music.play(-1)

    screen.fill((255, 255, 255))

    screen.blit(text1, (320 - text1.get_width() // 2, 200 - text1.get_height() // 2))
    screen.blit(text2, (320 - text2.get_width() // 2, 240 - text2.get_height() // 2))

    pygame.display.flip()
