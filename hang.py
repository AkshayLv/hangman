from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox as mb
import random
from PIL import Image, ImageTk
import webbrowser

# word selection
words = open("hangwords.txt", 'r')
word_list =[x for x in words.read().split("\n") if 3<len(x)<14 and x.isalpha()]
question = random.choice(word_list).upper()
ques_disp = "_ "*len(question)
p = ques_disp.split()

#input pos in word
def find_char(word: str, xletter: str):
    x = word.count(xletter)
    t = word.find(xletter)
    loc_arr = [t]
    while len(loc_arr) < x:
        t2 = word.find(xletter, t+1)
        t = t2
        loc_arr.append(t2)
    
    return loc_arr
    

#mistake count
fail = 0

#letter input fn
def letter_clk(alpha):
    exec('but_'+alpha+'.config(bg = "#ff0000", state = DISABLED)')
    x = find_char(question, alpha)
    global fail
    if x[0] != -1:
        for i in x:
            p[i] = alpha
    else:
        fail+=1
        if fail<7:
            exec('piclbl = Label(root, image=pic_shw'+str(fail)+')')
            exec('piclbl.place(x=450, y=120)')
        else:
            piclal = Label(root, image=pic_shw8)
            piclal.place(x=450, y=120)
            mb.showinfo("Defeat","You have lost. The word was "+question)
            for i in range(65,91):
                exec('but_'+chr(i)+'.config(state = DISABLED)')
    ques.config(text=" ".join(p))

    if not '_' in p:
        piclov = Label(root, image=pic_shw9)
        piclov.place(x=450, y=120)
        mb.showinfo("Victory", "You have found the word!")
        for i in range(65,91):
                exec('but_'+chr(i)+'.config(state = DISABLED)')

#restart game fn
def reset():
    global question
    global ques_disp
    global p
    question = random.choice(word_list).upper()
    piclabel = Label(root, image=pic_shw0)
    piclabel.place(x=450, y=120)
    global fail
    fail = 0
    ques_disp = "_ "*len(question)
    p = ques_disp.split()
    ques.config(text=ques_disp)
    for i in range(65,91):
        exec('but_'+chr(i)+'.config(state = NORMAL, bg = letter_bg)')

def instr():
    mb.showinfo("Instructions", "Find the hidden word to save the Dude from gallows. Mistakes lead to Death!")

#window
root = Tk()
root.title("Hangman")
root.geometry("700x600+450+150")
root.resizable(False, False)
root.configure(bg="light gray")
root.iconbitmap("icon2.ico")

#heading
head = Label(root, text="HANGMAN")
head_fnt = ("Calibri", 40, "bold",)
head.configure(font=head_fnt, fg = "dark red", bg="light gray")
head.place(x= 230, y = 30)

#input, image canvas
can = Canvas(root, highlightbackground="black", bg="gold", width=600, height=280, bd = 5)
can.place(x=50, y=100)

#pic border
picframe = Frame(root, bg="black", width=203, height=258)
picframe.place(x=448, y=118)

#Question Word
ques = Label(root, text = ques_disp)
ques_fnt = ("Comic Sans MS", 20)
ques.configure(font=ques_fnt, fg="white", bg="black")
ques.place(x = 80, y = 180)

#picture display
letter_width = 5
letter_height = 1
letter_bg = "green"
letter_fg = "white"

for i in range(0,10):
    exec('pic = Image.open("hangpics/hang'+str(i)+'.png")')
    pic_resize = pic.resize((195,250), Image.ANTIALIAS)
    exec('pic_shw'+str(i)+' = ImageTk.PhotoImage(pic_resize)')

piclabel = Label(root, image=pic_shw0)
piclabel.place(x=450, y=120)

#letter btn display
for i,j in zip(range(65,78), range(30,631,50)):
    exec('but_'+chr(i)+' = Button(root, text="'+chr(i)+'", width=letter_width, height=letter_height, bg = letter_bg, fg = letter_fg, command=lambda: letter_clk("'+chr(i)+'"))')
    exec('but_'+chr(i)+'.place(x='+str(j)+', y=420)')
for i,j in zip(range(78,91), range(30,631,50)):
    exec('but_'+chr(i)+' = Button(root, text="'+chr(i)+'", width=letter_width, height=letter_height, bg = letter_bg, fg = letter_fg, command=lambda: letter_clk("'+chr(i)+'"))')
    exec('but_'+chr(i)+'.place(x='+str(j)+', y=460)')

#reset display
res = Button(root, text="New Game", width = 25, height = 2, bd = 3, bg="brown", fg="white", command=lambda: reset())
res.place(x=490, y=530)

#git
git = Button(root, text="GIT", bg="blue", fg="white", width = 8, height = 2, bd = 3, command=lambda: webbrowser.open("https://github.com/AkshayLv", new=2))
git.place(x=620,y=10)

#instruction
inst = Button(root, text="Instructions", width = 12, height = 2, bd = 3, command=lambda: instr())
inst.place(x=30, y=530)

root.mainloop()