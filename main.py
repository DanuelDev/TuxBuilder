# importações do python
import tkinter as tk
from tkinter import messagebox

#importações tuxbuilder
from ui.menu import create_menu

# Aviso inicial
messagebox.showwarning("ATENÇÃO!", "Antes de prosseguir, certifique-se de rodar o seguinte comando no terminal:\n"
                       "\nsudo apt update && sudo apt upgrade")

# Inicia a interface
create_menu()