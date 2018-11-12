import tkinter

root = tkinter.Tk()
root.title("Frank's Calculator")


label_calculator = tkinter.Label(root, text="Frank's calculator")
label_calculator.grid(row=1, column=1, columnspan=4)


def one():
    one = answer.get()
    answer.set(one + "1")


answer = tkinter.StringVar()

labelEntry = tkinter.Entry(root, textvariable=answer)
labelEntry.grid(row=2, column=1, columnspan=4)

label1 = tkinter.Button(root, text="1", command=one)
label1.grid(row=6, column=1)


label2 = tkinter.Button(root, text="2", )
label2.grid(row=6, column=2)

label3 = tkinter.Label(root, text="3")
label3.grid(row=6, column=3)

label4 = tkinter.Label(root, text="4")
label4.grid(row=5, column=1)

label5 = tkinter.Label(root, text="5")
label5.grid(row=5, column=2)

label6 = tkinter.Label(root, text="6")
label6.grid(row=5, column=3)

label7 = tkinter.Label(root, text="7")
label7.grid(row=4, column=1)

label8 = tkinter.Label(root, text="8")
label8.grid(row=4, column=2)

label9 = tkinter.Label(root, text="9")
label9.grid(row=4, column=3)

label0 = tkinter.Label(root, text="0")
label0.grid(row=7, column=1, columnspan=2)

label_clear = tkinter.Label(root, text="C")
label_clear.grid(row=3, column=1)

label_equal = tkinter.Label(root, text="=")
label_equal.grid(row=3, column=2)

label_divide = tkinter.Label(root, text="/")
label_divide.grid(row=3, column=3)

label_multiply = tkinter.Label(root, text="*")
label_multiply.grid(row=3, column=4)

label_minus = tkinter.Label(root, text="-")
label_minus.grid(row=4, column=4)

label_plus = tkinter.Label(root, text="+")
label_plus.grid(row=5, column=4)

label_enter = tkinter.Label(root, text="enter")
label_enter.grid(row=6, rowspan=2, column=4)

label_point = tkinter.Label(root, text=".")
label_point.grid(row=7, column=3)

root.mainloop()