import tkinter as tk

def get_values():
    num1 = int(number_1_entry.get())
    num2 = int(number_2_entry.get())
    return num1, num2
def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)




window = tk.Tk()
window.title("Калькулятор")
window.geometry("350x350")
window.resizable(False, False)
window.configure(bg='grey20')
button_add = tk.Button(window, text="+",
                       width=2,
                       height=2,
                       command=add,
                       bg='orange',
                       fg="white",
                       font=("Arial", 12, "bold"))
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text="−",
                       width=2,
                       height=2,
                       command=sub,
                       bg='orange',
                       fg="white",
                       font=("Arial", 13, "bold"))
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text="x",
                       width=2,
                       height=2,
                       command=mul,
                       bg='orange',
                       fg="white",
                       font=("Arial", 12, "bold"))
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text="÷",
                       width=2,
                       height=2,
                       command=div,
                       bg='orange',
                       fg="white",
                       font=("Arial", 12, "bold"))
button_div.place(x=250, y=200)
number_1_entry = tk.Entry(window, width=30,bg='grey90')
number_1_entry.place(x=100, y=75)
number_2_entry = tk.Entry(window, width=30, bg='grey90')
number_2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=30, bg='grey90')
answer_entry.place(x=100, y=300)
number_1 = tk.Label(window, text="Введите первое число:",
                    bg="grey20",
                    fg="white",
                    font=("Arial", 11, "bold") )
number_1.place(x=100, y=50)
number_2 = tk.Label(window, text="Введите второе число:",
                    bg="grey20",
                    fg="white",
                    font=("Arial", 11, "bold"))
number_2.place(x=100, y=125)
answer = tk.Label(window, text="Ответ:",
                  bg='grey20',
                  fg="#FF6347",
                  font=("Arial", 12, "bold"))
answer.place(x=100, y=275)
window.mainloop()