import tkinter as tk
from tkinter import messagebox
import subprocess
import json
import os

# Lista de aplicativos a partir do arquivo JSON
with open("apps.json", "r") as file:
    APPS = json.load(file)

# Aviso inicial
messagebox.showwarning("ATENÇÃO!", "Antes de prosseguir, certifique-se de rodar o seguinte comando no terminal:\n"
                       "\nsudo apt update && sudo apt upgrade")

PKEXEC = "/usr/bin/pkexec"
APT = "/usr/bin/apt"

# Função de instalação
def install():
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
root = tk.Tk()
root.title("Penguin")
root.geometry("400x300")

tk.Label(root, text="Selecione os aplicativos:", font=("Arial", 11, "bold")).pack(pady=5)

vars_apps = {}

# Criação dos checkbuttons
for app in APPS:
    var = tk.BooleanVar()
    vars_apps[app] = var
    tk.Checkbutton(root, text=app, variable=var).pack(anchor="w", padx=20)

tk.Button(
    root,
    text="Instalar",
    command=install,
    bg="#4CAF50",
    fg="white",
    width=15
).pack(pady=15)

# Verificação do sistema operacional
if not os.path.exists("/etc/debian_version"):
    messagebox.showerror("ERRO FATAL!", "Este programa é destinado a sistemas baseados em Debian/Ubuntu."
                         "Por favor, verifique seu sistema operacional e tente novamente.")
    root.destroy()
root.mainloop()
