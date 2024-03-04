import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime


class Tabeladegastos:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabela de Gastos | Developer | Cássio Estevão")

        self.label_numero = tk.Label(root, text="Descrição do produto :",padx=10,pady=10)
        self.label_numero.pack()
        self.entry_numero = tk.Entry(root)
        self.entry_numero.pack()

        self.label_data = tk.Label(root, text="Data da de compra do produto (dd/mm/aaaa):",padx=10,pady=10)
        self.label_data.pack()
        self.entry_data = tk.Entry(root)
        self.entry_data.pack()

        self.label_valor = tk.Label(root, text="Valor do produto:",padx=10,pady=10)
        self.label_valor.pack()
        self.entry_valor = tk.Entry(root)
        self.entry_valor.pack()

        self.button_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar,padx=10,pady=10)
        self.button_cadastrar.pack()

    def cadastrar(self):
        numero = self.entry_numero.get()
        data = self.entry_data.get()
        valor = self.entry_valor.get()

        if not numero or not data or not valor:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        try:
            datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Erro", "Formato de data inválido. Use dd/mm/aaaa.")
            return

        try:
            valor = float(valor)
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido. Use somente números.")
            return

        with open('Tabela de Gastos.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([numero, data, valor])
        
        messagebox.showinfo("Sucesso", "produto cadastrado com sucesso.")

    def visualizar(self):
        numero = self.entry_numero.get()
        data = self.entry_data.get()
        valor = self.entry_valor.get()

root = tk.Tk()
app = Tabeladegastos(root)
root.mainloop()
