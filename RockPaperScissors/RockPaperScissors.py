
import random
import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("Rock Paper Scissors Game")

user_score = 0
comp_score = 0
user_choice = ""
comp_choice = ""

def choice_to_num(choice):
    rps = {'rock':0,'paper':1,'scissor':2}
    return rps[choice]
def num_to_choice(number):
    rps = {0:'rock',1:'paper',2:'scissor'}
    return rps[number]
def random_choice():
    return random.choice(['rock','paper','scissor']) 
def result(human_choice,comp_choice):
    global user_score
    global comp_score
    user = choice_to_num(human_choice)
    comp = choice_to_num(comp_choice)
    if(user == comp):
        print("Tie")
    elif((user-comp) % 3 == 1):
        print("You Win")
        user_score+=1
    else:
        print("Comp Wins")
        comp_score+=1
    text_area = tk.Text(master=window,height = 12,width = 30,bg = "#FFFF99")
    text_area.grid(column=0,row=4)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=human_choice,cc=comp_choice,u=user_score,c=comp_score)    
    text_area.insert(tk.END,answer)
def rock():
    global user_choice
    global comp_choice
    user_choice='rock'
    comp_choice=random_choice()
    result(user_choice,comp_choice)
def paper():
    global user_choice
    global comp_choice
    user_choice='paper'
    comp_choice=random_choice()
    result(user_choice,comp_choice)
def scissor():
    global user_choice
    global comp_choice
    user_choice='scissor'
    comp_choice=random_choice() 
    result(user_choice,comp_choice)

button1 = tk.Button(text="       Rock       ",bg="skyblue",command=rock)
button1.grid(column=0,row=1)
button2 = tk.Button(text="       Paper      ",bg="pink",command=paper)
button2.grid(column=0,row=2)
button3 = tk.Button(text="      Scissor     ",bg="lightgreen",command=scissor)
button3.grid(column=0,row=3)

window.mainloop()