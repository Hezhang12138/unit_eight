import tkinter

root = tkinter.Tk()

fahrenheit = tkinter.StringVar()

celsius = tkinter.StringVar()

label1 = tkinter.Label(root, text="degrees F:")
label1.grid(row=1, column=1)

label2 = tkinter.Entry(root, textvariable=fahrenheit)
label2.grid(row=1, column=2)

label3 = tkinter.Label(root, text="degrees C:")
label3.grid(row=2, column=1)

label4 = tkinter.Label(root, textvariable=celsius)
label4.grid(row=2, column=2)

root.mainloop()