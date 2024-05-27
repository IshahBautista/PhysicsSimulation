import pygame
import os
import sys
import math
from pygame.locals import *
from button import Button  # Imports the class Button from the python file button
from textInput import TextInput
from buttonImage import ButtonImg

pygame.init()

# Get the current screen resolution
info = pygame.display.Info()
screenWidthPixels = info.current_w
screenHeightPixels = info.current_h

# Set the display mode to the screen resolution
screen = pygame.display.set_mode((screenWidthPixels, screenHeightPixels))

# Initialize font
font = pygame.font.SysFont("Oswald", 80)

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Load images
play_background = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'PLAY_background.png'))
scaled_background = pygame.transform.scale(play_background, (screenWidthPixels, screenHeightPixels))
sim2_background = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'SIM2_background.png'))
sim2scaled_background = pygame.transform.scale(sim2_background, (screenWidthPixels, screenHeightPixels))

# Load Assets and Art
BOXasset = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'BOX.png'))
scaledBOXasset = pygame.transform.scale(BOXasset, (screenWidthPixels * 0.09, screenWidthPixels * 0.09))
PUSHFORCEasset = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'PUSHFORCE.png'))
scaledPUSHFORCEasset = pygame.transform.scale(PUSHFORCEasset, (screenWidthPixels * 0.07, screenWidthPixels * 0.07))
BOX_2asset = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'BOX_2.png'))
scaledBOX_2asset = pygame.transform.scale(BOX_2asset, (screenWidthPixels * 0.09, screenWidthPixels * 0.09))
RAMPasset = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'RAMP.png')) #unscaled
scaledRAMPasset = pygame.transform.scale(RAMPasset, (screenWidthPixels, screenHeightPixels))

# BUTTONS IMAGES
RETRYbutton = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'RETRY.png'))
scaledRETRYbutton = pygame.transform.scale(RETRYbutton, (screenWidthPixels * 0.07, screenWidthPixels * 0.07))
PLAYbutton = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'PLAY.png'))
scaledPLAYbutton = pygame.transform.scale(PLAYbutton, (screenWidthPixels * 0.07, screenWidthPixels * 0.07))
PAUSEbutton = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'PAUSE.png'))
scaledPAUSEbutton = pygame.transform.scale(PAUSEbutton, (screenWidthPixels * 0.07, screenWidthPixels * 0.07))
SIM1button = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'SIM1BUTTON.png'))
SIM2button = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'SIM2BUTTON.png'))
EXITbutton = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'EXIT.png'))
MENUbutton = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'MENU.png'))
INCREASEbutton = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'INCREASE.png'))
scaledINCREASEbutton = pygame.transform.scale(INCREASEbutton, (screenWidthPixels * 0.07, screenWidthPixels * 0.07))
DECREASEbutton = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'DECREASE.png'))
scaledDECREASEbutton = pygame.transform.scale(DECREASEbutton, (screenWidthPixels * 0.07, screenWidthPixels * 0.07))

# HOVERED BUTTONS IMAGES
RETRYhover = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'RETRYhover.png'))
scaledRETRYhover = pygame.transform.scale(RETRYhover, (screenWidthPixels * 0.07, screenWidthPixels * 0.07))
PLAYhover = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'PLAYhover.png'))
scaledPLAYhover = pygame.transform.scale(PLAYhover, (screenWidthPixels * 0.07, screenWidthPixels * 0.07))
PAUSEhover = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'PAUSEhover.png'))
scaledPAUSEhover = pygame.transform.scale(PAUSEhover, (screenWidthPixels * 0.07, screenWidthPixels * 0.07))
SIM1hover = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'SIM1BUTTONhover.png'))
SIM2hover = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'SIM2BUTTONhover.png'))
EXIThover = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'EXIThover.png'))
MENUhover = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'MENUhover.png'))
INCREASEhover = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'INCREASEhover.png'))
scaledINCREASEhover = pygame.transform.scale(INCREASEhover, (screenWidthPixels * 0.07, screenWidthPixels * 0.07))
DECREASEhover = pygame.image.load(os.path.join(script_dir, 'ASSETS', 'DECREASEhover.png'))
scaledDECREASEhover = pygame.transform.scale(DECREASEhover, (screenWidthPixels * 0.07, screenWidthPixels * 0.07))

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

# Image Buttons
#for sim1
RETRYbutton = ButtonImg(scaledRETRYbutton, scaledRETRYhover, screenWidthPixels * 0.515, screenHeightPixels * 0.6)
PLAYbutton = ButtonImg(scaledPLAYbutton, scaledPLAYhover, screenWidthPixels * 0.615, screenHeightPixels * 0.6)
PAUSEbutton = ButtonImg(scaledPAUSEbutton, scaledPAUSEhover, screenWidthPixels * 0.715, screenHeightPixels * 0.6)
SIM1button = ButtonImg(SIM1button, SIM1hover, screenWidthPixels * 0.36, screenHeightPixels * 0.15)
SIM2button = ButtonImg(SIM2button, SIM2hover, screenWidthPixels * 0.36, screenHeightPixels * 0.4)
EXITbutton = ButtonImg(EXITbutton, EXIThover, screenWidthPixels * 0.36, screenHeightPixels * 0.65)
MENUbutton = ButtonImg(MENUbutton, MENUhover, screenWidthPixels * 0.715, screenHeightPixels * 0.8)

# for sim2
RETRYbutton2 = ButtonImg(scaledRETRYbutton, scaledRETRYhover, screenWidthPixels * 0.18, screenHeightPixels * 0.65)
PLAYbutton2 = ButtonImg(scaledPLAYbutton, scaledPLAYhover, screenWidthPixels * 0.1, screenHeightPixels * 0.65)
PAUSEbutton2 = ButtonImg(scaledPAUSEbutton, scaledPAUSEhover, screenWidthPixels * 0.1, screenHeightPixels * 0.80)
INCREASEbutton = ButtonImg(scaledINCREASEbutton, scaledINCREASEhover, screenWidthPixels * 0.02, screenHeightPixels * 0.65)
DECREASEbutton = ButtonImg(scaledDECREASEbutton, scaledDECREASEhover, screenWidthPixels * 0.02, screenHeightPixels * 0.80)

#function for creating text
def draw_text(surface, text, font, color, pos):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)

timePassed = 0

# GAME LOOPS 
def game():
    clock = pygame.time.Clock()
    global timePassed
    timePassed = 0

    # Conversion factor from pixels to meters
    pixels_per_meter = 20

    # Initialize text input fields
    input_force = TextInput(screenWidthPixels * 0.154, screenHeightPixels * 0.098, screenWidthPixels *  0.10421, screenHeightPixels * 0.0555566, font, '')
    input_mass = TextInput(screenWidthPixels * 0.154, screenHeightPixels * 0.179, screenWidthPixels *  0.10421, screenHeightPixels * 0.0555566, font, '')

    isReleased = False

    # Initialize box position and velocity (convert initial position to meters)
    box_x_pixels = screenWidthPixels * 0.4
    box_y_pixels = screenHeightPixels * 0.391
    box_x = box_x_pixels / pixels_per_meter
    box_y = box_y_pixels / pixels_per_meter
    box_velocity = 0  # Initial horizontal velocity in m/s
    box_acceleration = 0

    # Initialize arrow position and velocity (convert initial position to meters)
    arrow_x_pixels = screenWidthPixels * 0.337
    arrow_y_pixels = screenHeightPixels * 0.43
    arrow_x = arrow_x_pixels / pixels_per_meter
    arrow_y = arrow_y_pixels / pixels_per_meter
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if RETRYbutton.is_over(mouse_pos):
                    box_x_pixels = screenWidthPixels * 0.4
                    box_y_pixels = screenHeightPixels * 0.391
                    box_x = box_x_pixels / pixels_per_meter
                    box_y = box_y_pixels / pixels_per_meter
                    box_velocity = 0
                    box_acceleration = 0

                    arrow_x_pixels = screenWidthPixels * 0.337
                    arrow_y_pixels = screenHeightPixels * 0.43
                    arrow_x = arrow_x_pixels / pixels_per_meter
                    arrow_y = arrow_y_pixels / pixels_per_meter
                    arrow_velocity = 0

                    KineticEnergy = 0
                    Displacement_x = 0
                    Work = 0
                    timePassed = 0
                
                if PLAYbutton.is_over(mouse_pos):
                    force = input_force.get_value()
                    mass = input_mass.get_value()
                    box_acceleration = (force / mass)
                    isReleased = True

                if PAUSEbutton.is_over(mouse_pos):
                    isReleased = False
                if MENUbutton.is_over(mouse_pos):
                    mainMenu()
                
            input_force.handle_event(event)
            input_mass.handle_event(event)

        if isReleased:
            timePassed += dt

        input_force.update()
        input_mass.update()

        if isReleased:
            box_velocity += box_acceleration * dt
            box_x += box_velocity * dt
            arrow_velocity += box_acceleration * dt
            arrow_x += arrow_velocity * dt
            KineticEnergy = 0.5 * mass * box_velocity ** 2
            Displacement_x = (box_x - (screenWidthPixels * 0.4 / pixels_per_meter))
            Work = force * Displacement_x

        surface_left = screenWidthPixels * 0.33 / pixels_per_meter
        surface_right = (screenWidthPixels * 0.98 - scaledBOXasset.get_width()) / pixels_per_meter
        if box_x < surface_left:
            box_x = surface_left
        elif box_x > surface_right:
            box_x = surface_right
            isReleased = False

        if arrow_x < surface_left:
            arrow_x = surface_left
        elif arrow_x > surface_right - scaledBOXasset.get_width() / pixels_per_meter + (screenWidthPixels * 0.03 / pixels_per_meter):
            arrow_x = surface_right - scaledBOXasset.get_width() / pixels_per_meter + (screenWidthPixels * 0.03 / pixels_per_meter)

        Veloc = font.render(f"{box_velocity:.2f} m/s", True, white)
        Veloc_rect = Veloc.get_rect(center=(screenWidthPixels * 0.154, screenHeightPixels * 0.44))
        win.blit(Veloc, Veloc_rect)

        Time = font.render(f"{timePassed:.2f} s", True, white)
        Time_rect = Veloc.get_rect(center=(screenWidthPixels * 0.435, screenHeightPixels * 0.6))
        win.blit(Time, Time_rect)

        KinEn = font.render(f"{KineticEnergy:.2f} J", True, white)
        KinEn_rect = KinEn.get_rect(center=(screenWidthPixels * 0.154, screenHeightPixels * 0.6))
        win.blit(KinEn, KinEn_rect)

        Displacement = font.render(f"{Displacement_x:.2f} m", True, white)
        Displacement_rect = Displacement.get_rect(center=(screenWidthPixels * 0.154, screenHeightPixels * 0.76))
        win.blit(Displacement, Displacement_rect)

        WorkFinal = font.render(f"{Work:.2f} J", True, white)
        WorkFinal_rect = WorkFinal.get_rect(center=(screenWidthPixels * 0.154, screenHeightPixels * 0.92))
        win.blit(WorkFinal, WorkFinal_rect)

        if (timePassed > 2 and timePassed < 4) or (timePassed > 8 and timePassed < 12) or (timePassed > 15 and timePassed < 18):
            win.blit(scaledBOX_2asset, (box_x * pixels_per_meter, box_y * pixels_per_meter))
        else:
            win.blit(scaledBOXasset, (box_x * pixels_per_meter, box_y * pixels_per_meter))

        win.blit(scaledPUSHFORCEasset, (arrow_x * pixels_per_meter, arrow_y * pixels_per_meter))

        input_force.draw(win)
        input_mass.draw(win)

        RETRYbutton.draw(win)
        mouse_pos = pygame.mouse.get_pos()
        if RETRYbutton.is_over(mouse_pos):
            RETRYbutton.is_hovered = True
        else:
            RETRYbutton.is_hovered = False

        PLAYbutton.draw(win)
        mouse_pos = pygame.mouse.get_pos()
        if PLAYbutton.is_over(mouse_pos):
            PLAYbutton.is_hovered = True
        else:
            PLAYbutton.is_hovered = False

        PAUSEbutton.draw(win)
        mouse_pos = pygame.mouse.get_pos()
        if PAUSEbutton.is_over(mouse_pos):
            PAUSEbutton.is_hovered = True
        else:
            PAUSEbutton.is_hovered = False

        MENUbutton.draw(win)
        mouse_pos = pygame.mouse.get_pos()
        if MENUbutton.is_over(mouse_pos):
            MENUbutton.is_hovered = True
        else:
            MENUbutton.is_hovered = False

        pygame.display.update()

def sim2():
    clock = pygame.time.Clock()
    global timePassed  # Declare timePassed as a global variable
    timePassed = 0

     # Conversion factor: 50 pixels = 1 meter
    pixel_to_meter = 20

    # Initialize text input fields
    input_angle = TextInput(screenWidthPixels * 0.154, screenWidthPixels * 0.098, screenWidthPixels * 0.10421, screenHeightPixels * 0.0555566, font, '')

    # Initialize box position, velocity, and acceleration
    gravity = 9.81
    box_vel = 0
    height = 0
    isReleased = False
    isPaused = False

    # Circle properties
    circle_center = (screenWidthPixels * 0.5, screenHeightPixels * 0.7)
    circle_radius = screenWidthPixels * 0.4

    initialheight = screenHeightPixels * 0.7 / pixel_to_meter

    angle = 0  # Angle in degrees


    # Function to convert degrees to radians
    def degrees_to_radians(degrees):
        return degrees * (math.pi / 180)

    while True:
        dt = clock.tick(60) / 1000  # Time step in seconds
        win.fill(bgColor)
        win.blit(sim2scaled_background, (0, 0))
        for event in pygame.event.get():
            if not isReleased:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        angle -= 1  # Decrease the angle by 1 degree
                    elif event.key == pygame.K_DOWN:
                        angle += 1  # Increase the angle by 1 degree

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Release box
                    angle_radians = math.radians(angle)
                    increment_x = math.cos(angle_radians)
                    increment_y = math.sin(angle_radians)
                    box_accel = gravity * math.sin(angle_radians)
                    isReleased = True

            input_angle.handle_event(event)

            # All button press events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENUbutton.is_over(pygame.mouse.get_pos()):
                    mainMenu()

                if PAUSEbutton2.is_over(mouse_pos):
                    isReleased = False
                    isPaused = True
                
                if PLAYbutton2.is_over(mouse_pos):
                    angle_radians = math.radians(angle)
                    increment_x = math.cos(angle_radians)
                    increment_y = math.sin(angle_radians)
                    box_accel = gravity * math.sin(angle_radians)
                    isReleased = True
                    isPaused = False

                if RETRYbutton2.is_over(mouse_pos):
                    isReleased = False
                    isPaused = False
                    box_vel = 0
                    angle = 0
                
                if INCREASEbutton.is_over(mouse_pos):
                    angle -= 1  # Decrease the angle by 1 degree

                if DECREASEbutton.is_over(mouse_pos):
                    angle += 1  # Increase the angle by 1 degree

        # Calculate the object's position along the circle using the angle
        input_angle.update()

        radian_angle = degrees_to_radians(angle)
        if not isReleased and not isPaused:
            box_x = circle_center[0] + int(circle_radius * math.cos(radian_angle))
            box_y = circle_center[1] + int(circle_radius * math.sin(radian_angle))
            height = initialheight - (box_y / pixel_to_meter)
        elif isReleased and not isPaused:
            timePassed += dt
            box_vel += box_accel * dt
            box_x += (box_vel * dt * pixel_to_meter) * increment_x
            box_y += (box_vel * dt * pixel_to_meter) * increment_y
            height = initialheight - (box_y / pixel_to_meter)

        # Draw the rotated box
        rotated_box = pygame.transform.rotate(scaledBOXasset, -angle)
        box_rect = rotated_box.get_rect(center=(box_x, box_y))
        win.blit(rotated_box, box_rect.topleft)

        Ramp = pygame.transform.rotate(scaledRAMPasset, -angle)
        Ramp_rect = Ramp.get_rect(center=(circle_center))
        win.blit(Ramp, Ramp_rect.topleft)

        # PRINTS ANGLE
        AngleFinal = font.render(f"{angle*(-1):.2f}°", True, white)
        AngleFinal_rect = AngleFinal.get_rect(center=(screenWidthPixels * 0.22, screenHeightPixels * 0.13))
        win.blit(AngleFinal, AngleFinal_rect)

        # BUTTONS ______________________________________
        # MENU BUTTON
        MENUbutton.draw(win)
        # Changes the image if hovered over
        mouse_pos = pygame.mouse.get_pos()
        if MENUbutton.is_over(mouse_pos):
            MENUbutton.is_hovered = True
        else:
            MENUbutton.is_hovered = False

        INCREASEbutton.draw(win)
        mouse_pos = pygame.mouse.get_pos()
        if INCREASEbutton.is_over(mouse_pos):
            INCREASEbutton.is_hovered = True
        else:
            INCREASEbutton.is_hovered = False

        DECREASEbutton.draw(win)
        mouse_pos = pygame.mouse.get_pos()
        if DECREASEbutton.is_over(mouse_pos):
            DECREASEbutton.is_hovered = True
        else:
            DECREASEbutton.is_hovered = False

        PLAYbutton2.draw(win)
        mouse_pos = pygame.mouse.get_pos()
        if PLAYbutton2.is_over(mouse_pos):
            PLAYbutton2.is_hovered = True
        else:
            PLAYbutton2.is_hovered = False

        PAUSEbutton2.draw(win)
        mouse_pos = pygame.mouse.get_pos()
        if PAUSEbutton2.is_over(mouse_pos):
            PAUSEbutton2.is_hovered = True
        else:
            PAUSEbutton2.is_hovered = False
        
        RETRYbutton2.draw(win)
        mouse_pos = pygame.mouse.get_pos()
        if RETRYbutton2.is_over(mouse_pos):
            RETRYbutton2.is_hovered = True
        else:
            RETRYbutton2.is_hovered = False

        Height = font.render(f"{height:.2f} m", True, white)
        Height_rect = Height.get_rect(center=(screenWidthPixels * 0.3, screenHeightPixels * 0.86))
        win.blit(Height, Height_rect)
        
        pygame.display.update()

def mainMenu():
    pygame.display.set_caption("Main Menu")  # Main menu title

    while True:
        # Fill the screen with the color
        win.fill(bgColor)

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if SIM1button.is_over(mouse_pos):
                    game()

                if SIM2button.is_over(mouse_pos):
                    sim2()

                if EXITbutton.is_over(mouse_pos):
                    pygame.quit()
                    return
        
            # If the X is pressed then quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # sim1 BUTTON 
        SIM1button.draw(win)
        # Changes the image if hovered over
        mouse_pos = pygame.mouse.get_pos()
        if SIM1button.is_over(mouse_pos):
            SIM1button.is_hovered = True
        else:
            SIM1button.is_hovered = False

        # sim2 BUTTON 
        SIM2button.draw(win)
        # Changes the image if hovered over
        mouse_pos = pygame.mouse.get_pos()
        if SIM2button.is_over(mouse_pos):
            SIM2button.is_hovered = True
        else:
            SIM2button.is_hovered = False

        # EXIT BUTTON 
        EXITbutton.draw(win)
        # Changes the image if hovered over
        mouse_pos = pygame.mouse.get_pos()
        if EXITbutton.is_over(mouse_pos):
            EXITbutton.is_hovered = True
        else:
            EXITbutton.is_hovered = False

        pygame.display.update()

        # Frame rate of the game
        pygame.time.Clock().tick(60)

mainMenu()