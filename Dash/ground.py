import pygame

class Ground():

    def  __init__ (self,screen):
        #initialization
        self.screen = screen

        self.ground1 = pygame.image.load("images/ground/ground1.png")
        self.ground2 = pygame.image.load("images/ground/ground2.png")

    def blitme(self,groundX):
        self.screen.blit(self.ground1,(0,600))
        self.screen.blit(self.ground2,(groundX,600))


        
    

