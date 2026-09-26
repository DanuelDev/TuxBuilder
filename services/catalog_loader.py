# importações do python
import json

# Lista de aplicativos a partir do arquivo JSON
def load_catalog(catalog):
    """
    Docstring para carregar os arquivos do catálogo de aplicativos
    """
    with open(catalog, "r") as file:
        APPS = json.load(file)
    return APPS