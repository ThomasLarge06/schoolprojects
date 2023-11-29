import pygame
from pygame.locals import *
from pygame import mixer
# importing test.py
import test

# initialize all imported pygame modules
pygame.init()

clock = pygame.time.Clock()
# Frames Per Second
fps = 60

# Getting the size of the screen
screenWidth = 1000
screenHeight = 1000

# The screen being implemented
surface = pygame.display.set_mode((screenHeight, screenWidth))
pygame.display.set_caption('B-tech Mario')

# font
font = pygame.font.SysFont("arialblack", 40)
bigfont = pygame.font.SysFont("arialblack", 80)

# text colour
text_colour = (0, 0, 0)

# load button images
start_img = pygame.image.load("start_btn.png").convert_alpha()
options_img = pygame.image.load("option_btn.png").convert_alpha()
quit_img = pygame.image.load("quit_btn.png").convert_alpha()
credits_img = pygame.image.load("credits.png").convert_alpha()
credits_img = pygame.transform.scale(credits_img, (200, 100))
title_img = pygame.image.load('title.png')
back_img = pygame.image.load('back.png')
back_img = pygame.transform.scale(back_img, (200, 100))


# function for draw text
def draw_text(text, font, text_colour, x, y):
    # turn the text into a picture
    img = font.render(text, True, text_colour)
    surface.blit(img, (x, y))


# variables
tile_size = 50
gameOver = 0
mainMenu = True
menuState = "main"
level = 1
max_levels = 3

# Background music
mixer.music.load('music.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.1)

# Images
sun_img = pygame.image.load('sun.png')
bg_img = pygame.image.load('bg (2).jpg')
bg_img = pygame.transform.scale(bg_img, (screenHeight, screenWidth))
reset_img = pygame.image.load('reset.png')
reset_img = pygame.transform.scale(reset_img, (300, 100))
gameOver_img = pygame.image.load('gameover.png')
win_img = pygame.image.load('win.png')


# function for reset level
def reset_level(level):
    # reset player back to the start of the game
    character.reset(100, screenHeight - 130)
    # empty classes so then we don't get the same placement from the last level into the next level
    goomba_group.empty()
    spike_group.empty()
    finish_group.empty()

    # from test.py, if level == 1 then the world will run level 1
    if level == 1:
        list = test.level1
    # from test.py, if level == 2 then the world will run level 2
    elif level == 2:
        list = test.level2
    # from test.py, if level == 3 then the world will run level 3
    elif level == 3:
        list = test.level3
    world = World(list)
    return world


# creating a class for our world
class World():
    # constructor for the init function that will take the data argument
    def __init__(self, data):
        # Creating a list that equals an empty list
        self.tile_list = []
        # load images
        dirt_img = pygame.image.load('dirt.jpg')
        grass_img = pygame.image.load('grass.jpg')
        # for loop for creating the tiles in the world
        row_count = 0
        for row in data:
            column_count = 0
            for tile in row:
                # if tile equals 1 then the image is dirt
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    # Getting a rectangle object for the image, so I can use it later on for collisions
                    img_rect = img.get_rect()
                    # X and Y coordinate to position my dirt
                    img_rect.x = column_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    # it will ignore the zeros from the World Data
                    self.tile_list.append(tile)
                # if tile equals 1 then the image is grass
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    # X and Y coordinate to positon my grass
                    img_rect.x = column_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    # it will ignore the zeros from the World Data
                    self.tile_list.append(tile)
                # if tile equals 3 then the class is Enemy
                if tile == 3:
                    # X and Y coordinate to position my Enemy
                    goomba = Enemy(column_count * tile_size, row_count * tile_size)
                    # Add the enemy that I created
                    goomba_group.add(goomba)
                # if tile equals 4 then the class is Obstacle
                if tile == 4:
                    # X and Y coordinate to position my Obstacle
                    spike = Obstacle(column_count * tile_size, row_count * tile_size)
                    # Add the Obstacle that I created
                    spike_group.add(spike)
                # if tile equals 5 then the class is Finish
                if tile == 5:
                    # X and Y coordinate to position my endpoint
                    finish = Finish(column_count * tile_size, row_count * tile_size - 20)
                    # Add the endpoint that I created
                    finish_group.add(finish)
                # As soon as the user has gone through the tiles and he moves on to the next one, he then knows he is moving along the row
                column_count += 1
            row_count += 1

    def draw(self):
        # Go through each item in the list
        for tile in self.tile_list:
            # draw the item on the screen from getting a particular value from the list by using the indices
            surface.blit(tile[0], tile[1])


# creating a class for the buttons
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        # Position for the rectangle in the X and Y coordinate
        self.rect.x = x
        self.rect.y = y

        self.clicked = False

    def draw(self):
        action = False
        # mouse position, getting the X and Y coordinate of the mouse
        mouse_pos = pygame.mouse.get_pos()
        # checking for a collision with a point
        if self.rect.collidepoint(mouse_pos):
            # which button is being clicked, and for the left mouse click it would be the index at zero, and also prevent the user for holding the click button
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        # release the mouse button
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        # draw button
        surface.blit(self.image, self.rect)

        return action


# Creating a class for the player
class Player():
    # constructor for the init function that takes the arguments of the x and y coordinates
    def __init__(self, x, y):
        self.reset(x, y)

    def update(self, gameOver):
        delta_x = 0
        delta_y = 0
        # walk cooldown
        cooldown = 7

        if gameOver == 0:
            # key presses
            key_press = pygame.key.get_pressed()
            # if the user presses the up arrow key, he will jump 15 pixels higher and it will make a jump sound
            if key_press[pygame.K_UP] and self.jump == False:
                self.vel_y = -15
                self.jump = True
                jump_sound = mixer.Sound('mariojump.mp3')
                jump_sound.play()
                jump_sound.set_volume(0.01)
            # if the user presses the left arrow key, he will move 5 pixels to the left
            if key_press[pygame.K_LEFT]:
                delta_x -= 5
                self.counter += 1
                self.direction = -1
            # if the user presses the left arrow key, he will move 5 pixels to the right
            if key_press[pygame.K_RIGHT]:
                delta_x += 5
                self.counter += 1
                self.direction = 1
            if key_press[pygame.K_LEFT] == False and key_press[pygame.K_RIGHT] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # animation
            if self.counter > cooldown:
                self.counter = 0
                self.index += 1
                # If gone through all the pictures, return back to beginning animation
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # creating gravity
            self.vel_y += 1
            # If the character exceeds 10 then it will never go past 10
            if self.vel_y > 10:
                self.vel_y = 10
            delta_y += self.vel_y

            # check for collision of going through each individual tiles
            for tile in world.tile_list:
                # check for collision in x direction
                if tile[1].colliderect(self.rect.x + delta_x, self.rect.y, self.width, self.height):
                    delta_x = 0
                # check for collision in y direction, rectangle data stored in index 1
                if tile[1].colliderect(self.rect.x, self.rect.y + delta_y, self.width, self.height):
                    # Get collision from below the block
                    if self.vel_y < 0:
                        delta_y = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # Get collision from above the block
                    elif self.vel_y >= 0:
                        delta_y = tile[1].top - self.rect.bottom
                        self.jump = False
            # if the user collides with the enemy it will make a death sound and set variable gameOver to 1
            if pygame.sprite.spritecollide(self, goomba_group, False):
                gameOver = 1
                hit_sound = mixer.Sound('death.mp3')
                hit_sound.play()
                hit_sound.set_volume(0.1)
                mixer.music.fadeout(1)
            # if the user collides with the spike it will make a death sound and set variable gameOver to 1
            if pygame.sprite.spritecollide(self, spike_group, False):
                gameOver = 1
                hit_sound = mixer.Sound('death.mp3')
                hit_sound.play()
                hit_sound.set_volume(0.1)
                mixer.music.fadeout(1)
            # if the user collides with the pipe the variable gameOver will be set to -1
            if pygame.sprite.spritecollide(self, finish_group, False):
                gameOver = -1
            # The Character's coordinates
            self.rect.x += delta_x
            self.rect.y += delta_y
        # drawing the character on the screen
        surface.blit(self.image, self.rect)

        # return back out to the global variables
        return gameOver

    # Reset method for the class Player once the reset button is clicked
    def reset(self, x, y):
        # blank list
        self.images_right = []
        self.images_left = []
        # track the index a list that corresponds to which item I want from the list
        self.index = 0
        # control the speed the animation runs through
        self.counter = 0
        # Looping the images 6 times to have the character have a walking animation
        for num in range(1, 6):
            img_right = pygame.image.load(f'character{num}.png')
            # scaling the size of the character
            img_right = pygame.transform.scale(img_right, (40, 75))
            img_left = pygame.transform.flip(img_right, True, False)
            # have a list that has 5 images
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        # Character in standing position
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        # Position for the rectangle in the X and Y coordinate
        self.rect.x = x
        self.rect.y = y
        # Width and Height variables for the rectangle
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jump = False
        self.direction = 0
        # once resetted, it will play the same background music
        mixer.music.load('music.mp3')
        mixer.music.play(-1)


# creating a class for the enemy
class Enemy(pygame.sprite.Sprite):
    # constructor for the init function that takes the arguments of the x and y coordinates
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('enemy.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        # Position for the rectangle in the X and Y coordinate
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
        self.counter = 0

    def update(self):
        # increase the x coordinate (meaning increasing to the right)
        self.rect.x += self.direction
        self.counter += 1
        # If the counter exceeds 75 then it will flip direction
        if self.counter > 75:
            self.direction *= -1
            self.counter = 0


# creating a class for the spike/obstacle
class Obstacle(pygame.sprite.Sprite):
    # constructor for the init function that takes the arguments of the x and y coordinates
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('spike.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        # Position for the rectangle in the X and Y coordinate
        self.rect.x = x
        self.rect.y = y


# creating a class for the end point of the level
class Finish(pygame.sprite.Sprite):
    # constructor for the init function that takes the arguments of the x and y coordinates
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('pipe.png')
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        # Position for the rectangle in the X and Y coordinate
        self.rect.x = x
        self.rect.y = y


# from test.py, if level == 1 then the world will run level 1
if level == 1:
    list = test.level1
# from test.py, if level == 2 then the world will run level 2
elif level == 2:
    list = test.level2
# from test.py, if level == 3 then the world will run level 3
elif level == 3:
    list = test.level3

# character's height
character = Player(100, screenHeight - 130)

# Empty Group, like a list, that can add into
goomba_group = pygame.sprite.Group()
spike_group = pygame.sprite.Group()
finish_group = pygame.sprite.Group()

world = World(list)

# buttons placement in main menu
reset_button = Button(screenWidth // 2 - 150, screenHeight // 2 + 300, reset_img)
quit_button = Button(screenWidth // 2 - 60, screenHeight // 2 + 150, quit_img)
option_button = Button(screenWidth // 2 - 60, screenHeight // 2, options_img)
start_button = Button(screenWidth // 2 - 60, screenHeight // 2 - 150, start_img)
credits_button = Button(screenWidth // 2 - 60, screenHeight // 2 + 330, credits_img)
back_button = Button(screenWidth // 2 + 300, screenHeight // 2 + 400, back_img)

run = True
# main program
while run:

    # framerate to limit to limit how quickly the character is running
    clock.tick(fps)

    # draw image
    surface.blit(bg_img, (0, 0))
    surface.blit(sun_img, (-200, -200))

    # mainMenu is already set to true, so when the user runs the program, it will show the Main menu
    if mainMenu == True:
        # If the menu state is main then it will give 2 other menu states and 1 for quit button and the other for start button
        if menuState == "main":
            # If the user clicks on the quit button, the program finishes
            if quit_button.draw() == True:
                run = False
            # If the user clicks on the start button, the main menu will be set to false, and it will start the game
            if start_button.draw() == True:
                mainMenu = False
            # If the user clicks on the option button, menu state will be set to options
            if option_button.draw() == True:
                menuState = "options"
            # If the user clicks on the credits button, menu state will be set to credits
            if credits_button.draw() == True:
                menuState = "credits"
            surface.blit(title_img, (300, 200))

        # When the Menu state is set to options, it will show the key binds, Instructions, and a back button
        if menuState == "options":
            draw_text("Key Binds: ", font, (255, 0, 0), 45, 50)
            draw_text("LEFT ARROW KEY --> Move left", font, text_colour, 155, 100)
            draw_text("RIGHT ARROW KEY --> Move right", font, text_colour, 155, 150)
            draw_text("UP ARROW KEY --> Jump", font, text_colour, 155, 200)
            draw_text("ESCAPE KEY --> Return to menu", font, text_colour, 155, 250)
            draw_text("Instructions: ", font, (255, 0, 0), 45, 350)
            draw_text("To start playing, use your mouse", font, text_colour, 45, 400)
            draw_text("to click on the start button.", font, text_colour, 45, 450)
            draw_text("You will have to go through many obstacles", font, text_colour, 45, 500)
            draw_text("and enemies to pass the level.", font, text_colour, 45, 550)
            draw_text("There is going to be 3 levels ", font, text_colour, 45, 600)
            draw_text("where each level gets harder and harder.", font, text_colour, 45, 650)
            draw_text("You will have one extra jump in mid air, ", font, text_colour, 45, 700)
            draw_text("not a double jump. Reach the pipe to win. ", font, text_colour, 45, 750)
            # If the user clicks on the button, the menu state will return back to the main menu
            if back_button.draw():
                menuState = "main"
        # When the Menu state is set to credits, it will show who created the game, how long it took to make the game and a back button
        if menuState == "credits":
            draw_text("CREATED BY", font, (255, 0, 0), 400, 100)
            draw_text("Thomas Large", bigfont, (246, 190, 0), 200, 200)
            draw_text("Jerod Sparrow", bigfont, (246, 190, 0), 200, 300)
            draw_text("WORLD DESIGN BY:", font, (255, 0, 0), 350, 500)
            draw_text("Jerod Sparrow", bigfont, (246, 190, 0), 200, 550)
            draw_text("Time Spent: 7 hours", font, (246, 190, 0), 0, 950)
            # If the user clicks on the button, the menu state will return back to the main menu
            if back_button.draw():
                menuState = "main"

    # else statement if mainMenu is not set to true
    else:
        # draw world
        world.draw()

        if gameOver == 0:
            # drawing what level the player is on
            draw_text('Level: ' + str(level), font, (255, 255, 255), 50, 0)
            # updates the whole Enemy class
            goomba_group.update()
        spike_group.draw(surface)
        goomba_group.draw(surface)
        finish_group.draw(surface)

        gameOver = character.update(gameOver)

        # If the user dies, it will draw the gameover image and the reset button
        if gameOver == 1:
            surface.blit(gameOver_img, (200, 200))
            # If the user clicks on the reset button, it will reset to the same level
            if reset_button.draw():
                list = []
                world = reset_level(level)
                gameOver = 0
        if gameOver == -1:
            level += 1
            # If statement to not go beyond the levels
            if level <= max_levels:
                # load in a brand new empty list
                list = []
                world = reset_level(level)
                gameOver = 0
            # Else if the user finishes beyond the level, he wins the game
            else:
                surface.blit(win_img, (250, 200))
                # If the user clicks on the reset button, it will reset to the first level
                if reset_button.draw():
                    level = 1
                    list = []
                    world = reset_level(level)
                    gameOver = 0

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # if the user hits escape the screen will return back to the main menu
            if event.key == pygame.K_ESCAPE:
                mainMenu = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()