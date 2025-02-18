"""
Based on previous classes and examples you will create a ping pong game, with the following characteristics:

Will create 2 platforms *
Will create a ball *
The ball must bounce off the walls and platforms. *
If the ball touches any horizontal side, the opposing side will score a point. *
You must show the scoreboard on the screen.*
When any player scores 5 points, a victory screen will be displayed and the game will close. 
You should be able to pause the game if you press the P key.* 
Add music and hit sounds.* 
"""

import pygame

GRIS = (125, 125, 125)
LILA = (251, 243, 207)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

BLANCO = (255, 255, 255)

pygame.mixer.init()
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

hit_sound = pygame.mixer.Sound("Golpe.mp3")

pygame.init()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("PingPong")

font = pygame.font.Font(None, 36)

is_game_over = False
is_paused = False

left_points = 0
right_points = 0

def show_text(text, x=100, y=200, color=GRIS):
    texto = font.render(text, True, color)
    window.blit(texto, (x, y))

def main():

    global is_game_over, is_paused, right_points, left_points

    ball = pygame.image.load("ball.png")

    platform_left = pygame.image.load("computer.png")
    platform_right = pygame.image.load("player.png")

    speed = [3, 3]

    ballrect = ball.get_rect()
    ballrect.move_ip(320, 450)

    platform_left_rect = platform_left.get_rect()
    platform_left_rect.move_ip(50, 150)

    platform_right_rect = platform_right.get_rect()
    platform_right_rect.move_ip(560, 150)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and is_game_over:
                    ballrect.topleft = (320, 150)
                    is_game_over = False
                    pygame.mixer.music.unpause()
                    pygame.quit()
                if event.key == pygame.K_p:
                    is_paused = not is_paused

        if not is_game_over and not is_paused:

            keys = pygame.key.get_pressed()
            # left
            if keys[pygame.K_w] and platform_left_rect.top > 0:
                platform_left_rect = platform_left_rect.move(0, -5)
            if keys[pygame.K_s] and platform_left_rect.bottom < 480:
                platform_left_rect = platform_left_rect.move(0, 5)
            #Top
            if keys[pygame.K_UP] and platform_right_rect.top > 0:
                platform_right_rect = platform_right_rect.move(0, -5)
            if keys[pygame.K_DOWN] and platform_right_rect.bottom < 480:
                platform_right_rect = platform_right_rect.move(0, 5)


            ballrect = ballrect.move(speed)

            if (ballrect.top < 0 or ballrect.bottom > window.get_height()) :
                speed[1] = -speed[1]

            if (ballrect.left < 0):
                right_points += 1
                ballrect.topleft = (320, 150)
            elif (ballrect.right > window.get_width()):
                left_points += 1                
                ballrect.topleft = (320, 150)                

            if (platform_left_rect.colliderect(ballrect)):
                hit_sound.play()
                speed[0] = -speed[0]
            elif (platform_right_rect.colliderect(ballrect)):
                hit_sound.play()
                speed[0] = -speed[0]

 
            if not is_paused and not is_game_over:
                window.fill((251, 243, 207))
                window.blit(ball, ballrect)
                window.blit(platform_left, platform_left_rect)
                window.blit(platform_right, platform_right_rect)
                show_text(str(left_points), x = 100, y =50)
                show_text(str(right_points), x= 500, y= 50)
            
            if left_points >= 5 :
                is_game_over = True
                pygame.mixer.music.pause()
                show_text("Left Victory...", 100, 200)
                show_text("Presiona espacio para cerrar el juego", y=250) 
            elif right_points >=5:             
                is_game_over = True
                pygame.mixer.music.pause()
                show_text("Right victory...", 100, 200)
                show_text("Presiona Espacio para cerrar el juego", y=250)                  
        elif is_paused:
            show_text("Game Paused")
            show_text("Presiona Escape para regresar", y=240)       
        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()                