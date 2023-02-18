import pygame
import sys

pygame.init()
class Button():
	def __init__(self, surface=None, pos=None, width=None, height=None, text_input=None, font=None, base_color=None, hovering_color=None):
		self.surface = surface
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.width = width
		self.height = height
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.surface is None:
			self.surface = self.text
		else:
			self.surface = pygame.transform.smoothscale(self.surface, (width, height))
		self.rect = self.surface.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.surface is not None:
			screen.blit(self.surface, self.rect)
		screen.blit(self.text, self.text_rect)

	def check_for_input(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def change_color(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

def timeinput():
        global newtime
        print('''Enter the Time''')
        m = int(input("Enter the time in minutes: "))
        s = int(input("Enter the time in seconds: "))
        newtime=m*60+s        

curtime = 0
pygame.time.set_timer(pygame.USEREVENT, 1000)
started = False
w=900
h=600
scr = pygame.display.set_mode((w, h))
pygame.display.set_caption("Timer")

CLOCK = pygame.time.Clock()

BACKDROP = pygame.image.load("assets/backdrop.png")
WHITE_BUTTON = pygame.image.load("assets/button.png")

FONT = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 120)
timer_text = FONT.render("25:00", True, "white")
timer_text_rect = timer_text.get_rect(center=(w/2, h/2-25))

START_BUTTON = Button(WHITE_BUTTON, (150, 400), 170, 60, "START", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#c97676", "#9ab034")
STOP_BUTTON = Button(WHITE_BUTTON, (350, 400), 170, 60, "STOP", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#c97676", "#9ab034")
RESUME_BUTTON = Button(WHITE_BUTTON, (550, h/2+100), 170, 60, "PAUSE", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#c97676", "#9ab034")
RESET_BUTTON = Button(WHITE_BUTTON, (750, h/2+100), 170, 60, "RESET", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#c97676", "#9ab034")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if START_BUTTON.check_for_input(pygame.mouse.get_pos()):
                timeinput()
                curtime=newtime
                started = True
            if STOP_BUTTON.check_for_input(pygame.mouse.get_pos()):
                curtime=0
                started = False
            if RESUME_BUTTON.check_for_input(pygame.mouse.get_pos()):
                if started:
                    started = False
                else:
                    started = True
            if RESET_BUTTON.check_for_input(pygame.mouse.get_pos()):
                curtime=newtime
                started = False
            

            if started:
                RESUME_BUTTON.text_input = "PAUSE"
                RESUME_BUTTON.text = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20).render(
                                        START_BUTTON.text_input, True, START_BUTTON.base_color)
            else:
                RESUME_BUTTON.text_input = "RESUME"
                RESUME_BUTTON.text = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20).render(
                                        START_BUTTON.text_input, True, START_BUTTON.base_color)
        if event.type == pygame.USEREVENT and started:
            curtime -= 1

    scr.fill("#ba4949")
    scr.blit(BACKDROP, BACKDROP.get_rect(center=(w/2, h/2)))

    START_BUTTON.update(scr)
    START_BUTTON.change_color(pygame.mouse.get_pos())
    STOP_BUTTON.update(scr)
    STOP_BUTTON.change_color(pygame.mouse.get_pos())
    RESUME_BUTTON.update(scr)
    RESUME_BUTTON.change_color(pygame.mouse.get_pos())
    RESET_BUTTON.update(scr)
    RESET_BUTTON.change_color(pygame.mouse.get_pos())

    if curtime >= 0:
        display_seconds = curtime % 60
        display_minutes = int(curtime / 60) % 60
    timer_text = FONT.render(f"{display_minutes:02}:{display_seconds:02}", True, "white")
    scr.blit(timer_text, timer_text_rect)

    pygame.display.update()

print(newtime)
