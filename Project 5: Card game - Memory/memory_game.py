# implementation of card game - Memory

import simplegui
import random
list1 = range(8)
list2 = range(8)
disp_list = []
pos_num = [10,70]
my_dict = {}
rect_pos = [25,0]
state = 0
moves = 0
comp = [0,0,0]
exposed=[]
pair = 0

# helper function to initialize globals
def init():
    global disp_list, list1, list2, my_dict, state, exposed, moves
    pos_num = [10,70]
    pair = 0
    rect_pos = [25,0]
    state = 0
    moves = 0
    comp = [0,0,0]
    disp_list = list1 + list2
    random.shuffle(disp_list)
    for n in range(16):
        my_dict[n]=disp_list[n]
    state = 0
    exposed = my_dict.keys()
    label.set_text("Moves = " + str(moves))

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global moves, comp, my_dict, pair
    x_ind = pos[0]//50
    global state
    if state == 0:
        comp[0]=x_ind
        if comp[0] in exposed:
            state = 1
            exposed.remove(comp[0])
    elif state == 2:
        comp[0]=x_ind
        if comp[0] in exposed:
            state = 1
            moves = moves+1
            exposed.remove(comp[0])
            label.set_text("Moves = " + str(moves))
            if pair==0:
                exposed.extend([comp[1],comp[2]])
    elif state == 1:
        comp[2]=x_ind
        if comp[2] in exposed:
            state = 2
            comp[1]=comp[0]
            exposed.remove(comp[2])
        if my_dict[comp[1]] == my_dict[comp[2]]:
            pair = 1
        else:
            pair = 0

# cards are logically 50x100 pixels in size
def draw(canvas):
    for key, value in my_dict.items():
        num = str(value)
        canvas.draw_text(num,(pos_num[0]+(key*50),pos_num[1]),60,"White")
    for i in exposed:
        canvas.draw_line((rect_pos[0]+(i*50), 0), (rect_pos[0]+(i*50), 100), 48, "Green")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
