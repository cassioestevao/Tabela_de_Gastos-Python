import tkinter as tk
from tkinter import messagebox
import pandas as pd
from openpyxl import Workbook
#...

root = tk.Tk()
root.title("Gastos")

valor_label = tk.Label(root, text="Valor:")
valor_label.grid(row=0, column=0)
valor_entry = tk.Entry(root)
valor_entry.grid(row=0, column=1, padx=10)

descricao_label = tk.Label(root, text="Descrição:")
descricao_label.grid(row=1, column=0, padx= 10)
descricao_entry = tk.Entry(root)
descricao_entry.grid(row=1, column=1)

data_label = tk.Label(root, text="Data:")
data_label.grid(row=2, column=0)
data_entry = tk.Entry(root)
data_entry.grid(row=2, column=1)

teste_label = tk.Label(root, text="Teste:")
teste_label.grid(row=3, column=0)
teste_entry = tk.Entry(root)
teste_entry.grid(row=3, column=1)

def salvar():
    valor = valor_entry.get()
    descricao = descricao_entry.get()
    data = data_entry.get()
    arquivo = teste_entry.get()
    final = f"{arquivo}.txt"
    
    # adiciona os dados à lista de gastos
    wb = Workbook()
    momentum = wb.active
    momentum.append([valor, descricao, data])
    wb.save(final)
    messagebox.showinfo("Gastos", "Gasto adicionado com sucesso!")

    #Def execel

salvar_button = tk.Button(root, text="Salvar", command=salvar)
salvar_button.grid(row=4, column=1)


root.mainloop()