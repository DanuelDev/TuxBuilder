# importações do python
import tkinter as tk
import math
import subprocess
from tkinter import messagebox
from services.catalog_loader import load_catalog

# Constantes
PKEXEC = "/usr/bin/pkexec"
APT = "/usr/bin/apt"

# Função de calculo de colunas e largura da janela
def calculate_columns(num_apps):
    """
    Calcula o número de colunas necessárias para exibir os checkbuttons
    """
    col_res = num_apps / 10
    
    return int(math.ceil(col_res))

def calculate_root_width(num_apps):
    """
    Calcula a largura da janela principal com base no número de colunas
    """
    columns = calculate_columns(num_apps)
    width = (columns * 150) + 50  # 150 pixels por coluna + margem
    
    return width

# Função de instalação
def install(vars_apps, APPS):
    """
    Função do botão de instalação dos aplicativos
    """
    selected_apps = [nome for nome, var in vars_apps.items() if var.get()]

    if not selected_apps:
        messagebox.showwarning("Aviso", "Nenhum aplicativo selecionado.")
        return
    comandos = [PKEXEC, APT, "install", "-y"] + [APPS[nome] for nome in selected_apps]
    try:
        subprocess.run(comandos, check=True)
        messagebox.showinfo("Sucesso", "Aplicativos instalados com sucesso!\n"
                            "Reinicie o sistema se necessário.\n"
                            "Confira o terminal para mais detalhes.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Falha na instalação: {e}")
    

# Interface
def create_category_view(catalog):
    """
    Função para criar a janela de seleção de aplicativos
    """
    
    # Função para importar o catálogo de aplicativos
    APPS = load_catalog(catalog)
    print(APPS)
    # Criação da janela principal
    root = tk.Tk()
    root.title("TuxBuilder")
    root.geometry(f"{calculate_root_width(len(APPS))}x600")

    ## Configuração do grid
    # configuração row
    root.rowconfigure(0, weight=2)
    for i in range(1, 10):
        root.rowconfigure(i, weight=2)
    # configuração col
    for i in range(calculate_columns(len(APPS))):
        root.columnconfigure(i, weight=2)

    tk.Label(root, text="Selecione os aplicativos:", font=("Arial", 11, "bold")).grid(row=0, columnspan=2, pady=10)

    vars_apps = {}

    # Criação dos checkbuttons
    index_col = 0
    index_row = 1
    for app in APPS:
        if index_row > 10:
            index_col += 1
            index_row = 1
        var = tk.BooleanVar()
        vars_apps[app] = var
        chk = tk.Checkbutton(root, text=app, variable=var)
        chk.grid(row=index_row, column=index_col, sticky="w", padx=20)
        index_row += 1

    # Botão de instalação
    button = tk.Button(
        root,
        text="Instalar",
        command=lambda: install(vars_apps, APPS),
        bg="#4CAF50",
        fg="white",
        width=15
    )
    button.grid(columnspan=2, pady=30)

    root.mainloop()