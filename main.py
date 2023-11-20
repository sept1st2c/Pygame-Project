import pygame
import os


from tkinter import *
import tkinter.messagebox 

from turtle import *
import time 
import random
import winsound
import sys # We will use sys.exit to exit the program
import pygame
from pygame.locals import * # Basic pygame imports


from pygame.locals import *
from pygame.math import Vector2
from pygame import mixer
import time

from copy import deepcopy


def game1():
    def eat_food():
        winsound.PlaySound("Eat_sound.wav", winsound.SND_ASYNC)

    def game_over():
        winsound.PlaySound("Game_Over.wav", winsound.SND_ASYNC)

    score=0 
    execution_delay=0.3
    root=Screen()
    root.title("Snake Game")
    root.setup(width=600, height=600)
    root.bgcolor('black')
    root.bgpic('border.gif')
    root.tracer(False)
    root.addshape('upmouth.gif')
    root.addshape('food.gif')
    root.addshape('downmouth.gif')
    root.addshape('leftmouth.gif')
    root.addshape('rightmouth.gif')
    root.addshape('body.gif')
    root.addshape('border.gif')

    head=Turtle()
    head.shape('upmouth.gif')
    head.penup()
    head.goto(0,0)
    head.direction='stop'

    food=Turtle()
    food.penup()
    food.shape('food.gif')
    food.goto(0,100)

    text=Turtle()
    text.penup()
    text.goto(-35,274)
    text.color('White')
    text.write('Score:0', font=('Algerian'), align='center')
    text.hideturtle()

    lost=Turtle()
    lost.color('white')
    lost.penup()
    lost.hideturtle()


    def move_snake():
        if head.direction=='up':
            y=head.ycor()
            y=y+20
            head.sety(y)

        if head.direction=='down':
            y=head.ycor()
            y=y-20
            head.sety(y)

        if head.direction=='right':
            x=head.xcor()
            x=x+20
            head.setx(x)

        if head.direction=='left':
            x=head.xcor()
            x=x-20
            head.setx(x) 

    def go_up():   
        if head.direction!='down':
            head.direction='up' 
            head.shape('upmouth.gif') 
    def go_down():
        if head.direction!='up':
            head.direction='down' 
            head.shape('downmouth.gif')
    def go_right():   
        if head.direction!='left':
            head.direction='right' 
            head.shape('rightmouth.gif') 
    def go_left():
        if head.direction!='right':
            head.direction='left'
            head.shape('leftmouth.gif') 


    root.listen()

    root.onkeypress(go_up,'Up')
    root.onkeypress(go_down,'Down')
    root.onkeypress(go_left,'Left')
    root.onkeypress(go_right,'Right')
    segments=[]

    while True:
        root.update()

        if head.xcor()>255 or head.xcor()<-255 or head.ycor()>240 or head.ycor()<-240:
            game_over()
            lost.write('Game Lost',align='center',font=('courier,34,bold'))
            head.goto(0,0)
            head.direction='stop'
            lost.clear()
            for bodies in segments:
                bodies.goto(1000,1000)
            score=0
            execution_delay=0.3    

            segments.clear()
            text.clear()
            text.write('Score:0',align='center', font=('Algerian'))   



        if head.distance(food)<20:
            eat_food()
            x=random.randint(-255,255)
            y=random.randint(-255,255) 
            food.goto(x,y)
            execution_delay=execution_delay-0.003

            body=Turtle()
            body.penup()
            body.shape('body.gif')
            segments.append(body)

            score=score+10
            text.clear()
            text.write(f'Score:{score}',font=('Algerian'))



        for i in range(len(segments)-1,0,-1):
            x=segments[i-1].xcor() 
            y=segments[i-1].ycor()
            segments[i].goto(x,y)

        if len(segments)>0:
            x=head.xcor()
            y=head.ycor()  
            segments[0].goto(x,y)   

        move_snake()

        for bodies in segments:
            if bodies.distance(head)<20:
                game_over()
                time.sleep(1)
                head.goto(0,0)
                head.direction=('stop')

                for bodies in segments:
                    bodies.goto(1000,1000)

                segments.clear()
                score=0
                execution_delay=0.3

                lost.write('Game Lost',align='center')
                time.sleep(1)
                lost.clear()

                text.clear()
                text.write('Score:0',align='center', font=('Algerian'))   
                

        time.sleep(execution_delay)

def game2():
    pygame.init()

    # Initials
    WIDTH, HEIGHT = 1000, 600
    wn = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PING-PONG")
    run = True
    player_1 = player_2 = 0
    directions = [-1, 1]
    angle = [0, 1, 2]

    # Color
    VIOLET = (115, 41, 210)
    LUSH_TEAL = (51, 255, 173)
    BACKGROUND_COLOR = (29, 30, 34)
    WHITE = (255, 255, 255)

    # BALL
    radius = 15
    ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius

    # Initialize with random velocity
    dir = random.choice(directions)
    ang = random.choice(angle)

    if dir == -1:
        ball_val_x = -1.5
    else:
        ball_val_x = 1.5

    if ang == 0:
        ball_val_y = random.uniform(-1.0, 1.0)
    elif ang == 1:
        ball_val_y = random.uniform(-1.0, 1.0)
    else:
        ball_val_y = random.uniform(-1.0, 1.0)

    # PADDLE
    paddle_width, paddle_height = 20, 120
    left_paddle_y = right_paddle_y = HEIGHT / 2 - paddle_height / 2
    left_paddle_x = 100 - paddle_width / 2
    right_paddle_x = WIDTH - 100 - paddle_width / 2
    wn.fill(BACKGROUND_COLOR)

    # Paddle velocities
    right_paddle_vel = left_paddle_vel = 1

    # Gadgets
    left_gadget = right_gadget = 0
    left_gadget_remaining = right_gadget_remaining = 5

    # Primary loop
    while run:
        wn.fill(BACKGROUND_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_DOWN]:
            right_paddle_y += right_paddle_vel
        if pressed[pygame.K_UP]:
            right_paddle_y -= right_paddle_vel
        if pressed[pygame.K_RIGHT] and right_gadget_remaining > 0:
            right_gadget = 1
        if pressed[pygame.K_LEFT] and right_gadget_remaining > 0:
            right_gadget = 2

        if pressed[pygame.K_w]:
            left_paddle_y -= left_paddle_vel
        if pressed[pygame.K_s]:
            left_paddle_y += left_paddle_vel
        if pressed[pygame.K_d] and left_gadget_remaining > 0:
            left_gadget = 1
        if pressed[pygame.K_a] and left_gadget_remaining > 0:
            left_gadget = 2

        # Paddle movement
        if right_paddle_y < 0:
            right_paddle_y = 0
        elif right_paddle_y > HEIGHT - paddle_height:
            right_paddle_y = HEIGHT - paddle_height

        if left_paddle_y < 0:
            left_paddle_y = 0
        elif left_paddle_y > HEIGHT - paddle_height:
            left_paddle_y = HEIGHT - paddle_height

        # Collisions
        # left
        if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
            if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                ball_x = left_paddle_x + paddle_width
                ball_val_x *= -1
        # right
        if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
            if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                ball_x = right_paddle_x
                ball_val_x *= -1

        # Gadgets action
        # left
        if left_gadget == 1:
            if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
                if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                    ball_x = left_paddle_x + paddle_width
                    ball_val_x *= -2
                    left_gadget = 0
                    left_gadget_remaining -= 1
        elif left_gadget == 2:
            left_paddle_y = ball_y
            left_gadget = 0
            left_gadget_remaining -= 1

        # right
        if right_gadget == 1:
            if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
                if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                    ball_x = right_paddle_x
                    ball_val_x *= -2
                    right_gadget = 0
                    right_gadget_remaining -= 1

        elif right_gadget == 2:
            right_paddle_y = ball_y
            right_gadget = 0
            right_gadget_remaining -= 1

        # Movements
        ball_x += ball_val_x
        ball_y += ball_val_y

        # Ball control
        if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
            ball_val_y *= -1
        if ball_x >= WIDTH - radius:
            player_1 += 1
            ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
            dir = random.choice(directions)
            ang = random.choice(angle)

            if dir == -1:
                ball_val_x = -1.5
            else:
                ball_val_x = 1.5

            if ang == 0:
                ball_val_y = random.uniform(-1.0, 1.0)
            elif ang == 1:
                ball_val_y = random.uniform(-1.0, 1.0)
            else:
                ball_val_y = random.uniform(-1.0, 1.0)

        if ball_x <= 0 + radius:
            player_2 += 1
            ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
            dir = random.choice(directions)
            ang = random.choice(angle)

            if dir == -1:
                ball_val_x = -1.5
            else:
                ball_val_x = 1.5

            if ang == 0:
                ball_val_y = random.uniform(-1.0, 1.0)
            elif ang == 1:
                ball_val_y = random.uniform(-1.0, 1.0)
            else:
                ball_val_y = random.uniform(-1.0, 1.0)

        # -----------------------------scoreboard------------------------------

        font = pygame.font.SysFont('callibri', 32)

        score_1 = font.render("Points: " + str(player_1), True, WHITE)
        wn.blit(score_1, (25, 25))

        score_2 = font.render("Points: " + str(player_2), True, WHITE)
        wn.blit(score_2, (825, 25))

        gad_left_1 = font.render("Powers Left: " + str(left_gadget_remaining), True, WHITE)
        wn.blit(gad_left_1, (25, 65))

        gad_left_2 = font.render("Powers Left: " + str(right_gadget_remaining), True, WHITE)
        wn.blit(gad_left_2, (825, 65))
        # ------------------------------------------------------------------------

        # Objects
        pygame.draw.circle(wn, VIOLET, (int(ball_x), int(ball_y)), radius)
        pygame.draw.rect(wn, LUSH_TEAL, pygame.Rect(int(left_paddle_x), int(left_paddle_y), paddle_width, paddle_height))
        pygame.draw.rect(wn, LUSH_TEAL, pygame.Rect(int(right_paddle_x), int(right_paddle_y), paddle_width, paddle_height))
        
        if left_gadget == 1:
            pygame.draw.circle(wn, WHITE, (left_paddle_x + 10, left_paddle_y + 10), 4)
        if right_gadget == 1:
            pygame.draw.circle(wn, WHITE, (right_paddle_x + 10, right_paddle_y + 10), 4)

        # Endscreen
        winning_font = pygame.font.SysFont('callibri', 100)

        if player_1 >= 5:
            wn.fill(BACKGROUND_COLOR)
            endscreen = winning_font.render("PLAYER 1 WON 🤾‍♀️", True, WHITE)
            wn.blit(endscreen, (200, 250))

        if player_2 >= 5:
            wn.fill(BACKGROUND_COLOR)
            endscreen = winning_font.render("PLAYER 2 WON 🏂", True, WHITE)
            wn.blit(endscreen, (200, 250))
            
        pygame.display.update()

def game3():
    tk = Tk()
    tk.title("Tic Tac Toe")

    pa = StringVar()
    playerb = StringVar()
    p1 = StringVar()
    p2 = StringVar()

    player1_name = Entry(tk, textvariable=p1, bd=5)
    player1_name.grid(row=1, column=1, columnspan=8)
    player2_name = Entry(tk, textvariable=p2, bd=5)
    player2_name.grid(row=2, column=1, columnspan=8)

    bclick = True
    flag = 0

    def disableButton():
        button1.configure(state=DISABLED)
        button2.configure(state=DISABLED)
        button3.configure(state=DISABLED)
        button4.configure(state=DISABLED)
        button5.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button7.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        button9.configure(state=DISABLED)



    def btnClick(buttons):
        global bclick, flag, player2_name, player1_name, player, pa
        if buttons["text"]  == " " and bclick == True:
            buttons["text"] = "X"
            bclick = False
            playerb = p2.get() + " Wins!"
            pa = p1.get() + " Wins!"
            checkForWin()
            flag += 1

        
        elif buttons["text"] == " " and bclick == False:
            buttons["text"]  = "O"
            bclick = True
            checkForWin()
            flag += 1
        else:
            tkinter.messagebox.showinfo("Tic Tac Toe", "Buttons alredy Clicked!")

    def checkForWin():
        if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or 
            button4['text'] =='X' and button5['text'] == 'X' and button6['text'] == 'X' or
            button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or 
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
            button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
            button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or 
            button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X'):
            disableButton()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

        elif(flag == 8):
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

        elif(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
            button4['text'] =='O' and button5['text'] == 'O' and button6['text'] == 'O' or
            button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
            button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
            button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
            button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
            button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
            button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or 
            button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O'):
            disableButton()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)        


    buttons = StringVar()

    label = Label( tk, text="Player 1:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
    label.grid(row=1, column=0)


    label = Label( tk, text="Player 2:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
    label.grid(row=2, column=0)

    button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button1))
    button1.grid(row=3, column=0)

    button2 = Button(tk, text=' ' , font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button2))
    button2.grid(row=3, column=1)

    button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button3))
    button3.grid(row=3, column=2)

    button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button4))
    button4.grid(row=4, column=0)

    button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button5))
    button5.grid(row=4, column=1)

    button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button6))
    button6.grid(row=4, column=2)

    button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button7))
    button7.grid(row=5, column=0)

    button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button8))
    button8.grid(row=5, column=1)

    button9 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button9))
    button9.grid(row=5, column=2)

    tk.mainloop()     

def game4():
    FPS = 32
    SCREENWIDTH = 289
    SCREENHEIGHT = 511
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    GROUNDY = SCREENHEIGHT * 0.8
    GAME_SPRITES = {}
    GAME_SOUNDS = {}
    PLAYER = 'gallery/sprites/bird.png'
    BACKGROUND = 'gallery/sprites/background.png'
    PIPE = 'gallery/sprites/pipe.png'

    def welcomeScreen():
        """
        Shows welcome images on the screen
        """

        playerx = int(SCREENWIDTH/5)
        playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
        messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
        messagey = int(SCREENHEIGHT*0.13)
        basex = 0
        while True:
            for event in pygame.event.get():
                # if user clicks on cross button, close the game
                if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                # If the user presses space or up key, start the game for them
                elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                    return
                else:
                    SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
                    SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))    
                    SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))    
                    SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
                    pygame.display.update()
                    FPSCLOCK.tick(FPS)

    def mainGame():
        score = 0
        playerx = int(SCREENWIDTH/5)
        playery = int(SCREENWIDTH/2)
        basex = 0

        # Create 2 pipes for blitting on the screen
        newPipe1 = getRandomPipe()
        newPipe2 = getRandomPipe()

        # my List of upper pipes
        upperPipes = [
            {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y']},
        ]
        # my List of lower pipes
        lowerPipes = [
            {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']},
        ]

        pipeVelX = -4

        playerVelY = -9
        playerMaxVelY = 10
        playerMinVelY = -8
        playerAccY = 1

        playerFlapAccv = -8 # velocity while flapping
        playerFlapped = False # It is true only when the bird is flapping


        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    if playery > 0:
                        playerVelY = playerFlapAccv
                        playerFlapped = True
                        GAME_SOUNDS['wing'].play()


            crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) # This function will return true if the player is crashed
            if crashTest:
                return     

            #check for score
            playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
            for pipe in upperPipes:
                pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
                if pipeMidPos<= playerMidPos < pipeMidPos +4:
                    score +=1
                    print(f"Your score is {score}") 
                    GAME_SOUNDS['point'].play()


            if playerVelY <playerMaxVelY and not playerFlapped:
                playerVelY += playerAccY

            if playerFlapped:
                playerFlapped = False            
            playerHeight = GAME_SPRITES['player'].get_height()
            playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

            # move pipes to the left
            for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
                upperPipe['x'] += pipeVelX
                lowerPipe['x'] += pipeVelX

            # Add a new pipe when the first is about to cross the leftmost part of the screen
            if 0<upperPipes[0]['x']<5:
                newpipe = getRandomPipe()
                upperPipes.append(newpipe[0])
                lowerPipes.append(newpipe[1])

            # if the pipe is out of the screen, remove it
            if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
                upperPipes.pop(0)
                lowerPipes.pop(0)
            
            # Lets blit our sprites now
            SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
                SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

            SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
            SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
            myDigits = [int(x) for x in list(str(score))]
            width = 0
            for digit in myDigits:
                width += GAME_SPRITES['numbers'][digit].get_width()
            Xoffset = (SCREENWIDTH - width)/2

            for digit in myDigits:
                SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
                Xoffset += GAME_SPRITES['numbers'][digit].get_width()
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def isCollide(playerx, playery, upperPipes, lowerPipes):
        if playery> GROUNDY - 25  or playery<0:
            GAME_SOUNDS['hit'].play()
            return True
        
        for pipe in upperPipes:
            pipeHeight = GAME_SPRITES['pipe'][0].get_height()
            if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
                GAME_SOUNDS['hit'].play()
                return True

        for pipe in lowerPipes:
            if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
                GAME_SOUNDS['hit'].play()
                return True

        return False

    def getRandomPipe():
        """
        Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
        """
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        offset = SCREENHEIGHT/3
        y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height()  - 1.2 *offset))
        pipeX = SCREENWIDTH + 10
        y1 = pipeHeight - y2 + offset
        pipe = [
            {'x': pipeX, 'y': -y1}, #upper Pipe
            {'x': pipeX, 'y': y2} #lower Pipe
        ]
        return pipe



    def inirun():
        while True:
            welcomeScreen() # Shows welcome screen to the user until he presses a button
            mainGame() # This is the main game function 
            


    if __name__ == "__main__":
            # This will be the main point from where our game will start
        pygame.init() # Initialize all pygame's modules
        FPSCLOCK = pygame.time.Clock()
        pygame.display.set_caption('Flappy Bird by CodeWithHarry')
        GAME_SPRITES['numbers'] = ( 
            pygame.image.load('gallery/sprites/0.png').convert_alpha(),
            pygame.image.load('gallery/sprites/1.png').convert_alpha(),
            pygame.image.load('gallery/sprites/2.png').convert_alpha(),
            pygame.image.load('gallery/sprites/3.png').convert_alpha(),
            pygame.image.load('gallery/sprites/4.png').convert_alpha(),
            pygame.image.load('gallery/sprites/5.png').convert_alpha(),
            pygame.image.load('gallery/sprites/6.png').convert_alpha(),
            pygame.image.load('gallery/sprites/7.png').convert_alpha(),
            pygame.image.load('gallery/sprites/8.png').convert_alpha(),
            pygame.image.load('gallery/sprites/9.png').convert_alpha(),
        )

        GAME_SPRITES['message'] =pygame.image.load('gallery/sprites/message.png').convert_alpha()
        GAME_SPRITES['base'] =pygame.image.load('gallery/sprites/base.png').convert_alpha()
        GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load( PIPE).convert_alpha(), 180), 
        pygame.image.load(PIPE).convert_alpha()
        )

        # Game sounds
        GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
        GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
        GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
        GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
        GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

        GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
        GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
        inirun()



pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

#BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3')
#BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')

HEALTH_FONT = pygame.font.SysFont('comicsans', 20)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 110, 80

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.jpg')), (WIDTH, HEIGHT))

SNAKEGAME_IMAGE = pygame.image.load(
    os.path.join('Assets', 'Snakegame.png'))
SNAKEGAME = pygame.transform.scale(
    SNAKEGAME_IMAGE, (190,55))

PINGPONG_IMAGE = pygame.image.load(
    os.path.join('Assets', 'Pingpong.png'))
PINGPONG = pygame.transform.scale(
    PINGPONG_IMAGE, (190,55))

TICTACTOE_IMAGE = pygame.image.load(
    os.path.join('Assets', 'Tictactoe.png'))
TICTAKTOE = pygame.transform.scale(
    TICTACTOE_IMAGE, (190,55))

HEAD_IMAGE = pygame.image.load(
    os.path.join('Assets', 'Heading.png'))
HEAD = pygame.transform.scale(
    HEAD_IMAGE, (900,500))

FLAP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'Flappybird.png'))
FLAP = pygame.transform.scale(
    FLAP_IMAGE, (190,55))


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0, 0))
    
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    
    WIN.blit(SNAKEGAME, (355,240))
    WIN.blit(PINGPONG, (355,300))
    WIN.blit(TICTAKTOE, (355,360))
    WIN.blit(HEAD, (0,-130))
    WIN.blit(FLAP, (355,420))
    
    
    
    
    

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:  # DOWN
        yellow.y += VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
        red.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    snake = pygame.Rect(355,240, 190,55)
    pipo = pygame.Rect(355,300, 190,55)
    ttt= pygame.Rect(355,360, 190,55)
    flap= pygame.Rect(355,420, 190,55)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    #BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    #BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                #BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                #BULLET_HIT_SOUND.play()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if snake.collidepoint(event.pos):
                        print("Sprite clicked!")
                        game1()
                    if pipo.collidepoint(event.pos):
                        print("game 2!!")
                        game2()
                    if ttt.collidepoint(event.pos):
                        print("game 3!!")
                        game3()
                    if flap.collidepoint(event.pos):
                        print("game 3!!")
                        game4()
                        

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets,
                    red_health, yellow_health)

    main()


if __name__ == "__main__":
    main()
