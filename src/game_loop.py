import pygame
import time

class GameLoop:
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Game Window")

        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((30, 30, 60))  # 深蓝背景
            pygame.draw.circle(screen, (255, 0, 0), (320, 240), 50)  # 中间画个圆

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
