# template for "Stopwatch: The Game"
import simplegui

# define global variables

t = 0
disp = "0:00.0"
n_attempt = 0
total_attempt = 0
game = str(n_attempt)+"/"+str(total_attempt)


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    sec = int(t/10)%60
    mint = int(t/600)
    if sec>9:
        return str(mint)+":"+str(sec)+"."+str(t%10)
    else:
        return str(mint)+":0"+str(sec)+"."+str(t%10)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    timer.start()

def stop_button():
    if timer.is_running():
        timer.stop()
        global total_attempt, n_attempt, game
        total_attempt = total_attempt + 1
        if (t%10)==0:
            n_attempt = n_attempt + 1
        game = str(n_attempt)+"/"+str(total_attempt)

def reset_button():
    global t, n_attempt, total_attempt, disp, game
    timer.stop()
    n_attempt = 0
    total_attempt = 0
    t = 0
    disp = "0:00.0"
    game = str(n_attempt)+"/"+str(total_attempt)


# define event handler for timer with 0.1 sec interval

def update():
    global t, disp, game
    t = t+1
    disp = format(t)

# define draw handler
def draw(canvas):
    canvas.draw_text(disp, [50,80], 40, "White")
    canvas.draw_text(game, [160,20], 20, "Green")

# create frame
frame = simplegui.create_frame("Stop Watch", 200,150)

# register event handlers
timer = simplegui.create_timer(100,update)
frame.set_draw_handler(draw)
frame.add_button("Start",start_button,50)
frame.add_button("Stop",stop_button,50)
frame.add_button("Reset",reset_button,50)

# start frame
frame.start()
