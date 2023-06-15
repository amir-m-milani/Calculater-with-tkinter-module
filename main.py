import tkinter
import math
# window
calculater = tkinter.Tk()
calculater.title("Calculater")
calculater.geometry("250x300")

# functions


def appendInFile(text: str):
    with open("history.txt", "a", encoding="utf8") as history:
        history.write(f"{text}\n")


def show_num(num):
    message = textBox.get()
    textBox.delete(0, tkinter.END)
    message += str(num)
    textBox.insert(0, message)


def clear_num():
    textBox.delete(0, tkinter.END)
    number1 = 0


def equal():
    if textBox.get().isdigit():
        number2 = float(textBox.get())
        # insert choice & number2 to history
        appendInFile(f"{choice}{number2}")

    textBox.delete(0, tkinter.END)
    match choice:
        case "+":
            test = number1 + number2
            textBox.insert(0, str(test))
            appendInFile(f"={test}")
        case "-":
            test = number1 - number2
            textBox.insert(0, str(test))
            appendInFile(f"={test}")
        case "/":
            try:
                number1 / number2
            except ZeroDivisionError:
                textBox.insert(0, "Can not Divide by ZERO!")
            else:
                test = number1/number2
                textBox.insert(0, str(test))
                appendInFile(f"={test}")
        case "x":
            test = number1 * number2
            textBox.insert(0, str(test))
            appendInFile(f"={test}")
        case "P":
            test = number1 ** number2
            textBox.insert(0, str(test))
            appendInFile(f"={test}")
        case "F":
            test = math.factorial(int(number1))
            textBox.insert(0, str(test))
            appendInFile(f"={test}")
        case "R":
            test = math.sqrt(number1)
            textBox.insert(0, str(test))
            appendInFile(f"={test}")


def opperation(ch):
    global number1
    global choice
    choice = ch
    number1 = float(textBox.get())
    appendInFile(textBox.get())  # insert number 1 to history
    textBox.delete(0, tkinter.END)
    match choice:
        case "F":
            textBox.insert(0, f"({number1})!")
            # insert this in history
            appendInFile(f"({number1})!")
            # appendInFile("({:.0f})!".format(number1))

        case "R":
            textBox.insert(0, f"Radikal({number1})")
            appendInFile(f"Radikal({number1})")  # insert this in history


# textBox
textBox = tkinter.Entry(calculater, width="30", background="gray")
# textBox.Grid
textBox.grid(row="0", column="0", columnspan="3")
# Buttons
btn0 = tkinter.Button(calculater, text="0", padx=23,
                      pady=10, command=lambda: show_num(0))
btn1 = tkinter.Button(calculater, text="1", padx=23,
                      pady=10, command=lambda: show_num(1))
btn2 = tkinter.Button(calculater, text="2", padx=23,
                      pady=10, command=lambda: show_num(2))
btn3 = tkinter.Button(calculater, text="3", padx=23,
                      pady=10, command=lambda: show_num(3))
btn4 = tkinter.Button(calculater, text="4", padx=23,
                      pady=10, command=lambda: show_num(4))
btn5 = tkinter.Button(calculater, text="5", padx=23,
                      pady=10, command=lambda: show_num(5))
btn6 = tkinter.Button(calculater, text="6", padx=23,
                      pady=10, command=lambda: show_num(6))
btn7 = tkinter.Button(calculater, text="7", padx=23,
                      pady=10, command=lambda: show_num(7))
btn8 = tkinter.Button(calculater, text="8", padx=23,
                      pady=10, command=lambda: show_num(8))
btn9 = tkinter.Button(calculater, text="9", padx=23,
                      pady=10, command=lambda: show_num(9))
btn_add = tkinter.Button(calculater, text="+", padx=45,
                         pady=10, command=lambda: opperation("+"))
btn_minus = tkinter.Button(
    calculater, text="-", padx=23, pady=10, command=lambda: opperation("-"))
btn_multiple = tkinter.Button(
    calculater, text="x", padx=23, pady=10, command=lambda: opperation("x"))
btn_taghsim = tkinter.Button(
    calculater, text="/", padx=15, pady=10, command=lambda: opperation("/"))
btn_equal = tkinter.Button(
    calculater, text="=", padx=15, pady=100, command=equal)
btn_clear = tkinter.Button(calculater, text="clear",
                           padx=10, pady=5, command=clear_num)
btn_power = tkinter.Button(calculater, text="()^n",
                           padx=13, pady=5, command=lambda: opperation("P"))
btn_radikal = tkinter.Button(
    calculater, text="(n)^-1/2", padx=13, pady=5, command=lambda: opperation("R"))
btn_factorial = tkinter.Button(
    calculater, text="n!", padx=13, pady=5, command=lambda: opperation("F"))
# Buttons.Grid
btn0.grid(row="4", column="0")
btn1.grid(row="3", column="0")
btn2.grid(row="3", column="1")
btn3.grid(row="3", column="2")
btn4.grid(row="2", column="0")
btn5.grid(row="2", column="1")
btn6.grid(row="2", column="2")
btn7.grid(row="1", column="0")
btn8.grid(row="1", column="1")
btn9.grid(row="1", column="2")
btn_add.grid(row="4", column="1", columnspan="2")
btn_minus.grid(row="5", column="0")
btn_multiple.grid(row="5", column="1")
btn_taghsim.grid(row="5", column="2")
btn_equal.grid(row="1", column="3", rowspan="5")
btn_clear.grid(row="0", column="3")
btn_power.grid(row="6", column="0")
btn_radikal.grid(row="6", column="1")
btn_factorial.grid(row="6", column="2")

calculater.mainloop()
