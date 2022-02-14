from tkinter import *

# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=250)
window.config(padx=20, pady=20)

# Labels
label_1 = Label(text="is equal to")
label_1.grid(column=0, row=1)
label_1.config(padx=20, pady=20)

label_2 = Label(text="Miles")
label_2.grid(column=2, row=0)
label_2.config(padx=20, pady=20)

label_3 = Label(text="Km")
label_3.grid(column=2, row=1)
label_3.config(padx=20, pady=20)

label_result = Label(text="0")
label_result.grid(column=1, row=1)
label_result.config(padx=20, pady=20)


# Entry
input = Entry(width=10)
input.grid(column=1, row=0)



# Button
def on_click():
    miles=input.get()
    km = int(miles)*1.6
    label_result.config(text=km)

button = Button(text="Calculate", command=on_click)
button.grid(row=2, column=1)
button.config(padx=20, pady=20)

mainloop()
