import tkinter

root = tkinter.Tk()
root.title("Temperature Converter")


def f_to_c():
    f_value = int(fahrenheit.get())
    c_value = 5/9 * (f_value - 32)
    celsius.set(str(c_value))


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


convert_button = tkinter.Button(root, text="Convert", command=f_to_c)
convert_button.grid(row=3, column=1)


root.mainloop()