from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Temperature Convertor")
root.geometry("900x500+50+50")
t = ("Century" , 40 , "bold" , "italic")
f = ("Arial" , 20 , "bold" , "italic")

labTitle = Label(root , text = "Temperature Convertor" , font = t)
labTitle.pack(pady = 50)

labCel = Label(root , text = "Enter Temperature in Celsius : " , font = f)
labCel.place(x = 50 , y = 200)

entCel = Entry(root , font = f)
entCel.place(x = 500 , y = 200)

def show():
	cel = entCel.get()

	if (len(entCel.get()) == 0) :
		showerror("Issue" , "You did not enter Celsius amount")
		entCel.focus()
		return
	
	if cel.isalpha():
		showerror("issue" , "Celsius amount cannot be text")
		entCel.delete(0 , END)
		entCel.focus()
		return

	if cel.isspace():
		showerror("issue" , "Celsius amount cannot be spaces")
		entCel.delete(0 , END)
		entCel.focus()
		return
	
	try:
		cel = float(entCel.get())
		if (cel >= 0) and (cel <= 100):
			fah = (cel * 9 / 5) + 32
			msg = round(fah , 2)
			labAns.configure(text = msg)
			entCel.delete(0,END)
			entCel.focus()
		else :
			showerror("issue" ,"Enter Temperature in range 0 to 100 only")
			entCel.delete(0 , END)
			entCel.focus()

	except ValueError :
		showerror("issue" ,"Celsius amount cannot be special character")
		entCel.delete(0 , END)
		entCel.focus()

	

btn = Button(root , text = "Convert" , font = f , command = show)
btn.place(x = 500 , y = 300)

labAns = Label(root , font = f)
labAns.place(x = 250 , y = 400)


def confirmExit():
	if askyesno('Exit' , 'Do you want to exit?'):
		root.destroy()

root.protocol('WM_DELETE_WINDOW' , confirmExit) 
root.mainloop()






















