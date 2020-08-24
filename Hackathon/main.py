import pygame
pygame.init()




screenWidth = 1280
screenHeight = 720
run = True


#Initialize colors here
white = (255, 255, 255)
black = (0, 0, 0)

#Initialize fonts here
titleFont = pygame.font.SysFont("Calibri", 50, bold=True)


#Initialize texts here
titleText = titleFont.render("Education in the 21st Century", True, black)


#Initialize images here
pg1background = pygame.image.load(r"images\pg1background.png")
pg1text = pygame.image.load(r"images\pg1text.png")
nextbutton = pygame.image.load(r"images\nextbutton.png")
nextbutton_highlighted = pygame.image.load(r"images\nextbutton_highlighted.png")
pg2text = pygame.image.load(r"images\pg2text.png")
pg3text = pygame.image.load(r"images\pg3text.png")
graph = pygame.image.load(r"images\graph.png")
plus_symbol = pygame.image.load(r"images\plus_symbol.png")
subtract_symbol = pygame.image.load(r"images\subtract_symbol.png")



# Here are the variables




#Initialize functions here
win = pygame.display.set_mode( (screenWidth, screenHeight) )
state = "page1"

def click_button(pos_x, pos_y, width, height, original_button, highlighted_button): #key = state to change to 
    global mouse
    global state
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #Checking if the mouse is within the boundaries of the box
    if pos_x + width > mouse[0] > pos_x and pos_y + height > mouse[1] > pos_y :
        win.blit(highlighted_button, (pos_x, pos_y))
        #check is button is clicked
        if click[0] == 1:
            #state = key
            return True
    else:
        win.blit(original_button, (pos_x, pos_y))
        return False




count = 0
#Main loop
while run:
    count += 1000000
    pygame.time.delay(60) #Set a framerate
    if state == "page1":
        win.blit(pg1background, (0, 0))
        win.blit(titleText, (72, 50))
        win.blit(pg1text, (0, 0))
        if count > 10000000:
            click_button(1160, 295, 100, 100, nextbutton, nextbutton_highlighted)
            if click_button(1160, 295, 100, 100, nextbutton, nextbutton_highlighted) == True:
                state = "page2"
                count = 0

    if state == "page2":
        win.blit(pg1background, (0, 0))
        win.blit(titleText, (72, 50))
        win.blit(pg2text, (0, 0))
        if count > 10000000:
            click_button(1160, 295, 100, 100, nextbutton, nextbutton_highlighted)
            if click_button(1160, 295, 100, 100, nextbutton, nextbutton_highlighted) == True:
                state = "page3"
                count = 0

    if state == "page3":
        win.blit(pg1background, (0, 0))
        win.blit(titleText, (72, 50))
        win.blit(pg3text, (0, 0))
        if count > 10000000:
            click_button(1160, 295, 100, 100, nextbutton, nextbutton_highlighted)
            if click_button(1160, 295, 100, 100, nextbutton, nextbutton_highlighted) == True:
                state = "page3.5"
                count = 0

    if state == "page3.5":
        win.blit(pg1background, (0, 0))
        win.blit(titleText, (72, 50))
        win.blit(graph, (0, 0))







    



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #updating display
    pygame.display.update()

pygame.quit()

