import tkinter as tk
from tkinter import messagebox
import subprocess
import json
import os
import sys
import math

root = tk.Tk()

# Verificação do sistema operacional
if not os.path.exists("/etc/debian_version"):
    messagebox.showerror("ERRO FATAL!", "Este programa é destinado a sistemas baseados em Debian/Ubuntu."
                         "Por favor, verifique seu sistema operacional e tente novamente.")
    root.destroy()
    sys.exit()

if not os.path.exists("/usr/bin/pkexec"):
    messagebox.showerror("ERRO FATAL!", "O 'pkexec' não foi encontrado no sistema.\n"
                         "Por favor, instale o 'policykit-1' com o seguinte comando no terminal:\n"
                         "sudo apt install -y policykit-1")
    root.destroy()
    sys.exit()

if not os.path.exists("apps.json"):
    messagebox.showerror("ERRO FATAL!", "O arquivo 'apps.json' não foi encontrado.\n"
                         "Certifique-se de que ele está no mesmo diretório que este programa.")
    root.destroy()
    sys.exit()

# Lista de aplicativos a partir do arquivo JSON
with open("apps.json", "r") as file:
    APPS = json.load(file)

PKEXEC = "/usr/bin/pkexec"
APT = "/usr/bin/apt"

# Função de instalação
def install():
    """
    Função do botão de instalação dos aplicativos
    """
    selected_apps = [nome for nome, var in vars_apps.items() if var.get()]
    if not selected_apps:
        messagebox.showwarning("Aviso", "Nenhum aplicativo selecionado.")
        return
    comandos = [PKEXEC, APT, "install", "-y"] + [APPS[nome] for nome in selected_apps]
    try:
        button['state'] = tk.DISABLED
        subprocess.run(comandos, check=True)
        messagebox.showinfo("Sucesso", "Aplicativos instalados com sucesso!\n"
                            "Reinicie o sistema se necessário.\n"
                            "Confira o terminal para mais detalhes.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Falha na instalação: {e}")
    
    button['state'] = tk.NORMAL

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

# Interface
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
    command=install,
    bg="#4CAF50",
    fg="white",
    width=15
)
button.grid(columnspan=2, pady=30)

# Aviso inicial
messagebox.showwarning("ATENÇÃO!", "Antes de prosseguir, certifique-se de rodar o seguinte comando no terminal:\n"
                       "\nsudo apt update && sudo apt upgrade")

root.mainloop()
