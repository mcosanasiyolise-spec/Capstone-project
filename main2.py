import random
import pygame


class Button():
    def _init_(self, x, y, pos, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = pos

        def clicked(self, pos):
            self.pos = pygame.mouse.get_pos()
            if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
                if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                    return True
                return False
            

            class RpsGame():
                def __init__(self):
                    pygame.init()

                    self.screen = pygame.display.set_mode((960, 640))
                    pygame.display.set_caption("RPS Smasher")

                    self.bg = pygame.image.load("background.jpg")
                    self.r_btn = pygame.image.load("rock button.jpg").convert_alpha()
                    self.r_btn = pygame.image.load("paper button.jpg").convert_alpha()
                    self.r_btn = pygame.image.load("scissors button.jpg").convert_alpha()

                    self.r_btn = pygame.image.load("rock.jpg").convert_alpha()
                    self.r_btn = pygame.image.load("paper.jpg").convert_alpha()
                    self.r_btn = pygame.image.load("scissors button.jpg").convert_alpha()

                    self.screen.blit(self.bg, (0,0))
                    self.screen.blit(self.rock button, (20, 500))
                    self.screen.blit(self.paper button, (330, 500))
                    self.screen.blit(self.scissors button, (640, 500))

                    self.rock_btn + Button(30, 520, (30, 520), 300, 140)
                    self.paper_btn = Button(340, 520, (340, 520), 300, 140)
                    self.scissors_btn = Button(640, 520, (640, 520), 300, 140)

                    self.font = pygamefont.Font(('Splatch.ttf'), 90)
                    self.text = self.font.render(f" ", True, (255, 255, 255))

                    self.pl_score = 0
                    self.pl_score = 0
                    .def player(self):
                    if self.rock_btn.clicked(30):
                        self.p_option = "rock"
                        self.screen.blit(self.choose_rock,)