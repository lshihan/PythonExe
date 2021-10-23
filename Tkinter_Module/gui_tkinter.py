from tkinter import *

window = Tk()
window.title("My First GUI Programs")
window.minsize(width=500,height=300)

# Label
my_label = Label(text="I am a label",font=("Arial",24,))
my_label.pack() # can choose side with side and expand method
my_label["text"] = "New Text" # This line and below line do the same work
my_label.config(text="New Text")

# Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command = button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()




window.mainloop()