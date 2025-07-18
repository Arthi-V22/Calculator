
import tkinter as tk
def calculate(operator):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operator == '+':
            result.set(num1 + num2)
        elif operator == '-':
            result.set(num1 - num2)
        elif operator == '*':
            result.set(num1 * num2)
        elif operator == '/':
            if num2 != 0:
                result.set(num1 / num2)
            else:
                result.set("Error: Div by 0")
    except ValueError:
        result.set("Invalid input")

window = tk.Tk()
window.title("Calculator App")

tk.Label(window, text="Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

tk.Label(window, text="Enter second number:").grid(row=1, column=0)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

result = tk.StringVar()
tk.Label(window, text="Result:").grid(row=2, column=0)
tk.Label(window, textvariable=result).grid(row=2, column=1)

tk.Button(window, text="+", width=5, command=lambda: calculate('+')).grid(row=3, column=0)
tk.Button(window, text="-", width=5, command=lambda: calculate('-')).grid(row=3, column=1)
tk.Button(window, text="*", width=5, command=lambda: calculate('*')).grid(row=4, column=0)
tk.Button(window, text="/", width=5, command=lambda: calculate('/')).grid(row=4, column=1)

window.mainloop()


