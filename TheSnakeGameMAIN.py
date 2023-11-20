from turtle import *
import time 
import random
import winsound


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
