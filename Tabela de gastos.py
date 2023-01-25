import tkinter as tk
from openpyxl import Workbook

def save_expense():
    expense = expense_entry.get()
    category = category_entry.get()
    date = date_entry.get()


    #Def execel
    wb = Workbook()
    sheet = wb.active
    sheet.append([expense, category, date])
    wb.save("tab.xlsx")

root = tk.Tk()
root.title("Controle de Gastos")

expense_label = tk.Label(root, text="Gastos:")
expense_label.grid(row=0, column=0)

expense_entry = tk.Entry(root)
expense_entry.grid(row=0, column=1, padx= 10)

category_label = tk.Label(root, text="Descrição:")
category_label.grid(row=1, column=0)

category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1,padx=10, pady= 15)

date_label = tk.Label(root, text="Data:")
date_label.grid(row=2, column=0)

date_entry = tk.Entry(root)
date_entry.grid(row=2, column=1)

save_button = tk.Button(root, text="Pull", command=save_expense)
save_button.grid(row=3, column=1)

root.mainloop()
