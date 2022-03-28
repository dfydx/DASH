import pygame

class Player():

    def __init__(self,screen):
        #initialization
        self.screen = screen

        self.defaultLeft = pygame.image.load("images/player/L1.png")

        self.defaultRight = pygame.image.load("images/player/R1.png")

        self.walkLeft = pygame.image.load("images/player/L1.png") #not finish

        self.walkRight = pygame.image.load("images/player/R1.png") #not finish

        self.jumpLeft = pygame.image.load("images/player/L1.png") #not finish

        self.jumpRight = pygame.image.load("images/player/R1.png") #not finish

        self.isright = True
        self.isjump = False

        #about HP 
        self.HPframe = pygame.image.load("images/player/about HP.png")

    def blitme(self,y,ismove,default_isright,isright,isjump,screen,playerHP):
        #show player
        #turns to right? and jump?(animation)
        if ismove == True:
            if isright == True:
                if isjump == True:
                    self.screen.blit(self.jumpRight,(50,y))
                else:
                    self.screen.blit(self.walkRight,(50,y))
            elif isright == False:
                if isjump == True:
                    self.screen.blit(self.jumpLeft,(50,y))
                else:
                    self.screen.blit(self.walkLeft,(50,y))
            elif isjump == True:
                if self.isright == True:
                    self.screen.blit(self.jumpRight,(50,y))
        else:
            if default_isright == False:
                self.screen.blit(self.defaultLeft,(50,y))
            else:
                self.screen.blit(self.defaultRight,(50,y))
        #show HP
        self.screen.blit(self.HPframe,(320,-20))
        pygame.draw.rect(screen,[255,0,0],[360,24,int(playerHP * 3.8),15],0,border_radius=2)
            
        

        
