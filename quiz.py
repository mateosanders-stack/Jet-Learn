import pgzrun

TITLE="QUIZ MASTER"
WIDTH=970
HEIGHT=750

question=["Heat or thermal energy can be transferred in different ways. How is heat moved in a liquid?","Convection","Evaporation","Conduction","Radiation","1"]
question_count=0
question_index=0
time_left=10
questionfile="questions.txt"
score=0

marquee_box=Rect(0,0,880,80)
question_box=Rect(0,0,650,150)
timer_box=Rect(0,0,150,150)
a1box=Rect(0,0,300,150)
a2box=Rect(0,0,300,150)
a3box=Rect(0,0,300,150)
a4box=Rect(0,0,300,150)
skip_box=Rect(0,0,150,330)
boxes=[a1box,a2box,a3box,a4box]

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
a1box.move_ip(20,270)
a2box.move_ip(370,270)
a3box.move_ip(20,450)
a4box.move_ip(370,450)
skip_box.move_ip(700,270)

marquee_message=""

def draw():
  global marquee_message
  screen.clear()
  screen.fill(color="black")
  screen.draw.filled_rect(marquee_box,"black")
  screen.draw.filled_rect(question_box,"navy blue")
  screen.draw.filled_rect(timer_box,"navy blue")
  screen.draw.filled_rect(skip_box,"dark green")
  for box in boxes:
    screen.draw.filled_rect(box,"yellow")
  marquee_message="Welcome To Quiz Master..." + f" Q: {question_index} of {question_count}"
  screen.draw.textbox(marquee_message, marquee_box, color="white")
  screen.draw.textbox(str(time_left), timer_box, color="white", shadow=(0.5,0.5), scolor="dim grey")
  screen.draw.textbox("skip", skip_box, color="black", shadow=(0.5,0.5), scolor="dim grey")
  screen.draw.textbox(question[0], question_box, color="white", shadow=(0.5,0.5), scolor="dim grey")
  
  index=1
  for box in boxes:
    screen.draw.textbox(question[index], question_box, color="white" , shadow=(0.5,0.5), scolor="dim grey")
    index+=1

def move_marquee():
  marquee_box.x=marquee_box.x + 2
  if marquee_box.left > WIDTH:
    marquee_box.right=0

def update():
  move_marquee()

def read():
  global question_box, question_count, question
  openfile=open(questionfile,"r")
  for q in openfile:
    question.append(q)
    question_count+=1
    openfile.close()

def readnext():
  global question_index
  question_index+=1
  return question.pop().split

def correct():
   global question, time_left, score
   score+=1
   if question:
    readnext()
    time_left=10
   else:
    game_over()


def incorrect():
   


def skip_question():
   


def game_over():
  


def on_mouse_down(pos):
    index=1
    for box in boxes:
        if box.collidepoint(pos):
            if index is int(question[5]):
               correct()
            else:
               incorrect()
        index+=1
    if skip_box.collidepoint(pos):
       skip_question()


pgzrun.go()