import pygame
import os
import sys
from pygame.locals import *
from button import Button  # Imports the class Button from the python file button
from textInput import TextInput
from buttonImage import ButtonImg
pygame.init()


screenWidthPixels = 1920
screenHeightPixels = 1080
# Initialize font
font = pygame.font.SysFont("Oswald", 80)



# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Load images
mrFreshimage = pygame.image.load(os.path.join(script_dir, 'mrFresh.png'))
scaled_mrFreshimage = pygame.transform.scale(mrFreshimage, (screenWidthPixels, screenHeightPixels))
play_background = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'PLAY_background.png'))
scaled_background = pygame.transform.scale(play_background, (screenWidthPixels, screenHeightPixels))

# Load Assets and Art
BOXasset = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'BOX.png'))
scaledBOXasset = pygame.transform.scale(BOXasset, (screenWidthPixels * 0.09, screenWidthPixels * 0.09))
PUSHFORCEasset = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'PUSHFORCE.png'))
scaledPUSHFORCEasset = pygame.transform.scale(PUSHFORCEasset, (screenWidthPixels * 0.07, screenWidthPixels * 0.07))
BOX_2asset = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'BOX_2.png'))
scaledBOX_2asset = pygame.transform.scale(BOX_2asset, (screenWidthPixels * 0.09, screenWidthPixels * 0.09))

# BUTTONS IMAGES
RETRYbutton = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'RETRY.png'))
scaledRETRYbutton = pygame.transform.scale(RETRYbutton, (screenWidthPixels * 0.07, screenWidthPixels * 0.07))
PLAYbutton = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'PLAY.png'))
scaledPLAYbutton = pygame.transform.scale(PLAYbutton, (screenWidthPixels * 0.07, screenWidthPixels * 0.07))
PAUSEbutton = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'PAUSE.png'))
scaledPAUSEbutton = pygame.transform.scale(PAUSEbutton, (screenWidthPixels * 0.07, screenWidthPixels * 0.07))

# HOVERED BUTTONS IMAGES
RETRYhover = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'RETRYhover.png'))
scaledRETRYhover = pygame.transform.scale(RETRYhover, (screenWidthPixels * 0.07, screenWidthPixels * 0.07))
PLAYhover = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'PLAYhover.png'))
scaledPLAYhover = pygame.transform.scale(PLAYhover, (screenWidthPixels * 0.07, screenWidthPixels * 0.07))
PAUSEhover = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'PAUSEhover.png'))
scaledPAUSEhover = pygame.transform.scale(PAUSEhover, (screenWidthPixels * 0.07, screenWidthPixels * 0.07))

# Colors
bgColor = (219, 244, 255)
sideBarColor = (255, 221, 217)
sideBarBorder = (201, 135, 127)
white = (255, 255, 255)
pink = (245, 91, 175)
darkBlue = (40, 55, 79)
fadedRed = (156, 89, 104)

# Initialize window
win = pygame.display.set_mode((screenWidthPixels, screenHeightPixels))

# Define the buttons needed for the game
PLAY_START = Button(image=None, pos=(screenWidthPixels // 2, int(screenHeightPixels * 0.3)),
                    text_input="PLAY", font=font, base_color=darkBlue, hovering_color=pink)

PLAY_TUTORIAL = Button(image=None, pos=(screenWidthPixels // 2, int(screenHeightPixels * 0.5)),
                       text_input="TUTORIAL", font=font, base_color=darkBlue, hovering_color=pink)

PLAY_EXIT = Button(image=None, pos=(screenWidthPixels // 2, int(screenHeightPixels * 0.7)),
                   text_input="EXIT", font=font, base_color=darkBlue, hovering_color=pink)

PLAY_BACK = Button(image=None, pos=(int(screenWidthPixels * 0.92), int(screenHeightPixels * 0.9)),
                   text_input="BACK", font=font, base_color=darkBlue, hovering_color=pink)

# Image Buttons
RETRYbutton = ButtonImg(scaledRETRYbutton, scaledRETRYhover, screenWidthPixels * 0.515, screenHeightPixels * 0.6)
PLAYbutton = ButtonImg(scaledPLAYbutton, scaledPLAYhover, screenWidthPixels * 0.615, screenHeightPixels * 0.6)
PAUSEbutton = ButtonImg(scaledPAUSEbutton, scaledPAUSEhover, screenWidthPixels * 0.715, screenHeightPixels * 0.6)

#function for creating text
def draw_text(surface, text, font, color, pos):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)

timePassed = 0

# GAME LOOPS 
def game():
    clock = pygame.time.Clock()
    global timePassed # Declare timePassed as a global variable

    # Initialize text input fields
    input_force = TextInput(screenWidthPixels * 0.154, screenHeightPixels * 0.098, screenWidthPixels *  0.10421, screenHeightPixels * 0.0555566, font, '')
    input_mass = TextInput(screenWidthPixels * 0.154, screenHeightPixels * 0.179, screenWidthPixels *  0.10421, screenHeightPixels * 0.0555566, font, '')
    
    isReleased = False

    # Initialize box position and velocity
    box_x = screenWidthPixels * 0.4
    box_y = screenHeightPixels * 0.391
    box_velocity = 0  # Initial horizontal velocity
    box_acceleration = 0
    

    # Initialize arrow position and velocity
    arrow_x = screenWidthPixels * 0.337
    arrow_y = screenHeightPixels * 0.43
    arrow_velocity = 0
    KineticEnergy = 0
    Displacement_x = 0
    Work = 0

    while True:
        dt = clock.tick(60) / 1000  # Time step in seconds
        win.fill(bgColor)
        win.blit(scaled_background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Move right
                    force = input_force.get_value()
                    mass = input_mass.get_value()
                    box_acceleration = (force / mass)
                    isReleased = True

            # Checks if the mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:  # Checks if mouse is pressed
                if PLAY_BACK.checkForInput(pygame.mouse.get_pos()):
                    mainMenu()

                # If retry button is pressed then restart the window
                mouse_pos = pygame.mouse.get_pos()
                if RETRYbutton.is_over(mouse_pos):
                    # Initialize box position and velocity
                    box_x = screenWidthPixels * 0.4
                    box_y = screenHeightPixels * 0.391
                    box_velocity = 0  # Initial horizontal velocity
                    box_acceleration = 0

                    # Initialize arrow position and velocity
                    arrow_x = screenWidthPixels * 0.337
                    arrow_y = screenHeightPixels * 0.43
                    arrow_velocity = 0

                    KineticEnergy = 0
                    Displacement_x = 0
                    Work = 0
                    timePassed = 0
                
                # If the play button is pressed start the simulation
                mouse_pos = pygame.mouse.get_pos()
                if PLAYbutton.is_over(mouse_pos):
                    force = input_force.get_value()
                    mass = input_mass.get_value()
                    box_acceleration = (force / mass)
                    isReleased = True
                    
                # If the pause button is pressed pause the simulation
                mouse_pos = pygame.mouse.get_pos()
                if PAUSEbutton.is_over(mouse_pos):
                    isReleased = False
                
            # Handle text input events
            input_force.handle_event(event)
            input_mass.handle_event(event)

        # Calculate time passed since the start/play button was pressed
        if isReleased:
            timePassed += dt  # Increment timePassed by the time step
            
        input_force.update()
        input_mass.update()
        
        # changes the box position if the space button is pressed
        # changes the box position if the space button is pressed
        if isReleased:
            # Update box position
            box_velocity += box_acceleration * dt
            box_x += box_velocity * dt
            arrow_velocity += box_acceleration * dt
            arrow_x += arrow_velocity * dt
            KineticEnergy = 0.5 * mass * box_velocity ** 2
            Displacement_x = (box_x - (screenWidthPixels * 0.4))
            Work = force * Displacement_x


        # Ensure the box stays within the bounds of the surface
        surface_left = screenWidthPixels * 0.33
        surface_right = screenWidthPixels * 0.98 - scaledBOXasset.get_width()
        if box_x < surface_left:
            box_x = surface_left
        elif box_x > surface_right:
            box_x = surface_right
            isReleased = False
        # Does the same but for the arrow
        if arrow_x < surface_left:
            arrow_x = surface_left
        elif arrow_x > surface_right - scaledBOXasset.get_width() + (screenWidthPixels * 0.03):
            arrow_x = surface_right - scaledBOXasset.get_width() + (screenWidthPixels * 0.03)

        # Displays the Results
        # PRINTS VELOCITY
        Veloc = font.render(f"{box_velocity:.2f} m/s", True, white)
        Veloc_rect = Veloc.get_rect(center = (screenWidthPixels * 0.154, screenHeightPixels * 0.44))
        win.blit(Veloc, Veloc_rect)

        # PRINTS TIME
        Time = font.render(f"{timePassed:.2f} s", True, white)
        Time_rect = Veloc.get_rect(center = (screenWidthPixels * 0.435, screenHeightPixels * 0.6))
        win.blit(Time, Time_rect)

        # PRINTS KINETIC ENERGY
        KinEn = font.render(f"{KineticEnergy:.2f} J", True, white)
        KinEn_rect = KinEn.get_rect(center = (screenWidthPixels * 0.154, screenHeightPixels * 0.6))
        win.blit(KinEn, KinEn_rect)
        
        # PRINTS DISPLACEMENT
        Displacement = font.render(f"{Displacement_x:.2f} m", True, white)
        Displacement_rect = Displacement.get_rect(center = (screenWidthPixels * 0.154, screenHeightPixels * 0.76))
        win.blit(Displacement, Displacement_rect)

        # PRINTS WORK
        WorkFinal = font.render(f"{Work:.2f} J", True, white)
        WorkFinal_rect = WorkFinal.get_rect(center = (screenWidthPixels * 0.154, screenHeightPixels * 0.92))
        win.blit(WorkFinal, WorkFinal_rect)
        
        # Draw the frictionless surface
        pygame.draw.rect(win, darkBlue, (screenWidthPixels * 0.33, screenHeightPixels * 0.55, screenWidthPixels * 0.651, screenHeightPixels * 0.01))

        if (timePassed > 2 and timePassed < 4) or (timePassed > 8 and timePassed < 12) or (timePassed > 15 and timePassed < 18):
            # Draw the box on the surface
            win.blit(scaledBOX_2asset, (box_x, box_y))
        else:
            # Draw the box on the surface
            win.blit(scaledBOXasset, (box_x, box_y))

        # Draw the push force
        win.blit(scaledPUSHFORCEasset, (arrow_x, arrow_y))

        # Draw input fields
        #FORCE
        input_force.draw(win)
        #MASS
        input_mass.draw(win)

        PLAY_BACK.changeColor(pygame.mouse.get_pos())
        PLAY_BACK.update(win)
        
        # RETRY BUTTON 
        RETRYbutton.draw(win)
        # Changes the image if hovered over
        mouse_pos = pygame.mouse.get_pos()
        if RETRYbutton.is_over(mouse_pos):
            RETRYbutton.is_hovered = True
        else:
            RETRYbutton.is_hovered = False

        # PLAY BUTTON 
        PLAYbutton.draw(win)
        # Changes the image if hovered over
        mouse_pos = pygame.mouse.get_pos()
        if PLAYbutton.is_over(mouse_pos):
            PLAYbutton.is_hovered = True
        else:
            PLAYbutton.is_hovered = False

        # PAUSE BUTTON 
        PAUSEbutton.draw(win)
        # Changes the image if hovered over
        mouse_pos = pygame.mouse.get_pos()
        if PAUSEbutton.is_over(mouse_pos):
            PAUSEbutton.is_hovered = True
        else:
            PAUSEbutton.is_hovered = False

        pygame.display.update()


def tutorial():
    while True:
        win.fill((0, 0, 0))

        win.blit(scaled_mrFreshimage, (0, 0))

        for event in pygame.event.get():
            # If the X is pressed then quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Checks if the mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:  # Checks if mouse is pressed
                # Same with the rest in if(), once the mouse is within bounds and is pressed, do function
                if PLAY_BACK.checkForInput(pygame.mouse.get_pos()):
                    mainMenu()

        # Draw the EXIT button
        PLAY_BACK.changeColor(pygame.mouse.get_pos())
        PLAY_BACK.update(win)

        pygame.display.update()

        # Frame rate of the game
        pygame.time.Clock().tick(60)

def mainMenu():
    pygame.display.set_caption("Main Menu")  # Main menu title

    while True:
        # Fill the screen with the color
        win.fill(bgColor)

        for event in pygame.event.get():
            # If the X is pressed then quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Checks if the mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Same with the rest in if(), once the mouse is within bounds and is pressed, do function
                if PLAY_START.checkForInput(pygame.mouse.get_pos()):
                    game()  # Call the game function when the button is pressed

                if PLAY_TUTORIAL.checkForInput(pygame.mouse.get_pos()):
                    tutorial()

                if PLAY_EXIT.checkForInput(pygame.mouse.get_pos()):
                    pygame.quit()
                    return

        # Draw the PLAY button
        PLAY_START.changeColor(pygame.mouse.get_pos())
        PLAY_START.update(win)

        # Draw the TUTORIAL button
        PLAY_TUTORIAL.changeColor(pygame.mouse.get_pos())
        PLAY_TUTORIAL.update(win)

        # Draw the EXIT button
        PLAY_EXIT.changeColor(pygame.mouse.get_pos())
        PLAY_EXIT.update(win)

        pygame.display.update()

        # Frame rate of the game
        pygame.time.Clock().tick(60)

mainMenu()
