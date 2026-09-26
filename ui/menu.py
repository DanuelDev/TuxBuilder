#importações do python
import tkinter as tk
from tkinter import messagebox

# Importações tuxbuilder
from system.dependencies import check_system
from ui.category_view import create_category_view

# cria a janela principal
def create_menu():
    # Verifica se o sistema é compatível
    erro = check_system()
    if erro:
        messagebox.showerror("ERRO FATAL!", erro)
        exit()
        
    root = tk.Tk()
    root.title("TuxBuilder")
    root.geometry("400x300")

    for i in range(0, 4):
        root.rowconfigure(i, weight=2)

    root.columnconfigure(0, weight=2)

    button_web = tk.Button(root, text="Web", command=lambda: create_category_view("data/web.json")).grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
    button_programacao = tk.Button(root, text="Programação", command=lambda: create_category_view("data/development.json")).grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
    button_office = tk.Button(root, text="Escritório", command=lambda: create_category_view("data/office.json")).grid(row=2, column=0, sticky="nsew", padx=20, pady=20)
    button_multimidia = tk.Button(root, text="Multimídia", command=lambda: create_category_view("data/multimedia.json")).grid(row=3, column=0, sticky="nsew", padx=20, pady=20)


    root.mainloop()