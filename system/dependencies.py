import os

# Verificação do sistema operacional
def check_system():
    """
    Função para verificar se o sistema é baseado em Debian/Ubuntu
    e se os arquivos necessários estão presentes.
    """
    if not os.path.exists("/etc/debian_version"):
        erro = "Este programa é destinado a sistemas baseados em Debian/Ubuntu. Por favor, verifique seu sistema operacional e tente novamente."
        return erro

    if not os.path.exists("/usr/bin/pkexec"):
        erro = "O 'pkexec' não foi encontrado no sistema.\n Por favor, instale o 'policykit-1' com o seguinte comando no terminal:\n sudo apt install -y policykit-1"
        return erro

    if not os.path.exists("apps.json"):
        erro = "O arquivo 'apps.json' não foi encontrado.\n Certifique-se de que ele está no mesmo diretório que este programa."
        return erro