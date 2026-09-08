from  tkinter import *
window =Tk()
window.title("my first gui program")
window.minsize(width=500,height=300)

#BUTTON
def button_clicked():
    print("i got clicked")
    new_text= input.get()
    my_label.config(text=new_text)

#Label

my_label=Label(text="I am a label",font=("Arial",24,"bold"))
my_label.pack()                                                           #dispalys what is written

my_label["text"]="new text"
my_label.config(text="New Text")

button=Button(text="click me",command=button_clicked)
button.pack()

#ENTRY

input= Entry(width=10)
print(input.get())
input.pack()






window.mainloop()