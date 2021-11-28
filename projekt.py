import pygame

pygame.init()
aken = pygame.display.set_mode([640, 480])

mäng_töötab = True

lind = pygame.image.load("tom.png")
linnu_x = 0
linnu_y = 0

while mäng_töötab:
    hiire_x, hiire_y = pygame.mouse.get_pos()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            mäng_töötab = False

    linnu_x = hiire_x
    linnu_y = hiire_y

    aken.fill([255, 255, 0])
    aken.blit(lind, [linnu_x, linnu_y])
    pygame.display.flip()

pygame.quit()