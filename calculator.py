import tkinter as tk
import math

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        # Create the display
        self.display = tk.Entry(master, width=20, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=6, padx=5, pady=5)
        
        # Create the buttons
        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('/', 1, 3)
        self.create_button('^', 1, 4)
        self.create_button('sin', 1, 5)
        
        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('*', 2, 3)
        self.create_button('(', 2, 4)
        self.create_button('cos', 2, 5)
        
        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('-', 3, 3)
        self.create_button(')', 3, 4)
        self.create_button('tan', 3, 5)
        
        self.create_button('0', 4, 0)
        self.create_button('.', 4, 1)
        self.create_button('=', 4, 2)
        self.create_button('+', 4, 3)
        self.create_button('C', 4, 4)
        self.create_button('pi', 4, 5)
        
    def create_button(self, text, row, col):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 16), command=lambda: self.button_click(text))
        button.grid(row=row, column=col, padx=5, pady=5)
        
    def button_click(self, text):
        if text == '=':
            try:
                expression = self.display.get()
                expression = expression.replace('sin', 'math.sin')
                expression = expression.replace('cos', 'math.cos')
                expression = expression.replace('tan', 'math.tan')
                expression = expression.replace('^', '**')
                expression = expression.replace('pi', str(math.pi))
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Error')
                raise
        elif text == 'C':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, text)

root = tk.Tk()
calculator = CalculatorGUI(root)
root.mainloop()