# Frank Zhang
# November 14th last edit
# I finally make my calculator work by using a special function to "equal" which is "eval", and I finish my calculator.


import tkinter

root = tkinter.Tk()
root.title("Frank's Calculator")


label_calculator = tkinter.Label(root, text="Frank's calculator")
label_calculator.grid(row=1, column=1, columnspan=4)


answer = tkinter.StringVar()


def one():
    one = answer.get()
    answer.set(one + "1")


def two():
    two = answer.get()
    answer.set(two + "2")


def three():
    three = answer.get()
    answer.set(three + "3")


def four():
    four = answer.get()
    answer.set(four + "4")


def five():
    five = answer.get()
    answer.set(five + "5")


def six():
    six = answer.get()
    answer.set(six + "6")


def seven():
    seven = answer.get()
    answer.set(seven + "7")


def eight():
    eight = answer.get()
    answer.set(eight + "8")


def nine():
    nine = answer.get()
    answer.set(nine + "9")


def zero():
    zero = answer.get()
    answer.set(zero + "0")


def clear():
    answer.set("")


def equal():
    equal = answer.get()
    answer.set(eval(equal))


def divide():
    divide = answer.get()
    answer.set(divide + "/")


def multiply():
    multiply = answer.get()
    answer.set(multiply + "*")


def minus():
    minus = answer.get()
    answer.set(minus + "-")


def plus():
    plus = answer.get()
    answer.set(plus + "+")


def enter():
    enter = answer.get()
    answer.set(eval(enter))


def point():
    point = answer.get()
    answer.set(point + ".")


labelEntry = tkinter.Entry(root, textvariable=answer)
labelEntry.grid(row=2, column=1, columnspan=4)

label1 = tkinter.Button(root, text="   1   ", command=one)
label1.grid(row=6, column=1)


label2 = tkinter.Button(root, text="   2   ", command=two)
label2.grid(row=6, column=2)

label3 = tkinter.Button(root, text="   3   ", command=three)
label3.grid(row=6, column=3)

label4 = tkinter.Button(root, text="   4   ", command=four)
label4.grid(row=5, column=1)

label5 = tkinter.Button(root, text="   5   ", command=five)
label5.grid(row=5, column=2)

label6 = tkinter.Button(root, text="   6   ", command=six)
label6.grid(row=5, column=3)

label7 = tkinter.Button(root, text="   7   ", command=seven)
label7.grid(row=4, column=1)

label8 = tkinter.Button(root, text="   8   ", command=eight)
label8.grid(row=4, column=2)

label9 = tkinter.Button(root, text="   9   ", command=nine)
label9.grid(row=4, column=3)

label0 = tkinter.Button(root, text="       0       ", command=zero)
label0.grid(row=7, column=1, columnspan=2)

label_clear = tkinter.Button(root, text="   C   ", command=clear)
label_clear.grid(row=3, column=1)

label_equal = tkinter.Button(root, text="   =   ", command=equal)
label_equal.grid(row=3, column=2)

label_divide = tkinter.Button(root, text="   /   ", command=divide)
label_divide.grid(row=3, column=3)

label_multiply = tkinter.Button(root, text="   *   ", command=multiply)
label_multiply.grid(row=3, column=4)

label_minus = tkinter.Button(root, text="   -   ", command=minus)
label_minus.grid(row=4, column=4)

label_plus = tkinter.Button(root, text="   +   ", command=plus)
label_plus.grid(row=5, column=4)

label_enter = tkinter.Button(root, text="enter", command=enter)
label_enter.grid(row=6, rowspan=2, column=4)

label_point = tkinter.Button(root, text="   .   ", command=point)
label_point.grid(row=7, column=3)

root.mainloop()