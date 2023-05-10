### Author:  CJ
### Date written: 5/10/2023
### Description:   The intention of this tKinter Python application is to create a tic tac toe game.


from tkinter import * #imports tkinter
from tkinter import messagebox
window = Tk()
window.title("Tic tac toe game") 


clicked = True
count = 0


def restart():
   global clicked, count, winner
   clicked = True
   count = 0
   winner = False
   
   b1.config(text= " ", bg= "SystemButtonFace")   
   b2.config(text= " ", bg= "SystemButtonFace")   
   b3.config(text= " ", bg= "SystemButtonFace")   
   b4.config(text= " ", bg= "SystemButtonFace")   
   b5.config(text= " ", bg= "SystemButtonFace")   
   b6.config(text= " ", bg= "SystemButtonFace")   
   b7.config(text= " ", bg= "SystemButtonFace")   
   b8.config(text= " ", bg= "SystemButtonFace")   
   b9.config(text= " ", bg= "SystemButtonFace")
   enable_buttons()


def disable_buttons():
   b1.config(state=DISABLED)
   b2.config(state=DISABLED)
   b3.config(state=DISABLED)
   b4.config(state=DISABLED)
   b5.config(state=DISABLED)
   b6.config(state=DISABLED)
   b7.config(state=DISABLED)
   b8.config(state=DISABLED)
   b9.config(state=DISABLED)

def enable_buttons():
   b1.config(state=NORMAL)
   b2.config(state=NORMAL)
   b3.config(state=NORMAL)
   b4.config(state=NORMAL)
   b5.config(state=NORMAL)
   b6.config(state=NORMAL)
   b7.config(state=NORMAL)
   b8.config(state=NORMAL)
   b9.config(state=NORMAL)

def check_win():
   global winner
   winner = False
   
   if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
      b1.config(bg="blue")
      b2.config(bg="blue")
      b3.config(bg="blue")
      winner = True
      messagebox.showinfo("Tic tac toe", "X is the winner!")
      disable_buttons()
      restart()

   elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
      b4.config(bg="blue")
      b5.config(bg="blue")
      b6.config(bg="blue")
      winner = True
      messagebox.showinfo("Tic tac toe", "X is the winner!")
      disable_buttons()
      restart()

   elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
      b7.config(bg="blue")
      b8.config(bg="blue")
      b9.config(bg="blue")
      winner = True
      messagebox.showinfo("Tic tac toe", "X is the winner!")
      disable_buttons()
      restart()

   elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
      b1.config(bg="blue")
      b4.config(bg="blue")
      b7.config(bg="blue")
      winner = True
      messagebox.showinfo("Tic tac toe", "X is the winner!")
      disable_buttons()
      restart()

   elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
      b2.config(bg="blue")
      b5.config(bg="blue")
      b8.config(bg="blue")
      winner = True
      messagebox.showinfo("Tic tac toe", "X is the winner!")
      disable_buttons()
      restart()

   elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
      b3.config(bg="blue")
      b6.config(bg="blue")
      b9.config(bg="blue")
      winner = True
      messagebox.showinfo("Tic tac toe", "X is the winner!")
      disable_buttons()
      restart()

   elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
      b1.config(bg="blue")
      b5.config(bg="blue")
      b9.config(bg="blue")
      winner = True
      messagebox.showinfo("Tic tac toe", "X is the winner!")
      disable_buttons()
      restart()

   elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
      b3.config(bg="blue")
      b5.config(bg="blue")
      b7.config(bg="blue")
      winner = True
      messagebox.showinfo("Tic tac toe", "X is the winner!")
      disable_buttons()
      restart()

   elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
      b1.config(bg="blue")
      b2.config(bg="blue")
      b3.config(bg="blue")
      winner = True
      messagebox.showinfo("Tic tac toe", "O is the winner!")
      disable_buttons()
      restart()

   elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
      b4.config(bg="blue")
      b5.config(bg="blue")
      b6.config(bg="blue")
      winner = True
      messagebox.showinfo("Tic tac toe", "O is the winner!")
      disable_buttons()
      restart()

   elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
      b7.config(bg="blue")
      b8.config(bg="blue")
      b9.config(bg="blue")
      winner = True
      messagebox.showinfo("Tic tac toe", "O is the winner!")
      disable_buttons()
      restart()
   
   elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
      b1.config(bg="blue")
      b4.config(bg="blue")
      b7.config(bg="blue")
      winner = True
      messagebox.showinfo("Tic tac toe", "O is the winner!")
      disable_buttons()
      restart()
   
   elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
      b2.config(bg="blue")
      b5.config(bg="blue")
      b8.config(bg="blue")
      winner = True
      messagebox.showinfo("Tic tac toe", "O is the winner!")
      disable_buttons()
      restart()
   
   elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
      b3.config(bg="blue")
      b6.config(bg="blue")
      b9.config(bg="blue")
      winner = True
      messagebox.showinfo("Tic tac toe", "O is the winner!")
      disable_buttons()
      restart()
   
   elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
      b1.config(bg="blue")
      b5.config(bg="blue")
      b9.config(bg="blue")
      winner = True
      messagebox.showinfo("Tic tac toe", "O is the winner!")
      disable_buttons()
      restart()
   
   elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
      b3.config(bg="blue")
      b5.config(bg="blue")
      b7.config(bg="blue")
      winner = True
      messagebox.showinfo("Tic tac toe", "O is the winner!")
      disable_buttons()
      restart()
   elif count == 9:
      winner = True
      messagebox.showinfo("Tic tac toe", "The result is a draw!")
      disable_buttons()
      restart()

def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
      b["text"] = "X"
      clicked = False
      count += 1
      check_win()
    elif b["text"] == " " and clicked == False:
      b["text"] = "O"
      clicked = True
      count += 1
      check_win()
    else:
      messagebox.showerror("Tic tac toe", "That box has already been chosen.\n Please choose another.")
      

b1= Button(window, text=" ", font= ("Arial", 20),height=3, width=6, command= lambda: b_click(b1))

b2= Button(window, text=" ", font= ("Arial", 20),height=3, width=6,command= lambda: b_click(b2))

b3= Button(window, text=" ", font= ("Arial", 20),height=3, width=6, command= lambda: b_click(b3))

b4= Button(window, text=" ", font= ("Arial", 20),height=3, width=6, command= lambda: b_click(b4))

b5= Button(window, text=" ", font= ("Arial", 20),height=3, width=6, command= lambda: b_click(b5))

b6= Button(window, text=" ", font= ("Arial", 20),height=3, width=6, command= lambda: b_click(b6))

b7= Button(window, text=" ", font= ("Arial", 20),height=3, width=6, command= lambda: b_click(b7))

b8= Button(window, text=" ", font= ("Arial", 20),height=3, width=6, command= lambda: b_click(b8))

b9= Button(window, text=" ", font= ("Arial", 20),height=3, width=6, command= lambda: b_click(b9))



b1.grid(row=0, column= 0)
b2.grid(row=0, column= 1)
b3.grid(row=0, column= 2)
b4.grid(row=1, column= 0)
b5.grid(row=1, column= 1)
b6.grid(row=1, column= 2)
b7.grid(row=2, column= 0)
b8.grid(row=2, column= 1)
b9.grid(row=2, column= 2)

   

window.mainloop() # main window loop